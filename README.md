# Personal Website

A minimalist personal website for a UIUC CS undergraduate student. Built with [Astro](https://astro.build).

## Features

- Static site with a shared layout and reusable components
- Pure-CSS hover tooltips for explaining text (e.g. name pronunciation)
- Placeholders for personal information (name, links, coursework, projects, etc.)

## Project structure

```
src/
  styles/global.css          # reset, typography, layout, tooltip styles
  layouts/BaseLayout.astro   # shared HTML shell
  components/Tooltip.astro   # reusable pure-CSS tooltip
  pages/index.astro          # homepage
public/
  favicon.svg
```

## Getting started

Install dependencies and run the dev server:

```sh
npm install
npm run dev
```

Build the static site to `dist/`:

```sh
npm run build
```

Serve the built site locally:

```sh
npm run preview
```

## Serving over the local network (Python)

Build the site, then serve `dist/` with the included Python server so other
devices on the same Wi-Fi can reach it:

```sh
npm run build
python3 serve.py
```

The server listens on `0.0.0.0:8000`. Find your machine's LAN IP (e.g. via
`ip addr` or `hostname -I`) and visit `http://<your-ip>:8000` from another device.

## Extending

- Add new pages under `src/pages/`
- Use the `<Tooltip>` component for hover explanations
- Swap placeholder values in `src/pages/index.astro` with real content
