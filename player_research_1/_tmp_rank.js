const fs = require("fs");
const path = require("path");

function parseCsv(text) {
  const lines = text.split(/\r?\n/).filter((l) => l.length);
  const headers = splitCsvLine(lines[0]);
  return lines.slice(1).map((line) => {
    const cells = splitCsvLine(line);
    const o = {};
    headers.forEach((h, i) => (o[h] = cells[i] ?? ""));
    return o;
  });
}
function splitCsvLine(line) {
  const out = [];
  let cur = "", q = false;
  for (let i = 0; i < line.length; i++) {
    const c = line[i];
    if (c === '"') q = !q;
    else if (c === "," && !q) { out.push(cur); cur = ""; }
    else cur += c;
  }
  out.push(cur);
  return out;
}

const dir = path.join("vinh", "player_research_1", "football_ml", "data");
const rows = parseCsv(fs.readFileSync(path.join(dir, "players_master_dataset.csv"), "utf8"));
console.log("n", rows.length, Object.keys(rows[0]));

const teams = {};
for (const r of rows) {
  const t = r.national_team;
  if (!teams[t]) teams[t] = { maxM: 0, G: 0, A: 0, GA: 0, tackles: 0, saves: 0, nplay: 0, ratPlay: 0 };
  const d = teams[t];
  const m = +r.matches || 0;
  if (m > d.maxM) d.maxM = m;
  d.G += +r.goals || 0;
  d.A += +r.assists || 0;
  d.GA += +r.goals_against || 0;
  d.tackles += +r.tackles_won || 0;
  d.saves += +r.saves || 0;
  if ((+r.minutes || 0) > 0) {
    d.nplay++;
    d.ratPlay += +r.overall_rating || 0;
  }
}
console.log("\nTEAMS");
Object.entries(teams)
  .sort((a, b) => b[1].maxM - a[1].maxM || b[1].G - a[1].G)
  .forEach(([t, d]) => {
    const rat = d.nplay ? (d.ratPlay / d.nplay).toFixed(1) : "0";
    console.log(t, "maxM", d.maxM, "G", d.G, "A", d.A, "GA", d.GA, "GD", d.G - d.GA, "rat", rat, "play", d.nplay);
  });

const num = (r, k) => +r[k] || 0;
console.log("\nTOP GOALS");
rows.slice().sort((a, b) => num(b, "goals") - num(a, "goals") || num(b, "assists") - num(a, "assists")).slice(0, 20)
  .forEach((r) => console.log(r.player_id, r.player_name, r.national_team, r.position, "G", r.goals, "A", r.assists, "min", r.minutes, "m", r.matches, "rat", r.overall_rating, "tw", r.tackles_won, "club", r.club, "age", r.age));

console.log("\nTOP TACKLES");
rows.slice().sort((a, b) => num(b, "tackles_won") - num(a, "tackles_won")).slice(0, 15)
  .forEach((r) => console.log(r.player_id, r.player_name, r.national_team, r.position, r.tackles_won, "min", r.minutes, "m", r.matches, "rat", r.overall_rating));

console.log("\nTOP SAVES");
rows.filter((r) => r.position_group === "GK").sort((a, b) => num(b, "saves") - num(a, "saves")).slice(0, 15)
  .forEach((r) => console.log(r.player_id, r.player_name, r.national_team, "saves", r.saves, "pct", r.save_pct, "ga", r.goals_against, "min", r.minutes, "m", r.matches, "rat", r.overall_rating));

console.log("\nTOP RATING min>0");
rows.filter((r) => num(r, "minutes") > 0).sort((a, b) => num(b, "overall_rating") - num(a, "overall_rating")).slice(0, 25)
  .forEach((r) => console.log(r.player_id, r.player_name, r.national_team, r.position, r.overall_rating, "G", r.goals, "A", r.assists, "min", r.minutes, "m", r.matches));

const pass = parseCsv(fs.readFileSync(path.join(dir, "player_passing_clean.csv"), "utf8"));
console.log("\nPASS nonempty");
Object.keys(pass[0]).forEach((k) => {
  const n = pass.filter((r) => r[k] && r[k] !== "Matches").length;
  console.log(k, n);
});

const keep = parseCsv(fs.readFileSync(path.join(dir, "player_keeper_clean.csv"), "utf8"));
console.log("\nGK WDL");
keep.slice().sort((a, b) => num(b, "wins") - num(a, "wins")).slice(0, 20)
  .forEach((r) => console.log(r.player_name, r.national_team, "W", r.wins, "D", r.draws, "L", r.losses, "m", r.matches, "saves", r.saves, "pct", r.save_pct));
