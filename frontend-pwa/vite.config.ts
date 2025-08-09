import tailwindcss from '@tailwindcss/vite';
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import { VitePWA } from 'vite-plugin-pwa'

export default defineConfig({
	plugins: [tailwindcss(), sveltekit(),
	VitePWA({
		registerType: 'autoUpdate',
		includeAssets: [ 'favicon.ico', 'icon-192.png', 'icon-512.png', 'logo-small.png' ],	
		manifest: {
			name: 'Thought Partner',
			short_name: 'Thought Partner',
			description: 'A personal AI assistant for your thoughts',
			start_url: '/',
			display: 'standalone',
			background_color: '#141420',
			theme_color: '#f5c07a',
			icons:[
				{
					src: '/icon-192.png',
					sizes: '192x192',
					type: 'image/png'
				},
				{
					src: '/icon-512.png',
					sizes: '512x512',
					type: 'image/png'
				}
			]
		}
    })
  ]
});
