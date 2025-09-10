/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html","./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        "umd-red":  "#E21833",
        "umd-gold": "#FFD200",
      },
      boxShadow: { card: "0 10px 30px rgba(0,0,0,0.08)" },
    },
  },
  plugins: [],
}
