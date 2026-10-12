// WORLD CUP 2026 FULL CONTINENTS & EXTENDED SCROLLABLE TEAMS DATASET

const worldCupData = {
  asia: {
    continentName: "ASIA",
    subtitle: "AFC • 8.5 SLOTS IN WORLD CUP 2026",
    description: "Asian Football Confederation (AFC) featuring elite national teams with outstanding global performance.",
    teams: [
      { id: "japan", tag: "AFC / JAPAN", title: "JAPAN", subtitle: "Samurai Blue", description: "Japan - Samurai Blue leads the Asian FIFA rankings with mesmerizing possession control and relentless press.", image: "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?auto=format&fit=crop&w=1200&q=80" },
      { id: "south-korea", tag: "AFC / SOUTH KOREA", title: "SOUTH KOREA", subtitle: "Taegeuk Warriors", description: "South Korea - Taegeuk Warriors hold an 11-consecutive World Cup qualification record with world-class stars.", image: "https://images.unsplash.com/photo-1517154421773-0529f29ea451?auto=format&fit=crop&w=1200&q=80" },
      { id: "saudi-arabia", tag: "AFC / SAUDI ARABIA", title: "SAUDI ARABIA", subtitle: "Green Falcons", description: "Saudi Arabia - Green Falcons feature resilient tactical discipline and elite tournament experience.", image: "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=1200&q=80" },
      { id: "iran", tag: "AFC / IRAN", title: "IRAN", subtitle: "Team Melli", description: "Iran - Team Melli boasts rock-solid defensive structure and physical dominance across West Asia.", image: "https://images.unsplash.com/photo-1565008447742-97f6f38c985c?auto=format&fit=crop&w=1200&q=80" },
      { id: "australia", tag: "AFC / AUSTRALIA", title: "AUSTRALIA", subtitle: "Socceroos", description: "Australia - Socceroos bring relentless high-tempo physical football and aerial threat.", image: "https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9?auto=format&fit=crop&w=1200&q=80" }
    ]
  },

  europe: {
    continentName: "EUROPE",
    subtitle: "UEFA • 16 SLOTS IN WORLD CUP 2026",
    description: "Union of European Football Associations (UEFA) represents the most decorated giants in football history.",
    teams: [
      { id: "france", tag: "UEFA / FRANCE", title: "FRANCE", subtitle: "Les Bleus", description: "France - 2018 Champions & 2022 Runners-Up boasting Europe's most explosive squad.", image: "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=1200&q=80" },
      { id: "england", tag: "UEFA / ENGLAND", title: "ENGLAND", subtitle: "The Three Lions", description: "England - The Three Lions feature a world-class young squad aiming for World Cup glory.", image: "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?auto=format&fit=crop&w=1200&q=80" },
      { id: "spain", tag: "UEFA / SPAIN", title: "SPAIN", subtitle: "La Roja", description: "Spain - Reigning EURO 2024 Champions displaying fluid high-tempo possession football.", image: "https://images.unsplash.com/photo-1543783207-ec64e4d95325?auto=format&fit=crop&w=1200&q=80" },
      { id: "germany", tag: "UEFA / GERMANY", title: "GERMANY", subtitle: "Nationalelf", description: "Germany - 4-time World Cup winners driven by elite tactical heritage and championship pedigree.", image: "https://images.unsplash.com/photo-1467269204594-9661b134dd2b?auto=format&fit=crop&w=1200&q=80" },
      { id: "portugal", tag: "UEFA / PORTUGAL", title: "PORTUGAL", subtitle: "A Seleção", description: "Portugal - A Seleção fields explosive technical talent with ambitions to conquer North America.", image: "https://images.unsplash.com/photo-1555881400-74d7acaacd8b?auto=format&fit=crop&w=1200&q=80" }
    ]
  },

  americas: {
    continentName: "AMERICAS",
    subtitle: "CONCACAF & CONMEBOL • WORLD CUP 2026 HOSTS",
    description: "The Americas host the 2026 World Cup (USA, Mexico, Canada) alongside South American titans Argentina & Brazil.",
    teams: [
      { id: "usa", tag: "CONCACAF / USA", title: "USA", subtitle: "The Stars & Stripes", description: "USA - Host nation featuring MetLife Stadium for the historic 2026 World Cup Final.", image: "https://images.unsplash.com/photo-1485738422979-f5c462d49f74?auto=format&fit=crop&w=1200&q=80" },
      { id: "argentina", tag: "CONMEBOL / ARGENTINA", title: "ARGENTINA", subtitle: "La Albiceleste", description: "Argentina - Reigning 2022 World Cup Champions holding the #1 FIFA world ranking.", image: "https://images.unsplash.com/photo-1612294037637-ec328d0e075e?auto=format&fit=crop&w=1200&q=80" },
      { id: "brazil", tag: "CONMEBOL / BRAZIL", title: "BRAZIL", subtitle: "Seleção", description: "Brazil - Record 5-time World Cup Champions bringing iconic Samba magic to North America.", image: "https://images.unsplash.com/photo-1483729558449-99ef09a8c325?auto=format&fit=crop&w=1200&q=80" },
      { id: "mexico", tag: "CONCACAF / MEXICO", title: "MEXICO", subtitle: "El Tri", description: "Mexico - Co-hosts generating electrifying atmosphere at the legendary Estadio Azteca.", image: "https://images.unsplash.com/photo-1512813195386-6cf811ad3542?auto=format&fit=crop&w=1200&q=80" },
      { id: "canada", tag: "CONCACAF / CANADA", title: "CANADA", subtitle: "Les Rouges", description: "Canada - Co-hosts featuring an energetic generation of European-based stars.", image: "https://images.unsplash.com/photo-1503614472-8c93d56e92ce?auto=format&fit=crop&w=1200&q=80" }
    ]
  },

  africa: {
    continentName: "AFRICA",
    subtitle: "CAF • 9.5 SLOTS IN WORLD CUP 2026",
    description: "Confederation of African Football (CAF) brings explosive speed, physical dominance, and tactical flare.",
    teams: [
      { id: "morocco", tag: "CAF / MOROCCO", title: "MOROCCO", subtitle: "Atlas Lions", description: "Morocco - Historic 2022 World Cup Semi-Finalists setting a new benchmark for African football.", image: "https://images.unsplash.com/photo-1597212618440-806262de4f6b?auto=format&fit=crop&w=1200&q=80" },
      { id: "senegal", tag: "CAF / SENEGAL", title: "SENEGAL", subtitle: "Lions of Teranga", description: "Senegal - Lions of Teranga combine formidable athletic power with world-class technical flair.", image: "https://images.unsplash.com/photo-1523821741446-edb2b68bb7a0?auto=format&fit=crop&w=1200&q=80" },
      { id: "nigeria", tag: "CAF / NIGERIA", title: "NIGERIA", subtitle: "Super Eagles", description: "Nigeria - Super Eagles bring explosive attacking power and rich World Cup tradition.", image: "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=1200&q=80" },
      { id: "egypt", tag: "CAF / EGYPT", title: "EGYPT", subtitle: "Pharaohs", description: "Egypt - Legendary Pharaohs holding record AFCON titles and rich continental pedigree.", image: "https://images.unsplash.com/photo-1503177119275-0aa32b3a9368?auto=format&fit=crop&w=1200&q=80" }
    ]
  },

  oceania: {
    continentName: "OCEANIA",
    subtitle: "OFC • 1.5 SLOTS IN WORLD CUP 2026",
    description: "Oceania Football Confederation (OFC) awarded a direct qualification slot for FIFA World Cup 2026.",
    teams: [
      { id: "new-zealand", tag: "OFC / NEW ZEALAND", title: "NEW ZEALAND", subtitle: "All Whites", description: "New Zealand - All Whites dominate Oceania with organized tactical structure and physical presence.", image: "https://images.unsplash.com/photo-1507699622108-4be3abd695ad?auto=format&fit=crop&w=1200&q=80" },
      { id: "fiji", tag: "OFC / FIJI", title: "FIJI", subtitle: "Bula Boys", description: "Fiji - Bula Boys bring passionate island spirit and determination to the global stage.", image: "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80" }
    ]
  }
};


class ScrollableTeamsApp {
  constructor() {
    this.currentContinentKey = "asia";
    this.currentIndex = 0;

    // DOM Elements
    this.modalContinentTitle = document.getElementById("modal-continent-title");
    this.bgActive = document.getElementById("bg-active");
    this.heroTag = document.getElementById("hero-tag");
    this.heroTitle = document.getElementById("hero-title");
    this.heroDesc = document.getElementById("hero-desc");
    this.scrollTrack = document.getElementById("scrollable-cards-track");
    this.prevBtn = document.getElementById("scroll-prev-btn");
    this.nextBtn = document.getElementById("scroll-next-btn");
    this.scrollThumb = document.getElementById("scrollbar-thumb");

    if (this.scrollTrack) {
      this.attachEvents();
    }
  }

  loadContinent(continentKey) {
    if (!worldCupData[continentKey]) continentKey = "asia";
    this.currentContinentKey = continentKey;
    this.currentIndex = 0;

    const data = worldCupData[this.currentContinentKey];
    if (this.modalContinentTitle) {
      this.modalContinentTitle.textContent = `${data.continentName} • ${data.subtitle}`;
    }

    this.renderTrack();
    this.updateActiveState(true);
  }

  getCurrentTeams() {
    return worldCupData[this.currentContinentKey].teams;
  }

  renderTrack() {
    if (!this.scrollTrack) return;
    this.scrollTrack.innerHTML = "";

    const teams = this.getCurrentTeams();

    teams.forEach((team, idx) => {
      const card = document.createElement("div");
      card.className = `dest-card ${idx === this.currentIndex ? "active" : ""}`;
      card.dataset.index = idx;

      card.innerHTML = `
        <div class="card-img-wrap">
          <img src="${team.image}" alt="${team.title}" class="card-img" />
          <div class="card-overlay"></div>
          <div class="card-info">
            <span class="card-country">${team.tag.split(" / ")[0]}</span>
            <h4 class="card-name">${team.title}</h4>
          </div>
        </div>
      `;

      card.addEventListener("click", () => {
        this.currentIndex = idx;
        this.updateActiveState();
        this.scrollToActiveCard();
      });

      this.scrollTrack.appendChild(card);
    });

    this.updateScrollbar();
  }

  nextTeam() {
    const teams = this.getCurrentTeams();
    if (!teams || !teams.length) return;
    this.currentIndex = (this.currentIndex + 1) % teams.length;
    this.updateActiveState();
    this.scrollToActiveCard();
  }

  prevTeam() {
    const teams = this.getCurrentTeams();
    if (!teams || !teams.length) return;
    this.currentIndex = (this.currentIndex - 1 + teams.length) % teams.length;
    this.updateActiveState();
    this.scrollToActiveCard();
  }

  scrollToActiveCard() {
    if (!this.scrollTrack) return;
    const cards = this.scrollTrack.querySelectorAll(".dest-card");
    const activeCard = cards[this.currentIndex];
    if (activeCard) {
      activeCard.scrollIntoView({
        behavior: "smooth",
        block: "nearest",
        inline: "center"
      });
    }
  }

  updateActiveState(isInitial = false) {
    const teams = this.getCurrentTeams();
    const team = teams[this.currentIndex];

    // Background Image update
    if (this.bgActive) {
      this.bgActive.style.backgroundImage = `url('${team.image}')`;
    }

    // Entrance text animation
    if (!isInitial && window.gsap) {
      gsap.fromTo(
        [this.heroTag, this.heroTitle, this.heroDesc],
        { opacity: 0, y: 15 },
        { opacity: 1, y: 0, duration: 0.5, stagger: 0.08, ease: "power3.out" }
      );
    }

    if (this.heroTag) this.heroTag.textContent = `${team.tag} • ${team.subtitle}`;
    if (this.heroTitle) this.heroTitle.textContent = team.title;
    if (this.heroDesc) this.heroDesc.textContent = team.description;

    // Active Card Highlight
    if (this.scrollTrack) {
      const cards = this.scrollTrack.querySelectorAll(".dest-card");
      cards.forEach((c, idx) => {
        c.classList.toggle("active", idx === this.currentIndex);
      });
    }
  }

  updateScrollbar() {
    if (!this.scrollTrack || !this.scrollThumb) return;
    const scrollLeft = this.scrollTrack.scrollLeft;
    const maxScroll = this.scrollTrack.scrollWidth - this.scrollTrack.clientWidth;
    if (maxScroll <= 0) {
      this.scrollThumb.style.width = "100%";
      this.scrollThumb.style.transform = "translateX(0)";
      return;
    }
    const ratio = scrollLeft / maxScroll;
    const thumbWidth = Math.max(30, (this.scrollTrack.clientWidth / this.scrollTrack.scrollWidth) * 100);
    this.scrollThumb.style.width = `${thumbWidth}%`;
    const maxThumbTravel = 100 - thumbWidth;
    this.scrollThumb.style.transform = `translateX(${(ratio * maxThumbTravel)}%)`;
  }

  attachEvents() {
    if (this.scrollTrack) {
      this.scrollTrack.addEventListener("scroll", () => {
        this.updateScrollbar();
      });
    }

    if (this.prevBtn) {
      this.prevBtn.addEventListener("click", () => {
        this.prevTeam();
      });
    }

    if (this.nextBtn) {
      this.nextBtn.addEventListener("click", () => {
        this.nextTeam();
      });
    }
  }
}

// Global initialization
window.ScrollableTeamsApp = ScrollableTeamsApp;

document.addEventListener("DOMContentLoaded", () => {
  window.timedCardsApp = new ScrollableTeamsApp();
});
