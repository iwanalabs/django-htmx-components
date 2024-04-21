function updateTabs() {
  Prism.highlightAll();
  const tabsSelect = document.getElementById("tabs");
  const contentTabs = document.getElementsByClassName("tab-content");

  for (let i = 0; i < contentTabs.length; i++) {
    contentTabs[i].classList.add("hidden");
  }

  let tabOption = document.getElementById(tabsSelect.value);
  let tabContent = document.getElementById(tabOption.dataset.target);
  console.log(tabContent);
  tabContent.classList.remove("hidden");

  tabsSelect.addEventListener("change", function (event) {
    tabOption = document.getElementById(event.target.value);
    tabContent = document.getElementById(tabOption.dataset.target);

    for (let i = 0; i < contentTabs.length; i++) {
      contentTabs[i].classList.add("hidden");
    }

    tabContent.classList.remove("hidden");
  });
}

document.addEventListener("DOMContentLoaded", function (event) {
  if (window.location.pathname !== "/") {
    updateTabs();
  }
});

document.addEventListener("htmx:afterSwap", function (event) {
  if (event.detail.target.id == "header" && window.location.pathname !== "/") {
    updateTabs();
  }
});
