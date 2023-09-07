import streamlit as st
import spacy
import textstat

# Load English language model for spaCy
nlp = spacy.load("en_core_web_lg")

# Streamlit app title
st.title("Article Analysis App")


# User input
user_input = st.text_area("Enter your article:", height=600)


if user_input:
    # Analyze the text with spaCy
    doc = nlp(user_input)

    # Count words
    word_count = len(doc)

    # Calculate Flesch-Kincaid Grade Level
    fk_grade_level = textstat.textstat.flesch_kincaid_grade(user_input)
    fk_read_level = textstat.textstat.flesch_reading_ease(user_input)
    difficult_word_count = textstat.textstat.difficult_words(user_input)

    # Display the results
    st.write(f"Word Count: {word_count}")
    st.write(f"Flesch-Kincaid Grade Level: {fk_grade_level}")
    st.write(f"Text readable Score: {fk_read_level}")

    # Interpret the FK Grade Level
    if fk_grade_level <= 6:
        st.write("This article is at an elementary school reading level.")
    elif fk_grade_level <= 8:
        st.write("This article is at a middle school reading level.")
    elif fk_grade_level <= 10:
        st.write("This article is at a high school reading level.")
    else:
        st.write("This article is at a professional or college-level reading.")

    # Calculate a score out of 100 (you can define your own scoring logic)
    st.write(f"Difficult words count: {difficult_word_count}")
    score = min(100, max(0, 100 - (fk_grade_level - 6) * 10))
    st.write(f"Article Score (out of 100): {score:.2f}")
