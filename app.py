import streamlit as st
import pandas as pd
import nltk
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Ensure necessary NLTK datasets are downloaded
nltk.download('punkt')

# Function to analyze sentiment
def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity  # Returns sentiment score (-1 to 1)

# Function to categorize microaggressions (basic NLP)
def categorize_microaggression(text):
    keywords = {
        "microinvalidation": ["you're overreacting", "stop being so sensitive", "I don’t see color"],
        "microinsult": ["you’re so articulate", "where are you really from", "you must be good at math"],
        "microassault": ["racial slur", "explicit insult", "offensive joke"]
    }
    
    for category, phrases in keywords.items():
        for phrase in phrases:
            if phrase in text.lower():
                return category
    return "Uncategorized"

# Streamlit UI
st.title("MicroAggression Insight Tool")
st.write("Analyze, categorize, and visualize reported microaggressions.")

# Collect user input
user_input = st.text_area("Enter a microaggression example:")

if st.button("Analyze"):
    if user_input:
        sentiment_score = analyze_sentiment(user_input)
        category = categorize_microaggression(user_input)

        # Display results
        st.write(f"**Predicted Category:** {category}")
        st.write(f"**Sentiment Score:** {sentiment_score:.2f} (Negative: -1, Neutral: 0, Positive: 1)")

        # Store input in a dataframe
        df = pd.DataFrame({"Text": [user_input], "Category": [category], "Sentiment": [sentiment_score]})
        
        # Save locally (optional)
        df.to_csv("data.csv", mode='a', header=False, index=False)

# Load existing data
try:
    data = pd.read_csv("data.csv", names=["Text", "Category", "Sentiment"])
    
    if not data.empty:
        st.subheader("Data Insights")
        
        # Show category distribution
        st.write("### Microaggression Category Distribution")
        category_counts = data["Category"].value_counts()
        fig, ax = plt.subplots()
        category_counts.plot(kind='bar', ax=ax)
        st.pyplot(fig)

        # Generate a word cloud
        st.write("### Common Words in Microaggressions")
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(data["Text"]))
        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation="bilinear")
        ax.axis("off")
        st.pyplot(fig)
except FileNotFoundError:
    st.write("No data available yet.")
