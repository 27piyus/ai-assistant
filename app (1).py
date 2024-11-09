import torch
from transformers import pipeline
import speech_recognition as sr
import os
from pydub import AudioSegment
import streamlit as st
from io import BytesIO
from PIL import Image
import easyocr

# Load the GPT model for text generation
model_name = "distilgpt2"  
chatbot = pipeline("text-generation", model=model_name)

# Initialize easyocr Reader
reader = easyocr.Reader(['en'])

# Chat function
def chat_with_gpt(text):
    response = chatbot(text, max_length=150, num_return_sequences=1)
    return response[0]["generated_text"]

# Convert audio to text
def audio_to_text(audio_file):
    recognizer = sr.Recognizer()
    if audio_file.lower().endswith(('.mp3', '.ogg', '.flac')):
        audio_file = convert_audio_to_wav(audio_file)
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Could not understand the audio"
        except sr.RequestError:
            return "Could not request results from Google Speech Recognition service"

# Convert audio to WAV format
def convert_audio_to_wav(audio_file):
    audio = AudioSegment.from_file(audio_file)
    wav_file = "converted_audio.wav"
    audio.export(wav_file, format="wav")
    return wav_file

# Image to text function using easyocr
def image_to_text(image_file):
    image = Image.open(image_file)
    result = reader.readtext(image)
    extracted_text = " ".join([text for _, text, _ in result])
    return extracted_text

# Main function
def main():
    st.title("AI Assistant - GPT with Speech and Image Recognition")
    st.write("Choose input type: Text, Audio, or Image.")

    input_type = st.radio("Input Type", ('Text', 'Audio', 'Image'))

    if input_type == "Text":
        text_input = st.text_input("Enter your question:")
        if text_input:
            response = chat_with_gpt(text_input)
            st.write("Answer:", response)
    
    elif input_type == "Audio":
        uploaded_audio = st.file_uploader("Upload an audio file (wav, mp3, etc.):", type=["wav", "mp3", "flac"])
        if uploaded_audio:
            audio_file_path = "uploaded_audio.wav"
            with open(audio_file_path, "wb") as f:
                f.write(uploaded_audio.getbuffer())
            text_from_audio = audio_to_text(audio_file_path)
            st.write("Transcribed Text:", text_from_audio)
            response = chat_with_gpt(text_from_audio)
            st.write("Answer:", response)
            os.remove(audio_file_path)

    elif input_type == "Image":
        uploaded_image = st.file_uploader("Upload an image:", type=["png", "jpg", "jpeg"])
        if uploaded_image:
            text_from_image = image_to_text(uploaded_image)
            st.write("Extracted Text:", text_from_image)
            response = chat_with_gpt(text_from_image)
            st.write("Answer:", response)

if __name__ == "__main__":
    main()
