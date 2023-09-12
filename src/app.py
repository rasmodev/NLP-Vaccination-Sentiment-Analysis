import gradio as gr
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load the fine-tuned model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("path_to_saved_model")
tokenizer = AutoTokenizer.from_pretrained("path_to_saved_tokenizer")

# Define the prediction function
def predict_sentiment(text):
    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    
    # Make predictions
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Get the predicted label
    predicted_label = torch.argmax(outputs.logits).item()
    
    # Map the label to sentiment (e.g., 0 -> Negative, 1 -> Neutral, 2 -> Positive)
    sentiment_mapping = {0: 'Negative', 1: 'Neutral', 2: 'Positive'}
    sentiment = sentiment_mapping[predicted_label]
    
    return sentiment

# Create a Gradio interface
iface = gr.Interface(fn=predict_sentiment, inputs="text", outputs="text")

# Launch the Gradio app
iface.launch()
