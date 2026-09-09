/// <reference types="vitest" />
import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  server: {
    port: 5174,
    // Add any needed proxy here e.g.
    // proxy: { '/api': { target: 'http://127.0.0.1:8000', changeOrigin: true } }
  },
  test: {
    environment: 'jsdom',
    globals: true,
  },
})
