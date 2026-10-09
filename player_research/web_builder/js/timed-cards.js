// SECTION 1: MODERN TIMED CARDS (GSAP FLIP & Auto-Play Slider)

const destinationsData = [
  {
    id: "kyoto",
    tag: "JAPAN / KYOTO",
    title: "KYOTO",
    description: "Walk through lantern-lit alleys where tradition breathes quietly beneath cedar mountains and ancient cherry blossom sanctuaries.",
    image: "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?auto=format&fit=crop&w=1200&q=80",
    cta: "EXPLORE LOCATION"
  },
  {
    id: "marrakech",
    tag: "MOROCCO / MARRAKECH",
    title: "MARRAKECH",
    description: "Lose yourself in spice-scented souks and terracotta riads glowing under desert light and starlit Atlas skies.",
    image: "https://images.unsplash.com/photo-1597212618440-806262de4f6b?auto=format&fit=crop&w=1200&q=80",
    cta: "EXPLORE LOCATION"
  },
  {
    id: "lofoten",
    tag: "NORWAY / LOFOTEN",
    title: "LOFOTEN",
    description: "Jagged granite peaks rising straight from arctic fjords, bathed in midnight sun and green dancing northern auroras.",
    image: "https://images.unsplash.com/photo-1517411032315-54ef2cb783bb?auto=format&fit=crop&w=1200&q=80",
    cta: "EXPLORE LOCATION"
  },
  {
    id: "cappadocia",
    tag: "TURKEY / CAPPADOCIA",
    title: "CAPPADOCIA",
    description: "Float across surreal fairy chimneys and ancient cave dwellings as dawn fills the sky with hundreds of hot air balloons.",
    image: "https://images.unsplash.com/photo-1641128324972-af3212f0f6bd?auto=format&fit=crop&w=1200&q=80",
    cta: "EXPLORE LOCATION"
  }
];

class TimedCardsSlider {
  constructor() {
    this.currentIndex = 0;
    this.timerDuration = 4.5; // seconds
    this.timerTween = null;
    this.isAnimating = false;

    // DOM Elements
    this.bgActive = document.getElementById("bg-active");
    this.heroTag = document.getElementById("hero-tag");
    this.heroTitle = document.getElementById("hero-title");
    this.heroDesc = document.getElementById("hero-desc");
    this.heroCta = document.getElementById("hero-cta");
    this.cardsDeck = document.getElementById("cards-deck");
    this.timerProgress = document.getElementById("timer-progress");
    this.prevBtn = document.getElementById("prev-btn");
    this.nextBtn = document.getElementById("next-btn");

    if (this.cardsDeck) {
      this.init();
    }
  }

  init() {
    this.renderDeck();
    this.updateActiveState(true);
    this.attachEvents();
    this.startTimer();
  }

  renderDeck() {
    if (!this.cardsDeck) return;
    this.cardsDeck.innerHTML = "";
    destinationsData.forEach((dest, idx) => {
      const card = document.createElement("div");
      card.className = `dest-card ${idx === this.currentIndex ? "active" : ""}`;
      card.dataset.index = idx;
      card.dataset.id = dest.id;

      card.innerHTML = `
        <div class="card-img-wrap">
          <img src="${dest.image}" alt="${dest.title}" class="card-img" />
          <div class="card-overlay"></div>
          <div class="card-info">
            <span class="card-country">${dest.tag.split(" / ")[0]}</span>
            <h4 class="card-name">${dest.title}</h4>
          </div>
        </div>
      `;

      card.addEventListener("click", (e) => {
        e.stopPropagation();
        if (this.isAnimating || idx === this.currentIndex) return;
        this.goToIndex(idx);
      });

      this.cardsDeck.appendChild(card);
    });
  }

  updateActiveState(isInitial = false) {
    const dest = destinationsData[this.currentIndex];

    // Background Image update with scale transition
    if (this.bgActive) {
      this.bgActive.style.backgroundImage = `url('${dest.image}')`;
    }

    // Text update with GSAP entrance animation
    if (!isInitial && window.gsap) {
      gsap.fromTo(
        [this.heroTag, this.heroTitle, this.heroDesc],
        { opacity: 0, y: 20 },
        { opacity: 1, y: 0, duration: 0.6, stagger: 0.08, ease: "power3.out" }
      );
    }

    if (this.heroTag) this.heroTag.textContent = dest.tag;
    if (this.heroTitle) this.heroTitle.textContent = dest.title;
    if (this.heroDesc) this.heroDesc.textContent = dest.description;

    // Update active class on cards
    if (this.cardsDeck) {
      const cards = this.cardsDeck.querySelectorAll(".dest-card");
      cards.forEach((card, idx) => {
        card.classList.toggle("active", idx === this.currentIndex);
      });
    }
  }

  goToIndex(newIndex) {
    if (this.isAnimating) return;
    this.isAnimating = true;

    // Stop current timer
    if (this.timerTween) this.timerTween.kill();

    this.currentIndex = (newIndex + destinationsData.length) % destinationsData.length;
    
    this.updateActiveState();

    setTimeout(() => {
      this.isAnimating = false;
      this.startTimer();
    }, 500);
  }

  next() {
    this.goToIndex(this.currentIndex + 1);
  }

  prev() {
    this.goToIndex(this.currentIndex - 1);
  }

  startTimer() {
    if (!this.timerProgress) return;
    if (this.timerTween) this.timerTween.kill();

    if (window.gsap) {
      gsap.set(this.timerProgress, { scaleX: 0 });

      this.timerTween = gsap.to(this.timerProgress, {
        scaleX: 1,
        duration: this.timerDuration,
        ease: "none",
        onComplete: () => {
          this.next();
        }
      });
    }
  }

  attachEvents() {
    if (this.nextBtn) {
      this.nextBtn.addEventListener("click", (e) => {
        e.stopPropagation();
        this.next();
      });
    }

    if (this.prevBtn) {
      this.prevBtn.addEventListener("click", (e) => {
        e.stopPropagation();
        this.prev();
      });
    }

    if (this.cardsDeck) {
      this.cardsDeck.addEventListener("mouseenter", () => {
        if (this.timerTween) this.timerTween.pause();
      });

      this.cardsDeck.addEventListener("mouseleave", () => {
        if (this.timerTween) this.timerTween.resume();
      });
    }
  }
}

// Global initialization
window.TimedCardsSlider = TimedCardsSlider;

document.addEventListener("DOMContentLoaded", () => {
  window.timedCardsApp = new TimedCardsSlider();
});
