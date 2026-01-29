from textblob import TextBlob

def analyze_vibe(text):
    # This function checks if the text is positive or negative
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0.1:
        return "Positive ✨"
    elif polarity < -0.1:
        return "Serious/Controversial ⚠️"
    else:
        return "Neutral/Informative 📝"
