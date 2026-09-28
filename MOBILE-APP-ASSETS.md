# Mobile app artwork

All generated artwork uses fictional brands. The hero uses six distinct apps with three complementary screens each. The five template examples and six footer examples introduce separate products. Six native vector feature illustrations and two native Runable editor previews are separate designs, too.

- Hero: SOMA yoga, ROAM travel, DEW skincare, TALLY habits, MOSS loyalty, CLUBHOUSE artists.
- Templates: PACE running, FORME furniture, KIN community, SPROUT plants, LOOM salon.
- Features: TRAIL hiking, FOLIO creative boards, STORYTIME reading, STUDIO movement, DRIFT meditation, PANTRY cooking.
- Manage: FLORA garden journal and WAVE podcasts.
- Walkthrough artwork: VELO cycling. This is static overview artwork; no demonstration video has been supplied for this page yet.
- Footer: AMPLI music, SIMMER recipes, MONO budget, PAWLY pets, LINGO learning, NOVA astronomy.

Raster art was created with the built-in image generation tool. Exact prompts and original output paths are in `mobile-app-prompts.json`. All production files live in `dist/assets/mobile-apps/`. Hero screen SVGs use viewports over the three-screen artwork; template SVGs frame individual mobile screenshots. Native UI artwork is reproducible via `build-mobile-ui.py`.

The original hero input position and enlarged overlapping phone layout are retained. The closing gallery uses six distinct apps, with no duplicate cards.

## Realistic replacement pass

The six feature cards and both manage previews now use built-in imagegen artwork with realistic photography and detailed interfaces. Files are `dist/assets/mobile-apps/*-real.webp` (PNG originals alongside). Exact prompts are in `realistic-app-prompts.json`. The original vector versions remain as earlier revisions. Closing gallery corners are 16px at all viewport sizes.
