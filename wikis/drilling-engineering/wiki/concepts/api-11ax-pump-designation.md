---
title: "API 11AX Pump Designation"
tags: [rod-pump, api-11ax, pump-designation, insert-pump, tubing-pump, barrel-type]
sources:
  - api-spec-11ax
added: 2026-05-13
last_updated: 2026-05-13
---

# API 11AX Pump Designation

## Scope

The 12-character API Spec 11AX pump-designation code for subsurface sucker-rod pumps. Encodes the pump's tubing-size compatibility, bore size, type (insert vs tubing), barrel and plunger configuration in a compact label that operators specify when ordering replacement pumps.

## Designation structure (paraphrased)

| Position | Field | Common values |
|---|---|---|
| 1-2 | Tubing size | 25 = 2⅜"; 30 = 2⅞"; 35 = 3½" |
| 3-4 | Pump bore | 125 = 1¼"; 150 = 1½"; 175 = 1¾"; 200 = 2" |
| 5 | Pump type | R = rod (insert); T = tubing |
| 6 | Barrel type | H = heavy-wall; W = thin-wall |
| 7 | Plunger length | 1 = standard; 2 = extended |
| 8-9 | Barrel length | designation in feet |
| 10-12 | Plunger extensions / accessories | manufacturer-specific |

## Insert pump vs tubing pump

- **Insert pump (R)** — entire pump assembly is run on sucker rods and inserts into a seating-nipple on the tubing string. Pulled and replaced without pulling tubing. Operationally cheaper to service; dominates light-duty applications.
- **Tubing pump (T)** — pump barrel is part of the tubing string; only the plunger and traveling valve run on the rods. Larger bore at the same tubing size (deeper draw-down) but requires pulling tubing for any pump-barrel work. Used in higher-rate / larger-bore applications.

## Worked examples

- `25-125-R-H-B-M` — 2⅜" tubing, 1¼" bore, insert rod-pump with heavy-wall barrel
- `30-175-T-W-A-X` — 2⅞" tubing, 1¾" bore, tubing pump with thin-wall barrel
- `35-200-R-H-B-M` — 3½" tubing, 2" bore, heavy-duty insert pump

## Public references

- **API Spec 11AX** — [api-spec-11ax.md](../standards/api-spec-11ax.md)
- **Takacs 2003** — pump-designation worked-example tabulations
- [Sovonex API 11AX summary](https://www.sovonex.com/drilling-equipment/api-subsurface-rod-pumps/api-11ax-pump-designation/) — public cross-check

## Cross-references

- [Sucker-Rod Pumping Overview](sucker-rod-pumping-overview.md)
- [API Spec 11AX](../standards/api-spec-11ax.md)
