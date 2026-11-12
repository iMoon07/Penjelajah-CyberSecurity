# PortSwigger Grid Infographic Style
## Modular Cybersecurity Thumbnail System

Create a professional cybersecurity article thumbnail using the PortSwigger-inspired Grid Infographic Style.

The prompt must adapt dynamically to the supplied lab title, vulnerability category, technical concepts, attack mechanism, and learning objectives.

### 1. Global Visual Identity

Maintain a consistent visual identity across the entire Web Security Academy article collection.

- Canvas: 16:9 landscape, preferably 1920 × 1080.
- Background: clean white with a subtle, evenly spaced square grid.
- Primary colors: deep navy and vibrant PortSwigger-inspired orange.
- Secondary colors: light blue, cool gray, and white.
- Typography: bold, modern, clean sans-serif.
- Illustrations: professional flat-vector cybersecurity illustrations.
- Composition: editorial infographic with clear visual hierarchy.
- Use generous whitespace and balanced visual distribution.
- Use subtle geometric accents, orange brush strokes, and diagonal corner decorations.

### 2. Branding

Use consistent PortSwigger-inspired visual branding.

- Position the PortSwigger wordmark at the upper-left corner.
- Prefer an authentic supplied logo asset when available.
- Do not invent or distort the official logo.
- Maintain consistent placement, proportions, and visual treatment across thumbnails.

### 3. Dynamic Title System

Extract the main topic and supporting title from the supplied article information.

- Main keyword: white typography over a vibrant orange brush-stroke background.
- Secondary keyword: large, bold, deep navy typography.
- Supporting text: optional short technical description or learning objective.
- Keep titles prominent and readable at reduced thumbnail sizes.
- Never place the main title inside an unnecessary rectangular UI box.

The title hierarchy must remain consistent, but its wording must adapt to each lab.

### 4. Dynamic Technical Illustration

Analyze the actual vulnerability before designing the illustration.

Automatically identify:

- The vulnerable component or technology.
- The attacker-controlled input.
- The attack vector.
- The underlying vulnerability mechanism.
- The resulting impact.
- Relevant defense or mitigation concepts, when appropriate.

Build the illustration around the actual technical subject.

Examples of possible visual elements:

- Browser requests and HTTP messages.
- Servers, APIs, databases, and network infrastructure.
- Attackers, clients, and target systems.
- JSON, XML, HTTP headers, cookies, and code snippets.
- Authentication tokens, sessions, and access controls.
- Network connections, proxies, and internal services.
- Race-condition timelines and concurrent requests.
- WebSocket communication flows.
- File paths, upload interfaces, and filesystem structures.

Only include elements that are technically relevant to the supplied article.

### 5. Dynamic Diagram Composition

Do not force every thumbnail into the same diagram layout.

Choose a composition that best communicates the vulnerability:

- Request → Processing → Impact.
- Attacker → Vulnerable Component → Target.
- Browser → Server → Internal Network.
- Input → Injection → Execution.
- Client ↔ Server communication.
- Before vs. After.
- Normal Behavior vs. Exploited Behavior.
- Parallel requests and timing sequences.
- Authentication → Authorization → Access.

Use clear directional arrows and meaningful visual connections.

The composition may change between articles while preserving the overall visual identity.

### 6. Technical Accuracy

Technical accuracy takes priority over decoration.

- Use realistic and contextually correct technical examples.
- Ensure payloads, HTTP methods, headers, parameters, and code snippets match the supplied article.
- Never invent vulnerability behavior.
- Never substitute SQL Injection concepts into NoSQL Injection or vice versa.
- Avoid misleading protocol diagrams.
- Avoid unnecessary code snippets and unreadable technical text.
- Do not add attack techniques that are unrelated to the article.

### 7. Visual Restrictions

Avoid:

- Excessive 3D effects.
- Neon colors and dark hacker-themed backgrounds.
- Generic stock hacker imagery.
- Excessive decorative icons.
- Unnecessary rectangular title containers.
- Crowded diagrams.
- Tiny unreadable text.
- Random programming symbols.
- Repeated layouts that do not suit the vulnerability.
- Fabricated logos or inaccurate technical illustrations.

### 8. Final Quality Requirements

Every thumbnail must look like part of the same cybersecurity publication.

Maintain consistent:
- Typography.
- Color palette.
- Background grid.
- Branding placement.
- Orange and navy visual identity.
- Illustration quality.
- Overall editorial character.

Allow variation in:
- Diagram structure.
- Illustration subjects.
- Technical symbols.
- Attack-flow direction.
- Supporting elements.
- Main visual composition.

The final result must be professional, technically accurate, visually distinctive, clean, and recognizable as part of one unified PortSwigger-inspired thumbnail collection.

### 9. Article Input

Use the following information to generate the thumbnail:

LAB TITLE: [INSERT LAB TITLE]

VULNERABILITY CATEGORY: [INSERT CATEGORY]

ARTICLE CONTENT: [INSERT ARTICLE CONTENT]

IMPORTANT TECHNICAL CONCEPTS: [INSERT CONCEPTS, IF AVAILABLE]

REFERENCE IMAGE: [OPTIONAL]

Analyze the supplied information first. Then generate a unique visual composition that accurately represents the article while preserving the global visual identity.