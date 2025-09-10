# College Park Apartment Portal

A single-page React app that guides students through choosing and applying for apartments near the University of Maryland. The flow is one step per screen with a progress bar and a UMD-inspired palette.

## Overview

Steps: Welcome → Eligibility → Major & Proximity → Budget → Choose Apartment & Group → Application → Thank You.

This frontend mirrors the decision logic from the original backend prototype (`final_project.py`), including:
- Eligibility checks (ID and income)
- Mapping majors to nearby apartments
- Minimum-budget affordability checks
- Optional group size for shared units
- Basic input validations for the application

There is **no server** required. Datasets are loaded as static JSON from `/public/data`.

## Tech Stack

- React (Vite)
- Tailwind CSS v4 + PostCSS
- JavaScript (ESNext)

## Data

JSON files:

public/data/apartments.json
public/data/amenities.json
public/data/historical.json

markdown
Copy code

Expected fields 

- `apartments.json` (from `CP Apartments_Version3.csv`):
  - `Apartment Name`, `Minimum Price`, `Apartment Number`, `Number of Rooms Available`
- `amenities.json` (from `Amenitites_Version2.csv`):
  - `Apartment Name`, plus amenity columns like `Pool`, `Gym`, `Parking`, `Electronic Key Locks`, `Study Rooms`, `Game Lounge` (values 0/1)
- `historical.json` (from `Major Historical Data_Version3.csv`):
  - `Major`, `Apartment` (used for simple historical context)


## Project Structure

<details>
  <summary><code>public/</code></summary>

pgsql
Copy code
public/
├─ vite.svg
└─ data/
   ├─ apartments.json
   ├─ amenities.json
   └─ historical.json
html
Copy code
</details>

<details>
  <summary><code>src/</code></summary>

css
Copy code
src/
├─ App.jsx
├─ index.css
└─ main.jsx
html
Copy code
</details>


## Tailwind v4 Wiring

`postcss.config.js`
```js
export default {
  plugins: {
    '@tailwindcss/postcss': {},
  },
}
src/index.css

css
Copy code
@import "tailwindcss";
Run Locally
bash
Copy code
npm install
npm run dev
Open the URL printed by Vite (usually http://localhost:5173).

Build
bash
Copy code
npm run build
Deploy the contents of dist/ to any static host (Vercel, Netlify, GitHub Pages, Cloudflare Pages).

Notes
The UI is based on the backend logic from final_project.py but runs entirely in the browser with static JSON. If you include the Python file in this repo, keep it under a non-runtime folder (e.g., legacy/) and note that it is not required to run the app.
