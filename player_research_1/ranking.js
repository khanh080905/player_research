(function () {
  const { players } = window.RANKING_DATA;

  const state = {
    playerSort: "rating",
    playerPos: "ALL",
    q: ""
  };

  const playerSorts = [
    { id: "rating", label: "Best Players" },
    { id: "goals", label: "Top Scorers" },
    { id: "assists", label: "Most Assists" },
    { id: "tackles", label: "Top Tacklers" },
    { id: "saves", label: "GK Saves" }
  ];

  function $(id) { return document.getElementById(id); }

  function medal(rank) {
    if (rank === 1) return "rank-gold";
    if (rank === 2) return "rank-silver";
    if (rank === 3) return "rank-bronze";
    return "";
  }

  function sortPlayers(list) {
    const copy = list.slice();
    switch (state.playerSort) {
      case "goals": return copy.sort((a, b) => b.goals - a.goals || b.assists - a.assists || b.rating - a.rating);
      case "assists": return copy.sort((a, b) => b.assists - a.assists || b.goals - a.goals);
      case "tackles": return copy.sort((a, b) => b.tackles - a.tackles || b.rating - a.rating);
      case "saves": return copy.sort((a, b) => b.saves - a.saves || b.rating - a.rating);
      default: return copy.sort((a, b) => b.rating - a.rating || b.minutes - a.minutes);
    }
  }

  function filteredPlayers() {
    const q = state.q.toLowerCase().trim();
    return sortPlayers(players.filter((p) => {
      const posOk = state.playerPos === "ALL" || p.pos === state.playerPos;
      const qOk = !q || p.name.toLowerCase().includes(q) || p.team.toLowerCase().includes(q) || p.club.toLowerCase().includes(q);
      return posOk && qOk;
    }));
  }

  function renderPills() {
    $("sort-pills").innerHTML = playerSorts.map((s) =>
      `<button class="pill ${state.playerSort === s.id ? "on" : ""}" data-psort="${s.id}">${s.label}</button>`
    ).join("");
    $("extra-pills").innerHTML = [
      { id: "ALL", l: "All Positions" },
      { id: "FW", l: "FW Forward" },
      { id: "MF", l: "MF Midfielder" },
      { id: "DF", l: "DF Defender" },
      { id: "GK", l: "GK Goalkeeper" }
    ].map((c) =>
      `<button class="pill ${state.playerPos === c.id ? "on" : ""}" data-pos="${c.id}">${c.l}</button>`
    ).join("");
  }

  function playerVal(p) {
    if (state.playerSort === "goals") return p.goals + " G";
    if (state.playerSort === "assists") return p.assists + " A";
    if (state.playerSort === "tackles") return p.tackles + " TKL";
    if (state.playerSort === "saves") return p.saves + " SV";
    return p.rating.toFixed(1);
  }

  function podiumHtml(items) {
    const top = items.slice(0, 3);
    if (top.length < 3) return "";
    const order = [top[1], top[0], top[2]];
    const places = [2, 1, 3];
    return `<div class="podium">${order.map((item, i) => {
      const place = places[i];
      const title = item.name;
      const sub = item.pos + " · " + item.team + " (" + item.club + ")";
      const val = playerVal(item);
      return `<div class="podium-card ${medal(place)} p${place}">
        <span class="podium-rank">${place}</span>
        <strong>${title}</strong>
        <small>${sub}</small>
        <b>${val}</b>
      </div>`;
    }).join("")}</div>`;
  }

  function renderPlayers() {
    const list = filteredPlayers();
    const sortObj = playerSorts.find((s) => s.id === state.playerSort);
    const sortLabel = sortObj ? sortObj.label : "Best Players";
    $("count-txt").textContent = `Showing ${list.length} players · Sorted by ${sortLabel}`;
    $("podium").innerHTML = podiumHtml(list);

    const sort = state.playerSort;

    // Cấu hình cột theo từng mục yêu cầu:
    // 1. "rating" (Best Players): Bỏ hết goals, assists, tackles, saves
    // 2. "goals", "assists", "tackles" (Top Scorers, Most Assists, Top Tacklers): Bỏ cột saves
    // 3. "saves" (GK Saves): Bỏ các cột goals, assists, tackles
    let extraTh = "";
    if (sort === "goals" || sort === "assists" || sort === "tackles") {
      extraTh = `<th>Goals</th><th>Assists</th><th>Tackles</th>`;
    } else if (sort === "saves") {
      extraTh = `<th>Saves</th>`;
    }

    $("table-wrap").innerHTML = `
      <table class="rk-table">
        <thead>
          <tr>
            <th>#</th>
            <th>Player</th>
            <th>Team</th>
            <th>Position</th>
            <th>Rating</th>
            ${extraTh}
            <th>Minutes</th>
          </tr>
        </thead>
        <tbody>
          ${list.slice(0, 100).map((p, i) => {
            const rank = i + 1;
            let extraTd = "";
            if (sort === "goals" || sort === "assists" || sort === "tackles") {
              extraTd = `
                <td><b class="${sort === 'goals' ? 'gold' : ''}">${p.goals}</b></td>
                <td><b class="${sort === 'assists' ? 'gold' : ''}">${p.assists}</b></td>
                <td><b class="${sort === 'tackles' ? 'gold' : ''}">${p.tackles}</b></td>`;
            } else if (sort === "saves") {
              extraTd = `<td><b class="gold">${p.saves}</b></td>`;
            }

            return `<tr class="${medal(rank)}">
              <td><span class="rk-num">${rank}</span></td>
              <td>${p.name}<div class="sub">${p.club}</div></td>
              <td>${p.team}</td>
              <td><span class="pos-badge pos-${p.pos}">${p.pos}</span></td>
              <td><b class="gold">${p.rating.toFixed(1)}</b></td>
              ${extraTd}
              <td>${p.minutes}'</td>
            </tr>`;
          }).join("")}
        </tbody>
      </table>`;
  }

  function render() {
    renderPills();
    renderPlayers();
  }

  document.addEventListener("click", (e) => {
    const btn = e.target.closest("button");
    if (!btn) return;
    if (btn.dataset.psort) { state.playerSort = btn.dataset.psort; render(); }
    if (btn.dataset.pos) { state.playerPos = btn.dataset.pos; render(); }
  });

  $("q").addEventListener("input", (e) => {
    state.q = e.target.value;
    render();
  });

  render();
})();
