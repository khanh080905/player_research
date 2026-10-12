(function () {
  const { teams, players, wcNote } = window.RANKING_DATA;

  const state = {
    view: "teams",
    teamSort: "wc",
    teamConf: "ALL",
    playerSort: "rating",
    playerPos: "ALL",
    q: ""
  };

  const teamSorts = [
    { id: "wc", label: "Final WC 2026 Rank" },
    { id: "rating", label: "Team Rating" },
    { id: "gf", label: "Goals Scored" },
    { id: "gd", label: "Goal Difference" }
  ];

  const playerSorts = [
    { id: "rating", label: "Best Players" },
    { id: "goals", label: "Top Scorers" },
    { id: "assists", label: "Most Assists" },
    { id: "tackles", label: "Top Tacklers" },
    { id: "saves", label: "GK Saves" },
    { id: "savePct", label: "Save Percentage" }
  ];

  function $(id) { return document.getElementById(id); }

  function medal(rank) {
    if (rank === 1) return "rank-gold";
    if (rank === 2) return "rank-silver";
    if (rank === 3) return "rank-bronze";
    return "";
  }

  function sortTeams(list) {
    const copy = list.slice();
    switch (state.teamSort) {
      case "rating": return copy.sort((a, b) => b.rating - a.rating || a.wc - b.wc);
      case "gf": return copy.sort((a, b) => b.gf - a.gf || a.wc - b.wc);
      case "gd": return copy.sort((a, b) => (b.gf - b.ga) - (a.gf - a.ga) || a.wc - b.wc);
      default: return copy.sort((a, b) => a.wc - b.wc);
    }
  }

  function sortPlayers(list) {
    const copy = list.slice();
    switch (state.playerSort) {
      case "goals": return copy.sort((a, b) => b.goals - a.goals || b.assists - a.assists || b.rating - a.rating);
      case "assists": return copy.sort((a, b) => b.assists - a.assists || b.goals - a.goals);
      case "tackles": return copy.sort((a, b) => b.tackles - a.tackles || b.rating - a.rating);
      case "saves": return copy.sort((a, b) => b.saves - a.saves || b.savePct - a.savePct);
      case "savePct":
        return copy
          .filter((p) => p.pos === "GK" && p.minutes >= 180)
          .sort((a, b) => b.savePct - a.savePct || b.saves - a.saves);
      default: return copy.sort((a, b) => b.rating - a.rating || b.minutes - a.minutes);
    }
  }

  function filteredTeams() {
    const q = state.q.toLowerCase().trim();
    return sortTeams(teams.filter((t) => {
      const confOk = state.teamConf === "ALL" || t.conf === state.teamConf;
      const qOk = !q || t.name.toLowerCase().includes(q) || t.code.toLowerCase().includes(q) || t.stage.toLowerCase().includes(q);
      return confOk && qOk;
    }));
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
    if (state.view === "teams") {
      $("sort-pills").innerHTML = teamSorts.map((s) =>
        `<button class="pill ${state.teamSort === s.id ? "on" : ""}" data-sort="${s.id}">${s.label}</button>`
      ).join("");
      $("extra-pills").innerHTML = ["ALL", "UEFA", "CONMEBOL", "CONCACAF", "AFC", "CAF", "OFC"].map((c) =>
        `<button class="pill ${state.teamConf === c ? "on" : ""}" data-conf="${c}">${c === "ALL" ? "All Confederations" : c}</button>`
      ).join("");
    } else {
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
  }

  function playerVal(p) {
    if (state.playerSort === "goals") return p.goals + " G";
    if (state.playerSort === "assists") return p.assists + " A";
    if (state.playerSort === "tackles") return p.tackles + " TKL";
    if (state.playerSort === "saves") return p.saves + " SV";
    if (state.playerSort === "savePct") return p.savePct.toFixed(1) + "%";
    return p.rating.toFixed(1);
  }

  function podiumHtml(items, kind) {
    const top = items.slice(0, 3);
    if (top.length < 3) return "";
    const order = [top[1], top[0], top[2]];
    const places = [2, 1, 3];
    return `<div class="podium">${order.map((item, i) => {
      const place = places[i];
      const title = item.name;
      const sub = kind === "teams" ? item.stage + " · " + item.conf : item.pos + " · " + item.team;
      const val = kind === "teams" ? item.stage : playerVal(item);
      return `<div class="podium-card ${medal(place)} p${place}">
        <span class="podium-rank">${place}</span>
        <strong>${title}</strong>
        <small>${sub}</small>
        <b>${val}</b>
      </div>`;
    }).join("")}</div>`;
  }

  function renderTeams() {
    const list = filteredTeams();
    $("count-txt").textContent = `Showing ${list.length} teams · ${wcNote}`;
    $("podium").innerHTML = podiumHtml(list, "teams");
    $("table-wrap").innerHTML = `
      <table class="rk-table">
        <thead>
          <tr>
            <th>Rank</th><th>Team</th><th>Stage</th><th>Confederation</th>
            <th>MP</th><th>GF</th><th>GA</th><th>GD</th><th>Rating</th>
          </tr>
        </thead>
        <tbody>
          ${list.map((t) => {
            const gd = t.gf - t.ga;
            return `<tr class="${medal(t.wc)}">
              <td><span class="rk-num">${t.wc}</span></td>
              <td><span class="code">${t.code}</span> ${t.name}</td>
              <td><span class="stage">${t.stage}</span></td>
              <td>${t.conf}</td>
              <td>${t.matches}</td>
              <td>${t.gf}</td>
              <td>${t.ga}</td>
              <td class="${gd >= 0 ? "pos" : "neg"}">${gd >= 0 ? "+" : ""}${gd}</td>
              <td><b class="gold">${t.rating.toFixed(1)}</b></td>
            </tr>`;
          }).join("")}
        </tbody>
      </table>
      <p class="count-txt" style="margin-top:14px;">* Matches / goals / ratings compiled from the World Cup 2026 master dataset.</p>`;
  }

  function renderPlayers() {
    const list = filteredPlayers();
    const sortLabel = playerSorts.find((s) => s.id === state.playerSort).label;
    $("count-txt").textContent = `Showing ${list.length} featured players · Sorted by ${sortLabel}`;
    $("podium").innerHTML = podiumHtml(list, "players");
    $("table-wrap").innerHTML = `
      <table class="rk-table">
        <thead>
          <tr>
            <th>#</th><th>Player</th><th>Team</th><th>Position</th><th>Rating</th>
            <th>Goals</th><th>Assists</th><th>Tackles</th><th>Saves</th><th>Save %</th><th>Minutes</th>
          </tr>
        </thead>
        <tbody>
          ${list.slice(0, 50).map((p, i) => {
            const rank = i + 1;
            const saveCell = p.pos === "GK" ? p.saves : "—";
            const pctCell = p.pos === "GK" ? p.savePct.toFixed(1) + "%" : "—";
            return `<tr class="${medal(rank)}">
              <td><span class="rk-num">${rank}</span></td>
              <td>${p.name}<div class="sub">${p.club}</div></td>
              <td>${p.team}</td>
              <td><span class="pos-badge pos-${p.pos}">${p.pos}</span></td>
              <td><b class="gold">${p.rating.toFixed(1)}</b></td>
              <td>${p.goals}</td>
              <td>${p.assists}</td>
              <td>${p.tackles}</td>
              <td>${saveCell}</td>
              <td>${pctCell}</td>
              <td>${p.minutes}'</td>
            </tr>`;
          }).join("")}
        </tbody>
      </table>`;
  }

  function render() {
    document.querySelectorAll("[data-view]").forEach((b) => {
      b.classList.toggle("on", b.dataset.view === state.view);
    });
    $("q").placeholder = state.view === "teams"
      ? "Search teams, FIFA codes, stages (champion, quarter-final...)..."
      : "Search players, teams, clubs...";
    renderPills();
    if (state.view === "teams") renderTeams();
    else renderPlayers();
  }

  document.addEventListener("click", (e) => {
    const btn = e.target.closest("button");
    if (!btn) return;
    if (btn.dataset.view) { state.view = btn.dataset.view; render(); }
    if (btn.dataset.sort) { state.teamSort = btn.dataset.sort; render(); }
    if (btn.dataset.conf) { state.teamConf = btn.dataset.conf; render(); }
    if (btn.dataset.psort) { state.playerSort = btn.dataset.psort; render(); }
    if (btn.dataset.pos) { state.playerPos = btn.dataset.pos; render(); }
  });

  $("q").addEventListener("input", (e) => {
    state.q = e.target.value;
    render();
  });

  render();
})();
