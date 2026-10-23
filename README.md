<a href="https://amansinghnp.com">
  <img src="./assets/banner.svg" width="100%" alt="Aman Singh. Founding engineer at Gradstack. UTS graduate." />
</a>

<p align="center">
  <a href="https://amansinghnp.com"><img src="https://img.shields.io/badge/site-amansinghnp.com-a0cbad?style=for-the-badge&labelColor=0c1326" alt="amansinghnp.com" /></a>
  <a href="https://amansinghnp.com/writing"><img src="https://img.shields.io/badge/writing-latest-ff6a3d?style=for-the-badge&labelColor=0c1326" alt="Writing" /></a>
  <a href="https://amansinghnp.com/projects/gradstack"><img src="https://img.shields.io/badge/building-gradstack-6e95a4?style=for-the-badge&labelColor=0c1326" alt="Gradstack" /></a>
  <a href="https://www.linkedin.com/in/aman-singh-np"><img src="https://img.shields.io/badge/linkedin-aman--singh--np-5eb3ff?style=for-the-badge&labelColor=0c1326" alt="LinkedIn" /></a>
</p>

<img src="./assets/terminal.svg" width="100%" alt="Terminal: whoami. Aman Singh, founding engineer at Gradstack, UTS graduate." />

## Right now

I'm a founding engineer at [Gradstack](https://amansinghnp.com/projects/gradstack) in Sydney. We build verified skills profiles for early-career talent, plus GAFI, an index that measures how well people actually work with AI.

I graduated from UTS. While I was there, LiPi Sort, our handwritten postcode reader with a robot arm, won People's Choice at the Tech Fest 2026 AI Showcase.

Most of my public code is AI work or seismology tooling. I also write up security incidents, usually the week they happen.

## AI work

<table>
<tr>
<td width="50%" valign="top">

**LiPi Sort**<br/>
YOLO11s fine-tuned on 1,310 postcards, 1,200 of them synthetic. It finds the handwritten postcode, reads it, looks up the suburb, and a robot arm sorts the card. People's Choice, UTS Tech Fest 2026.<br/>
<sub>[Try it](https://huggingface.co/spaces/AmanSNP/postcard-yolo-app) · [Report](https://amansinghnp.com/writing/lipisort-deeplearning) · `PyTorch` `YOLO11` `EasyOCR`</sub>

</td>
<td width="50%" valign="top">

**Memora**<br/>
A Slack agent that remembers what a team decided and says how sure it is. Built with teammates in three countries for the Slack Agent Builder Challenge.<br/>
<sub>[Case study](https://amansinghnp.com/projects/memora) · [Write-up](https://amansinghnp.com/writing/memora-slack-agent) · `LLM agents` `Slack API`</sub>

</td>
</tr>
<tr>
<td width="50%" valign="top">

**[crowdcal](https://github.com/AmanSinghNp/crowdcal)**<br/>
Does 70% mean 70% of people agree? Measures how well typed decision models are calibrated against the spread of human labels.<br/>
<sub>`Python` `calibration` `evaluation`</sub>

</td>
<td width="50%" valign="top">

**Klarity**<br/>
Students prove they understand a topic by teaching an AI that gets things wrong on purpose. Built at the EduX Hackathon 2026.<br/>
<sub>[Case study](https://amansinghnp.com/projects/klarity) · `TypeScript` `LLMs`</sub>

</td>
</tr>
<tr>
<td width="50%" valign="top">

**[torch-friction](https://github.com/AmanSinghNp/torch-friction)**<br/>
Differentiable rate-and-state friction layers for physics-informed neural networks. Fault slip physics you can backprop through.<br/>
<sub>[Report](https://amansinghnp.com/writing/seismic-pytorch) · `PyTorch` `PINNs`</sub>

</td>
<td width="50%" valign="top">

**[PalmLab](https://github.com/AmanSinghNp/palmlab-gesture-playground)**<br/>
Sculpt a 3D clay sphere with two hands in the browser. MediaPipe tracks the pinches and React Three Fiber deforms the mesh.<br/>
<sub>[Live demo](https://amansinghnp.github.io/palmlab-gesture-playground/) · [Report](https://amansinghnp.com/projects/palmlab) · `MediaPipe` `R3F`</sub>

</td>
</tr>
<tr>
<td width="50%" valign="top">

**[ASL Interpreter](https://github.com/AmanSinghNp/ASL-Interpreter-AI)**<br/>
A fingerspelling prototype. Hand landmarks become 42 numbers for a 24.5 KB TensorFlow Lite model.<br/>
<sub>[Report](https://amansinghnp.com/projects/asl) · `OpenCV` `MediaPipe` `TFLite`</sub>

</td>
<td width="50%" valign="top">

**[seismic-linter](https://github.com/AmanSinghNp/seismic-linter)**<br/>
A linter for seismic ML pipelines. It flags future data leaking into your training set before it inflates your forecast scores. On PyPI.<br/>
<sub>`Python` `MLOps` `time series`</sub>

</td>
</tr>
</table>

## Security

I write incident breakdowns from primary sources: the timeline, what leaked, and what to patch or rotate first. Most come with interactive charts and a full reference list.

| Date | Write-up | Read |
|:--|:--|:--|
| Oct 2026 | [Day zero: seven incidents, ten days, and what AI changes](https://amansinghnp.com/writing/day-zero)<br/><sub>PHP2Shell, GitLab, Node.js, QUIC, LiteLLM, Railway and OpenCode, plus a playbook.</sub> | 17 min |
| Oct 2026 | [The Railway breach explained: what leaked and what to rotate](https://amansinghnp.com/writing/railway-breach)<br/><sub>Exposed environment variables, the AI-key campaign behind it, and the rotation order.</sub> | 10 min |
| Oct 2026 | [PHP2Shell: CVE-2026-109618 and CVE-2026-109619](https://amansinghnp.com/writing/php2shell)<br/><sub>Two unauthenticated RCE flaws in PHP. What broke and what to patch first. 54 sources.</sub> | 13 min |
| May 2026 | [Inside the 2026 Canvas breach](https://amansinghnp.com/writing/canvas-breach)<br/><sub>Our team's incident response plan for UTS Cybersecurity Tech Fest 2026, mapped to MITRE ATT&CK.</sub> | 11 min |

On the code side, [PhishGuard-AI](https://github.com/AmanSinghNp/PhishGuard-AI) is a browser extension that flags phishing pages.

## Systems and seismic

<table>
<tr>
<td width="50%" valign="top">

**[Basalt](https://github.com/AmanSinghNp/Basalt)**<br/>
Bare-metal f-k noise attenuation for seismic data. Custom memory arenas, mmap I/O and x86-64 SIMD.<br/>
<sub>`C++` `SIMD`</sub>

</td>
<td width="50%" valign="top">

**[fast-trigger](https://github.com/AmanSinghNp/fast-trigger)**<br/>
STA/LTA earthquake event detection as a Python package, with the core in C++23, OpenMP for batches and pybind11 bindings.<br/>
<sub>`C++23` `OpenMP` `Python`</sub>

</td>
</tr>
<tr>
<td width="50%" valign="top">

**[nepal-earthquake-severity-prediction](https://github.com/AmanSinghNp/nepal-earthquake-severity-prediction)**<br/>
Predicts earthquake severity in Nepal from USGS data, with 100% recall on its 2024+ test set.<br/>
<sub>Related: [South Asia Earthquake Severity](https://github.com/AmanSinghNp/South-Asia-Earthquake-Severity)</sub>

</td>
<td width="50%" valign="top">

**[global-seismic-analysis](https://github.com/AmanSinghNp/global-seismic-analysis)**<br/>
23,409 M5.5+ earthquakes from 1965 to 2016. Sixteen of them released half the energy, and a depth classifier turned out to have memorised the map.<br/>
<sub>[Report](https://amansinghnp.com/writing/global-seismicity)</sub>

</td>
</tr>
</table>

The four tools above, torch-friction and seismic-linter included, are covered in one long report: [Four tools for seismic data](https://amansinghnp.com/writing/seismic-pytorch).

## Sandbox

[Mini-JavaScript-Projects](https://github.com/AmanSinghNp/Mini-JavaScript-Projects) has 30 browser apps and 25 algorithm visualisers in plain, framework-free JavaScript. Highlights: a [Wolfenstein-style ray caster](https://amansinghnp.com/projects/raycaster), a [limit order book](https://amansinghnp.com/projects/pocket) that matches by price-time priority, Black-Scholes Greeks and a piece-table code editor.

[SplitSmart-iOS](https://github.com/AmanSinghNp/SplitSmart-iOS) splits bills in SwiftUI and reads receipts with VisionKit OCR.

## Writing

Everything lives at [amansinghnp.com/writing](https://amansinghnp.com/writing).

| Date | Post | Topic |
|:--|:--|:--|
| Oct 2026 | [Day zero: seven incidents, ten days, and what AI changes](https://amansinghnp.com/writing/day-zero) | Security, AI |
| Oct 2026 | [The Railway breach explained](https://amansinghnp.com/writing/railway-breach) | Security |
| Oct 2026 | [PHP2Shell: what we know about CVE-2026-109618 and CVE-2026-109619](https://amansinghnp.com/writing/php2shell) | Security |
| Jul 2026 | [Memora: a Slack agent for teams that forget](https://amansinghnp.com/writing/memora-slack-agent) | AI engineering |
| Jun 2026 | [Reading handwritten postcodes](https://amansinghnp.com/writing/lipisort-deeplearning) | Computer vision |
| May 2026 | [Inside the 2026 Canvas breach](https://amansinghnp.com/writing/canvas-breach) | Security |
| Apr 2026 | [The model had memorised the map](https://amansinghnp.com/writing/global-seismicity) | Data science |
| Mar 2026 | [Four tools for seismic data](https://amansinghnp.com/writing/seismic-pytorch) | Scientific computing |

## Toolbelt

<img src="./assets/agents.svg" width="100%" alt="Agents I build with: Claude, Codex, DeepSeek, Mistral, Pi, OpenCode, Antigravity, Gemini, Cursor, Grok and Kimi." />

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,cpp,ts,js,swift,pytorch,tensorflow,opencv,react,nextjs,threejs,cloudflare,linux,bash,git&theme=dark&perline=15" alt="Python, C++, TypeScript, JavaScript, Swift, PyTorch, TensorFlow, OpenCV, React, Next.js, Three.js, Cloudflare, Linux, Bash, Git" />
</p>

## Contributions

<img src="./profile-3d-contrib/profile-night-green.svg" width="100%" alt="3D contribution graph" />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/AmanSinghNp/AmanSinghNp/output/github-contribution-grid-snake-dark.svg" />
  <img src="https://raw.githubusercontent.com/AmanSinghNp/AmanSinghNp/output/github-contribution-grid-snake.svg" width="100%" alt="Snake eating the contribution grid" />
</picture>

<img src="./assets/footer.svg" width="100%" alt="" />
