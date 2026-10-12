# Vent math

Vent math plans attic ventilation before the ladder goes up: the attic floor
at a labeled ratio becomes the net free area to aim for, the need at a
labeled intake share becomes the soffit-versus-ridge split, and each side's
need against a labeled vent rating becomes a vent count.

Live site: https://ilanis-agent.github.io/ventmath/

## The three tools

- **Area plan** - `floor sq m / labeled ratio (1 in 150) x 10000`, the net
  free area in sq cm, with a small / typical / big attic verdict.
- **Split plan** - `need x labeled intake share (50%)`, soffit and ridge
  areas, with a balanced / unbalanced split verdict.
- **Vent plan** - `ceil(need / labeled vent rating (150 sq cm))` vents, with
  a couple / row / lot verdict.

## Limits

Every default is labeled and illustrative. Real roofs have cathedral
ceilings, vapor questions and local codes. This is illustrative arithmetic,
not a ventilation design: local codes and the vent maker's net-free-area
rating govern, and a roofer or building scientist sizes the real system.

## Files

- `index.html` - landing page with the labeled norms
- `app.html` - the three calculators
- `engine.js` - shared calculation and render logic (browser + node)
- `oracle.py` - python mirror of the engine, writes `expected.json`
- `test.js` - runs the engine against `expected.json` (30 cases, 136 checks)

Run the tests: `python3 oracle.py && node test.js`
