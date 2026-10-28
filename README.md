# Week 9 – Chatbot Development

## Project Title
Building an Interactive AI Chatbot using Ollama

## Objective
- Build an interactive chatbot using Python and Ollama.
- Maintain conversation history.
- Save conversations with timestamps.
- Generate educational responses using Llama 3.2.

## Domain
Education

## Technologies Used
- Python
- Ollama
- Llama 3.2
- CSV

## Features
- Accepts continuous user input.
- Generates AI responses.
- Uses previous messages as context.
- Saves questions and responses in `dataset/chat_history.csv`.
- Stops when the user types `exit`.

## How to Run
1. Install Ollama and download the Llama 3.2 model.
2. Install the required Python libraries.
3. Run `python chatbot.py` in the terminal.
4. Type questions and enter `exit` to stop.

## Observations
The chatbot answers educational questions and uses conversation history to provide context-aware responses. Its answers may sometimes be incorrect or incomplete, so they should be verified.

## Limitations
- Responses depend on the local language model.
- The model may generate incorrect information.
- A local model must be available through Ollama.
# week_9
