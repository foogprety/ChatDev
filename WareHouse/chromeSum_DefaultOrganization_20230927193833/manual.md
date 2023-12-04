# Chrome Extension App User Manual

## Introduction

The Chrome Extension App is a tool that allows users to summarize articles from websites using the OpenAI API. This user manual will guide you through the installation process, explain the main functions of the software, and provide instructions on how to use it effectively.

## Installation

To use the Chrome Extension App, follow these steps:

1. Install Python: Make sure you have Python installed on your system. You can download the latest version of Python from the official website (https://www.python.org/downloads/).

2. Install Dependencies: Open a terminal or command prompt and navigate to the directory where you have downloaded the Chrome Extension App code. Run the following command to install the required dependencies:

   ```
   pip install tkinter requests openai
   ```

3. Obtain OpenAI API Key: In order to use the OpenAI API, you need to obtain an API key. Visit the OpenAI website (https://www.openai.com/) and sign up for an account. Once you have an account, you can generate an API key from the OpenAI dashboard.

## Main Functions

The Chrome Extension App provides the following main functions:

1. API Key Entry: Upon launching the app, you will be prompted to enter your OpenAI API key. Simply type your API key into the provided text field and click the "Submit" button.

2. Article Summarization: After entering your API key, you will be able to summarize articles from websites. To do this, simply navigate to the desired article on a website and copy the article content.

3. Displaying the Summary: Once you have copied the article content, return to the Chrome Extension App and click the "Summarize" button. The app will use the OpenAI API to generate a summary of the article. The summary will be displayed in the console.

## Usage

To use the Chrome Extension App, follow these steps:

1. Launch the App: Open a terminal or command prompt and navigate to the directory where you have downloaded the Chrome Extension App code. Run the following command to launch the app:

   ```
   python main.py
   ```

2. Enter API Key: When the app window appears, enter your OpenAI API key in the provided text field and click the "Submit" button.

3. Summarize an Article: Navigate to a website with an article you want to summarize. Copy the article content.

4. Generate Summary: Return to the Chrome Extension App window and click the "Summarize" button. The app will use the OpenAI API to generate a summary of the article.

5. View Summary: The generated summary will be displayed in the console.

## Conclusion

The Chrome Extension App is a powerful tool for summarizing articles from websites using the OpenAI API. By following the installation instructions and using the app as described in this user manual, you can easily summarize articles and extract key information efficiently. Enjoy using the Chrome Extension App!