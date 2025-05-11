import streamlit as st
from transformers import pipeline, set_seed

# Set up the text generation pipeline
@st.cache_resource
def load_model():
    generator = pipeline('text-generation', model='gpt2')
    return generator

generator = load_model()

# Streamlit UI
st.title("📝 Text Completion Generator")
st.write("Enter the beginning of a sentence, and let AI complete it!")

user_input = st.text_input("Enter your sentence:", "The world of AI is")

max_length = st.slider("Max length of output:", min_value=10, max_value=100, value=50)

if st.button("Generate Completion"):
    set_seed(42)  # For reproducibility
    result = generator(user_input, max_length=max_length, num_return_sequences=1)
    st.subheader("Completed Text:")
    st.write(result[0]['generated_text'])
