# Python Quiz

A robust, terminal-based application built in Python for creating, managing, and taking quizzes. This project utilizes Object-Oriented Programming (OOP) to model individual quiz questions and orchestrate full quiz sessions.

## Features
* **Quiz Item Management:** Create quiz questions with custom multiple-choice options and designated correct answers.
* **Dynamic Modification:** Edit existing questions, options, or correct answers on the fly.
* **Interactive Quiz Mode:** Test your knowledge by taking the quiz directly in the terminal with instant True/False feedback.
* **Persistence (Session-based):** View all current quiz items in a formatted list.
* **Error Handling:** Basic exception handling to manage invalid inputs and maintain program stability.

## Classes
* **Quiz_item** The data model for a single question. It handles the formatting of the question/choices and validation of answers.
* **Quiz:** A container class that manages a collection of Quiz_item objects within a dictionary.

## 🚀 How to Run
1. Ensure you have Python installed.
2. Run the script:
   ```bash
   python quiz_manager.py
