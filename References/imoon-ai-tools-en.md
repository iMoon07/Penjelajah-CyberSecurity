# ai-tools — scripts & asset pipeline

> Mirrored from the `ai-tools` repository README so the toolchain is readable next
> to the other references. Source of truth:
> <https://github.com/iMoon07/ai-tools>

---

Scripts, extracted assets, and working artifacts used to reproduce the Alur
assets (logos, icons, diagrams). Not an application: every folder stands on its
own and can be run from the repo root.

Only the generated output is published: the logo assets and the ` ```draw ` /
` ```topology ` blocks in articles. The scripts themselves are the reproducible
half of that pipeline, so they live here.

The generators expect the site checkout as a sibling directory
(`../imoon07.github.io`); every other script takes its paths as arguments.

**Total:** 7173 files.

## Requirements

- Python 3.9+
- `websocket-client` — CDP probes (`verify/`, `browser/`)
- `selenium`, `playwright` — browser automation (`browser/`, `verify/`)
- `Pillow` — image comparison (`verify/`, `renders/`)
- Chromium or Chrome for the headless probes

```bash
python3 -m pip install websocket-client selenium playwright pillow
python3 -m playwright install chromium
```

## Layout

| Folder | Contents | Key entry points |
| --- | --- | --- |
| `archive/` | Old documents and failed downloads, kept for audit | `backup-1/`, `backup-2/`, `failed-downloads/` |
| `assets/` | Extracted Unicons icons, ready for custom presets | 573 SVG |
| `browser/` | CDP/Playwright scripts that open, drag, and inspect pages | `cdp-check*.js`, `cdp-dragdebug*.js` |
| `fetch/` | Source asset downloaders (Thridy, Devfolio, Kali) | `thridy_fetch.py`, `fetch_kali_*.py` |
| `generators/` | Logo and manifest builders, plus cross-language doc sync | `build_logo_manifest.py`, `build_topology_icons.py`, `sync_topology_templates.py`, `sync_server_stack_langs.py` |
| `icons/` | Redrawn interface icons, 64×64 | `app-window.svg`, `bug-crawl.svg` |
| `js-extracts/` | Site JS/HTML excerpts, flow captures, extraction notes | `alur-inline.js`, `alur-scene.md` |
| `layout/` | Layout experiments (columns, diagnostics) as HTML + Python | `cols.py`, `diag.py` |
| `renders/` | Render captures kept for visual comparison | PNG, `canvas/` |
| `renders/canvas/` | Screenshots captured by the `verify/canvas/` probes | `sticky.png`, `hittest*.png` |
| `snapshots/` | Page, DOM, and per-session note captures | `pages/`, `dom/`, `design/` |
| `snapshots/kilo-scratch/` | Fixtures, backups, logs, and HTML captures kept from the old scratch dir | `draw.html.bak`, `spec.json`, `topo_head.html` |
| `test/` | Visual and asset function tests | `test_all_shapes_*.py` |
| `vendor/` | Third-party libraries, mostly Unicons (line/solid/monochrome) | `unicons/`, `marked.min.js` |
| `verify/` | Result audits (shapes, lines, arrows, plates, touch gestures) | `verify.py`, `audit-*.html`, `mobile_touch_scroll.py` |
| `verify/canvas/` | Headless CDP probes for `draw.html` and `topology.html` (canvas, arrows, tables, charts, responsive). 393 scripts | `draw_everywhere.py`, `stickyfill.py`, `tablepanel.py`, `shot.py`, `topo_mobile.py` |

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
| Sync the template topology across en/id/ms/tl | `python3 generators/sync_topology_templates.py --check` |
| Sync the server-stack diagram across en/id/ms/tl | `python3 generators/sync_server_stack_langs.py --check` |
| Preview the site and docs over http or https | `python3 serve/serve.py --port 8123` |
| Test shape/line interleaving | `python3 test/test_all_shapes_line.py` |
| Check list scrolling on a touch viewport | `python3 verify/mobile_touch_scroll.py --url http://localhost:8000/draw.html --open ".mobile-fab,[data-mobile-panel='assets']" --control` |
| Run every canvas probe | `for f in verify/canvas/*.py; do python3 "$f"; done` |

## Notes

- `fetch/thridy-candidates.json` is the Thridy slug index (groups `hack`,
  `crime`, `police`, `secure`) used by `thridy_fetch.py`; the script no longer
  depends on `/tmp`.
- `verify/mobile_touch_scroll.py` drives Chromium over CDP with emulated touch.
  Pass `--control` for an A/B run: it restores `touch-action: none` and shows
  that the list cannot be scrolled without the fix.
- Names ending in `~2` are duplicates of an earlier attempt; safe to delete once
  confirmed unused.
- Probe scripts keep their scratch (Chromium profiles, screenshots) in
  `/tmp/alur-probes/`, outside the repo. Override the port in the script when
  two runs collide.
- `.pyc` files and `__pycache__/` are caches, not sources; they are ignored.