// WORLD CUP 2026 FULL CONTINENTS & EXTENDED SCROLLABLE TEAMS DATASET

const worldCupData = {
  asia: {
    continentName: "ASIA",
    subtitle: "AFC • 8.5 SLOTS IN WORLD CUP 2026",
    description: "Liên đoàn bóng đá Châu Á (AFC) với các đại diện có phong độ vượt trội trên trường quốc tế.",
    teams: [
      { id: "japan", tag: "AFC / JAPAN", title: "JAPAN", subtitle: "Samurai Blue", description: "Đội tuyển Nhật Bản - Samurai Blue dẫn đầu bảng xếp hạng FIFA Châu Á với lối chơi kiểm soát bóng thăng hoa.", image: "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?auto=format&fit=crop&w=1200&q=80" },
      { id: "south-korea", tag: "AFC / SOUTH KOREA", title: "SOUTH KOREA", subtitle: "Taegeuk Warriors", description: "Đội tuyển Hàn Quốc - Kỷ lục 11 lần liên tiếp tham dự VCK World Cup sở hữu dàn sao đẳng cấp thế giới.", image: "https://images.unsplash.com/photo-1517154421773-0529f29ea451?auto=format&fit=crop&w=1200&q=80" },
      { id: "saudi-arabia", tag: "AFC / SAUDI ARABIA", title: "SAUDI ARABIA", subtitle: "Green Falcons", description: "Đội tuyển Ả Rập Xê Út - Chim ưng xanh với tinh thần thi đấu kiên cường và kinh nghiệm thi đấu đỉnh cao.", image: "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=1200&q=80" },
      { id: "iran", tag: "AFC / IRAN", title: "IRAN", subtitle: "Team Melli", description: "Đội tuyển Iran - Kỷ luật phòng ngự thép và sức mạnh thể hình vượt trội khu vực Tây Á.", image: "https://images.unsplash.com/photo-1565008447742-97f6f38c985c?auto=format&fit=crop&w=1200&q=80" },
      { id: "australia", tag: "AFC / AUSTRALIA", title: "AUSTRALIA", subtitle: "Socceroos", description: "Đội tuyển Australia - Socceroos bền bỉ với lối chơi bóng bổng nguy hiểm và thể lực sung mãn.", image: "https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9?auto=format&fit=crop&w=1200&q=80" }
    ]
  },

  europe: {
    continentName: "EUROPE",
    subtitle: "UEFA • 16 SLOTS IN WORLD CUP 2026",
    description: "Liên đoàn bóng đá Châu Âu (UEFA) sở hữu những thế lực hùng mạnh nhất lịch sử bóng đá thế giới.",
    teams: [
      { id: "france", tag: "UEFA / FRANCE", title: "FRANCE", subtitle: "Les Bleus", description: "Đội tuyển Pháp - Á quân World Cup 2022, Vô địch 2018 sở hữu dàn sao hàng đầu Châu Âu.", image: "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=1200&q=80" },
      { id: "england", tag: "UEFA / ENGLAND", title: "ENGLAND", subtitle: "The Three Lions", description: "Đội tuyển Anh - Tam Sư sở hữu đội hình ngôi sao trẻ trung và khao khát cúp vàng thế giới.", image: "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?auto=format&fit=crop&w=1200&q=80" },
      { id: "spain", tag: "UEFA / SPAIN", title: "SPAIN", subtitle: "La Roja", description: "Đội tuyển Tây Ban Nha - Đương kim Vô địch EURO 2024 với lối đá Tiki-Taka biến hóa.", image: "https://images.unsplash.com/photo-1543783207-ec64e4d95325?auto=format&fit=crop&w=1200&q=80" },
      { id: "germany", tag: "UEFA / GERMANY", title: "GERMANY", subtitle: "Nationalelf", description: "Đội tuyển Đức - Cỗ xe tăng 4 lần vô địch World Cup với truyền thống chiến thắng bản lĩnh.", image: "https://images.unsplash.com/photo-1467269204594-9661b134dd2b?auto=format&fit=crop&w=1200&q=80" },
      { id: "portugal", tag: "UEFA / PORTUGAL", title: "PORTUGAL", subtitle: "A Seleção", description: "Đội tuyển Bồ Đào Nha - Dàn cầu thủ tấn công kỹ thuật và tham vọng xưng vương tại Bắc Mỹ.", image: "https://images.unsplash.com/photo-1555881400-74d7acaacd8b?auto=format&fit=crop&w=1200&q=80" }
    ]
  },

  americas: {
    continentName: "AMERICAS",
    subtitle: "CONCACAF & CONMEBOL • WORLD CUP 2026 HOSTS",
    description: "Châu Mỹ hội tụ 3 nước chủ nhà (Mỹ, Mexico, Canada) cùng hai gã khổng lồ Nam Mỹ Argentina & Brazil.",
    teams: [
      { id: "usa", tag: "CONCACAF / USA", title: "USA", subtitle: "The Stars & Stripes", description: "Đội tuyển Mỹ - Nước chủ nhà World Cup 2026, nơi diễn ra trận Chung kết lịch sử tại sân MetLife.", image: "https://images.unsplash.com/photo-1485738422979-f5c462d49f74?auto=format&fit=crop&w=1200&q=80" },
      { id: "argentina", tag: "CONMEBOL / ARGENTINA", title: "ARGENTINA", subtitle: "La Albiceleste", description: "Đội tuyển Argentina - Đương kim Vô địch World Cup 2022 với vị thế số 1 thế giới.", image: "https://images.unsplash.com/photo-1612294037637-ec328d0e075e?auto=format&fit=crop&w=1200&q=80" },
      { id: "brazil", tag: "CONMEBOL / BRAZIL", title: "BRAZIL", subtitle: "Seleção", description: "Đội tuyển Brazil - Kỷ lục 5 lần bước lên đỉnh cao thế giới với vũ điệu Samba rực lửa.", image: "https://images.unsplash.com/photo-1483729558449-99ef09a8c325?auto=format&fit=crop&w=1200&q=80" },
      { id: "mexico", tag: "CONCACAF / MEXICO", title: "MEXICO", subtitle: "El Tri", description: "Đội tuyển Mexico - Đồng chủ nhà World Cup 2026 với bầu không khí cuồng nhiệt tại Estadio Azteca.", image: "https://images.unsplash.com/photo-1512813195386-6cf811ad3542?auto=format&fit=crop&w=1200&q=80" },
      { id: "canada", tag: "CONCACAF / CANADA", title: "CANADA", subtitle: "Les Rouges", description: "Đội tuyển Canada - Đồng chủ nhà World Cup 2026 sở hữu thế hệ cầu thủ trẻ bứt phá.", image: "https://images.unsplash.com/photo-1503614472-8c93d56e92ce?auto=format&fit=crop&w=1200&q=80" }
    ]
  },

  africa: {
    continentName: "AFRICA",
    subtitle: "CAF • 9.5 SLOTS IN WORLD CUP 2026",
    description: "Liên đoàn bóng đá Châu Phi (CAF) tràn đầy sức mạnh, tốc độ và tiềm năng gây bất ngờ lớn.",
    teams: [
      { id: "morocco", tag: "CAF / MOROCCO", title: "MOROCCO", subtitle: "Atlas Lions", description: "Đội tuyển Ma-rốc - Đội bóng Châu Phi đầu tiên đạt cột mốc lọt vào Bán kết World Cup 2022.", image: "https://images.unsplash.com/photo-1597212618440-806262de4f6b?auto=format&fit=crop&w=1200&q=80" },
      { id: "senegal", tag: "CAF / SENEGAL", title: "SENEGAL", subtitle: "Lions of Teranga", description: "Đội tuyển Senegal - Sư tử Teranga hùng mạnh sở hữu thể lực và kỹ thuật toàn diện.", image: "https://images.unsplash.com/photo-1523821741446-edb2b68bb7a0?auto=format&fit=crop&w=1200&q=80" },
      { id: "nigeria", tag: "CAF / NIGERIA", title: "NIGERIA", subtitle: "Super Eagles", description: "Đội tuyển Nigeria - Đại bàng xanh với lối chơi bùng nổ và truyền thống lâu đời.", image: "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=1200&q=80" },
      { id: "egypt", tag: "CAF / EGYPT", title: "EGYPT", subtitle: "Pharaohs", description: "Đội tuyển Ai Cập - Những Pharaoh huyền thoại giàu thành tích bậc nhất Châu Phi.", image: "https://images.unsplash.com/photo-1503177119275-0aa32b3a9368?auto=format&fit=crop&w=1200&q=80" }
    ]
  },

  oceania: {
    continentName: "OCEANIA",
    subtitle: "OFC • 1.5 SLOTS IN WORLD CUP 2026",
    description: "Châu Đại Dương lần đầu tiên được trao suất trực tiếp tham dự VCK FIFA World Cup 2026.",
    teams: [
      { id: "new-zealand", tag: "OFC / NEW ZEALAND", title: "NEW ZEALAND", subtitle: "All Whites", description: "Đội tuyển New Zealand - Đội bóng thống trị khu vực Châu Đại Dương với phong độ ổn định.", image: "https://images.unsplash.com/photo-1507699622108-4be3abd695ad?auto=format&fit=crop&w=1200&q=80" },
      { id: "fiji", tag: "OFC / FIJI", title: "FIJI", subtitle: "Bula Boys", description: "Đội tuyển Fiji - Đại diện kiên cường từ đảo quốc nhiệt đới với quyết tâm bứt phá.", image: "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80" }
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
