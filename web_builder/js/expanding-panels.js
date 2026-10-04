// EXPANDING NAV PANELS MENU & MODAL TRANSITION MECHANICS

document.addEventListener("DOMContentLoaded", () => {
  const panels = document.querySelectorAll(".flex-panel");
  const sliderModal = document.getElementById("slider-modal");
  const genericModal = document.getElementById("generic-modal");

  const openSliderBtn = document.getElementById("open-slider-btn");
  const closeSliderBtn = document.getElementById("close-slider-btn");
  const closeGenericBtns = document.querySelectorAll(".close-generic-btn");

  const navLinkBtns = document.querySelectorAll(".nav-link-btn");

  // 1. Panel Accordion Mechanics (Matches Screenshot)
  if (panels.length) {
    panels.forEach((panel) => {
      panel.addEventListener("mouseenter", () => {
        setActivePanel(panel);
      });

      panel.addEventListener("click", (e) => {
        // If user clicks action button inside panel, don't re-trigger panel toggle
        if (e.target.closest(".panel-action-btn")) return;
        setActivePanel(panel);
      });
    });
  }

  function setActivePanel(targetPanel) {
    panels.forEach((p) => p.classList.remove("active"));
    targetPanel.classList.add("active");
  }

  // 2. Action Buttons Click -> Open Feature View Modal
  document.querySelectorAll(".panel-action-btn").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.stopPropagation();
      const targetModalId = btn.dataset.target;

      if (targetModalId === "slider-modal") {
        openSliderModal();
      } else {
        openGenericModal(btn);
      }
    });
  });

  // Open Slider Modal
  function openSliderModal() {
    if (sliderModal) {
      sliderModal.classList.add("active");
      document.body.style.overflow = "hidden";

      // Start / resume slider timer
      if (window.timedCardsApp) {
        window.timedCardsApp.startTimer();
      }
    }
  }

  // Close Slider Modal
  if (closeSliderBtn) {
    closeSliderBtn.addEventListener("click", () => {
      closeSliderModal();
    });
  }

  function closeSliderModal() {
    if (sliderModal) {
      sliderModal.classList.remove("active");
      document.body.style.overflow = "";

      // Pause slider timer
      if (window.timedCardsApp && window.timedCardsApp.timerTween) {
        window.timedCardsApp.timerTween.pause();
      }
    }
  }

  // Generic Modal Handling
  function openGenericModal(btn) {
    const panel = btn.closest(".flex-panel");
    const num = panel ? panel.querySelector(".panel-num")?.textContent : "01";
    const heading = panel ? panel.querySelector(".panel-heading")?.textContent : "FEATURE DETAILS";
    const desc = panel ? panel.querySelector(".panel-desc")?.textContent : "";

    document.getElementById("modal-num").textContent = num;
    document.getElementById("modal-title").textContent = heading;
    document.getElementById("modal-desc").textContent = desc;

    if (genericModal) {
      genericModal.classList.add("active");
      document.body.style.overflow = "hidden";
    }
  }

  closeGenericBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      if (genericModal) genericModal.classList.remove("active");
      document.body.style.overflow = "";
    });
  });

  // Navbar Buttons -> Open Panel or Modal directly
  navLinkBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      const panelId = btn.dataset.openPanel;
      if (panelId === "destinations") {
        openSliderModal();
      } else {
        const targetPanel = document.getElementById(`panel-${panelId}`);
        if (targetPanel) {
          setActivePanel(targetPanel);
          targetPanel.scrollIntoView({ behavior: "smooth" });
        }
      }
    });
  });

  // ESC Key to close any open modal
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      closeSliderModal();
      if (genericModal) genericModal.classList.remove("active");
      document.body.style.overflow = "";
    }
  });
});
