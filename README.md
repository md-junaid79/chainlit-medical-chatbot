# CyberHeal
## a medical chatbot implemented using chainlit

![CyberHeal Logo](https://github.com/md-junaid79/chainlit-medical-chatbot/blob/main/gamma.jpg?raw=true)

CyberHeal is a futuristic medical chatbot designed to provide general information and answer common questions related to health and wellness. It uses the Gemini model from Google's Generative AI to generate responses.

## Features

- Provides general health information and answers common health-related questions.
- Maintains conversation history for a more personalized experience.
- Supports spontaneous file uploads with messages.
- Customizable UI with support for custom CSS and JavaScript.

## Important Disclaimer

This chatbot is for informational purposes only and **cannot provide medical diagnoses or treatment recommendations**. For any health concerns, please consult with a qualified healthcare professional or your doctor.

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/md-junaid79/chainlit-medical-chatbot.git
    cd chainlit-medical-chatbot
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    venv\Scripts\activate  
    ```

3. Install the required dependencies:
    ```sh
    pip install -r req.txt
    ```

4. Create a [`.env`](.env ) file and add your Google API key:
    ```env
    GOOGLE_API_KEY=your_gemini_api_key
    ```

5. Run the Chainlit :
    ```sh
    chainlit run app.py -w
    ```



## Configuration

You can customize the chatbot's behavior and appearance by modifying the [`.chainlit/config.toml`](.chainlit/config.toml ) file. For example, you can change the assistant's name, description, logo, and more.

## License

This project is licensed under the MIT License. See the [`LICENSE`](LICENSE ) file for more details.

## Acknowledgements

- [Chainlit](https://github.com/Chainlit/chainlit) for providing the framework for building chatbots.
- [Google Generative AI](https://ai.google/tools/generative-ai/) for the Gemini model.

# Feel free to contribute to this project by submitting issues or pull requests.
