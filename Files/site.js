document.documentElement.dataset.js = "enabled";

const navToggle = document.querySelector("[data-nav-toggle]");
const siteNav = document.querySelector(".site-nav");

if (navToggle && siteNav) {
  navToggle.addEventListener("click", () => {
    const expanded = navToggle.getAttribute("aria-expanded") === "true";
    navToggle.setAttribute("aria-expanded", String(!expanded));
    siteNav.dataset.open = String(!expanded);
  });
}
