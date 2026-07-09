# SelectSenz.AI — Where Skills Meet Strategy

A content-based recommendation engine that maps a user's skills to the closest-matching tech career role using **TF-IDF weighting** and **cosine similarity** — no external ML libraries, pure JavaScript.

## Live Demo
https://<your-github-username>.github.io/selectsenz-ai/

## How it works (IPO pipeline)
1. **Ingestion** — user selects 3+ skills from a shared, controlled vocabulary (prevents naming mismatches like "Web Design" vs "Frontend Development").
2. **Vector Mapping** — skills are mapped into a numerical vector space shared between the user profile and 14 job-role "items".
3. **TF-IDF Scoring** — term frequency × inverse document frequency down-weights generic skills (e.g. Python, Automation) and up-weights specific ones (e.g. Cryptography, Figma).
4. **Cosine Similarity** — measures the angle between the user vector and each role vector (scale-invariant, unlike Euclidean distance).
5. **Sorting & Filtering** — results are ranked and truncated to the Top-3 matches.
6. **Cold Start Handling** — if there's zero overlap with any tracked role, the engine falls back to the most globally-connected "trending" roles.

## Tech
Single-file HTML/CSS/JS. No build step, no dependencies. Works entirely client-side.

## Run locally
Just open `index.html` in any browser.

## Author
Rahul — B.Tech CSE (AI & ML), CMR Engineering College (CMREC), JNTU Hyderabad.
Project 3 — AI Recommendation Logic, DecodeLabs Industrial Training Kit.
