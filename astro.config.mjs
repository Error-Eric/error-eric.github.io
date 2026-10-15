import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://error-eric.github.io',
  markdown: {
    shikiConfig: {
      theme: 'github-dark',
    },
  },
});
