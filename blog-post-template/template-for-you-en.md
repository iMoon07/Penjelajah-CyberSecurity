# Write for Fun, Build for Enjoy

![Explore, Write, Build, Enjoy](./explore-write-build-enjoy.png)

[🇮🇩 Baca dalam Bahasa Indonesia](template-for-you-id.md)
[🇲🇾 Baca dalam Bahasa Melayu](template-for-you-ms.md)
[🇵🇭 Basahin sa Tagalog](template-for-you-tl.md)

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

## Conclusion

This article is still an experiment, but its purpose is simple: to make sure my blog can display Markdown cleanly, comfortably, and enjoyably—for both casual writing and technical writing.

Readers should be able to follow the text, inspect code blocks clearly, navigate a long article, open images, read footnotes, view diagrams, open regular media links, and watch YouTube through a thumbnail or embed.

The renderer should add good presentation and interaction without changing the original Markdown source or making content disappear.

The final goal is simple: a blog that is comfortable to read, clean, responsive, and still feels like a place where I write for fun.