importScripts("https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js");
importScripts("https://cdn.jsdelivr.net/npm/xhr-shim@0.1.3/src/index.min.js");

self.XMLHttpRequest = self.XMLHttpRequestShim;

let pyodide, loaded;
const cookies = {};

const setupWorker = async () => {
  pyodide = await loadPyodide();
  await pyodide.loadPackage("micropip");
  const micropip = pyodide.pyimport("micropip");
  await micropip.install("tzdata");
  await micropip.install("sqlite3");
  await micropip.install("./dist/django_components-0.34.1-py3-none-any.whl");
  await micropip.install(
    "./dist/django_htmx_components-0.1.0-py3-none-any.whl"
  );
  pyodide.runPython(await (await fetch("./init.py")).text());
  loaded = true;
};

self.addEventListener("install", (event) => {
  event.waitUntil(setupWorker());
});

const djangoRequest = async (request) => {
  if (!loaded) {
    await setupWorker();
  }
  // Create an object to hold the request headers
  const reqHeaders = {};

  // Copy all headers from the incoming request to the reqHeaders object
  for (const [key, value] of request.headers.entries()) {
    reqHeaders[key] = value;
  }

  // Add or override specific headers as needed
  let cookieHeader = "";
  for (const key in cookies) {
    const val = `${key}=${cookies[key]}`;
    cookieHeader += cookieHeader ? `; ${val}` : val;
  }
  if (cookieHeader) {
    reqHeaders["Cookie"] = cookieHeader;
  }
  reqHeaders["Referer"] = request.referrer;

  const method = request.method.toLowerCase();
  let params = "";
  if (["post", "put", "patch"].includes(method)) {
    params = await request.text();
  }

  let response = pyodide.runPython(`
      response = app.${method}(
          "${request.url}",
          params="${params}",
          headers=${JSON.stringify(reqHeaders)},
          expect_errors=True,
      )
      try:
          body = response.text
      except UnicodeDecodeError:
          body = [b for b in response.body]
      body`);
  if (typeof response === "object") {
    // response is binary data
    response = new Uint8Array(response);
  }
  const headersPy = pyodide.runPython(`
      import json
      json.dumps(dict(response.headers))`);
  const respHeaders = JSON.parse(headersPy);
  // we cannot access the cookies of the intercepted requests coming in, so save
  // them now as they come back from django to use for building subsequent requests.
  const setCookie = respHeaders["Set-Cookie"];
  if (setCookie) {
    // only saving first one right now
    const nameValue = setCookie.split(";")[0].split("=");
    cookies[nameValue[0].trim()] = nameValue[1];
  }
  if (
    respHeaders["Content-Type"] === "application/octet-stream" &&
    request.url.endsWith(".woff")
  ) {
    respHeaders["Content-Type"] = "font/woff";
  }

  const status = pyodide.runPython("response.status_code");
  if (status === 302 || status === 301) {
    return Response.redirect(respHeaders["Location"], status);
  }

  return new Response(response, { headers: respHeaders, status: status });
};

self.addEventListener("fetch", (event) => {
  event.respondWith(djangoRequest(event.request));
});

self.addEventListener("activate", function (event) {
  event.waitUntil(self.clients.claim());
});
