# ai-tools — scripts & asset pipeline

> Mirrored from `/home/moon/Projects/ai-tools/README.md` so the local
> toolchain is readable next to the other references. `ai-tools/` is not a
> published repository: only its output (assets in `logo/`, ` ```draw ` /
> ` ```topology ` blocks in articles) reaches the site.

---

Scripts, extracted assets, and working artifacts used to reproduce the Alur
assets (logos, icons, diagrams). Not an application: every folder stands on its
own and can be run from the repo root.

Location: `/home/moon/Projects/ai-tools` — **local only**, never published. Only
its output reaches the site: assets in `logo/` and the ` ```draw ` /
` ```topology ` blocks in articles.

**Total:** 3264 files.

## Layout

| Folder | Contents | Key entry points |
| --- | --- | --- |
| `archive/` | Old documents and failed downloads, kept for audit | `backup-1/`, `backup-2/`, `failed-downloads/` |
| `assets/` | Extracted Unicons icons, ready for custom presets | 573 SVG |
| `browser/` | CDP/Playwright scripts that open, drag, and inspect pages | `cdp-check*.js`, `cdp-dragdebug*.js` |
| `fetch/` | Source asset downloaders (Thridy, Devfolio, Kali) | `thridy_fetch.py`, `fetch_kali_*.py` |
| `generators/` | Logo and manifest builders | `build_logo_manifest.py`, `build_topology_icons.py` |
| `icons/` | Redrawn interface icons, 64×64 | `app-window.svg`, `bug-crawl.svg` |
| `js-extracts/` | Site JS/HTML excerpts, flow captures, extraction notes | `alur-inline.js`, `alur-scene.md` |
| `layout/` | Layout experiments (columns, diagnostics) as HTML + Python | `cols.py`, `diag.py` |
| `renders/` | Render captures kept for visual comparison | PNG |
| `snapshots/` | Page, DOM, and per-session note captures | `pages/`, `dom/`, `design/` |
| `test/` | Visual and asset function tests | `test_all_shapes_*.py` |
| `vendor/` | Third-party libraries, mostly Unicons (line/solid/monochrome) | `unicons/`, `marked.min.js` |
| `verify/` | Result audits (shapes, lines, arrows, plates, touch gestures) | `verify.py`, `audit-*.html`, `mobile_touch_scroll.py` |

## Typical workflow

1. Fetch source assets into a scratch folder with the `fetch/` scripts.
2. Transform them with `generators/`, or a one-off script in `layout/`.
3. Verify the result with `verify/` and keep the evidence in `renders/`.
4. Save the original page and notes in `snapshots/` so the run can be repeated.

## Entry points

| Goal | Command |
| --- | --- |
| Download Thridy 3D icons (security groups) | `python3 fetch/thridy_fetch.py --group hack,crime` |
| Build the logo manifest for the site | `python3 generators/build_logo_manifest.py --site ../imoon07.github.io` |
| Build the topology icon sprite | `python3 generators/build_topology_icons.py` |
| Test shape/line interleaving | `python3 test/test_all_shapes_line.py` |
| Check list scrolling on a touch viewport | `python3 verify/mobile_touch_scroll.py --url http://localhost:8000/draw.html --open ".mobile-fab,[data-mobile-panel='assets']" --control` |

## Notes

- `fetch/thridy-candidates.json` is the Thridy slug index (groups `hack`,
  `crime`, `police`, `secure`) used by `thridy_fetch.py`; the script no longer
  depends on `/tmp`.
- `verify/mobile_touch_scroll.py` drives Chromium over CDP with emulated touch.
  Pass `--control` for an A/B run: it restores `touch-action: none` and shows
  that the list cannot be scrolled without the fix.
- Names ending in `~2` are duplicates of an earlier attempt; safe to delete once
  confirmed unused.
- `.pyc` files (5) are caches, not sources.