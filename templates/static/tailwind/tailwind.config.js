/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../../**/*.html',
    './node_modules/flowbite/**/*.js',
  ],
  theme: {
    fontFamily: {
      inter: ['Inter Tight', 'sans-serif'],
    },

    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}
