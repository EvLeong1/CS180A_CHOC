/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js,tsx,ts,jsx,css,scss,sass,less,vue}"],
  theme: {
    extend: {},
    fontFamily:{
      PlayfairDisplay: ['Playfair Display', 'serif'],
      Poppins: ['Poppins', 'sans-serif'],
      UnbuntoMono: ['Ubuntu Mono', 'monospace'],
    },
  },
  plugins: [],
}