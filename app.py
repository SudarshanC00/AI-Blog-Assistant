import streamlit as st
import google.generativeai as genai
import openai


openAI_api = "API KEY"
google_api = "API_KEY"

genai.configure(api_key=google_api)
openai.api_key=openAI_api

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

st.set_page_config(layout="wide")
st.title('📝 BlogCraft: Your AI Writing Companion')
st.subheader("Now you can craft perfect blogs with the help of AI - BlogCraft is your New AI Blog Companion")
blog = """

"""

with st.sidebar:
    st.title("Input Your Blog Details")
    st.subheader("Enter Details of the Blog You want to generate")

    blog_title = st.text_input("Blog Title")
    keywords = st.text_area("Keywords (Comma Separated)")
    num_words = st.slider("Number of words", min_value = 250, max_value = 1000, step=100)
    num_images = st.number_input("Number of images", min_value = 1, max_value = 5, step=1)

    prompt_parts = [
        f"Generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" and keywords \"{keywords}\" .Make sure to incorporate these keywords in the blog post. the blog should be approximately \"{num_words}\" words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout.",
    ]

    response = model.generate_content(prompt_parts)
    submit_button = st.button("Generate Blog")

if submit_button:
    response_image = openai.Image.create(
        model="dall-e-3",
        prompt= f"{blog_title}",
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response_image.data[0].url
    st.image(image_url, caption="Generated Image")
    st.title("YOUR BLOG POST:")
    st.write(response.text)