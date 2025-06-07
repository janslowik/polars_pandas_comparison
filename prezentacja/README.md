# Polars vs Pandas Presentation

A reveal.js presentation comparing Polars and Pandas performance.

## Setup

1. Install dependencies:
```bash
npm install
```

## Running the Presentation

### Option 1: Using serve (recommended)
```bash
npm start
```
Then open http://localhost:3000 in your browser.

### Option 2: Using live-server (with auto-reload)
```bash
npm run dev
```
Then open http://localhost:8080 in your browser.

### Option 3: Simple HTTP server
```bash
# Python 3
python -m http.server 8000

# Or Python 2
python -m SimpleHTTPServer 8000
```
Then open http://localhost:8000 in your browser.

## Navigation

- **Next slide**: Space, Arrow keys, or click
- **Previous slide**: Shift+Space, Arrow keys
- **Overview**: Press `Esc`
- **Speaker notes**: Press `S`
- **Fullscreen**: Press `F`

## Presentation Structure

1. **Introduction** - Overview of Polars and Pandas
2. **Performance Benchmarks** - Speed comparisons
3. **Memory Usage** - Memory efficiency comparison
4. **Syntax Differences** - Code examples
5. **Use Cases** - When to use which library
6. **Conclusion** - Key takeaways and summary

## Customization

- **Theme**: Edit the theme link in `index.html` (available themes: black, white, league, beige, sky, night, serif, simple, solarized)
- **Styling**: Modify the `<style>` section in `index.html`
- **Content**: Edit the slides within `<div class="slides">` in `index.html`

## Features

- Syntax highlighting for Python code
- Responsive design
- Smooth transitions
- Nested slides for complex topics
- Performance comparison tables
- Color-coded highlights (green for advantages, red for disadvantages) 