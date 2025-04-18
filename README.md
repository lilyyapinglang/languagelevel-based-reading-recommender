# 📚 Level-Based Reading Recommender for Language Learners

\_A multilingual reading recommendation system helping language learners find public domain books matching their CEFR language proficiency level (A2–C2), currently support English and French.

---

## Project Structure

```
level-based-reading-recommender/
│
├── data/
│   └── books_metadata.csv         # Book metadata (language, level, genre, etc.)
│
├── src/
│   ├── app.py                      # Main Gradio app (frontend)
│   ├── recommend.py                # Recommendation logic
│
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── LICENSE                         # Open-source license (MIT)
└── .gitignore                      # Ignored files
```

## 🌟 Features

    •	🎯 Level-Based Recommendation

Find public domain books based on your target language (English/French) and language proficiency level (A2–C2, CEFR standard).
• 📖 Detailed Book Information
Each recommended book comes with:
• Title and short summary
• Page count
• Word count
• Estimated reading time (based on average reading speed)
• 📚 Direct Access to Reading
Pick a book you like and directly jump to the reading page (e.g., Project Gutenberg).
(🌟 Future: Option to send books to Kindle or download epub/pdf.)
• 🌍 Focus on Public Domain Resources
Only books from public domain collections (e.g., Project Gutenberg), ensuring free and legal access.
• 🛠️ Lightweight and Fast
Built with Gradio and Pandas, no heavy setup required. Instant local deployment.
• 🔌 Designed for Expandability
Easy to extend to support:
• More languages (e.g., Chinese, Spanish)
• More levels (custom granularity)
• More book sources (external APIs)

---

## 🚀 Quick Start

```bash
git clone https://github.com/yourusername/level-based-reading-recommender.git
cd level-based-reading-recommender
pip install -r requirements.txt
python src/app.py
```

The Gradio web app will automatically open in your browser!

## 🎯 Future Work

- **Public Domain Book Scraping**  
  Build a larger dataset by crawling Project Gutenberg and other open public domain archives.

- **Automated Content Profiling**  
  Analyze the complexity of book texts (sentence length, vocabulary richness) to auto-predict difficulty level.

- **Personalized Recommendations**  
  Introduce user profiles, favorite genres, reading history, and personalized recommendation scores.

- **Adaptive Learning Paths**  
  Recommend books that slightly challenge users’ current level to promote progressive language learning.

- **GoodReads Integration**  
  Combine with GoodReads API to filter and prioritize highly-rated books for better reading experiences.

- **Send to Kindle Support**  
  Allow users to export selected books to Kindle devices or download epub/pdf versions.

- **Support for More Languages**  
  Expand from English/French to Chinese, Spanish, German, and beyond.

- **Dynamic Level Estimation**  
  Add a simple self-assessment quiz for users to estimate their language level before getting recommendations.
