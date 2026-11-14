# Topology editor — `topology.html`

> Mirrored from `imoon07.github.io/topology.html` so the guide is readable next to the other
> references. The site repository stays the source of truth:
> <https://github.com/iMoon07/imoon07.github.io/blob/main/topology.html>

Live editor: <https://imoon07.github.io/topology.html>

---

`topology.html` is the authoring side of the ` ```topology ` renderer documented in
[Topology Diagrams](imoon-topology-en.md). The article renderer is read-only: it
takes a JSON block and draws it. This page is the editor that produces that JSON,
with a live preview, a node/edge panel, a logo picker, and export back to a
` ```topology ` block.

Both sides share one engine: `js/topology.js` + `css/topology.css`. Nothing is
compiled and there is no server round-trip — the editor is static HTML/CSS/JS, and
what you see in the preview is exactly what the renderer will draw in an article.

## Layout

| Region | Purpose |
| --- | --- |
| Top bar | Home / Docs / About / Draw links, `Guides: off\|on`, `Panel` (narrow screens), `Export`, `Copy ```topology` |
| Stage | The live preview (`#preview.topology`) plus the legend bar (flow / back / context) |
| Dock | Five panes: **Nodes**, **Edges**, **Look**, **Logos**, **Topology** |

## Nodes pane

- **Starter** — inserts a ready-made diagram (replaces the current one).
- **Node list** — one card per node. `Column` decides the lane: `1` = left, `2` =
  centre, and so on, matching the `columns` array in the JSON.
- **Add node** — appends a node to the last column.
- Drag a logo from the **Logos** pane onto a card to set its glyph.

## Edges pane

One row per cable. `Label` is the context printed above the cable (for example
`POST /order` or `SQL`); `back` draws the return path, which is how a request /
response pair stays readable.

## Look pane

Theme and scale for the preview: the same keys the renderer accepts (`vertical`,
`columns`, `groups`, `legend`, `facilities`, colour slots).

## Logos pane

Searchable logo picker (`docker`, `nginx`, `burp`, …). Picking one assigns it to the
selected node; the glyph is emitted as the node's logo URL, so the exported block
carries the asset with it.

## Topology pane

The raw JSON, editable in place. This is the authoritative view: every change in the
other panes is a change to this document, and edits here re-render the preview.

## Export

- **Copy ```topology** — copies the fenced block, ready to paste into a Markdown file.
- **Export** — downloads `topology.md` containing the fenced block.
- **Guides** — toggles editor-only alignment guides; they are never exported.

## Where the block goes

Paste the exported block into any article or reference page that loads
`js/topology.js`. On this site that includes `read.html` (blog posts and
references) — see [Blog Post Template](https://imoon07.github.io/read.html?post=blog-post-template)
for a render test that mixes ` ```topology `, ` ```alur `, tables, and footnotes.

## Relationship to the other editors

- `topology.html` — this editor: topology diagrams, column layout, cable labels.
- `draw.html` — [Alur Visual Engine & draw.html](imoon-alur-draw-en.md): freeform
  canvas (shapes, arrows, tables, charts) emitted as ` ```alur ` blocks.

They are separate on purpose: a topology diagram is a structured, auto-laid-out
JSON document, while an Alur scene is a free canvas. The preview here is the
renderer, so a block exported from this page never needs a screenshot.