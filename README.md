# English Language Tutor with Chatbot Interaction

## Overview

This project integrates a chatbot with an English Language Tutor, providing users with language tutoring features, including pronunciation assessment, fluency evaluation, pitch analysis, mispronunced words. The chatbot is capable of engaging in conversations based on different contexts, enhancing the user experience.

## Features

- Pronunciation assessment
- Fluency evaluation
- Pitch analysis
- Contextual chatbot interaction
- Name recognition and personalization

## Options 
Choose from different chatbot contexts:

- Professional event
- Medical intern-patient conversation
- Job interview
- Coffee break with a friend
- Airline assistant-client conversation
- Event planner-client conversation (lively, professional, and brief)

## Dependencies

Ensure you have the necessary dependencies installed by running the following command:

```bash
pip install -r requirements.txt
```
Replace YOUR_OPENAI_API_KEY in the code with your actual OpenAI API key.

## Usage 
- Provide user input through audio.
- The system evaluates pronunciation, completeness, fluency, and pitch.
- Engage in contextual chatbot conversations.
- Chatbot recognizes and responds to user names.
- The system identifies mispronounced words and provides feedback.

To interact with the language tutoring chatbot set your selected role in the `option` variable and your innput in the `user_input_audio` variable and run the following command 
```python
python english_tutor_chatbot_while_git.py
```
To use the chatbot in a function use the following command after setting the selected role in the `option` variable and the user audio response in the `user_input_audio` variable 
```python
python english_tutor_chatbot_function_git.py
```
To interact with the chatbot through audio input through your microphone set the chatbot role in the `option` variable and run the following command 
```python
python english_tutor_chatbot_mic.py
```
In the above english_tutor_chatbot_mic.py file
- The chatbot prompts the user to select a role for the conversation.
- Users input text for pronunciation practice.
- The chatbot pronounces the user's input, emphasizing correct pronunciation.
- Users provide audio input for evaluation against the prompt.
- Pronunciation reports are generated, highlighting mispronounced words.
- The chatbot re-pronounces mispronounced words for further practice.
- Users repeat the process until correct pronunciation is achieved.
- Upon successful pronunciation, the chatbot generates a response.
- The loop continues until the user inputs exit.

## Acknowledgments
- This project utilizes the OpenAI API for conversation generation.
- This project utilizes Azure Speech SDK for speech evaluation. 

