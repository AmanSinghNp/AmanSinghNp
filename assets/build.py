"""Builds the animated SVGs in this folder. Edit the data below, then run: python3 assets/build.py"""
import html, os, re
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
      {"".join(f'<line x1="{x}" y1="340" x2="{x}" y2="346" stroke="#6e95a4" stroke-opacity="0.5"/><text x="{x+6}" y="347">T+{i*15:02d}s</text>' for i, x in enumerate(range(64, 1100, 206)))}
    </g>
  </g>
  <rect x="0.5" y="0.5" width="1199" height="359" rx="18" fill="none" stroke="#ffffff" stroke-opacity="0.08"/>
</svg>
'''

# ---------------------------------------------------------------- agents
# Square tiles the same size as skillicons.dev's (256 units), with a wider 340 pitch so the names fit.
# The README sets this image to 83% width: (11 * 340 - 44) / (15 * 300 - 44) keeps the tiles the same size
# as the 15-icon language row under it. Marks are from Simple Icons (CC0, simpleicons.org), drawn in one colour.
# Simple Icons has no mark for Codex, Grok or Antigravity, so those three are plain drawn marks.
SIMPLE_ICONS = {
    "claude": "m4.7144 15.9555 4.7174-2.6471.079-.2307-.079-.1275h-.2307l-.7893-.0486-2.6956-.0729-2.3375-.0971-2.2646-.1214-.5707-.1215-.5343-.7042.0546-.3522.4797-.3218.686.0608 1.5179.1032 2.2767.1578 1.6514.0972 2.4468.255h.3886l.0546-.1579-.1336-.0971-.1032-.0972L6.973 9.8356l-2.55-1.6879-1.3356-.9714-.7225-.4918-.3643-.4614-.1578-1.0078.6557-.7225.8803.0607.2246.0607.8925.686 1.9064 1.4754 2.4893 1.8336.3643.3035.1457-.1032.0182-.0728-.164-.2733-1.3539-2.4467-1.445-2.4893-.6435-1.032-.17-.6194c-.0607-.255-.1032-.4674-.1032-.7285L6.287.1335 6.6997 0l.9957.1336.419.3642.6192 1.4147 1.0018 2.2282 1.5543 3.0296.4553.8985.2429.8318.091.255h.1579v-.1457l.1275-1.706.2368-2.0947.2307-2.6957.0789-.7589.3764-.9107.7468-.4918.5828.2793.4797.686-.0668.4433-.2853 1.8517-.5586 2.9021-.3643 1.9429h.2125l.2429-.2429.9835-1.3053 1.6514-2.0643.7286-.8196.85-.9046.5464-.4311h1.0321l.759 1.1293-.34 1.1657-1.0625 1.3478-.8804 1.1414-1.2628 1.7-.7893 1.36.0729.1093.1882-.0183 2.8535-.607 1.5421-.2794 1.8396-.3157.8318.3886.091.3946-.3278.8075-1.967.4857-2.3072.4614-3.4364.8136-.0425.0304.0486.0607 1.5482.1457.6618.0364h1.621l3.0175.2247.7892.522.4736.6376-.079.4857-1.2142.6193-1.6393-.3886-3.825-.9107-1.3113-.3279h-.1822v.1093l1.0929 1.0686 2.0035 1.8092 2.5075 2.3314.1275.5768-.3218.4554-.34-.0486-2.2039-1.6575-.85-.7468-1.9246-1.621h-.1275v.17l.4432.6496 2.3436 3.5214.1214 1.0807-.17.3521-.6071.2125-.6679-.1214-1.3721-1.9246L14.38 17.959l-1.1414-1.9428-.1397.079-.674 7.2552-.3156.3703-.7286.2793-.6071-.4614-.3218-.7468.3218-1.4753.3886-1.9246.3157-1.53.2853-1.9004.17-.6314-.0121-.0425-.1397.0182-1.4328 1.9672-2.1796 2.9446-1.7243 1.8456-.4128.164-.7164-.3704.0667-.6618.4008-.5889 2.386-3.0357 1.4389-1.882.929-1.0868-.0062-.1579h-.0546l-6.3385 4.1164-1.1293.1457-.4857-.4554.0608-.7467.2307-.2429 1.9064-1.3114Z",
    "deepseek": "M23.748 4.651c-.254-.124-.364.113-.512.233-.051.04-.094.09-.137.137-.372.397-.806.657-1.373.626-.829-.046-1.537.214-2.163.848-.133-.782-.575-1.248-1.247-1.548-.352-.155-.708-.311-.955-.65-.172-.24-.219-.509-.305-.774-.055-.16-.11-.323-.293-.35-.2-.031-.278.136-.356.276-.313.572-.434 1.202-.422 1.84.027 1.436.633 2.58 1.838 3.393.137.094.172.187.129.323-.082.28-.18.553-.266.833-.055.179-.137.218-.328.14a5.5 5.5 0 0 1-1.737-1.179c-.857-.828-1.631-1.743-2.597-2.46a12 12 0 0 0-.689-.47c-.985-.957.13-1.743.387-1.836.27-.098.094-.433-.778-.428-.872.003-1.67.295-2.687.685a3 3 0 0 1-.465.136 9.6 9.6 0 0 0-2.883-.101c-1.885.21-3.39 1.1-4.497 2.622C.082 8.776-.231 10.854.152 13.02c.403 2.284 1.568 4.175 3.36 5.653 1.857 1.533 3.997 2.284 6.438 2.14 1.482-.085 3.132-.284 4.994-1.86.47.234.962.328 1.78.398.629.058 1.235-.031 1.705-.129.735-.155.684-.836.418-.961-2.155-1.004-1.682-.595-2.112-.926 1.095-1.295 2.768-3.598 3.284-6.733.05-.346.115-.834.108-1.114-.004-.171.035-.238.23-.257a4.2 4.2 0 0 0 1.545-.475c1.397-.763 1.96-2.016 2.093-3.517.02-.23-.004-.467-.247-.588M11.58 18.168c-2.088-1.642-3.101-2.183-3.52-2.16-.39.024-.32.472-.234.763.09.288.207.487.371.74.114.167.192.416-.113.603-.673.416-1.842-.14-1.897-.168-1.361-.801-2.5-1.86-3.301-3.306-.775-1.393-1.225-2.888-1.299-4.482-.02-.385.094-.522.477-.592a4.7 4.7 0 0 1 1.53-.038c2.131.311 3.946 1.264 5.467 2.774.868.86 1.525 1.887 2.202 2.89.72 1.066 1.494 2.082 2.48 2.915.348.291.626.513.892.677-.802.09-2.14.109-3.055-.615zm1.001-6.44a.306.306 0 0 1 .415-.287.3.3 0 0 1 .113.074.3.3 0 0 1 .086.214c0 .17-.136.307-.308.307a.303.303 0 0 1-.306-.307m3.11 1.596c-.2.081-.4.151-.591.16a1.25 1.25 0 0 1-.798-.254c-.274-.23-.47-.358-.551-.758a1.7 1.7 0 0 1 .015-.588c.07-.327-.007-.537-.238-.727-.188-.156-.426-.199-.689-.199a.6.6 0 0 1-.254-.078.253.253 0 0 1-.114-.358 1 1 0 0 1 .192-.21c.356-.202.767-.136 1.146.016.352.144.618.408 1.001.782.392.451.462.576.685.915.176.264.336.536.446.848.066.194-.02.353-.25.45",
    "mistralai": "M17.143 3.429v3.428h-3.429v3.429h-3.428V6.857H6.857V3.43H3.43v13.714H0v3.428h10.286v-3.428H6.857v-3.429h3.429v3.429h3.429v-3.429h3.428v3.429h-3.428v3.428H24v-3.428h-3.43V3.429z",
    "pi": "M0 0v24h6v-6h6v-6H6V6h6v6h6V0Zm18 12v12h6V12Z",
    "opencode": "M22 24H2V0h20zM17 4.8H7v14.4h10z",
    "googlegemini": "M11.04 19.32Q12 21.51 12 24q0-2.49.93-4.68.96-2.19 2.58-3.81t3.81-2.55Q21.51 12 24 12q-2.49 0-4.68-.93a12.3 12.3 0 0 1-3.81-2.58 12.3 12.3 0 0 1-2.58-3.81Q12 2.49 12 0q0 2.49-.96 4.68-.93 2.19-2.55 3.81a12.3 12.3 0 0 1-3.81 2.58Q2.49 12 0 12q2.49 0 4.68.96 2.19.93 3.81 2.55t2.55 3.81",
    "cursor": "M11.503.131 1.891 5.678a.84.84 0 0 0-.42.726v11.188c0 .3.162.575.42.724l9.609 5.55a1 1 0 0 0 .998 0l9.61-5.55a.84.84 0 0 0 .42-.724V6.404a.84.84 0 0 0-.42-.726L12.497.131a1.01 1.01 0 0 0-.996 0M2.657 6.338h18.55c.263 0 .43.287.297.515L12.23 22.918c-.062.107-.229.064-.229-.06V12.335a.59.59 0 0 0-.295-.51l-9.11-5.257c-.109-.063-.064-.23.061-.23",
    "kimi": "M21.765.351C22.998.351 24 1.353 24 2.586S22.998 4.82 21.765 4.82h-1.974c-.15 0-.26-.12-.26-.26V2.586A2.237 2.237 0 0 1 21.765.35M9.41 13.388l8.447-8.377c.16-.16.07-.471-.14-.471h-4.55s-.1.02-.14.06l-9.099 9.029c-.14.14-.35.02-.35-.21V4.81c0-.15-.1-.27-.221-.27H.22c-.12 0-.22.12-.22.27v18.57c0 .15.1.27.22.27h3.137c.12 0 .22-.12.22-.27v-3.79c0-.08.03-.16.08-.21l2.826-2.796c.07-.07.16-.08.241-.03l7.546 5.551a8.9 8.9 0 0 0 4.018 1.493c.12.01.23-.11.23-.27V19.76c0-.14-.08-.25-.19-.26a5.8 5.8 0 0 1-2.355-.942l-6.533-4.73c-.14-.09-.15-.32-.03-.441",
}
DRAWN = {
    "codex": '<path d="M4 7l5 5-5 5M12 17h8" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>',
    "grok": '<path d="M19.5 3.5L4.5 20.5M17 9a7 7 0 1 1-6.5-4.9" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>',
    "antigravity": '<path d="M4 20c2-9 5-15 8-15s6 6 8 15" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>',
}
AGENTS = [("Claude", "claude"), ("Codex", "codex"), ("DeepSeek", "deepseek"), ("Mistral", "mistralai"),
          ("Pi", "pi"), ("OpenCode", "opencode"), ("Antigravity", "antigravity"), ("Gemini", "googlegemini"),
          ("Cursor", "cursor"), ("Grok", "grok"), ("Kimi", "kimi")]

def mark(key):
    if key in SIMPLE_ICONS:
        return f'<path d="{SIMPLE_ICONS[key]}" fill="currentColor"/>'
    return DRAWN[key]

tiles = []
for i, (name, key) in enumerate(AGENTS):
    tiles.append(f"""<g transform="translate({i * 340 + 20} 0)"><g class="tile" style="animation-delay:{i * 60}ms">
      <rect width="256" height="256" rx="60" fill="#242938"/>
      <g transform="translate(53 53) scale(6.25)" color="#e6edf3">{mark(key)}</g>
      <text x="128" y="334" text-anchor="middle">{name}</text>
    </g></g>""")
AW = len(AGENTS) * 340 - 44
agents = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{AW}" height="356" viewBox="0 0 {AW} 356" role="img" aria-label="Agents I build with: {", ".join(n for n, _ in AGENTS)}">
  <style>
    text {{ font-family: {SANS}; font-size: 54px; fill: #8b949e; }}
    .tile {{ animation: rise .6s cubic-bezier(.2,.7,.2,1) both; }}
    @keyframes rise {{ from {{ opacity: 0; transform: translateY(24px); }} }}
    @media (prefers-reduced-motion: reduce) {{ .tile {{ animation: none; }} }}
  </style>
  {"".join(tiles)}
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
  <style>
    path {{ stroke-dasharray: 1 1; animation: draw 6s ease-out both; }}
    @keyframes draw {{ from {{ stroke-dashoffset: 1; }} to {{ stroke-dashoffset: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{ path {{ animation: none; }} }}
  </style>
  <path d="{FOOTER_PATH}" fill="none" stroke="#6e95a4" stroke-opacity="0.7" stroke-width="1.5" pathLength="1"/>
</svg>
'''

# ---------------------------------------------------------------- highlight cards
# Four cards for the main projects; everything else is a plain table in the README.
# Flat surfaces, one accent per card, no gradients. Motion is CSS so reduced-motion can switch it off.
ACCENT = {"ai": "#7cc4ff", "cyber": "#ff6a3d", "seismic": "#a0cbad"}

def card_glyph(kind):
    if kind == "ai":
        nodes = [(-13, 8), (0, -11), (13, 8), (0, 2)]
        lines = "".join(f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}"/>' for a, b in [(nodes[0], nodes[1]), (nodes[1], nodes[2]), (nodes[0], nodes[3]), (nodes[2], nodes[3]), (nodes[1], nodes[3])])
        dots = "".join(f'<circle class="pulse" style="animation-delay:{i * 0.6}s" cx="{x}" cy="{y}" r="4" fill="currentColor"/>' for i, (x, y) in enumerate(nodes))
        return f'<g stroke="currentColor" stroke-opacity="0.4" stroke-width="1.5">{lines}</g>{dots}'
    if kind == "cyber":
        return """<circle r="17" fill="none" stroke="currentColor" stroke-opacity="0.4"/><circle r="9" fill="none" stroke="currentColor" stroke-opacity="0.3"/>
        <path class="spin" d="M0 0V-17A17 17 0 0 1 14.7 -8.5Z" fill="currentColor" fill-opacity="0.45"/>"""
    if kind == "seismic":
        wave = "M-60 0 " + " ".join(f"L{x} {(-9 if (x // 4) % 2 else 9) * (1 if abs(x % 60 - 30) < 12 else 0.25):.1f}" for x in range(-56, 64, 4))
        return f"""<clipPath id="wc"><rect x="-20" y="-14" width="40" height="28"/></clipPath>
        <g clip-path="url(#wc)"><path class="scroll" d="{wave}" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></g>"""
    raise KeyError(kind)

# (slug, kind, title, context, sentence lines, stack, url)
CARDS = [
    ("lipisort", "ai", "LiPi Sort", "People's Choice, UTS Tech Fest 2026",
     ["Reads handwritten postcodes off postcards,", "then a robot arm sorts them."],
     "YOLO11s, EasyOCR, SO-101 arm", "https://amansinghnp.com/writing/lipisort-deeplearning"),
    ("memora", "ai", "Memora", "Slack Agent Builder Challenge",
     ["A Slack agent that remembers what your", "team decided, and says how sure it is."],
     "LLM agents, Slack API", "https://amansinghnp.com/projects/memora"),
    ("basalt", "seismic", "Basalt", "Open source, C++",
     ["Bare-metal f-k noise attenuation for", "seismic data, on mmap I/O and SIMD."],
     "C++, x86-64 SIMD, memory arenas", "https://github.com/AmanSinghNp/Basalt"),
    ("day-zero", "cyber", "Day zero", "October 2026, 17 minute read",
     ["Seven security incidents in ten days, read", "from the primary sources."],
     "PHP2Shell, LiteLLM, Railway, OpenCode", "https://amansinghnp.com/writing/day-zero"),
]

def project_card(kind, title, context, sentence, stack):
    c = ACCENT[kind]
    W, H = 600, 262
    body = "".join(f'<text x="28" y="{152 + i * 31}" class="body">{html.escape(l)}</text>' for i, l in enumerate(sentence))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{html.escape(title)}. {html.escape(" ".join(sentence))}">
  <style>
    text {{ font-family: {SANS}; }}
    .title {{ font-size: 36px; font-weight: 700; fill: #f0f3f6; }}
    .context {{ font-size: 19px; fill: #8b949e; }}
    .body {{ font-size: 22px; fill: #c9d1d9; }}
    .stack {{ font-size: 19px; fill: #6e95a4; }}
    .pulse {{ animation: pulse 2.4s ease-in-out infinite; }}
    @keyframes pulse {{ 50% {{ opacity: 0.35; }} }}
    .spin {{ transform-origin: 0 0; animation: spin 3s linear infinite; }}
    @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
    .scroll {{ animation: scroll 2.4s linear infinite; }}
    @keyframes scroll {{ to {{ transform: translateX(-60px); }} }}
    @media (prefers-reduced-motion: reduce) {{ .pulse, .spin, .scroll {{ animation: none; }} }}
  </style>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="14" fill="#0d1117" stroke="#30363d"/>
  <rect x="28" y="28" width="68" height="68" rx="14" fill="{c}" fill-opacity="0.12"/>
  <g transform="translate(62 62)" color="{c}">{card_glyph(kind)}</g>
  <text x="116" y="62" class="title">{html.escape(title)}</text>
  <text x="116" y="90" class="context">{html.escape(context)}</text>
  {body}
  <text x="28" y="{H - 28}" class="stack">{html.escape(stack)}</text>
</svg>
'''

import shutil
shutil.rmtree(os.path.join(OUT, "cards"), ignore_errors=True)
os.makedirs(os.path.join(OUT, "cards"))
for slug, kind, title, context, sentence, stack, url in CARDS:
    open(os.path.join(OUT, "cards", f"{slug}.svg"), "w").write(project_card(kind, title, context, sentence, stack))

for name, svg in [("banner", banner), ("agents", agents), ("terminal", terminal), ("footer", footer)]:
    open(os.path.join(OUT, f"{name}.svg"), "w").write(svg)
    print(name, len(svg))
