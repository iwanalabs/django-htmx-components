document.addEventListener("DOMContentLoaded", function () {
  const tabsSelect = document.getElementById("tabs");
  const contentTabs = document.getElementsByClassName("tab-content");

  for (let i = 0; i < contentTabs.length; i++) {
    contentTabs[i].classList.add("hidden");
  }

  let tabOption = document.getElementById(tabsSelect.value);
  let tabContent = document.getElementById(tabOption.dataset.target);
  tabContent.classList.remove("hidden");

  tabsSelect.addEventListener("change", function (event) {
    tabOption = document.getElementById(event.target.value);
    tabContent = document.getElementById(tabOption.dataset.target);

    for (let i = 0; i < contentTabs.length; i++) {
      contentTabs[i].classList.add("hidden");
    }

    tabContent.classList.remove("hidden");
  });
});
