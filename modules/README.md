# NATIONVK Red Hacker Lab — 16-Technology Starter Architecture

This directory adds starter modules for the planned multi-language lab. The existing root `index.html` and `cyber.py` remain the current working visualizer and Termux menu.

## Language / technology map

| Technology | Starter location | Responsibility |
|---|---|---|
| Python | `python/lab_core.py` | Local simulation core |
| JavaScript | `javascript/lab.js` | Browser-side utilities |
| TypeScript | `typescript/lab.ts` | Typed application contracts |
| HTML5 | `html5/panel.html` | Accessible UI fragment |
| CSS3 | `css3/panel.css` | Red hacker panel styling |
| Java | `java/LabStatus.java` | Android/JVM status model |
| Kotlin | `kotlin/LabStatus.kt` | Android-native status model |
| C | `c/lab_status.c` | Low-level status sample |
| C++ | `cpp/lab_status.cpp` | Native engine sample |
| Rust | `rust/src/main.rs` | Memory-safe native core sample |
| Go | `go/main.go` | Service/status sample |
| PHP | `php/status.php` | JSON response example |
| SQL | `sql/schema.sql` | Local event-log schema |
| Bash | `bash/lab-check.sh` | Termux shell check |
| Lua | `lua/status.lua` | Lightweight plugin/status module |
| Dart | `dart/lib/lab_status.dart` | Flutter-ready model |

HTML5 and CSS3 are web technologies rather than general-purpose programming languages; they are included as two of the 16 requested technologies.

## Important integration status

These are starter/reference modules, not yet one linked runtime. The current working app still runs with the existing HTML/CSS/JavaScript visualizer and Python Termux program. Native modules require their respective toolchains and will be integrated only where they add a real benefit. Do not install all compilers on the phone just to run the current visualizer.

## Safe-use boundary

All samples are local-only educational scaffolding. They do not scan external systems, bypass authentication, exploit devices, or perform unauthorized network actions. Any future networking lab should use localhost or explicitly authorized test targets.

## Android-first workflow

- Current visualizer: open the root `index.html` in a browser.
- Current Termux app: run `python cyber.py`.
- Python module check: `python modules/python/lab_core.py`.
- Bash check: `bash modules/bash/lab-check.sh`.
- Compile native examples only after installing the relevant compiler/toolchain.

## Planned next stages

1. Add a shared module interface and configuration.
2. Add syntax/build checks in GitHub Actions.
3. Integrate TypeScript/JavaScript into the browser visualizer.
4. Add optional native components only after performance profiling.
5. Add Android packaging after the core architecture is stable.
