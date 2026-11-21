# NATIONVK — Termux Cyber Animation Studio

Offline cyber-themed animations for Android / Termux, with a separate fullscreen browser visualizer.

## 1) Terminal mode (Termux)
Requirements: Python 3 (no pip packages).

```bash
pkg update -y
pkg install python git -y
git clone https://github.com/NATIONVK/Termux_animation-.git
cd Termux_animation-
python cyber.py
``

Choose Matrix Rain, Cyber Perimeter Scanner, Digital Glitch, Cyber Core Pulse, **Blue Cyber Heart (option 6)**, or **Dark Red Hacker (option 7)**. Press **Ctrl+C** to return to the menu.

## 2) Fullscreen graphics mode
Open `index.html` in a mobile browser. You can also serve it locally:

```bash
pkg install python -y
cd Termux_animation-
python -m http.server 8080
``

Then open `http://127.0.0.1:8080` in Chrome. Use the mode buttons, Change Color, Pause/Resume and Fullscreen controls. Tap or move on the stage to interact with particles.

## Features
- Matrix rain, radar sweep, connected particle field, glitch and perspective cyber grid
- Blue Cyber Heart in terminal and fullscreen: pulsing 3D-style particle mesh, orbit rings, electric arcs, touch shockwave and particle burst/rebuild
- Dark Red Hacker mode: crimson matrix rain, threat radar sweep, scanline glitches and simulated terminal diagnostics
- Responsive canvas rendering with capped device pixel ratio for mobile performance
- Offline; no API keys, external libraries, analytics, or network calls
- Terminal animation uses ANSI escape codes and Python standard library only

## Controls
- Terminal: 1–7 to select (5 = random demo, 6 = Blue Cyber Heart, 7 = Dark Red Hacker), Ctrl+C to return, 0 to exit
- Browser: tap animation modes including ♥ CYBER HEART and RED HACKER; touch the heart for a particle burst and shockwave; use Fullscreen / Pause / Change Color

Made for **NATIONVK** · FIND YOUR OWN PATH
