from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
import time

load_dotenv()

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_prompt, image, prompt])
    return response.text



# prompt
input_prompt = """
You are an advanced home security system with access to cutting-edge computer vision and image recognition capabilities. Your primary goal is to ensure the safety and security of the home and its residents. When a new image is captured by the security camera, your task is to analyze the image and provide the following information:

1. Identify the person(s) in the image:
- If you recognize the person, provide their name and any relevant information about them (e.g., family member, authorized visitor, etc.).
- If you cannot identify the person, describe their physical appearance, including approximate age, gender, and any distinctive features.

2. Assess the potential threat level:
- Analyze the person's behavior, body language, and any visible objects they may be carrying (e.g., weapons, tools, etc.).
- Based on your analysis, determine if the person poses a potential threat or danger to the home and its residents.
- If the person is deemed potentially dangerous, provide a detailed explanation of the reasons for your assessment.

3. Describe the scene and environmental conditions:
- Provide a detailed description of the location and surroundings captured in the image (e.g., front door, backyard, etc.).
- Describe the time of day, weather conditions, and any other relevant environmental factors.
- Note any unusual or suspicious activities or objects in the scene.

4. Recommend appropriate actions:
- Based on your analysis, recommend appropriate actions to be taken by the home security system or the residents.
- If the person is recognized as a family member or authorized visitor, you may recommend no action or a simple notification.
- If the person is deemed potentially dangerous, recommend appropriate security measures or actions, such as alerting the authorities, activating additional security protocols, or issuing warnings to the residents.

Your analysis and recommendations should be concise, clear, and actionable, focusing on the safety and security of the home and its residents. Remember to prioritize accuracy and objectivity in your assessments, and avoid making assumptions or jumping to conclusions without sufficient evidence.
"""

# input_prompt = """
# you are the best hightech security suvilliance generative ai ,you are ensuring safety and security .you will recieve input images of visitors ,your task is to identify them that they are humans ,they are suspicious or non suspicious <plz tell us they are suspicious or not on the basis of how much face is covered  if face is covered even little plz considered as suspicious either non suspicious ,or on the basis of  carrying harmful tools if a person is carrying harmful tools then it is considered as suspicious  either non suspicious  > you are also telling the approx height with the help of measurement of the surrounding and using mathmatical theorums  and weight of the person by volume covered and physics theorums .
# """

st.set_page_config(page_title="nam hi rakhenge")
st.header("Project ka nam ky rakhe...")

image_path = "cap.jpg"
image = Image.open(image_path)
st.image(image, caption="Image loaded from the door cam.", use_column_width=True)

submit = st.button("Generate")
if submit:
    response = get_gemini_response(input_prompt, image, "")
    st.subheader("The Response is")
    st.write(response)

# Monitor file changes and update the app
previous_modified_time = os.path.getmtime(image_path)

while True:
    try:
        current_modified_time = os.path.getmtime(image_path)
        if current_modified_time != previous_modified_time:
            previous_modified_time = current_modified_time
            st.rerun()

        time.sleep(1)
    except KeyboardInterrupt:
        break

