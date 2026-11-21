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

Choose Matrix Rain, Cyber Perimeter Scanner, Digital Glitch, or Cyber Core Pulse. Press **Ctrl+C** to return to the menu.

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
- Responsive canvas rendering with capped device pixel ratio for mobile performance
- Offline; no API keys, external libraries, analytics, or network calls
- Terminal animation uses ANSI escape codes and Python standard library only

## Controls
- Terminal: 1–5 to select, Ctrl+C to return, 0 to exit
- Browser: tap animation modes; use Fullscreen / Pause / Change Color

Made for **NATIONVK** · FIND YOUR OWN PATH
