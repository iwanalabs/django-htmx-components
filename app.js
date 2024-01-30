const loadingElement = document.getElementById("loading");
const loadedElement = document.getElementById("loaded");

loadedElement.style.display = "none";

if ("serviceWorker" in navigator) {
  navigator.serviceWorker.getRegistration("./").then((registration) => {
    if (registration) {
      console.log("Service worker already registered:", registration);
      loadingElement.style.display = "none";
      loadedElement.style.display = "block";
    } else {
      navigator.serviceWorker.register("./worker.js").then(
        (registration) => {
          console.log("Service worker registration succeeded:", registration);
          registration.installing?.addEventListener("statechange", (event) => {
            if (event.target.state === "activated") {
              console.log("Service worker activated");
              loadingElement.style.display = "none";
              loadedElement.style.display = "block";
            }
          });
        },
        (error) => {
          console.log(`Service worker registration failed: ${error}`);
        }
      );
    }
  });
} else {
  console.log("Service workers are not supported in this browser.");
}
