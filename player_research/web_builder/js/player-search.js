document.addEventListener("DOMContentLoaded", () => {
  const overlay = document.getElementById("player-search-overlay");
  const openBtn = document.getElementById("open-player-search");
  const closeBtn = document.getElementById("close-player-search");
  const form = document.getElementById("player-search-live-form");
  const input = document.getElementById("player-search-input");
  const teamSelect = document.getElementById("player-search-team");
  const positionSelect = document.getElementById("player-search-position");
  const matchedSelect = document.getElementById("player-search-matched");
  const resultsEl = document.getElementById("player-search-results");
  const statusEl = document.getElementById("player-search-status");

  if (!overlay || !openBtn || !form) {
    return;
  }

  let timer = null;

  function openSearch() {
    overlay.classList.add("active");
    document.body.style.overflow = "hidden";
    if (input) {
      input.focus();
    }
  }

  function closeSearch() {
    overlay.classList.remove("active");
    document.body.style.overflow = "";
  }

  openBtn.addEventListener("click", (e) => {
    e.preventDefault();
    openSearch();
    loadFilters();
  });

  if (closeBtn) {
    closeBtn.addEventListener("click", closeSearch);
  }

  overlay.addEventListener("click", (e) => {
    if (e.target === overlay) {
      closeSearch();
    }
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && overlay.classList.contains("active")) {
      closeSearch();
    }
  });

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    runSearch();
  });

  [input, teamSelect, positionSelect, matchedSelect].forEach((el) => {
    if (!el) return;
    el.addEventListener("input", () => {
      clearTimeout(timer);
      timer = setTimeout(runSearch, 250);
    });
    el.addEventListener("change", runSearch);
  });

  function fillSelect(select, items, placeholder) {
    if (!select || select.dataset.loaded === "1") {
      return;
    }
    const current = select.value;
    select.innerHTML = `<option value="">${placeholder}</option>` + items
      .map((item) => `<option value="${escapeHtml(item)}">${escapeHtml(item)}</option>`)
      .join("");
    select.value = current;
    select.dataset.loaded = "1";
  }

  function loadFilters() {
    if (teamSelect && teamSelect.dataset.loaded === "1") {
      return;
    }
    fetch("php/filters_api.php")
      .then((res) => res.json())
      .then((data) => {
        if (!data.ok) {
          return;
        }
        fillSelect(teamSelect, data.teams || [], "Tất cả đội tuyển");
        fillSelect(positionSelect, data.positions || [], "Tất cả vị trí");
      })
      .catch(() => {});
  }

  function runSearch() {
    const params = new URLSearchParams({
      q: input ? input.value.trim() : "",
      team: teamSelect ? teamSelect.value : "",
      position: positionSelect ? positionSelect.value : "",
      matched: matchedSelect ? matchedSelect.value : "",
    });

    if (![params.get("q"), params.get("team"), params.get("position"), params.get("matched")].some(Boolean)) {
      statusEl.textContent = "Nhập tên hoặc chọn bộ lọc để tìm cầu thủ.";
      resultsEl.innerHTML = "";
      return;
    }

    statusEl.textContent = "Đang tìm...";

    fetch(`php/search_api.php?${params.toString()}`)
      .then((res) => {
        if (!res.ok) {
          throw new Error("API lỗi");
        }
        return res.json();
      })
      .then((data) => {
        if (!data.ok) {
          throw new Error(data.error || "Không đọc được dữ liệu");
        }
        renderResults(data.players || []);
      })
      .catch(() => {
        statusEl.innerHTML =
          'Không gọi được PHP API. Mở trang <a href="search.php">search.php</a> hoặc chạy server PHP trong thư mục web_builder.';
        resultsEl.innerHTML = "";
      });
  }

  function renderResults(players) {
    if (!players.length) {
      statusEl.textContent = "Không tìm thấy cầu thủ phù hợp.";
      resultsEl.innerHTML = "";
      return;
    }

    statusEl.textContent = `${players.length} kết quả từ players_master_dataset.csv`;
    resultsEl.innerHTML = players
      .map((player) => {
        const matchLabel = player.is_matched
          ? `Khớp FBref: ${escapeHtml(player.fbref_name)}`
          : "Chưa có dữ liệu FBref";
        const matchClass = player.is_matched ? "is-matched" : "is-unmatched";
        const ga90 = (Number(player.goals_p90) + Number(player.assists_p90)).toFixed(2);
        return `
          <article class="player-card">
            <div class="player-card-top">
              <span class="card-country">${escapeHtml(player.national_team)} / ${escapeHtml(player.position)}</span>
              <span class="player-rating">${escapeHtml(String(player.overall_rating))}</span>
            </div>
            <h2 class="card-name">${escapeHtml(player.player_name)}</h2>
            <p class="player-meta">${escapeHtml(player.club)} · ${escapeHtml(String(player.age))} tuổi · ${escapeHtml(String(player.height_cm))} cm</p>
            <p class="player-match ${matchClass}">${matchLabel}</p>
            <dl class="player-stats">
              <div><dt>Bàn</dt><dd>${escapeHtml(String(player.goals))}</dd></div>
              <div><dt>Kiến tạo</dt><dd>${escapeHtml(String(player.assists))}</dd></div>
              <div><dt>Phút</dt><dd>${escapeHtml(String(player.minutes))}</dd></div>
              <div><dt>G+A/90</dt><dd>${escapeHtml(ga90)}</dd></div>
            </dl>
          </article>
        `;
      })
      .join("");
  }

  function escapeHtml(value) {
    return String(value ?? "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }
});
