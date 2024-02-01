const loadingElements = document.getElementsByClassName("loading");
const loadedElements = document.getElementsByClassName("ready");

function hideLoading() {
  for (let i = 0; i < loadingElements.length; i++) {
    loadingElements[i].style.display = "none";
  }

  for (let i = 0; i < loadedElements.length; i++) {
    loadedElements[i].style.display = "block";
  }
}

if ("serviceWorker" in navigator) {
  navigator.serviceWorker.getRegistration("./").then((registration) => {
    if (registration) {
      console.log("Service worker already registered:", registration);
      hideLoading();
    } else {
      navigator.serviceWorker.register("./worker.js").then(
        (registration) => {
          console.log("Service worker registration succeeded:", registration);
          registration.installing?.addEventListener("statechange", (event) => {
            if (event.target.state === "activated") {
              console.log("Service worker activated");
              hideLoading();
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
