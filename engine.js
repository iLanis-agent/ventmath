(function (root) {
  "use strict";
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }
  function round1(x) { return Math.round(x * 10) / 10; }

  function areaPlan(floorSqm, ratio) {
    if (!(floorSqm > 0)) return { error: "the attic floor area must be positive" };
    if (!(ratio > 0)) return { error: "the labeled ratio must be positive" };
    var nfa = round1(floorSqm / ratio * 10000);
    var verdict;
    if (floorSqm < 50) verdict = "a small attic";
    else if (floorSqm < 150) verdict = "a typical attic";
    else verdict = "a big attic";
    return { nfa: nfa, verdict: verdict };
  }

  function splitPlan(nfaSqcm, intakePct) {
    if (!(nfaSqcm > 0)) return { error: "the net free area must be positive" };
    if (!(intakePct > 0) || !(intakePct < 100)) return { error: "the labeled intake share must sit between 0 and 100" };
    var intake = round1(nfaSqcm * intakePct / 100);
    var exhaust = round1(nfaSqcm - intake);
    var verdict;
    if (intakePct >= 45 && intakePct <= 55) verdict = "a balanced split";
    else verdict = "an unbalanced split";
    return { intake: intake, exhaust: exhaust, verdict: verdict };
  }

  function ventPlan(needSqcm, perVentSqcm) {
    if (!(needSqcm > 0) || !(perVentSqcm > 0)) return { error: "the need and the labeled vent rating must be positive" };
    var count = Math.ceil(needSqcm / perVentSqcm);
    var verdict;
    if (count <= 2) verdict = "a couple of vents";
    else if (count <= 6) verdict = "a row of vents";
    else verdict = "a lot of vents";
    return { count: count, verdict: verdict };
  }

  function renderArea(r, floorSqm, ratio) {
    return "An attic floor of " + floorSqm + " sq m at the labeled 1 in " + ratio + " rule needs " + r.nfa + " sq cm of net free area - " + r.verdict + ".";
  }

  function renderSplit(r, nfaSqcm, intakePct) {
    return "A need of " + nfaSqcm + " sq cm at a labeled " + intakePct + "% intake becomes " + r.intake + " sq cm at the soffits and " + r.exhaust + " sq cm at the ridge - " + r.verdict + ".";
  }

  function renderVent(r, needSqcm, perVentSqcm) {
    return "A need of " + needSqcm + " sq cm against vents rated at a labeled " + perVentSqcm + " sq cm each means " + plural(r.count, "vent") + " - " + r.verdict + ".";
  }

  var api = { areaPlan: areaPlan, splitPlan: splitPlan, ventPlan: ventPlan, renderArea: renderArea, renderSplit: renderSplit, renderVent: renderVent };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.VentMath = api;
})(this);
