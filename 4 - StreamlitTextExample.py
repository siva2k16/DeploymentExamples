
import streamlit as st
from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment

st.title('Sentiment Analysis with TextBlob')

user_input = st.text_area("Enter your text")

if st.button('Analyze'):
    if user_input:
        sentiment = analyze_sentiment(user_input)
        
        # Display results
        st.write(f"Polarity: {sentiment.polarity}")
        st.write(f"Subjectivity: {sentiment.subjectivity}")

        if sentiment.polarity > 0:
            st.success(f"This text is positive with a polarity of {sentiment.polarity}")
        elif sentiment.polarity < 0:
            st.error(f"This text is negative with a polarity of {sentiment.polarity}")
        else:
            st.info("This text is neutral")
    else:
        st.warning("Please enter text for analysis")
