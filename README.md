---
title: MicroAggression Tool
emoji: 📚
colorFrom: pink
colorTo: indigo
sdk: streamlit
sdk_version: 1.42.0
app_file: app.py
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

MicroAggression Insight Tool

📌 An AI-powered tool for analyzing, categorizing, and visualizing microaggressions based on sentiment and NLP processing.

🔍 Project Overview

The MicroAggression Insight Tool is a research-driven web app that:
✅ Collects user-reported microaggression experiences
✅ Analyzes sentiment polarity (negative, neutral, positive)
✅ Categorizes microaggressions into: Microinvalidation, Microinsult, Microassault
✅ Visualizes trends using bar charts & word clouds
✅ Supports social psychology & intergroup relations research

This project aligns with social psychology research on discrimination perception and consequences, specifically for microaggressions in different social contexts.

🎯 How to Use the App

1️⃣ Enter a statement (e.g., “You’re so articulate for someone like you”)
2️⃣ Click Analyze
3️⃣ The app will:
	•	Categorize the statement into Microinvalidation, Microinsult, or Microassault
	•	Analyze Sentiment (-1 = Negative, 0 = Neutral, +1 = Positive)
	•	Visualize common patterns across all collected data

🔗 Live App: Check it out on Hugging Face Spaces

🖥️ Installation & Running Locally

🔧 If you want to run this app on your local machine, follow these steps:

1. Clone the Repository

git clone https://github.com/durganihantri/MicroAggression-Insight-Tool.git
cd MicroAggression-Insight-Tool

2. Create a Virtual Environment (Optional)

python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows

3. Install Dependencies

pip install -r requirements.txt

4. Run the Streamlit App

streamlit run app.py

✅ The app will launch in your browser at http://localhost:8501.

🚀 Deployment on Hugging Face Spaces

If you want to deploy this app on Hugging Face Spaces, follow these steps:

1️⃣ Go to Hugging Face Spaces
2️⃣ Click “Create new Space”
3️⃣ Set SDK to Streamlit
4️⃣ Upload these files:
	•	app.py (Main Streamlit app)
	•	requirements.txt (Dependencies)
5️⃣ Click “Commit” and wait for the app to deploy.

🔗 Live App URL: Your Hugging Face Spaces Link

🛠️ Technical Details
	•	Framework: Streamlit
	•	Backend: Python (NLTK, TextBlob for NLP processing)
	•	Data Storage: CSV-based (for collecting user input)
	•	Visualization: Matplotlib, WordCloud
	•	Modeling Techniques:
	•	Sentiment Analysis via TextBlob
	•	Categorization via basic NLP keyword matching

📌 Features & Future Enhancements

✅ Current Features

✔️ Microaggression categorization (Microinvalidation, Microinsult, Microassault)
✔️ Sentiment analysis for emotional impact
✔️ Bar chart & word cloud visualizations
✔️ User-reported microaggressions database

🔥 Planned Enhancements

🚀 Improve NLP classification (use GPT-based models for better accuracy)
🚀 Add multilingual support (expand analysis to other languages)
🚀 Integrate advanced analytics (e.g., time trends, deeper sentiment shifts)
🚀 Export reports for researchers (downloadable CSV files)

🧑‍💻 Author & Contact

👤 Developed by: Durganihantri
💡 For inquiries, research collaboration, or feedback:
📧 Email: ask@durganihantri.com
🔗 LinkedIn: http://linkedin.com/in/durganihantri

⭐ Contribute & Support

If you find this project useful, please consider starring the repo ⭐ and contributing!

📌 To contribute:
	•	Fork this repository
	•	Make improvements
	•	Submit a Pull Request!
