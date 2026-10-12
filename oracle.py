import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)

def area_plan(floorSqm, ratio):
    if not (floorSqm > 0):
        return {"error": "the attic floor area must be positive"}
    if not (ratio > 0):
        return {"error": "the labeled ratio must be positive"}
    nfa = round1(floorSqm / ratio * 10000)
    if floorSqm < 50: verdict = "a small attic"
    elif floorSqm < 150: verdict = "a typical attic"
    else: verdict = "a big attic"
    return {"nfa": nfa, "verdict": verdict}

def split_plan(nfaSqcm, intakePct):
    if not (nfaSqcm > 0):
        return {"error": "the net free area must be positive"}
    if not (intakePct > 0) or not (intakePct < 100):
        return {"error": "the labeled intake share must sit between 0 and 100"}
    intake = round1(nfaSqcm * intakePct / 100)
    exhaust = round1(nfaSqcm - intake)
    if 45 <= intakePct <= 55: verdict = "a balanced split"
    else: verdict = "an unbalanced split"
    return {"intake": intake, "exhaust": exhaust, "verdict": verdict}

def vent_plan(needSqcm, perVentSqcm):
    if not (needSqcm > 0) or not (perVentSqcm > 0):
        return {"error": "the need and the labeled vent rating must be positive"}
    count = math.ceil(needSqcm / perVentSqcm)
    if count <= 2: verdict = "a couple of vents"
    elif count <= 6: verdict = "a row of vents"
    else: verdict = "a lot of vents"
    return {"count": count, "verdict": verdict}

def render_area(r, floorSqm, ratio):
    return ("An attic floor of " + fmt(floorSqm) + " sq m at the labeled 1 in " + fmt(ratio) + " rule needs "
            + fmt(r["nfa"]) + " sq cm of net free area - " + r["verdict"] + ".")

def render_split(r, nfaSqcm, intakePct):
    return ("A need of " + fmt(nfaSqcm) + " sq cm at a labeled " + fmt(intakePct) + "% intake becomes "
            + fmt(r["intake"]) + " sq cm at the soffits and " + fmt(r["exhaust"]) + " sq cm at the ridge - " + r["verdict"] + ".")

def render_vent(r, needSqcm, perVentSqcm):
    return ("A need of " + fmt(needSqcm) + " sq cm against vents rated at a labeled " + fmt(perVentSqcm)
            + " sq cm each means " + plural(r["count"], "vent") + " - " + r["verdict"] + ".")

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[90,150],[40,150],[160,150],[100,150],[90,300],[0,150],[90,0],[150,150],[45.5,150],[49,150]]:
    add("areaPlan", area_plan, render_area, a)
for a in [[600,50],[600,40],[1000,55],[450,60],[0,50],[600,0],[600,100],[333.3,50],[600,45],[600,55]]:
    add("splitPlan", split_plan, render_split, a)
for a in [[300,150],[100,150],[900,150],[300,300],[301,300],[0,150],[300,0],[1200,150],[299.9,150],[950,140]]:
    add("ventPlan", vent_plan, render_vent, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
