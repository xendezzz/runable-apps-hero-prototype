# Runable Apps landing-page prototype

Copy variant of https://github.com/xendezzz/runable-websites-hero-prototype at `339109858c91a749105f44d81ebe49002eb3a647`.

The original layout, typography, section order, responsive rules and motion are retained. Copy is tailored to app generation. All showcase artwork and demo clips are grey placeholders with the original media dimensions. Brand marks, icons and fonts are retained. Usage metrics are unverified placeholders (—); pricing is inherited from the source and should be confirmed before launch.

## Preview

```sh
python3 -m http.server 8000 --directory dist
```

Open http://localhost:8000. No build step or dependency installation is required.

## Integration

This remains a marketing prototype. Generation, authentication, checkout and downloads are not connected. The source keeps a separate, unwired `hero-builder.js` integration helper. Its legacy event and selector IDs are retained for compatibility; the landing page CTAs remain prototype controls. The demo player is disabled until media is supplied. Replace media files under `dist/assets`, restore video sources and remove `dist/placeholders.css` when real assets are ready.

The original hosting project ID and canonical URL are deliberately omitted so this repository cannot overwrite the source site. Configure a separate deployment when ready.

## Feature copy source

The 6 feature cards under “Total control, remarkably simple” use the headings and descriptions from User-provided app-builder screenshot (2026-09-25). Updated September 25, 2026; grey media placeholders and the existing card presentation are retained.
