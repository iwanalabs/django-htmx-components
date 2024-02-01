document.addEventListener("DOMContentLoaded", function () {
  const tabsElement = document.getElementById("tabs");
  const tabButtons = document.querySelectorAll("#tabs > option");
  let tabElements = [];

  tabButtons.forEach((tabButton) => {
    const id = tabButton.value;
    const triggerEl = tabButton;
    const targetEl = document.getElementById(tabButton.dataset.target);
    tabElements.push({ id, triggerEl, targetEl });
  });

  const options = {
    defaultTabId: "content-1",
    activeClasses: "active-tab active",
    inactiveClasses: "inactive-tab",
  };
  const instanceOptions = {
    id: "tabs",
    override: true,
  };
  const tabs = new Tabs(tabsElement, tabElements, options, instanceOptions);

  let button = document.getElementsByClassName("copy-to-clipboard-button")[0];
});
