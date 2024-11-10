/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/templates/**/*.html", "./node_modules/flowbite/**/*.js"],
  safelist: [
    "text-red-800",
    "bg-red-50",
    "text-emerald-800",
    "bg-emerald-50",
    "text-green-800",
    "bg-green-50",
    "text-yellow-800",
    "bg-yellow-50",
    "text-gray-800",
    "bg-gray-50",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("flowbite/plugin")],
};
