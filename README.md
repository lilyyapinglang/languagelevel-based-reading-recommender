# 📚 Level-Based Reading Recommender for Language Learners

_A multilingual reading recommendation system helping English and French learners find public domain books matching their CEFR language proficiency level (A2–C2)._

---

## Structure

```
level-based-reading-recommender/
│
├── data/
│   └── books_metadata.csv
│
├── src/
│   ├── app.py
│   ├── recommend.py
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## 🌟 Features

- 🎯 Recommend English and French public domain books based on your language level
- 📖 Show book summary, page count, word count, and estimated reading time.
- 🌍 Focus on public domain resources like Project Gutenberg.

---

## 🔥 Quick Start

```bash
git clone https://github.com/yourusername/level-based-reading-recommender.git
cd level-based-reading-recommender
pip install -r requirements.txt
python src/app.py
```

## 🚀 Future Work

• Dynamic Level Estimation: Implement a simple quiz to predict user language level.
• Automated Content Profiling: Analyze texts to estimate reading difficulty.
• Public Domain Book Scraping: Expand book database by crawling Gutenberg.
• Personalized Recommendations: Introduce user preference modeling.
• Adaptive Learning Paths: Recommend progressively challenging readings.
