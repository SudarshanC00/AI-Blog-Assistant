# 🚀🚀BlogCraft: Your AI Writing Companion

## Overview
BlogCraft is an AI-powered tool that helps users generate engaging blog posts based on their input. Built with Streamlit, Google Gemini, and OpenAI's DALL-E, BlogCraft allows users to input blog details, including title, keywords, and word count, and generates a complete blog post along with a relevant image.

## Features
- **AI Blog Generation**: Generate comprehensive and informative blog posts based on user-defined title, keywords, and word count.
- **Image Generation**: Uses DALL-E to create relevant images based on the blog title.
- **Customizable Blog Parameters**: Adjust the number of words and images to tailor the output.

## Files
- **app.py**: The main application code that initializes the Streamlit interface, configures the Google Gemini model for text generation, and OpenAI’s DALL-E for image creation.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/YourUsername/BlogCraft.git
   ```
2. Navigate to the project directory:
   ```bash
   cd BlogCraft
   ```
4. Add your API keys:
   - Replace `"API_KEY"` in `app.py` with your OpenAI and Google Gemini API keys.

## Usage
1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. In the app, enter the blog details:
   - **Blog Title**: Title of the blog post.
   - **Keywords**: Keywords to incorporate into the blog.
   - **Number of Words**: Choose the length of the blog post.
   - **Number of Images**: Specify the number of images to generate.

3. Click **Generate Blog** to produce the blog post and images.

## Dependencies
- **Streamlit**: For creating the web interface.
- **Google Generative AI (Gemini)**: For generating blog content.
- **OpenAI DALL-E**: For creating relevant images.

## License
This project is licensed under the MIT License.
