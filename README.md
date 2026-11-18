# World News — Wednesday 18 November 2026

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/hamkazhaa/makefun-news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/hamkazhaa/makefun-news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

Built for the [make.fun "Sum up 18 November's world news in one image" bounty](https://make.fun/bounty/news-image-20261118) ($250 USDC, top 50 entries share it).

## What the image shows

A 1024x1024 front page for Wednesday 18 November 2026. A dramatic
illustration leads — a bridge arch collapsed into a dark strait under a
drone-filled dusk sky, a cyclone wall on the horizon — above five verified
headlines from the day:

1. **Ukraine — Kerch Bridge arch collapses in second-day strike.**
   Russia claims a record 1,441 drones downed; Kyiv's North and South
   bridges hit in reply.
2. **Asia — Trump meets Quad leaders, then heads to Xi–Putin talks.**
   First Quad summit in two years; he meets President Marcos Jr. today
   before APEC in Shenzhen.
3. **Gulf — Iran drones target US radar in Bahrain; US hits back on Qeshm.**
   Third attack on US targets in Bahrain in five days is intercepted; US
   jets strike a missile site in the Strait of Hormuz.
4. **Storm — Cyclone Akvan bears down on India's east coast.** Severe
   storm in the Bay of Bengal; landfall near Andhra Pradesh expected on
   20 November.
5. **Britain — UK sanctions firms over Israeli West Bank settlements.**
   London acts to protect the two-state solution.

Footer strip: Dhoni retires from the IPL; Canada and China extend trade
deals. Claims are labelled as claims ("Russia claims…", "Iran drones
target…" as reported); the image is an illustration, not a photograph.

## Sources (researched 18 Nov 2026, ~00:30 UTC)

- Reuters — Ukraine strikes Crimean bridge for second day as Russia
  pounds Kyiv bridges (17 Nov 2026); Trump meets key US regional allies
  in Manila ahead of China visit (17 Nov 2026); Iran attacks US military
  radar system in Bahrain (17 Nov 2026).
- AP / NPR — Ukraine strikes major Russian bridge with drones and
  missiles as aerial attacks escalate (17 Nov 2026); Iran launches a
  third round of strikes on Bahrain (17 Nov 2026).
- BBC Verify (via BBC, 17 Nov 2026) — Kerch Bridge's main road arch
  collapsed into the Kerch Strait; road traffic suspended.
- India Meteorological Department — Cyclonic Storm Akvan bulletins,
  17 Nov 2026 (severe cyclonic storm, landfall ~20 Nov).
- BBC — UK sanctions firms over Israeli West Bank settlements
  (18 Nov 2026).

## Program

`main.py` — Python 3.13, standard library only, no network. It copies
the `entry.png` in this repository to `/output/entry.png`
(`$MAKEFUN_OUTPUT_DIR`, or `argv[1]`, overrides the directory), byte for
byte, so two runs write identical bytes.

Run it:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Verify determinism:

```sh
mkdir -p out1 out2
MAKEFUN_OUTPUT_DIR=out1 python3 main.py
MAKEFUN_OUTPUT_DIR=out2 python3 main.py
sha256sum out1/entry.png out2/entry.png
```

The image is a 1024x1024 PNG, under 1 MiB.
