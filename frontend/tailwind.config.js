/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        accent: "#D19781",
        light: "#F0EFEA",
        dark: "#111111",
        background: {
          light: "#F0EFEA",
          dark: "#111111",
        },
      },
    },
    fontFamily: {
      sans: ["Galano Grotesque", "sans-serif"],
    },
  },
  darkMode: "class",
  plugins: [],
};
