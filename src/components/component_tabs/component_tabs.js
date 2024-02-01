document.addEventListener("DOMContentLoaded", function () {
  const tabsSelect = document.getElementById("tabs");
  const contentTabs = document.getElementsByClassName("tab-content");

  tabsSelect.addEventListener("change", function (event) {
    const tabOption = document.getElementById(event.target.value);
    const tabContent = document.getElementById(tabOption.dataset.target);

    for (let i = 0; i < contentTabs.length; i++) {
      contentTabs[i].classList.add("hidden");
    }

    tabContent.classList.remove("hidden");
  });
});
