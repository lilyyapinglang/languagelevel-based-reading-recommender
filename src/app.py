import gradio as gr
from recommend import load_books, recommend_books

# Load the dataset
df_books = load_books("data/books_metadata.csv")

def recommend_books_to_user(language, level):
    recs = recommend_books(df_books, language, level)
    if recs.empty:
        return "No books found for this language and level."
    else:
        result = ""
        for idx, row in recs.iterrows():
            result += f"📖 **{row['title']}**\n"
            result += f"- Genre: {row['genre']}\n"
            result += f"- Summary: {row['summary']}\n"
            result += f"- Pages: {row['page_count']}, Words: {row['word_count']}\n"
            result += f"- Estimated reading time: {row['estimated_read_time']}\n"
            result += f"- [Read here]({row['link']})\n\n"
        return result

demo = gr.Interface(
    fn=recommend_books_to_user,
    inputs=[
        gr.Dropdown(["English", "French"], label="Select Language"),
        gr.Dropdown(["A2", "B1", "B2", "C1", "C2"], label="Select Your Level")
    ],
    outputs="markdown",
    title="📚 Level-Based Reading Recommender for Language Learners",
    description="Select your target language and proficiency level to discover public domain books tailored for you!"
)

if __name__ == "__main__":
    demo.launch()