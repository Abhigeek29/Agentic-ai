# 🧠 Agentic AI Code Mentor
🌟 Empowering Education Through Code Feedback
    This project is a code authenticator and feedback mechanism designed to help learners and developers improve their programming skills. By leveraging the power of Agentic AI, this tool provides intelligent analysis, identifies errors, and offers recommendations to enhance code quality. Our goal is to contribute to SDG 4: Quality Education by making personalized and insightful code feedback accessible to everyone.
-------------------------------------------------------------------------------------------------------------------------------
✨ Features
    -Intuitive UI: A clean and easy-to-use web interface where you can paste your code.

    -Intelligent Analysis: The system analyzes the code using powerful language models to understand its purpose and logic.

    -Error Detection: It accurately points out syntax errors, logical flaws, and potential bugs.

    -Code Quality Improvement: The agent provides actionable feedback to improve code style, efficiency, and best practices.

    -Comprehensive Reporting: Receive a detailed summary, specific requirements met by the code, and recommendations for further enhancements.
-------------------------------------------------------------------------------------------------------------------------------
🛠️ Technology Stack
    Frontend:

        -HTML/CSS/JavaScript: For a responsive and interactive user interface.

    Backend:

        -Flask: A lightweight and efficient Python web framework to handle API requests.

    Agentic AI:

        -Gemini & OpenAI: The core of the feedback mechanism, providing the intelligence to analyze and generate insightful   feedback on the code.
-------------------------------------------------------------------------------------------------------------------------------
🚀 Getting Started
    -To get a local copy of this project up and running, follow these simple steps.

    -Prerequisites
        You will need Python and pip installed on your system.
    - Installation
        1.Clone the repository:

            git clone https://github.com/Abhigeek29/Agentic-ai.git
            cd Agentic-ai
        2. Install backend dependencies:

            pip install Flask
                # Install the necessary libraries for Gemini and OpenAI, e.g.,
                # pip install google-generativeai openai
        3. Set up your API keys:

            Create a .env file in the root directory and add your API keys.

                OPENAI_API_KEY="your_openai_api_key_here"
                GEMINI_API_KEY="your_gemini_api_key_here"
        4. Run the Flask application:

                python app.py
                Note: The main application file might be named differently, e.g., main.py.
------------------------------------------------------------------------------------------------------------------------------💡 How to Use
    Open your web browser and navigate to http://127.0.0.1:5000.

    Paste your code into the text area.

    Click the "Analyze" button.

    The Agentic AI will process your code and display a detailed report with feedback, errors, and recommendations.                
-------------------------------------------------------------------------------------------------------------------------------
🤝 Contributing
    Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

    Fork the Project.

    Create your Feature Branch (git checkout -b feature/NewFeature).

    Commit your Changes (git commit -m 'Add some NewFeature').

    Push to the Branch (git push origin feature/NewFeature).

    Open a Pull Request.
