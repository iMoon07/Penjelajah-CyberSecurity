# Write for Fun, Build for Enjoy

![Explore, Write, Build, Enjoy](./explore-write-build-enjoy.png)

[🇮🇩 Baca dalam Bahasa Indonesia](template-for-you-id.md)
[🇲🇾 Baca dalam Bahasa Melayu](template-for-you-ms.md)
[🇵🇭 Basahin sa Tagalog](template-for-you-tl.md)

> Render test template for [imoon07.github.io](https://imoon07.github.io/) — *Built portofolio to success.*

﷽

Hello, and welcome to my blog.

This blog is my space for exploration. It is where I write about things I am learning, try new ideas, save my experiments, and build things simply because it feels enjoyable.

I do not know everything yet, and I do not want to pretend that I do. I prefer to start from curiosity: try something, make a mistake, get confused, search online, make another mistake, and eventually make it work.

Think of this as my mantra:

> **Explore. Write. Build. Enjoy. Repeat.**

In a freer translation: explore, write, build, enjoy, repeat. In its more honest version: open the laptop, get confused, drink some water, and try again.

## Why this article exists

This is a **testing post** for my blog.

I recently redesigned the look of my blog, especially the typography, spacing, headings, lists, tables, images, links, and code blocks. Then I realized something: designing the layout is one thing, but making sure every type of content still renders properly is another story.

So this article is basically a practice ground. I throw almost every Markdown syntax at it, then see what looks good and what makes me think, “wait, why does it look like that?”

This article is written for two kinds of content:

- **Non-technical writing**, such as daily notes, opinions, reflections, and exploration stories.
- **Technical writing**, such as tutorials, learning notes, documentation, and experiments.

Think of it as a visual checklist:

- Is the heading hierarchy comfortable to read?
- Are paragraphs comfortable for long reading sessions?
- Do lists, tables, and callouts look clean?
- Do code blocks have syntax highlighting, line numbers, and a copy button?
- Do images, captions, and links work properly?
- Can YouTube appear as interactive media?
- Do footnotes, math, diagrams, and HTML elements remain safe?
- Does everything still make sense on mobile?

So yes, this is not a super serious article. It is a place for me to test my blog while still writing in a relaxed way.

> **Note:** If something looks strange, that means it is probably being tested. It is not necessarily your fault; I probably just have not found the bug yet.

## What is being tested?

- Reading comfort and typography for long-form content.
- Heading hierarchy and table of contents.
- Bold, italic, strikethrough, and inline code.
- Ordered lists, unordered lists, nested lists, and checklists.
- Blockquotes, nested blockquotes, and callouts.
- Inline technical content and special characters.
- Code blocks with syntax highlighting, line numbers, hover, selection, and copy.
- Long lines, whitespace, and source integrity.
- Reading progress.
- Local images, external images, captions, and fallbacks.
- Regular tables and wide tables.
- External links, internal anchors, autolinks, and reference links.
- Regular media and YouTube media.
- Footnotes, math, diagrams, and basic HTML.
- Responsive behavior across desktop, tablet, and mobile.
- Accessibility and keyboard/touch interactions.
- Long-form content integrity.

---

## 01 — Reading Experience

### A comfortable reading rhythm

Technical writing often alternates between explanation, commands, output, and interpretation. The transition between these elements should feel natural, not like riding a roller coaster without a seatbelt.

The body text should have a readable line length, generous but controlled line-height, and clear paragraph spacing. Headings should help readers understand the structure, not make the page feel like a corporate meeting.

Ideally, a reader can scan the article quickly, stop at an important paragraph, inspect a code block, and return to the explanation without losing their place.

Consider these common terms: `Content-Security-Policy`, `X-Forwarded-For`, `application/json`, `0xDEADBEEF`, `snake_case`, `camelCase`, `__init__()`, and `user_id`.

They should remain legible within normal sentences and wrap correctly when the viewport becomes narrow.

### Text formatting

This is **bold text**, *italic text*, and ~~strikethrough text~~.

You can also combine **bold emphasis** with `inline code`, reference an [external resource](https://example.com), or use an ordinary internal article anchor.

The styling should preserve readability without making every sentence look like a collection of colorful cards.

### Heading hierarchy

#### Third-level heading

##### Fourth-level heading

###### Sixth-level heading

These headings exist to test hierarchy and anchor generation. The table of contents should follow the renderer's configured heading-depth rules, avoid duplicate IDs, and maintain stable links.

## 02 — Article Metadata and Editorial Layout

The article header should accommodate:

- A prominent title and optional subtitle.
- Author avatar, name, and profile link.
- Publication date and optional update date.
- Estimated reading time.
- Categories, tags, and language selection.
- A short introduction or summary.
- Optional cover image.

Metadata should remain visually secondary to the article title. Long titles, multiple tags, missing avatars, and translated titles must not break the layout.

On mobile, metadata should wrap naturally rather than overflow horizontally, forcing readers to scroll sideways like they are reading a newspaper from 1998.

## 03 — Lists, Steps, and Technical Notes

### Investigation workflow

1. Establish the scope and objectives.
2. Prepare the testing environment.
3. Identify the relevant application components.
4. Execute the planned checks.
5. Record observations and supporting evidence.
6. Verify the findings.
7. Document conclusions and limitations.

### Nested procedures

1. **Environment preparation**
   - Verify system requirements.
   - Confirm network connectivity.
   - Check application dependencies.

2. **Testing**
   - Capture requests and responses.
   - Inspect relevant application behavior.
   - Compare observations with expected results.

3. **Reporting**
   - Summarize the evidence.
   - Explain the impact.
   - Document remediation options.

### Checklist

- [ ] Test environment documented.
- [ ] Application endpoints identified.
- [ ] All observations independently verified.
- [ ] Final report reviewed.

### Editorial callouts

> **Note:** Use callouts to provide supporting context without interrupting the main explanation.

> **Warning:** A warning should communicate a genuine risk. Do not use warning styling for ordinary information.

> **Important:** This article is only a rendering test. Nothing here needs to be taken too seriously.

These elements use standard Markdown blockquotes. If the renderer supports richer callouts, their presentation should be derived from a documented convention or existing metadata, not from fragile visual guesses.

## 04 — Inline Technical Content

Inline code should work inside paragraphs, lists, tables, and links.

For example, the command `sudo ./check-blog.sh` can be discussed in the same sentence as the expected HTTP status, an `application/json` response, or a configuration value such as `timeout_ms`.

Identifiers that differ only in capitalization must remain distinguishable: `ContentType`, `contentType`, `content_type`, and `CONTENT_TYPE`.

Special characters should survive parsing and rendering: `<`, `>`, `&`, quotes, backslashes, dollar signs, braces, brackets, and Unicode characters.

International text: Indonesia, 日本語, العربية, Español, Ελληνικά, and 🔐.

The renderer must not confuse literal code characters with HTML markup or Markdown syntax.

## 05 — Interactive Code Playground

This section tests the article renderer's primary code presentation feature.

The desired interface is one interactive playground with a language selector, rather than a separate UI card for every programming language. The reader should be able to choose a supported language and inspect its syntax highlighting while keeping the code panel, line numbers, controls, and reading position consistent.

### Playground requirements

- A searchable language selector when the number of available languages warrants it.
- Broad grammar support, including aliases and less common languages.
- Extensible language registration.
- Accurate line numbers and syntax highlighting.
- Line hover and a distinct active or selected line.
- Copy code without copying line numbers.
- Optional line wrapping.
- Horizontal scrolling for long source lines.
- Keyboard-accessible controls.
- A mobile-friendly selector and touch interactions.
- A readable plain-text fallback for unknown languages.
- No loss or mutation of the original source.

The language selector must not be presented as a built-in Markdown feature. Standard fenced Markdown identifies a code block and may identify its language, but a multi-language playground requires renderer-level functionality.

### Primary source fixture

The following is the single canonical code sample in this document. It deliberately contains enough lines, indentation, comments, strings, and nested structures to test the main code presentation.

```javascript
/**
 * Blog Renderer Test
 *
 * Inspect line numbers, syntax colors, indentation,
 * hover behavior, selection, copy, and scrolling.
 */

const configuration = {
  project: "My Personal Blog",
  environment: "local",
  features: {
    syntaxHighlighting: true,
    lineNumbers: true,
    copyButton: true,
    lineHighlighting: true,
  },
};

function summarizeNotes(notes) {
  return notes
    .filter((note) => note.published)
    .map((note, index) => ({
      number: index + 1,
      title: note.title,
      status: note.status,
    }));
}

async function loadArticle(url, options = {}) {
  if (!url) {
    throw new Error("An article URL is required");
  }

  const response = await fetch(url, {
    ...options,
    headers: {
      Accept: "application/json",
      ...options.headers,
    },
  });

  if (!response.ok) {
    throw new Error(`Request failed: HTTP ${response.status}`);
  }

  return response.json();
}

const exampleNotes = [
  {
    title: "Testing typography",
    status: "published",
    published: true,
  },
  {
    title: "Draft experiment",
    status: "draft",
    published: false,
  },
];

console.log(summarizeNotes(exampleNotes));
```

### Code interaction behavior

When the pointer moves across the source, the current line should receive a subtle highlight. The line-number gutter should remain aligned with the code, including when the code panel scrolls horizontally.

A selected line or range should have a separate visual state from hover. The interaction must not prevent ordinary text selection, keyboard navigation, or copying.

The copy button should provide visible and accessible feedback. If clipboard access fails, the reader should receive an appropriate fallback instead of a false “Copied!” state.

For large snippets, the interface may offer expand and collapse controls. Collapsing must never destroy the source content, and all hidden content must remain accessible through a clear interaction.

### Language support policy

The selector should expose the languages available through the chosen syntax-highlighting engine and any registered extensions.

The implementation must not rely on a hardcoded short list as its permanent language boundary. It should support language aliases, optional grammar loading, and graceful fallback when a grammar is unavailable.

A new language should be addable without redesigning the article page. Unknown languages must remain readable as plain text.

The source sample above is the canonical Markdown code fixture. Testing actual syntax across every supported grammar should be automated using a separate language corpus, rather than duplicating dozens of code blocks in this article.

## 06 — Long Lines, Whitespace, and Source Integrity

Long source lines should remain accessible without forcing the entire page to become wider than the viewport.

The renderer should offer horizontal scrolling by default for code where wrapping would damage alignment or meaning. If soft wrapping is available, line numbers must remain understandable even when one source line occupies several visual rows.

Whitespace matters. Indentation, blank lines, tabs, trailing newlines, and Unicode characters should be preserved according to the source and renderer's documented behavior.

A source line such as `if (response.status !== 200) {` must remain intact. Operators such as `===`, `!==`, `=>`, `->`, `::`, and `&&` must not be replaced by typographic lookalikes.

Line highlighting and line-number anchors should reference source lines, not merely the current visual rows.

## 07 — Reading Progress

The reading progress indicator should reflect the reader's actual position in the article.

It should:

- Update smoothly during scrolling.
- Remain unobtrusive.
- Handle short and long articles.
- Account for the article's actual content boundaries.
- Remain accurate when images finish loading.
- Avoid reporting completion while substantial article content remains unread.
- Respect reduced-motion preferences.

The progress indicator should complement the reading experience, not become an animation more interesting than the article itself.

## 08 — Table of Contents

The table of contents should be generated from eligible headings in the rendered Markdown.

Expected behavior:

- Nested heading structure.
- Stable heading anchors.
- An active section indicator.
- Smooth navigation when appropriate.
- Sticky navigation on desktop where space permits.
- A compact drawer, dropdown, or equivalent on mobile.
- Correct behavior for duplicate headings.
- No overlap with fixed headers or reading progress.
- No broken navigation when media changes document height.

TOC generation must use the same heading IDs as the actual rendered article.

## 09 — Images and External Media

### Local cover image

![Explore, Write, Build, Enjoy](./explore-write-build-enjoy.png)

*Caption: local image test for cover rendering, responsive sizing, and fallback behavior.*

### Landscape image

![Landscape placeholder for article media testing](https://placehold.co/1600x900?text=Landscape+Image)

*Caption: test image for responsive sizing, loading behavior, aspect ratio, and caption typography.*

### Additional image

![Technology hardware detail](https://placehold.co/1200x800?text=Technology+Detail)

*Caption: a second image for testing repeated media, spacing, and gallery transitions.*

### Media behavior

Test the following through ordinary Markdown images and supported links:

- Local images and externally hosted images.
- Portrait, landscape, and square aspect ratios.
- Alt text and captions.
- Lazy loading and reserved image dimensions.
- Image zoom or lightbox where supported.
- Broken URLs and unavailable media.
- Redirects, slow responses, and unsupported formats.
- Video and third-party embeds where the renderer explicitly supports them.

External image URLs should not be assumed to be universally fetchable. Browser restrictions, CORS, authentication, hotlink protection, and remote server failures can prevent access.

A failed image must not remove neighboring text, shift the reader unexpectedly, or break the TOC.

## 10 — Tables and Structured Data

| Feature | Expected behavior | Priority |
| --- | --- | --- |
| Syntax highlighting | Clear language-specific colors | Critical |
| Line numbers | Stable source-line alignment | Critical |
| Copy action | Copies source without the gutter | Critical |
| Reading progress | Accurate article position | High |
| Table of contents | Stable navigation and active section | High |
| Image lightbox | Accessible media enlargement | Medium |
| Related articles | Relevant navigation after the article | Medium |

### Wide technical table

| Endpoint | Method | Authentication | Content type | Expected response | Purpose |
| --- | --- | --- | --- | --- | --- |
| `/api/health` | `GET` | Optional | `application/json` | `200 OK` | Health check |
| `/api/notes` | `GET` | Required | `application/json` | `200 OK` | Retrieve notes |
| `/api/notes/export` | `POST` | Required | `application/json` | `202 Accepted` | Start export |
| `/api/notes/status` | `GET` | Required | `application/json` | `200 OK` | Check export status |

On narrow screens, a wide table should use a deliberate responsive strategy. Local horizontal scrolling is preferable to shrinking text until readers need a magnifying glass.

## 11 — Links and References

### External links

- [My GitHub Pages blog](https://github.com/iMoon07/imoon07.github.io/)
- [Example Domain](https://example.com)
- [GitHub](https://github.com)
- [MDN Web Docs](https://developer.mozilla.org)
- [Shiki documentation](https://shiki.style)
- [Rehype Pretty Code](https://rehype-pretty.pages.dev/)

External links should have recognizable styling, usable focus states, and appropriate handling for links that open a new tab.

### Link with title

[GitHub with title](https://github.com "Visit GitHub")

### Autolinks

https://example.com

<https://example.com>

### Reference links

This is a [reference link][gh].

[gh]: https://github.com "GitHub"

### Internal anchor

Jump back to [Reading Experience](#01--reading-experience).

Internal links should navigate to the correct article heading. Anchor generation must remain stable for repeated headings and headings containing punctuation or non-English characters.

## 12 — Regular Media and YouTube

Some articles need more than images and source code. The renderer should be able to distinguish between **regular media** and **YouTube media**.

There are two media behaviors to test:

1. **Regular media** — normal external links that remain regular links.
2. **YouTube media** — YouTube links that can be detected, fetched, and rendered as an interactive video card.

### Regular media

Regular media links should remain simple, accessible, and predictable. The renderer does not need to turn every external URL into an embed.

- [Example website](https://example.com)
- [GitHub repository](https://github.com)
- [MDN Web Docs](https://developer.mozilla.org)
- [Shiki documentation](https://shiki.style)

External links should have recognizable styling, usable focus states, and appropriate handling for links that open a new tab.

A regular link should not automatically become an embed. It should remain a normal link unless the renderer has an explicit rule for that domain.

### YouTube media

YouTube links are a special case. The renderer should be able to detect a YouTube URL, extract the video ID, fetch public metadata, and display an interactive video card.

The following link should be recognized as a YouTube video:

[Watch on YouTube](https://www.youtube.com/watch?v=8rkiwXkEA8M&list=PLsOgFqR0cppAEuYATcmAxyHeSTkWM4ZWj)

Expected renderer behavior:

- Detect the YouTube URL.
- Extract the video ID: `8rkiwXkEA8M`.
- Fetch public metadata through a safe backend endpoint.
- Display the video title, channel name, and high-quality thumbnail.
- Show a play button or interactive preview.
- Load the YouTube iframe only after the reader clicks play.
- Provide a direct fallback link if fetching or embedding fails.

The renderer should cache the fetched metadata so it does not request YouTube on every page load.

### YouTube thumbnail with play button

If interactive fetching is not available yet, this version should still render well: a YouTube thumbnail with a play button in the center.

<a
  href="https://www.youtube.com/watch?v=8rkiwXkEA8M&list=PLsOgFqR0cppAEuYATcmAxyHeSTkWM4ZWj"
  target="_blank"
  rel="noopener noreferrer"
  style="position: relative; display: block; max-width: 800px; margin: 0 auto;"
>
  <img
    src="https://img.youtube.com/vi/8rkiwXkEA8M/hqdefault.jpg"
    alt="Watch the video on YouTube"
    style="width: 100%; height: auto; display: block; border-radius: 12px;"
  />

  <span
    style="
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 72px;
      height: 72px;
      background: rgba(0, 0, 0, 0.65);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-size: 28px;
    "
  >
    ▶
  </span>
</a>

*Caption: YouTube thumbnail with a play button. Click the image to open the video.*

### YouTube embed fallback

If the renderer supports YouTube iframes, the video should render directly.

<iframe
  width="100%"
  height="480"
  src="https://www.youtube.com/embed/8rkiwXkEA8M"
  title="YouTube video player"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  allowfullscreen>
</iframe>

Each media type should have a clear fallback. If an external embed cannot load, the reader should still have access to the surrounding explanation and a direct link where available.

Do not execute arbitrary scripts from Markdown. HTML, embeds, SVG, and externally supplied content must follow the application's sanitization and security policy.

External metadata should be fetched through a controlled backend, with request timeouts, response-size limits, caching, and validation for allowed domains.

## 13 — Responsive Reading

Evaluate the same article at desktop, tablet, and mobile widths.

### Desktop

The article should have a comfortable prose column, with wider code panels where appropriate. A sticky TOC may occupy the side column if sufficient space exists.

### Tablet

The article should retain readable text and code. Secondary navigation may become more compact, and code controls should not compete for horizontal space.

### Mobile

The article should prioritize the text and keep interactive controls usable with touch. Code blocks may scroll horizontally within their own boundaries. Tables should remain accessible, images should scale correctly, and sticky elements must not obscure the content.

Test both portrait and landscape orientation, browser zoom, and increased text size.

## 14 — Accessibility and Interaction

All essential interactions must work without a mouse.

- Keyboard-accessible language selection.
- Clear focus indicators.
- Accessible copy feedback.
- Screen-reader-friendly line-number behavior.
- Sufficient contrast in light and dark themes.
- Reduced-motion support.
- Touch alternatives to hover interactions.
- Meaningful image alt text.
- Semantic headings, lists, tables, and links.

Syntax colors must not be the only way to communicate important information. Hover effects should remain subtle and must not interfere with text selection.

## 15 — Long-Form Content Integrity

This fixture should also be combined with generated stress-test documents.

Test progressively larger Markdown documents, for example 10 KB, 100 KB, 1 MB, and larger sizes appropriate to the application.

Include repeated paragraphs, nested headings, large lists, wide tables, remote images, and code samples containing thousands of lines.

Verify that:

- Every source paragraph remains accessible.
- No source lines disappear.
- Character encoding and indentation remain correct.
- Headings and anchors remain valid.
- Copy actions return the intended source.
- Rendering does not duplicate content.
- Media failures do not erase unrelated sections.
- The page does not acquire unwanted horizontal overflow.
- Memory usage and rendering latency are measured.
- Resource limits are handled explicitly rather than through silent truncation.

Do not claim mathematical unlimitedness. The requirement is to avoid arbitrary content-length limits and ensure that large documents have a defined, tested performance strategy.

If progressive rendering or virtualization is needed, preserve search, selection, source-line numbering, anchor navigation, and access to the complete article.

## 16 — Extended Markdown Coverage

This section tests additional syntax that is often useful for both technical and non-technical writing.

### Line breaks

This is the first line.  
This is the second line using two trailing spaces.

This is another line using a backslash.\
This should also break.

### Escaping

\*This should not become italic.\*

\# This should not become a heading.

\`This should not become inline code.\`

### Nested blockquote

> First level
>
> > Second level
> >
> > > Third level

### Footnotes

This sentence has a footnote.[^1]

[^1]: This is the footnote content.

### Ordered list with custom start

3. Third item
4. Fourth item
5. Fifth item

### Emphasis nesting

***Bold italic text***

**Bold with *nested italic* text**

*Italic with **nested bold** text*

### Code block without language

```
This is plain text.
No syntax highlighting expected.
```

### HTML-based elements

<details>
  <summary>Click to expand</summary>

  This content is inside a collapsible section.

</details>

Press <kbd>Ctrl</kbd> + <kbd>C</kbd> to copy.

<mark>Highlighted text</mark>

### Math

Inline math: $E = mc^2$

Block math:

$$
\int_{a}^{b} f(x)\,dx
$$

### Mermaid diagram

```mermaid
flowchart TD
  A[Write Markdown] --> B[Render Blog]
  B --> C{Looks good?}
  C -- Yes --> D[Publish]
  C -- No --> E[Fix CSS]
  E --> B
```

### Definition list

Term
: Definition of the term.

Another term
: Another definition.

### Highlight, subscript, and superscript

This is ==highlighted text==.

Water is H~2~O.

This is x^2^.

> **Note:** `footnotes`, `math`, `mermaid`, `==highlight==`, `~subscript~`, and `^superscript^` depend on renderer extensions. If they do not render, it does not necessarily mean the base Markdown is wrong.

## 17 — Final Verification Checklist

- [ ] Markdown content remains intact.
- [ ] Typography is comfortable for long reading sessions.
- [ ] Heading hierarchy and TOC agree.
- [ ] Reading progress follows the actual article.
- [ ] The code playground supports all registered grammars.
- [ ] Unknown languages fall back gracefully.
- [ ] Line numbers correspond to source lines.
- [ ] Hover does not interfere with selection.
- [ ] Copy excludes presentation-only line numbers.
- [ ] Long code lines do not overflow the entire page.
- [ ] Whitespace and Unicode characters are preserved.
- [ ] Wide tables remain usable on mobile.
- [ ] Images have appropriate fallbacks.
- [ ] External links, internal anchors, autolinks, and reference links work.
- [ ] Regular media links remain regular links.
- [ ] YouTube thumbnails with play buttons render correctly.
- [ ] YouTube embeds or metadata fetching work according to renderer capability.
- [ ] Footnotes, math, diagrams, and HTML elements render safely.
- [ ] Keyboard and touch interactions work.
- [ ] Browser zoom does not hide content.
- [ ] Large documents are tested for performance.
- [ ] No arbitrary character limit silently truncates the article.
- [ ] The existing Discuss feature remains functional.

## 18 — Alur Visual Lab

> **Note:** This section is a live render test for the Alur engine. One ` ```draw-tabs ` block below switches previews with buttons. The engine source lives in `imoon07.github.io/js/alur/`. **Preview/playground:** `http://localhost:8000/imoon07.github.io/draw.html` (or `https://iMoon07.github.io/draw.html`) — switch module, template, cable, motion, speed, and pick from all 575 logos.

### 18.1 Visual catalog

One draw block: use the buttons to switch visuals. It covers flow, reverse proxy, pipeline, graph, cables, motion, and 29 charts.

```draw-tabs
[
  {"label":"Flow with logos","spec":{"module":"flow","title":"Request path with logos","cable":"neon","motion":"comet","columns":[["client"],["edge"],["app1","app2"],["db"],["sec1","sec2"]],"nodes":{"client":{"label":"Client","sub":"browser","logo":"stack:github","color":"blue"},"edge":{"label":"Edge","sub":"nginx","logo":"stack:nginx","color":"cyan"},"app1":{"label":"App A","sub":"node","logo":"programming:nodejs","color":"green"},"app2":{"label":"App B","sub":"python","logo":"programming:python","color":"amber"},"db":{"label":"Data","sub":"postgres + redis","logos":["stack:postgresql","stack:redis"],"color":"purple"},"sec1":{"label":"Wireshark","sub":"capture","logo":"security:wireshark","color":"lime"},"sec2":{"label":"Nmap","sub":"scan","logo":"security:nmap","color":"amber"}},"edges":[["client","edge","TLS"],["edge","app1"],["edge","app2"],["app1","db"],["app2","db"],["app1","sec1"],["app2","sec2"]]}},
  {"label":"Reverse proxy","spec":{"module":"reverse-proxy","title":"Reverse Proxy: Single Front, Many Backends","speed":1}},
  {"label":"Pipeline with logos","spec":{"module":"pipeline","title":"Request pipeline","stages":[{"label":"Client","logo":"stack:github"},{"label":"Edge","logo":"stack:nginx"},{"label":"App","logo":"programming:nodejs"},{"label":"DB","logo":"stack:postgresql"}],"color":"cyan","items":4}},
  {"label":"BFS graph","spec":{"module":"graph","title":"BFS traversal","color":"green","start":"a","nodes":[{"id":"a","x":140,"y":90,"label":"A","logo":"stack:docker"},{"id":"b","x":330,"y":60,"label":"B"},{"id":"c","x":330,"y":150,"label":"C"},{"id":"d","x":520,"y":40,"label":"D"},{"id":"e","x":520,"y":120,"label":"E","logo":"stack:kubernetes"},{"id":"f","x":520,"y":200,"label":"F"},{"id":"g","x":710,"y":80,"label":"G","logo":"stack:prometheus"},{"id":"h","x":710,"y":170,"label":"H","logo":"stack:grafana"}],"edges":[{"from":"a","to":"b","w":4},{"from":"a","to":"c","w":2},{"from":"b","to":"d","w":5},{"from":"b","to":"e","w":3},{"from":"c","to":"e","w":2},{"from":"c","to":"f","w":6},{"from":"d","to":"g","w":4},{"from":"e","to":"g","w":2},{"from":"e","to":"h","w":5},{"from":"f","to":"h","w":3}]}},
  {"label":"Cable styles","spec":{"module":"flow","title":"Cable styles","cable":"solid","columns":[["a","b","c"],["d","e","f"]],"nodes":{"a":{"label":"Alpha","color":"blue"},"b":{"label":"Beta","color":"green"},"c":{"label":"Gamma","color":"amber"},"d":{"label":"Delta","color":"purple"},"e":{"label":"Epsilon","color":"cyan"},"f":{"label":"Zeta","color":"pink"}},"edges":[{"from":"a","to":"d","cable":"neon","motion":"none"},{"from":"b","to":"e","cable":"bundle","motion":"none"},{"from":"c","to":"f","cable":"relay","motion":"none"},{"from":"a","to":"d","cable":"ribbon","motion":"none"},{"from":"b","to":"e","cable":"dashed","motion":"none"},{"from":"c","to":"f","cable":"circuit","motion":"none"}]}},
  {"label":"Table (editable)","spec":{"module":"canvas","title":"Editable table","grid":false,"nodes":{"t1":{"id":"t1","x":20,"y":20,"w":700,"h":260,"shape":"table","color":"slate","columns":["Check","Status","Owner"],"rows":[["TLS terminator","pass","edge"],["WAF rules","review","sec"],["Backup restore","pass","ops"]]}},"edges":[]}},
  {"label":"Motion effects","spec":{"module":"flow","title":"Motion effects","cable":"solid","columns":[["a","b","c"],["d","e","f"]],"nodes":{"a":{"label":"Alpha","color":"blue"},"b":{"label":"Beta","color":"green"},"c":{"label":"Gamma","color":"amber"},"d":{"label":"Delta","color":"purple"},"e":{"label":"Epsilon","color":"cyan"},"f":{"label":"Zeta","color":"pink"}},"edges":[{"from":"a","to":"d","motion":"comet"},{"from":"b","to":"e","motion":"packets"},{"from":"c","to":"f","motion":"flowMany"},{"from":"a","to":"d","motion":"dash"},{"from":"b","to":"e","motion":"draw"},{"from":"c","to":"f","motion":"relay"}]}},
  {"label":"Bar","spec":{"module":"chart","type":"bar","title":"Bar","labels":["Jan","Feb","Mar","Apr","May"],"data":[12,18,15,22,28],"color":"blue"}},
  {"label":"Horizontal bar ranking","spec":{"module":"chart","type":"hbar","title":"Horizontal bar ranking","labels":["Nginx","Postgres","Redis","PHP","Go"],"data":[42,31,24,18,12],"color":"cyan"}},
  {"label":"Multi-series line","spec":{"module":"chart","type":"line","title":"Multi-series line","labels":["Mon","Tue","Wed","Thu","Fri"],"series":[{"name":"web","data":[12,18,15,22,28],"color":"blue"},{"name":"api","data":[8,11,14,12,18],"color":"green"}]}},
  {"label":"Area","spec":{"module":"chart","type":"area","title":"Area","labels":["Mon","Tue","Wed","Thu","Fri"],"data":[8,12,10,16,20],"color":"cyan"}},
  {"label":"Stacked bar composition","spec":{"module":"chart","type":"stacked","title":"Stacked bar composition","labels":["Mon","Tue","Wed","Thu"],"series":[{"name":"web","data":[12,14,10,16],"color":"blue"},{"name":"api","data":[8,9,12,11],"color":"green"},{"name":"job","data":[5,6,4,7],"color":"amber"}]}},
  {"label":"Donut percent breakdown","spec":{"module":"chart","type":"donut","title":"Donut percent breakdown","labels":["Web","API","DB","Cache"],"data":[38,27,21,14],"colors":["blue","green","amber","purple"],"centerLabel":"requests"}},
  {"label":"Single-value percent gauge","spec":{"module":"chart","type":"gauge","title":"Single-value percent gauge","data":[68],"max":100,"unit":"%","label":"cache hit","color":"cyan"}},
  {"label":"Spark line","spec":{"module":"chart","type":"spark","title":"Spark line","data":[3,5,4,7,6,9,8,11],"color":"green"}},
  {"label":"KPI callout","spec":{"module":"chart","type":"kpi","title":"KPI callout","data":[128],"label":"requests / sec","delta":"+12.4%"}},
  {"label":"Scatter plot","spec":{"module":"chart","type":"scatter","title":"Scatter plot","data":[[3,5],[5,8],[8,7],[11,12],[14,13],[17,18],[20,17]],"color":"purple"}},
  {"label":"Waterfall","spec":{"module":"chart","type":"waterfall","title":"Waterfall","labels":["Start","Add","Cache","Drop","End"],"data":[40,18,12,-9,21],"color":"blue"}},
  {"label":"Funnel conversion","spec":{"module":"chart","type":"funnel","title":"Funnel conversion","labels":["Visit","Signup","Active","Paid"],"data":[100,62,38,17],"colors":["blue","cyan","green","amber"]}},
  {"label":"Bell curve with marker","spec":{"module":"chart","type":"bell","title":"Bell curve with marker","mean":0,"sigma":1,"marker":0.6,"markerLabel":"p95","color":"blue"}},
  {"label":"Histogram","spec":{"module":"chart","type":"histogram","title":"Histogram","bins":8,"data":[1,2,2,3,3,3,4,4,4,5,5,6],"color":"cyan"}},
  {"label":"Stacked area trend","spec":{"module":"chart","type":"stackedArea","title":"Stacked area trend","labels":["Mon","Tue","Wed","Thu","Fri"],"series":[{"name":"web","data":[8,10,9,12,14],"color":"blue"},{"name":"api","data":[5,6,7,6,9],"color":"green"},{"name":"job","data":[3,4,3,5,6],"color":"amber"}]}},
  {"label":"Treemap","spec":{"module":"chart","type":"treemap","title":"Treemap","labels":["Web","API","DB","Cache","Queue"],"data":[38,27,18,11,6],"colors":["blue","green","amber","purple","pink"]}},
  {"label":"Box plot","spec":{"module":"chart","type":"box","title":"Box plot","boxes":[{"label":"Web","min":2,"q1":5,"median":8,"q3":11,"max":14},{"label":"API","min":3,"q1":6,"median":9,"q3":12,"max":16},{"label":"DB","min":1,"q1":4,"median":7,"q3":10,"max":13}]}},
  {"label":"Range bar with thresholds","spec":{"module":"chart","type":"range","title":"Range bar with thresholds","items":[{"label":"p50","from":20,"to":60},{"label":"p95","from":70,"to":140},{"label":"p99","from":150,"to":260}],"color":"amber"}},
  {"label":"Density curve","spec":{"module":"chart","type":"density","title":"Density curve","series":[{"name":"web","data":[0.05,0.2,0.6,0.9,0.6,0.2,0.05],"color":"blue"},{"name":"api","data":[0.1,0.3,0.5,0.7,0.5,0.3,0.1],"color":"amber"}]}},
  {"label":"Slope chart","spec":{"module":"chart","type":"slope","title":"Slope chart","items":[{"label":"Web","before":20,"after":48},{"label":"API","before":35,"after":28},{"label":"DB","before":12,"after":26}],"color":"cyan"}},
  {"label":"Two-axis combo","spec":{"module":"chart","type":"combo","title":"Two-axis combo","labels":["Mon","Tue","Wed","Thu","Fri"],"bars":[120,140,130,160,180],"line":[3,4,3.5,5,6],"color":"blue"}},
  {"label":"Annotated timeline","spec":{"module":"chart","type":"timeline","title":"Annotated timeline","events":[{"label":"deploy","at":0.1},{"label":"cache warm","at":0.35},{"label":"peak","at":0.6},{"label":"rollback drill","at":0.85}],"color":"green"}},
  {"label":"Bubble chart","spec":{"module":"chart","type":"bubble","title":"Bubble chart","data":[[3,4,2],[5,7,4],[8,6,3],[11,9,5],[14,12,6],[17,11,4]],"color":"purple"}},
  {"label":"Dumbbell plot","spec":{"module":"chart","type":"dumbbell","title":"Dumbbell plot","items":[{"label":"Web","a":20,"b":48},{"label":"API","a":35,"b":28},{"label":"DB","a":12,"b":26}]}},
  {"label":"Quadrant matrix","spec":{"module":"chart","type":"quadrant","title":"Quadrant matrix","q1":"scale","q2":"invest","q3":"fix","q4":"watch","data":[[2,8],[5,6],[7,3],[9,7],[4,4]],"color":"cyan"}},
  {"label":"Process flow steps","spec":{"module":"chart","type":"process","title":"Process flow steps","steps":["plan","build","test","ship"],"color":"green"}},
  {"label":"Cycle loop stages","spec":{"module":"chart","type":"cycle","title":"Cycle loop stages","steps":["plan","build","test","ship"],"color":"purple"}},
  {"label":"Progress bar stack","spec":{"module":"chart","type":"progress","title":"Progress bar stack","items":[{"label":"Web","parts":[{"value":60,"color":"blue"},{"value":25,"color":"green"},{"value":15,"color":"amber"}]},{"label":"API","parts":[{"value":40,"color":"cyan"},{"value":35,"color":"purple"},{"value":25,"color":"pink"}]}]}},
  {"label":"Comparison table","spec":{"module":"chart","type":"table","title":"Comparison table","columns":["Tool","Speed","Cost","Use"],"rows":[["Nginx","fast","low","edge"],["Postgres","medium","medium","data"],["Redis","fast","high","cache"]]}}
]
```

### 18.8 Logo library — security tools

All 575 logos from `iMoon07/logo-svg` are available to every node (`"logo": "security:nmap"`). This compact chain shows four representative phases; every tool is a node, and its logo is the catalogue entry.

```topology
{
  "title": "Security toolchain",
  "uniform": true,
  "columns": [
    [
      "recon"
    ],
    [
      "exploit"
    ],
    [
      "post"
    ],
    [
      "forensics"
    ]
  ],
  "nodes": {
    "recon": [
      "Recon",
      "Nmap · Wireshark",
      [
        "security:nmap",
        "security:wireshark"
      ],
      "tech"
    ],
    "exploit": [
      "Exploit",
      "Metasploit · Burp",
      [
        "security:metasploit",
        "security:burp"
      ],
      "tech"
    ],
    "post": [
      "Post-exploit",
      "Mimikatz · Hashcat",
      [
        "security:mimikatz",
        "security:hashcat"
      ],
      "tech"
    ],
    "forensics": [
      "Forensics",
      "Ghidra · Autopsy",
      [
        "security:ghidra",
        "security:autopsy"
      ],
      "tech"
    ]
  },
  "edges": [
    [
      "recon",
      "exploit",
      "1"
    ],
    [
      "exploit",
      "post",
      "2"
    ],
    [
      "post",
      "forensics",
      "3"
    ]
  ],
  "legend": {
    "flow": "Attack phase"
  },
  "facilities": [
    "Security",
    [
      "shield",
      "Hacking toolkit"
    ],
    [
      "terminal",
      "CLI first"
    ]
  ]
}
```

How to read: Recon → Exploit → Post-exploit → Forensics. Each arrow is the next phase; the footer repeats the security context.

## 19 — Topology Visual Lab

`topology` is the static renderer for article diagrams. It has no toolbar, panel, or zoom: the diagram follows the article column width and stacks vertically on narrow screens. Node logos can use the local Alur catalogue (575 logos from iMoon07/logo-svg), for example `"icon": "security:nmap"`.


### 19.1 Restaurant as a server request

Read left → right. Solid arrows are the order/request path; the dashed arrow is the return/response. The footer repeats the direction legend and the place chips, so the picture is not just a picture.

```topology
{
  "title": "The Flow",
  "uniform": true,
  "columns": [
    [
      "C"
    ],
    [
      "P"
    ],
    [
      "K"
    ],
    [
      "G"
    ]
  ],
  "nodes": {
    "C": [
      "Customer",
      "Places an order",
      "stack:github",
      "actor"
    ],
    "P": [
      "Waiter",
      "Takes the order",
      "stack:nginx",
      "process"
    ],
    "K": [
      "Chef",
      "Prepares the order",
      "programming:nodejs",
      "process"
    ],
    "G": [
      "Pantry",
      "Stores ingredients",
      "stack:postgresql",
      "store"
    ]
  },
  "edges": [
    [
      "C",
      "P",
      "1"
    ],
    [
      "P",
      "K",
      "2"
    ],
    [
      "K",
      "G",
      "3"
    ],
    [
      "G",
      "K",
      "4",
      true
    ]
  ],
  "legend": {
    "flow": "Order / request",
    "back": "Return / response"
  },
  "facilities": [
    "In this place",
    [
      "store",
      "Eatery"
    ],
    [
      "wifi",
      "Wi-Fi"
    ]
  ]
}
```

How to read: `Customer → Waiter → Chef → Pantry`. The return arrow `Pantry → Chef` is the response path. Colors group the kitchen side; the footer repeats the legend and the place chips.


### 19.2 Hospital platform

A hospital platform: WAF and cloud edge, PHP runtime stacks (LAMP, LEMP, WAMP, WIMP, FAMP, FIMP), patient data, and a SOC fed by Wazuh and ELK. Solid arrows are the request path; the dashed arrow is the response.

```topology
{
  "title": "Hospital platform",
  "uniform": true,
  "root": [
    "Hospital",
    "integrated platform",
    "building-2",
    "out"
  ],
  "rootWires": false,
  "columns": [
    [
      "edge"
    ],
    [
      "runtime"
    ],
    [
      "data"
    ],
    [
      "soc"
    ]
  ],
  "nodes": {
    "edge": [
      "Edge & WAF",
      "Cloudflare · Nginx · TLS",
      [
        "security:wafw00f",
        "stack:cloudflare",
        "stack:nginx"
      ],
      "network"
    ],
    "runtime": [
      "Runtime stacks",
      "LAMP · LEMP · WAMP · WIMP · FAMP · FIMP",
      [
        "stack:linux",
        "stack:apache",
        "stack:mysql",
        "programming:php"
      ],
      "tech"
    ],
    "data": [
      "Patient data",
      "MariaDB · MySQL · Redis · Postgres",
      [
        "stack:mariadb",
        "stack:mysql",
        "stack:redis",
        "stack:postgresql"
      ],
      "database"
    ],
    "soc": [
      "SOC / ELK",
      "Wazuh · Elasticsearch · Logstash · Kibana",
      [
        "security:wazuh",
        "stack:elasticsearch",
        "stack:logstash",
        "stack:kibana"
      ],
      "process"
    ]
  },
  "edges": [
    [
      "__root__",
      "edge"
    ],
    [
      "edge",
      "runtime"
    ],
    [
      "runtime",
      "data"
    ],
    [
      "data",
      "soc"
    ],
    [
      "data",
      "runtime",
      "",
      true
    ]
  ],
  "legend": {
    "flow": "Request",
    "back": "Response"
  },
  "facilities": [
    "Hospital",
    [
      "building-2",
      "Hospital"
    ],
    [
      "shield",
      "SOC"
    ],
    [
      "cloud",
      "Cloud"
    ]
  ]
}
```

## Conclusion

This article is still an experiment, but its purpose is simple: to make sure my blog can display Markdown cleanly, comfortably, and enjoyably—for both casual writing and technical writing.

Readers should be able to follow the text, inspect code blocks clearly, navigate a long article, open images, read footnotes, view diagrams, open regular media links, and watch YouTube through a thumbnail or embed.

The renderer should add good presentation and interaction without changing the original Markdown source or making content disappear.

The final goal is simple: a blog that is comfortable to read, clean, responsive, and still feels like a place where I write for fun.