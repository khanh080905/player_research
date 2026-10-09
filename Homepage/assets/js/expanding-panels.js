// EXPANDING PANELS MAIN PAGE, SVG WORLD MAP 5 CONTINENTS & COUNTRY SLIDER FLOW

document.addEventListener("DOMContentLoaded", () => {
  const panels = document.querySelectorAll(".flex-panel");
  const worldMapModal = document.getElementById("world-map-modal");
  const countrySliderModal = document.getElementById("country-slider-modal");

  const openWorldMapBtn = document.getElementById("open-world-map-btn");
  const closeMapBtn = document.getElementById("close-map-btn");
  const closeMapBarBtn = document.getElementById("close-map-bar-btn");
  const backToMapBtn = document.getElementById("back-to-map-btn");

  const svgContinents = document.querySelectorAll(".svg-continent");
  const sideContinentCards = document.querySelectorAll(".continent-card-item");
  const allContinentElements = [...svgContinents, ...sideContinentCards];

  const navLinkBtns = document.querySelectorAll(".nav-link-btn");

  // 1. MAIN PAGE 5 PANELS ACCORDION MECHANICS
  if (panels.length) {
    panels.forEach((panel) => {
      panel.addEventListener("mouseenter", () => {
        setActivePanel(panel);
      });

      panel.addEventListener("click", (e) => {
        if (panel.id === "panel-destinations" || e.target.closest("#open-world-map-btn")) {
          openWorldMap();
        } else {
          setActivePanel(panel);
        }
      });
    });
  }

  function setActivePanel(targetPanel) {
    panels.forEach((p) => p.classList.remove("active"));
    targetPanel.classList.add("active");
  }

  // 2. OPEN WORLD MAP MODAL (STEP 2 VIEW)
  if (openWorldMapBtn) {
    openWorldMapBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      openWorldMap();
    });
  }

  function openWorldMap() {
    if (worldMapModal) {
      worldMapModal.classList.add("active");
      document.body.style.overflow = "hidden";
    }
  }

  function closeWorldMap() {
    if (worldMapModal) {
      worldMapModal.classList.remove("active");
      document.body.style.overflow = "";
    }
  }

  if (closeMapBtn) {
    closeMapBtn.addEventListener("click", () => {
      closeWorldMap();
    });
  }

  if (closeMapBarBtn) {
    closeMapBarBtn.addEventListener("click", () => {
      closeWorldMap();
    });
  }

  // 3. CONTINENT SELECTION ON SVG WORLD MAP & SIDE PANEL (SYNCHRONIZED HOVER & CLICK)
  allContinentElements.forEach((element) => {
    const key = element.dataset.continent;
    if (!key) return;

    // Synchronized Hover
    element.addEventListener("mouseenter", () => {
      allContinentElements.forEach((item) => {
        if (item.dataset.continent !== key) {
          item.classList.add("dimmed");
        } else {
          item.classList.remove("dimmed");
        }
      });
    });

    element.addEventListener("mouseleave", () => {
      allContinentElements.forEach((item) => item.classList.remove("dimmed"));
    });

    // Click to view national teams slider
    element.addEventListener("click", () => {
      openCountrySlider(key);
    });
  });

  // 4. OPEN COUNTRY SLIDER MODAL
  function openCountrySlider(continentKey) {
    if (window.timedCardsApp) {
      window.timedCardsApp.loadContinent(continentKey);
    }

    if (countrySliderModal) {
      countrySliderModal.classList.add("active");
    }
  }

  function closeCountrySlider() {
    if (countrySliderModal) {
      countrySliderModal.classList.remove("active");
    }
  }

  if (backToMapBtn) {
    backToMapBtn.addEventListener("click", () => {
      closeCountrySlider();
    });
  }

  // 5. NAVBAR BUTTONS
  navLinkBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      const continentKey = btn.dataset.continent;
      if (continentKey) {
        openWorldMap();
        openCountrySlider(continentKey);
      }
    });
  });

  // 6. ESC KEY NAVIGATION
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      if (countrySliderModal && countrySliderModal.classList.contains("active")) {
        closeCountrySlider();
      } else if (worldMapModal && worldMapModal.classList.contains("active")) {
        closeWorldMap();
      }
    }
  });
});

