"""Builds the animated SVGs in this folder. Edit the data below, then run: python3 assets/build.py"""
import html, os
OUT = os.path.dirname(os.path.abspath(__file__))
import math, random
def trace(x0, x1, base, step, events, noise=1.6):
    pts=[]
    x=x0
    while x<=x1:
        y=random.gauss(0,noise)
        for (ex, amp, decay, freq) in events:
            if x>=ex:
                t=x-ex
                env=amp*math.exp(-t/decay)*(1-math.exp(-t/6))
                y+=env*math.sin(t*freq+random.uniform(-.5,.5))*random.uniform(.6,1)
        pts.append((x, base+y))
        x+=step
    return "M"+" L".join(f"{a:.0f} {b:.1f}" for a,b in pts)

random.seed(7)
BANNER_PATH = trace(0, 1200, 292, 3, [(640, 14, 40, 0.9), (735, 46, 70, 0.75), (900, 12, 60, 1.1)])
FOOTER_PATH = trace(0, 1200, 30, 3, [(520, 8, 40, 0.9), (600, 16, 60, 0.8)], noise=1.0)
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"
SERIF = "'Iowan Old Style', 'Palatino Linotype', Georgia, 'Times New Roman', serif"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"

def card_defs(w, h):
    return f'''
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#070a16"/>
      <stop offset="1" stop-color="#0c1326"/>
    </linearGradient>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M40 0H0V40" fill="none" stroke="#ffffff" stroke-opacity="0.045" stroke-width="1"/>
    </pattern>
    <clipPath id="card"><rect width="{w}" height="{h}" rx="18"/></clipPath>'''

# ---------------------------------------------------------------- banner
phrases = ["AI engineering", "security research", "seismic ML", "systems in C++", "writing about breaches"]
n = len(phrases); cyc = 3.0 * n
rot = []
for i, p in enumerate(phrases):
    a = i / n; b = (i + 1) / n; f = 0.25 / cyc
    kt = f"0;{a:.4f};{a+f:.4f};{b-f:.4f};{b:.4f};1"
    rot.append(f'''<text x="96" y="252" opacity="0">{html.escape(p)}<animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="{kt}" dur="{cyc}s" repeatCount="indefinite"/></text>''')

banner = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="360" viewBox="0 0 1200 360" role="img" aria-label="Aman Singh. Founding engineer at Gradstack. UTS graduate.">
  <defs>{card_defs(1200, 360)}
    <radialGradient id="glowL" cx="0.12" cy="0.2" r="0.6">
      <stop offset="0" stop-color="#2f6f5b" stop-opacity="0.35"/>
      <stop offset="1" stop-color="#2f6f5b" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glowR" cx="0.78" cy="0.85" r="0.5">
      <stop offset="0" stop-color="#b82c00" stop-opacity="0.28"/>
      <stop offset="1" stop-color="#b82c00" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="name" x1="0" y1="0" x2="1" y2="0" gradientUnits="objectBoundingBox">
      <stop offset="0" stop-color="#ffffff"/>
      <stop offset="0.42" stop-color="#ffffff"/>
      <stop offset="0.5" stop-color="#a0cbad"/>
      <stop offset="0.58" stop-color="#ffffff"/>
      <stop offset="1" stop-color="#ffffff"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="-1 0;-1 0;1 0" keyTimes="0;0.55;1" dur="7s" repeatCount="indefinite"/>
    </linearGradient>
    <linearGradient id="ink" x1="0" y1="0" x2="1200" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#6e95a4"/>
      <stop offset="0.5" stop-color="#a0cbad"/>
      <stop offset="0.62" stop-color="#ff6a3d"/>
      <stop offset="0.8" stop-color="#ffb199"/>
      <stop offset="1" stop-color="#6e95a4"/>
    </linearGradient>
    <linearGradient id="scan" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#a0cbad" stop-opacity="0"/>
      <stop offset="0.85" stop-color="#a0cbad" stop-opacity="0.07"/>
      <stop offset="1" stop-color="#a0cbad" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="below"><rect x="560" y="64" width="640" height="270"/></clipPath>
    <filter id="soft" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3"/></filter>
  </defs>
  <style>
    .mono {{ font-family: {MONO}; }}
    .rise {{ animation: rise 1.1s cubic-bezier(.2,.7,.2,1) both; }}
    .rise2 {{ animation: rise 1.1s .25s cubic-bezier(.2,.7,.2,1) both; }}
    .rise3 {{ animation: rise 1.1s .5s cubic-bezier(.2,.7,.2,1) both; }}
    @keyframes rise {{ from {{ opacity: 0; transform: translateY(14px); }} to {{ opacity: 1; transform: none; }} }}
    .grid {{ animation: drift 16s linear infinite; }}
    @keyframes drift {{ to {{ transform: translate(-40px, -40px); }} }}
    .blink {{ animation: blink 1.6s ease-in-out infinite; }}
    @keyframes blink {{ 50% {{ opacity: 0.15; }} }}
    @media (prefers-reduced-motion: reduce) {{ .grid, .blink, .rise, .rise2, .rise3 {{ animation: none; }} }}
  </style>
  <g clip-path="url(#card)">
    <rect width="1200" height="360" fill="url(#bg)"/>
    <rect class="grid" width="1280" height="440" fill="url(#grid)"/>
    <rect width="1200" height="360" fill="url(#glowL)"/>
    <rect width="1200" height="360" fill="url(#glowR)"/>

    <!-- header strip -->
    <g class="mono" font-size="14" letter-spacing="1.5" fill="#6e95a4">
      <text x="64" y="44">STATION SYD-01  ·  33.87°S 151.21°E  ·  CH HHZ</text>
      <g transform="translate(1136 44)" text-anchor="end">
        <text x="0" y="0">AMANSINGHNP.COM</text>
        <circle class="blink" cx="-176" cy="-4" r="4" fill="#ff4d1f"/>
        <text x="-188" y="0" fill="#ff8a66">REC</text>
      </g>
    </g>
    <line x1="64" y1="60" x2="1136" y2="60" stroke="#ffffff" stroke-opacity="0.07"/>


    <!-- epicentre ripples -->
    <g clip-path="url(#below)"><g transform="translate(940 178)" fill="none">
      {"".join(f'<circle r="0" stroke="#ff6a3d" stroke-width="1.2" opacity="0"><animate attributeName="r" values="4;190" dur="4.5s" begin="{d}s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.55;0" dur="4.5s" begin="{d}s" repeatCount="indefinite"/></circle>' for d in (0, 1.5, 3))}
      <circle r="58" stroke="#6e95a4" stroke-opacity="0.18" stroke-dasharray="2 6"/>
      <circle r="116" stroke="#6e95a4" stroke-opacity="0.12" stroke-dasharray="2 6"/>
      <path d="M-14 0H14M0 -14V14" stroke="#ff8a66" stroke-opacity="0.7"/>
      <rect x="-4" y="-4" width="8" height="8" fill="#ff4d1f" transform="rotate(45)"/>
    </g></g>

    <!-- identity -->
    <text class="rise" x="60" y="160" font-family="{SERIF}" font-size="108" letter-spacing="-3" fill="url(#name)">Aman Singh</text>
    <text class="rise2 mono" x="66" y="206" font-size="19" fill="#d5e0e6">Founding engineer <tspan fill="#a0cbad">@ Gradstack</tspan>  ·  UTS graduate  ·  Sydney</text>
    <g class="rise3 mono" font-size="17" fill="#ff8a66">
      <text x="66" y="252" fill="#6e95a4">&gt;</text>
      {"".join(rot)}
    </g>

    <!-- seismograph -->
    <path d="{BANNER_PATH}" fill="none" stroke="#ffffff" stroke-opacity="0.08" stroke-width="1.2"/>
    <path d="{BANNER_PATH}" fill="none" stroke="url(#ink)" stroke-width="3" stroke-opacity="0.5" filter="url(#soft)" pathLength="1" stroke-dasharray="1 1">
      <animate attributeName="stroke-dashoffset" values="1;0;0;-1" keyTimes="0;0.62;0.86;1" dur="9s" repeatCount="indefinite"/>
    </path>
    <path id="trace" d="{BANNER_PATH}" fill="none" stroke="url(#ink)" stroke-width="1.6" stroke-linejoin="round" pathLength="1" stroke-dasharray="1 1">
      <animate attributeName="stroke-dashoffset" values="1;0;0;-1" keyTimes="0;0.62;0.86;1" dur="9s" repeatCount="indefinite"/>
    </path>
    <g>
      <circle r="9" fill="#ff6a3d" opacity="0.25"/>
      <circle r="3.5" fill="#ffe2d8"/>
      <animateMotion dur="9s" repeatCount="indefinite" keyPoints="0;1;1;1" keyTimes="0;0.62;0.86;1" calcMode="linear"><mpath href="#trace"/></animateMotion>
      <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.62;0.66;1" dur="9s" repeatCount="indefinite"/>
    </g>
    <rect x="-160" y="62" width="160" height="298" fill="url(#scan)">
      <animate attributeName="x" values="-160;1200" dur="9s" repeatCount="indefinite"/>
    </rect>

    <!-- time axis -->
    <g class="mono" font-size="12" fill="#6e95a4" fill-opacity="0.7">
      {"".join(f'<line x1="{x}" y1="340" x2="{x}" y2="346" stroke="#6e95a4" stroke-opacity="0.5"/><text x="{x+6}" y="347">T+{i*15:02d}s</text>' for i, x in enumerate(range(64, 1140, 214)))}
    </g>
  </g>
  <rect x="0.5" y="0.5" width="1199" height="359" rx="18" fill="none" stroke="#ffffff" stroke-opacity="0.08"/>
</svg>
'''

# ---------------------------------------------------------------- agents
def glyph(kind, color):
    c = color
    if kind == "claude":
        rays = "".join(f'<line x1="0" y1="-7.5" x2="0" y2="7.5" transform="rotate({a})"/>' for a in range(0, 180, 30))
        return f'<g stroke="{c}" stroke-width="2.4" stroke-linecap="round">{rays}</g>'
    if kind == "codex":
        return f'<path d="M-6 -4 L-1.5 0 L-6 4 M0 5 H6" fill="none" stroke="{c}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>'
    if kind == "deepseek":
        return f'<path d="M-8 2 C-4 -6 4 -6 7 -1 C5 3 1 5 -3 4 M4 -2.5 h0.1" fill="none" stroke="{c}" stroke-width="2.2" stroke-linecap="round"/><path d="M7 -1 L9 -5 M7 -1 L10 1" stroke="{c}" stroke-width="2" stroke-linecap="round"/>'
    if kind == "mistral":
        cols = ["#ffd800", "#ffaf00", "#ff8205", "#fa500f"]
        return "".join(f'<rect x="{-7 + (i % 2) * 7}" y="{-7 + (i // 2) * 7}" width="6" height="6" fill="{cols[i]}"/>' for i in range(4))
    if kind == "pi":
        return f'<text x="0" y="5.5" text-anchor="middle" font-family="{SERIF}" font-size="18" fill="{c}">π</text>'
    if kind == "opencode":
        return f'<path d="M-3 -6 L-8 0 L-3 6 M3 -6 L8 0 L3 6" fill="none" stroke="{c}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>'
    if kind == "antigravity":
        return f'<path d="M0 7 V-6 M-6 0 L0 -7 L6 0" fill="none" stroke="{c}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>'
    if kind == "gemini":
        return f'<path d="M0 -9 C1 -3 3 -1 9 0 C3 1 1 3 0 9 C-1 3 -3 1 -9 0 C-3 -1 -1 -3 0 -9 Z" fill="url(#gem)"/>'
    if kind == "cursor":
        return f'<path d="M-5 -7 L6 0 L0.5 1.5 L-2 7 Z" fill="{c}"/>'
    if kind == "grok":
        return f'<path d="M-6 7 L6 -7 M-6 -7 L-1 -1.5" fill="none" stroke="{c}" stroke-width="2.4" stroke-linecap="round"/>'
    if kind == "kimi":
        return f'<path d="M3 -7 A7 7 0 1 0 7 4 A5.5 5.5 0 1 1 3 -7 Z" fill="{c}"/>'
    raise KeyError(kind)

AGENTS = [
    [("Claude", "claude", "#d97757"), ("Codex", "codex", "#10a37f"), ("DeepSeek", "deepseek", "#4d6bfe"),
     ("Mistral", "mistral", "#fa520f"), ("Pi", "pi", "#c4a7ff"), ("OpenCode", "opencode", "#e6edf3")],
    [("Antigravity", "antigravity", "#4285f4"), ("Gemini", "gemini", "#8e75ff"), ("Cursor", "cursor", "#e6edf3"),
     ("Grok", "grok", "#d1d5db"), ("Kimi", "kimi", "#5eb3ff")],
]

def pill_row(items, y):
    parts, x = [], 0
    for name, kind, color in items:
        w = 58 + len(name) * 10.2
        parts.append(f'''<g transform="translate({x:.0f} {y})">
        <rect width="{w:.0f}" height="44" rx="22" fill="#0f1730" stroke="{color}" stroke-opacity="0.45"/>
        <circle cx="24" cy="22" r="14" fill="{color}" fill-opacity="0.12"/>
        <g transform="translate(24 22)">{glyph(kind, color)}</g>
        <text x="46" y="28.5" font-family="{SANS}" font-size="17" font-weight="600" fill="#e6edf3">{name}</text>
      </g>''')
        x += w + 16
    return "".join(parts), x

rows = []
for r, items in enumerate(AGENTS):
    seq, W = pill_row(items, 0)
    copies = int(2600 // W) + 2
    body = "".join(f'<g transform="translate({k * W:.0f} 0)">{seq}</g>' for k in range(copies))
    y = 64 + r * 62
    dur = W / 40
    vals = f"0 {y};-{W:.0f} {y}" if r == 0 else f"-{W:.0f} {y};0 {y}"
    rows.append(f'<g transform="translate(0 {y})">{body}<animateTransform attributeName="transform" type="translate" values="{vals}" dur="{dur:.1f}s" repeatCount="indefinite"/></g>')

agents = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="200" viewBox="0 0 1200 200" role="img" aria-label="Agents I build with: Claude, Codex, DeepSeek, Mistral, Pi, OpenCode, Antigravity, Gemini, Cursor, Grok, Kimi">
  <defs>{card_defs(1200, 200)}
    <linearGradient id="gem" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#4796e3"/><stop offset="1" stop-color="#c06bd8"/></linearGradient>
    <linearGradient id="fade" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#000"/><stop offset="0.1" stop-color="#fff"/>
      <stop offset="0.9" stop-color="#fff"/><stop offset="1" stop-color="#000"/>
    </linearGradient>
    <mask id="edges"><rect width="1200" height="200" fill="url(#fade)"/></mask>
  </defs>
  <g clip-path="url(#card)">
    <rect width="1200" height="200" fill="url(#bg)"/>
    <rect width="1200" height="200" fill="url(#grid)"/>
    <g font-family="{MONO}" font-size="14" letter-spacing="1.5" fill="#6e95a4">
      <text x="40" y="38">// AGENTS IN THE LOOP</text>
      <text x="1160" y="38" text-anchor="end">11 MODELS  ·  1 TERMINAL</text>
    </g>
    <g mask="url(#edges)">{"".join(rows)}</g>
  </g>
  <rect x="0.5" y="0.5" width="1199" height="199" rx="18" fill="none" stroke="#ffffff" stroke-opacity="0.08"/>
</svg>
'''

# ---------------------------------------------------------------- terminal
PROMPT = "aman@sydney ~ %"
LINES = [
    ("cmd", "whoami"),
    ("out", "Aman Singh. Founding engineer at Gradstack. UTS graduate."),
    ("cmd", "cat now.txt"),
    ("out", "Building verified skills profiles and an AI fluency index at Gradstack."),
    ("out", "Writing up security incidents the week they land."),
    ("cmd", "ls ~/writing | head -4"),
    ("ls", ["day-zero", "railway-breach", "php2shell", "memora-slack-agent"]),
    ("cmd", "open https://amansinghnp.com"),
]
FS = 16; CW = FS * 0.62; LH = 28; X0 = 36; Y0 = 92
DUR = 20.0
t = 0.6; els = []; clips = []
px = X0 + (len(PROMPT) + 1) * CW
for i, (kind, val) in enumerate(LINES):
    y = Y0 + i * LH
    if kind == "cmd":
        appear = t
        typing = len(val) * 0.07
        w = len(val) * CW + 4
        k0, k1 = appear / DUR, (appear + typing) / DUR
        clips.append(f'''<clipPath id="c{i}"><rect x="{px:.1f}" y="{y-18}" height="26" width="0"><animate attributeName="width" values="0;0;{w:.0f};{w:.0f};0" keyTimes="0;{k0:.4f};{k1:.4f};0.97;1" dur="{DUR}s" repeatCount="indefinite"/></rect></clipPath>''')
        ka = (appear - 0.01) / DUR
        els.append(f'''<g opacity="0"><animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;{ka:.4f};{ka+0.0005:.4f};0.97;1" dur="{DUR}s" repeatCount="indefinite"/>
      <text x="{X0}" y="{y}" fill="#a0cbad">{PROMPT}</text>
      <text x="{px:.1f}" y="{y}" fill="#f4f7f9" clip-path="url(#c{i})">{html.escape(val)}</text></g>''')
        t = appear + typing + 0.45
    else:
        k = t / DUR
        if kind == "out":
            inner = f'<text x="{X0}" y="{y}" fill="#9fb3c8">{html.escape(val)}</text>'
        else:
            colors = ["#ff8a66", "#ff8a66", "#ff8a66", "#7cc4ff"]
            xs, x = [], X0
            for name, col in zip(val, colors):
                xs.append(f'<text x="{x:.1f}" y="{y}" fill="{col}">{name}</text>')
                x += (len(name) + 2) * CW
            inner = "".join(xs)
        els.append(f'''<g opacity="0"><animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;{k:.4f};{k+0.0005:.4f};0.97;1" dur="{DUR}s" repeatCount="indefinite"/>{inner}</g>''')
        t += 0.35
    if i == len(LINES) - 1:
        cx = px + len(val) * CW + 6
        k = (t - 0.45) / DUR
        els.append(f'''<g opacity="0"><animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;{k:.4f};{k+0.0005:.4f};0.97;1" dur="{DUR}s" repeatCount="indefinite"/><rect class="cursor" x="{cx:.1f}" y="{y-15}" width="9" height="19" fill="#a0cbad"/></g>''')
assert t < DUR * 0.8, t
H = Y0 + len(LINES) * LH + 10
terminal = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{H}" viewBox="0 0 1200 {H}" role="img" aria-label="Terminal: whoami, Aman Singh, founding engineer at Gradstack and UTS graduate. Latest writing: day-zero, railway-breach, php2shell, memora-slack-agent.">
  <defs>{card_defs(1200, H)}
    {"".join(clips)}
  </defs>
  <style>
    .cursor {{ animation: blink 1s steps(1) infinite; }}
    @keyframes blink {{ 50% {{ opacity: 0; }} }}
  </style>
  <g clip-path="url(#card)">
    <rect width="1200" height="{H}" fill="url(#bg)"/>
    <rect width="1200" height="44" fill="#ffffff" fill-opacity="0.03"/>
    <line x1="0" y1="44" x2="1200" y2="44" stroke="#ffffff" stroke-opacity="0.07"/>
    <circle cx="28" cy="22" r="6.5" fill="#ff5f57"/><circle cx="50" cy="22" r="6.5" fill="#febc2e"/><circle cx="72" cy="22" r="6.5" fill="#28c840"/>
    <text x="600" y="27" text-anchor="middle" font-family="{MONO}" font-size="13" fill="#6e95a4">aman@sydney: ~ (zsh)</text>
    <g font-family="{MONO}" font-size="{FS}">
      {"".join(els)}
    </g>
  </g>
  <rect x="0.5" y="0.5" width="1199" height="{H-1}" rx="18" fill="none" stroke="#ffffff" stroke-opacity="0.08"/>
</svg>
'''

# ---------------------------------------------------------------- footer
footer = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="64" viewBox="0 0 1200 64" role="img" aria-label="Seismograph trace">
  <defs>
    <linearGradient id="fink" x1="0" y1="0" x2="1200" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#6e95a4" stop-opacity="0"/>
      <stop offset="0.3" stop-color="#6e95a4"/>
      <stop offset="0.5" stop-color="#ff6a3d"/>
      <stop offset="0.7" stop-color="#a0cbad"/>
      <stop offset="1" stop-color="#a0cbad" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <path d="{FOOTER_PATH}" fill="none" stroke="url(#fink)" stroke-width="1.5" pathLength="1" stroke-dasharray="1 1">
    <animate attributeName="stroke-dashoffset" values="1;0;0" keyTimes="0;0.7;1" dur="8s" repeatCount="indefinite"/>
  </path>
</svg>
'''

# ---------------------------------------------------------------- project cards
# One clickable card per project. The README links each image to its url.
ACCENT = {"ai": "#7cc4ff", "cyber": "#ff6a3d", "seismic": "#a0cbad", "build": "#c4a7ff"}

def card_glyph(kind, c):
    if kind == "ai":
        nodes = [(-14, 8), (0, -12), (14, 8), (0, 2)]
        lines = "".join(f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}"/>' for a, b in [(nodes[0], nodes[1]), (nodes[1], nodes[2]), (nodes[0], nodes[3]), (nodes[2], nodes[3]), (nodes[1], nodes[3])])
        dots = "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="{c}"><animate attributeName="r" values="3;5.5;3" dur="2.4s" begin="{i * 0.6}s" repeatCount="indefinite"/><animate attributeName="fill-opacity" values="0.4;1;0.4" dur="2.4s" begin="{i * 0.6}s" repeatCount="indefinite"/></circle>' for i, (x, y) in enumerate(nodes))
        return f'<g stroke="{c}" stroke-opacity="0.35" stroke-width="1.5">{lines}</g>{dots}'
    if kind == "cyber":
        return f"""<circle r="20" fill="none" stroke="{c}" stroke-opacity="0.35"/><circle r="11" fill="none" stroke="{c}" stroke-opacity="0.25"/>
        <path d="M0 0 L0 -20 A20 20 0 0 1 17.3 -10 Z" fill="{c}" fill-opacity="0.35"><animateTransform attributeName="transform" type="rotate" values="0;360" dur="3s" repeatCount="indefinite"/></path>
        <circle cx="8" cy="-9" r="2.5" fill="{c}"><animate attributeName="opacity" values="0;1;0" dur="3s" repeatCount="indefinite"/></circle>"""
    if kind == "seismic":
        wave = "M-60 0 " + " ".join(f"L{x} {(-9 if (x // 4) % 2 else 9) * (1 if abs(x % 60 - 30) < 12 else 0.25):.1f}" for x in range(-56, 64, 4))
        return f"""<clipPath id="wc"><rect x="-24" y="-16" width="48" height="32"/></clipPath>
        <g clip-path="url(#wc)"><path d="{wave}" fill="none" stroke="{c}" stroke-width="1.8" stroke-linejoin="round"><animateTransform attributeName="transform" type="translate" values="0 0;-60 0" dur="2.4s" repeatCount="indefinite"/></path></g>"""
    if kind == "build":
        return f"""<path d="M-8 -10 L-18 0 L-8 10 M8 -10 L18 0 L8 10" fill="none" stroke="{c}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
        <rect x="-1.5" y="-9" width="3" height="18" fill="{c}"><animate attributeName="opacity" values="1;0;1" dur="1s" calcMode="discrete" repeatCount="indefinite"/></rect>"""
    raise KeyError(kind)

# (slug, kind, eyebrow, title, line, chips, url)
CARDS = [
    ("lipisort", "ai", "PEOPLE'S CHOICE · UTS TECH FEST 2026", "LiPi Sort", "Reads handwritten postcodes. A robot arm sorts the mail.", ["YOLO11s", "EasyOCR", "SO-101"], "https://amansinghnp.com/writing/lipisort-deeplearning"),
    ("memora", "ai", "SLACK AGENT BUILDER CHALLENGE", "Memora", "A Slack agent that remembers what your team decided.", ["LLM agents", "Slack API"], "https://amansinghnp.com/projects/memora"),
    ("klarity", "ai", "EDUX HACKATHON 2026", "Klarity", "Learn by teaching an AI that is wrong on purpose.", ["TypeScript", "LLMs"], "https://amansinghnp.com/projects/klarity"),
    ("crowdcal", "ai", "RESEARCH", "crowdcal", "Does 70% confidence mean 70% of people agree?", ["calibration", "evals", "Python"], "https://github.com/AmanSinghNp/crowdcal"),
    ("palmlab", "ai", "LIVE DEMO", "PalmLab", "Sculpt 3D clay with your hands, in the browser.", ["MediaPipe", "React Three Fiber"], "https://amansinghnp.github.io/palmlab-gesture-playground/"),
    ("asl", "ai", "COMPUTER VISION", "ASL Interpreter", "Fingerspelling from hand landmarks on a 24.5 KB model.", ["MediaPipe", "TFLite"], "https://github.com/AmanSinghNp/ASL-Interpreter-AI"),
    ("day-zero", "cyber", "OCT 2026 · 17 MIN READ", "Day zero", "Seven incidents in ten days, and what AI changes.", ["PHP2Shell", "LiteLLM", "OpenCode"], "https://amansinghnp.com/writing/day-zero"),
    ("railway", "cyber", "OCT 2026 · 10 MIN READ", "Railway breach", "What leaked, and the order to rotate your secrets.", ["LLMjacking", "secrets"], "https://amansinghnp.com/writing/railway-breach"),
    ("php2shell", "cyber", "OCT 2026 · 13 MIN READ", "PHP2Shell", "Two unauthenticated RCEs in PHP. What to patch first.", ["RCE", "54 sources"], "https://amansinghnp.com/writing/php2shell"),
    ("canvas", "cyber", "UTS CYBERSECURITY TECH FEST 2026", "Canvas breach", "One support ticket opened Canvas LMS. Our IR plan.", ["MITRE ATT&CK", "ACSC"], "https://amansinghnp.com/writing/canvas-breach"),
    ("basalt", "seismic", "C++ · SIMD", "Basalt", "Bare-metal f-k noise attenuation for seismic data.", ["mmap", "memory arenas"], "https://github.com/AmanSinghNp/Basalt"),
    ("fast-trigger", "seismic", "C++23 · PYTHON", "fast-trigger", "STA/LTA earthquake detection, batched with OpenMP.", ["pybind11", "OpenMP"], "https://github.com/AmanSinghNp/fast-trigger"),
    ("torch-friction", "seismic", "PYTORCH · PINNS", "torch-friction", "Rate-and-state fault friction you can backprop through.", ["autograd", "physics-informed"], "https://github.com/AmanSinghNp/torch-friction"),
    ("seismic-linter", "seismic", "ON PYPI", "seismic-linter", "Catches future data leaking into seismic ML training.", ["MLOps", "time series"], "https://github.com/AmanSinghNp/seismic-linter"),
    ("mini-js", "build", "55 APPS · NO FRAMEWORKS", "Mini JS Projects", "Ray caster, order book, Black-Scholes, code editor.", ["JavaScript", "Canvas 2D"], "https://github.com/AmanSinghNp/Mini-JavaScript-Projects"),
    ("splitsmart", "build", "NATIVE IOS", "SplitSmart", "Split bills and scan receipts with VisionKit OCR.", ["SwiftUI", "VisionKit"], "https://github.com/AmanSinghNp/SplitSmart-iOS"),
]

def project_card(kind, eyebrow, title, line, chips):
    c = ACCENT[kind]
    W, H = 600, 200
    chip_svg, x = [], 28
    for chip in chips:
        w = len(chip) * 9.1 + 24
        chip_svg.append(f'<g transform="translate({x:.0f} 146)"><rect width="{w:.0f}" height="30" rx="15" fill="{c}" fill-opacity="0.1" stroke="{c}" stroke-opacity="0.35"/><text x="{w / 2:.1f}" y="20.5" text-anchor="middle">{html.escape(chip)}</text></g>')
        x += w + 8
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{html.escape(title)}: {html.escape(line)}">
  <defs>{card_defs(W, H)}
    <linearGradient id="glow" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{c}" stop-opacity="0.16"/><stop offset="0.6" stop-color="{c}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="edge" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{c}" stop-opacity="0"/><stop offset="0.5" stop-color="{c}"/><stop offset="1" stop-color="{c}" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <g clip-path="url(#card)">
    <rect width="{W}" height="{H}" fill="url(#bg)"/>
    <rect width="{W}" height="{H}" fill="url(#grid)"/>
    <rect width="{W}" height="{H}" fill="url(#glow)"/>
    <rect x="-200" y="0" width="200" height="2" fill="url(#edge)"><animate attributeName="x" values="-200;{W}" dur="5s" repeatCount="indefinite"/></rect>
    <rect x="0" y="0" width="4" height="{H}" fill="{c}" fill-opacity="0.85"/>
    <text x="28" y="44" font-family="{MONO}" font-size="15" letter-spacing="1.2" fill="{c}">{html.escape(eyebrow)}</text>
    <text x="28" y="90" font-family="{SANS}" font-size="34" font-weight="700" letter-spacing="-0.5" fill="#f4f7f9">{html.escape(title)}</text>
    <text x="28" y="125" font-family="{SANS}" font-size="19" fill="#a9bacb">{html.escape(line)}</text>
    <g font-family="{MONO}" font-size="15" fill="#d5e0e6">{"".join(chip_svg)}</g>
    <g transform="translate({W - 56} 58)">{card_glyph(kind, c)}</g>
    <path d="M{W - 44} 172 L{W - 30} 158 M{W - 41} 158 H{W - 30} V169" fill="none" stroke="#6e95a4" stroke-width="2" stroke-linecap="round"/>
  </g>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="18" fill="none" stroke="#ffffff" stroke-opacity="0.08"/>
</svg>
'''

os.makedirs(os.path.join(OUT, "cards"), exist_ok=True)
for slug, kind, eyebrow, title, line, chips, url in CARDS:
    open(os.path.join(OUT, "cards", f"{slug}.svg"), "w").write(project_card(kind, eyebrow, title, line, chips))

for name, svg in [("banner", banner), ("agents", agents), ("terminal", terminal), ("footer", footer)]:
    open(os.path.join(OUT, f"{name}.svg"), "w").write(svg)
    print(name, len(svg))
