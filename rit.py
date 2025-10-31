# import streamlit as st
# import requests
# import os
# import json
# from datetime import datetime
# import numpy as np
#
# # Constants & Files
# GROK_API_URL = "https://api.grok.ai/v1/generate"  # Replace with actual endpoint
# GROK_API_KEY = os.environ.get("xai-nCB8xNFTzOFPCc8yWxmYPRgJgPvSBaiUoMFHZ910EXuzzAABvkbLDRwSwuLl59Z2ywxfSV6a8iuciXdM")
# FEEDBACK_FILE = "feedback.json"
#
#
# # Helper functions for feedback storage
# def load_feedback():
#     try:
#         with open(FEEDBACK_FILE, "r") as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return []
#
#
# def save_feedback(feedback_data):
#     with open(FEEDBACK_FILE, "w") as f:
#         json.dump(feedback_data, f, indent=4)
#
#
# def update_temperature(feedback_data, default_temp=0.7):
#     """
#     Simulate a reinforcement learning update:
#     - If average rating is high (>3.5), increase temperature to encourage more creative outputs.
#     - If rating is low (<3), lower temperature for more conservative output.
#     """
#     if not feedback_data:
#         return default_temp
#
#     ratings = [entry["rating"] for entry in feedback_data]
#     avg_rating = np.mean(ratings)
#     new_temp = default_temp
#     if avg_rating > 3.5:
#         new_temp = min(default_temp + 0.1, 1.0)
#     elif avg_rating < 3.0:
#         new_temp = max(default_temp - 0.1, 0.3)
#     return new_temp
#
#
# def generate_creative_content(prompt, temperature):
#     """
#     Call Grok API to generate creative content.
#     Adjust parameters as needed for the actual API.
#     """
#     headers = {
#         "Authorization": f"Bearer {GROK_API_KEY}",
#         "Content-Type": "application/json"
#     }
#     payload = {
#         "prompt": prompt,
#         "temperature": temperature,
#         "max_tokens": 150  # Adjust as needed
#     }
#     try:
#         response = requests.post(GROK_API_URL, headers=headers, json=payload)
#         response.raise_for_status()
#         data = response.json()
#         # Assume the response JSON contains a field "text" with the generated output.
#         return data.get("text", "No content generated.")
#     except Exception as e:
#         return f"Error generating content: {e}"
#
#
# # Streamlit App Layout
# st.title("AI-Powered Creative Collaboration Platform")
# st.write("Enter a creative brief to generate ideas. The system learns from your ratings to adapt its output.")
#
# # User input for creative brief
# prompt = st.text_area("Enter your creative brief:", "Generate an inspiring story idea about a futuristic city...")
#
# # Load previous feedback & compute current temperature
# feedback_data = load_feedback()
# default_temp = 0.7
# temperature = update_temperature(feedback_data, default_temp)
# st.write(f"Current generation temperature: {temperature:.2f}")
#
# # Generate content when the button is pressed
# if st.button("Generate Creative Content"):
#     generated_text = generate_creative_content(prompt, temperature)
#     st.subheader("Generated Content:")
#     st.write(generated_text)
#
#     # Allow user to rate the output (simulate RL feedback)
#     rating = st.slider("Rate this output (1 = poor, 5 = excellent):", 1, 5, 3)
#     if st.button("Submit Rating"):
#         feedback_entry = {
#             "prompt": prompt,
#             "generated_text": generated_text,
#             "rating": rating,
#             "timestamp": datetime.now().isoformat()
#         }
#         feedback_data.append(feedback_entry)
#         save_feedback(feedback_data)
#         st.success("Thanks for your feedback! The system will adjust its output based on ratings.")
#         # Recompute temperature after feedback submission
#         temperature = update_temperature(feedback_data, default_temp)
#         st.write(f"Updated generation temperature: {temperature:.2f}")
#
# # Optionally, display historical feedback for debugging/analysis
# if st.checkbox("Show Feedback History"):
#     st.subheader("Feedback History")
#     st.write(feedback_data)


from google import genai
client = genai.Client(api_key="AIzaSyCeCNb1ae8DhXOCk9ra6ERLUpcRLNGFXEY")

response = client.models.generate_content(
    model = "Gemini  2.O Flash",
    contents = "Explaiin the concept of reinforement learning ."
)