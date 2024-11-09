
# AI Assistant with Text, Audio, and Image Recognition

This repository hosts an AI-powered assistant that can process and respond to user queries through **text**, **audio**, and **image** inputs. It uses various models to perform text generation, speech-to-text, and optical character recognition (OCR) for text extraction from images. The project is built with **Streamlit** to provide a user-friendly interface.

## Features

- **Text-Based Responses**: Generate responses based on text input using a GPT-based model.
- **Speech Recognition**: Convert uploaded audio files to text and respond to transcribed queries.
- **Image-to-Text (OCR)**: Extract text from images and generate responses based on recognized text.

## Demo

This application can be deployed on **Hugging Face Spaces** or **locally** on your machine.

## Usage
![Screenshot (3)](https://github.com/user-attachments/assets/93e10310-29db-4445-975f-a918e956ab78)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/AI-assistant.git
   cd AI-assistant
   ```

2. **Install dependencies**:

   Ensure you have Python installed, then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

   Your `requirements.txt` includes:
   - `transformers`: For text generation.
   - `streamlit`: For creating the app interface.
   - `speechrecognition`, `pydub`: For audio processing.
   - `easyocr`: For image-to-text recognition.
   - `torch`, `torchaudio`, `sounddevice`, `numpy`: For handling data and model operations.


### Run the Application
Run the app using Streamlit:
```bash
streamlit run app.py
```

### Interacting with the Assistant
1. **Choose an input type**: You can select between **Text**, **Audio**, and **Image** inputs.
2. **Text Input**: Type your query, and the assistant will generate a response.
3. **Audio Input**: Upload an audio file (e.g., `wav`, `mp3`, or `flac`). The assistant will convert it to text and respond.
4. **Image Input**: Upload an image containing text (e.g., `png`, `jpg`). The assistant will extract text and respond based on the recognized content.

## Project Structure

- **app.py**: Main application code handling all input types (text, audio, image).
- **requirements.txt**: Lists the required packages for setting up the environment.

## Example Code Snippets

### Converting Audio to Text
Uses the `speechrecognition` library to transcribe audio files:
```python
def audio_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        return recognizer.recognize_google(audio)
```

### Image-to-Text (OCR)
Uses `easyocr` to extract text from an image:
```python
def image_to_text(image_file):
    image = Image.open(image_file)
    result = reader.readtext(image)
    return " ".join([text for _, text, _ in result])
```

### Text Generation
Uses the `transformers` library with a lightweight GPT model for generating responses:
```python
def chat_with_gpt(text):
    response = chatbot(text, max_length=150, num_return_sequences=1)
    return response[0]["generated_text"]
```

## Technologies Used

- **Python**
- **Hugging Face Transformers** for text generation
- **EasyOCR** for image-to-text recognition
- **SpeechRecognition and PyDub** for audio processing
- **Streamlit** for web interface

## Future Improvements

- Add real-time microphone input for live speech recognition.
- Expand the assistant’s functionality with more advanced NLP models.
- Optimize performance for faster responses.

## License

This project is open-source and available under the MIT License.
