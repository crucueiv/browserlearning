# BrowserLearning

An educational mini-browser project built to learn how browsers work by implementing one step by step from scratch.

## Project Purpose

This project is focused on **learning by building**.  
The main goal is to understand browser internals and gain practical experience with different technologies, while opening the door to new technical areas.

In short, this is not just a browser app — it is a study project to:
- explore browser architecture,
- practice networking/rendering/UI integration,
- and build confidence for creating more advanced systems in the future.

## Current Status

The project currently includes a working prototype with:
- a desktop UI built with **PySide6**,
- URL loading from web and local files,
- a basic HTML parser,
- a simple DOM tree representation,
- a basic layout pass,
- and text rendering in a custom widget.

It already demonstrates the core browser pipeline at a simplified level:

1. User enters URL.
2. Content is loaded (`http(s)` or `file://`).
3. HTML is parsed into an internal tree.
4. A layout tree is created and positioned.
5. Text nodes are painted in the render widget.

## Architecture Overview

### 1) Entry Point
- `main.py`
  - Starts the Qt application.
  - Creates and shows the main browser window.

### 2) UI Layer
- `ui/browser_window.py`
  - Loads the Qt Designer UI (`ui/QtDesigner/MainUI.ui`).
  - Handles URL input and the **Go** button action.
  - Executes the browser pipeline (load -> parse -> layout -> render).
  - Replaces initial placeholder text with rendered output.

### 3) Networking Layer
- `networking/loader.py`
  - `load_web_url(url)`: fetches remote content with `requests`.
  - `load_local_url(url)`: loads local files.
  - `load_url(url)`: dispatches between local and remote loading.

### 4) Rendering Pipeline
- `rendering/dom.py`
  - Defines a simple `Node` class for element/text nodes.

- `rendering/parser.py`
  - Parses raw HTML into a minimal tree structure.
  - Handles opening and closing tags in a stack-based approach.

- `rendering/layout.py`
  - Builds layout boxes from the parsed tree.
  - Assigns basic positions (`x`, `y`) to boxes.

- `rendering/render_widget.py`
  - Custom Qt widget that paints text nodes using `QPainter`.

- `rendering/text_renderer.py`
  - Alternative text extraction helper for rendering content as plain text.

## Repository Structure

```text
browserlearning/
├── main.py
├── networking/
│   └── loader.py
├── rendering/
│   ├── dom.py
│   ├── parser.py
│   ├── layout.py
│   ├── render_widget.py
│   └── text_renderer.py
├── ui/
│   ├── browser_window.py
│   └── QtDesigner/
│       └── MainUI.ui
└── .pruebas/
    └── example1.html
```

## What Works Right Now

- URL input with button-triggered loading.
- Basic remote page fetch with auto `http://` fallback when protocol is missing.
- Local file loading via `file://` URLs.
- HTML text extraction through a custom parser + renderer flow.
- Basic display of parsed text content in the app window.

## Current Limitations

As expected for a learning prototype, the browser is intentionally simple:
- No CSS parsing or styling engine.
- No JavaScript engine.
- Very limited HTML parsing rules.
- No advanced layout model (block/inline, flow calculations, sizing rules, etc.).
- No navigation history, tabs, bookmarks, or security model.
- Limited error handling and standards compliance.

These limitations are part of the learning process and define the next milestones.

## Future Plans (Roadmap)

### Short Term
- Improve HTML parser robustness (attributes, self-closing tags, malformed input handling).
- Expand layout logic (better spacing, nesting behavior, sizing).
- Improve URL and loading error handling with clearer user feedback.
- Add basic unit tests for parser, loader, and layout modules.

### Mid Term
- Add a minimal CSS parser and style application.
- Separate block vs inline rendering behavior.
- Introduce scrolling and larger document handling.
- Improve rendering performance and paint organization.

### Long Term
- Add a basic JavaScript execution experiment (sandboxed and educational).
- Add browser-like features (history, tabs, simple navigation controls).
- Improve architecture modularity to support experimentation with alternative rendering strategies.
- Document each subsystem in depth as a learning guide.

## Learning Goals

This project aims to help the author:
- understand browser internals through practical implementation,
- study and compare technologies involved in networking, parsing, rendering, and UI frameworks,
- and gradually move into broader software engineering domains by building a real, evolving system.

## How to Run

1. Install dependencies:
   - Python 3.x
   - `PySide6`
   - `requests`
2. From project root, run:

```bash
python main.py
```

3. Enter a URL (for example, `example.com`) or a local file URL (for example, `file:///absolute/path/to/file.html`) and click **Go**.

## Suggested Next Step for Contributors

If you want to contribute, a great first task is to improve parser correctness and add tests around edge cases. This gives immediate learning value and improves the core browser pipeline for all future work.
