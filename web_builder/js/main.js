// GLOBAL APP MAIN JS

document.addEventListener("DOMContentLoaded", () => {
  const navbar = document.querySelector(".navbar");

  // Sticky Navbar Blur and Shadow on Scroll
  window.addEventListener("scroll", () => {
    if (window.scrollY > 50) {
      navbar.style.background = "rgba(6, 8, 11, 0.95)";
      navbar.style.boxShadow = "0 10px 30px rgba(0, 0, 0, 0.5)";
    } else {
      navbar.style.background = "linear-gradient(180deg, rgba(0, 0, 0, 0.8) 0%, rgba(0, 0, 0, 0) 100%)";
      navbar.style.boxShadow = "none";
    }
  });

  // Smooth Scroll for Nav Links
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      e.preventDefault();
      const targetId = this.getAttribute("href");
      if (targetId === "#") return;
      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        targetElement.scrollIntoView({
          behavior: "smooth",
          block: "start"
        });
      }
    });
  });
});
