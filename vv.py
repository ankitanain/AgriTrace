# import google.generativeai as genai
# from pathlib import Path 
# import gradio as gr 
# from dotenv import load_dotenv
# import os

# load_dotenv()

# genai.configure(api_key=os.getenv("AIzaSyCX9ZL5J9BEaFiZpSvz1iRO0QsCy4ECH6s"))

# generation_config = {
#     "temperature": 0.5,
#     "top_p": 1.0,
#     "top_k": 32,
#     "max_output_tokens": 4096,
# }

# safety_settings = [
#     {"category": f"HARM_CATEGORY_{category}", "threshold": "BLOCK_MEDIUM_AND_ABOVE"}
#     for category in ["HARASSMENT", "HATE_SPEECH", "SEXUALLY_EXPLICIT", "DANGEROUS_CONTENT"]
# ]

# model = genai.GenerativeModel(
#     model_name="gemini-pro-vision",
#     generation_config=generation_config,
#     safety_settings=safety_settings,
# )

# def read_image_data(file_path):
#     image_path = Path(file_path)
#     if not image_path.exists():
#         raise ValueError(f"File not found: {image_path}")
#     return {"mime_type":"image/jpeg","data":image_path.read_bytes()}

# def generates_gemini_resoponse(prompt, image_path):
#     image_data = read_image_data(image_path)
#     response = model.generate_content([prompt, image_data])
#     return response.text

# input_prompt ="""As a highly skilled plant pathologist of  crop , your expertise is indispensable in our pursuit of maintaining optimal plant health. You will be provided with information or samples related to plant diseases, and your role involves conducting a detailed analysis to identify the specific issues, propose solutions, and offer recommendations.
# rice .

# *Analysis Guidelines:*

# 1. *Crop Healthy or not:* Tell weather the crop is healthy or not in one word

# .

# # 1. *Disease Identification:* Examine the provided information or samples to identify and characterize plant diseases accurately.
# 1. *Disease Identification:* Examine the provided information or samples to identify and characterize plant diseases accurately. Tell the disease name in one word 




# 2. *Detailed Findings:* Provide in-depth findings in the form of 3 bullet points on the nature and extent of the identified plant diseases, including affected plant parts, symptoms, and potential causes

# \n.

# 3 . *Name of fungicides : *  Give the value of fungicides which can cure the disease of the crop.Name some commonly used fungicides.

# 4. *Next Steps:* Outline the recommended course of action for managing and controlling the identified plant diseases. Involve treatment options, preventive measures, and name of pesticides or fungicides etc in bullet points

# .

# 5. *Recommendations:* Offer informed recommendations for maintaining plant health, preventing disease spread, and optimizing overall plant well-being

# .

# 6. *Important Note:* As a plant pathologist, your insights are vital for informed decision-making in agriculture and plant management. Your response should be thorough, concise, and focused on plant health.

# *Disclaimer:*
# "Please note that the information provided is based on plant pathology analysis and should not replace professional agricultural advice. Consult with qualified agricultural experts before implementing any strategies or treatments."

# Your role is pivotal in ensuring the health and productivity of plants. Proceed to analyze the provided information or samples, adhering to the structured 

# """

# def process_uploaded_files(files):
#     file_path = files[0].name if files else None
#     response = generates_gemini_resoponse(input_prompt, file_path) if file_path else None
#     return file_path, response

# with gr.Blocks() as demo:
#     file_output = gr.Textbox()
#     image_output = gr.Image()
#     combined_output = [image_output, file_output]
#     upload_button = gr.UploadButton(
#         "Click to upload an Image",
#         file_types = ['images'],
#         file_count ='multiple',
#     )

#     upload_button.upload(process_uploaded_files,upload_button,combined_output)

#     demo.launch(debug = True)


# def process_uploaded_files(files):
#     file_path = files[0].name if files else None
#     response = generates_gemini_resoponse(input_prompt, file_path) if file_path else None
#     if response:
#         response += "\n\nIf you want to buy these suggested fertilizers then click here."
#     return file_path, response


def process_uploaded_files(files):
    file_path = files[0].name if files else None
    response = generates_gemini_resoponse(input_prompt, file_path) if file_path else None
    additional_line = "\n\nIf you want to buy these suggested fertilizers then click here."
    return file_path, response, additional_line

with gr.Blocks() as demo:
    file_output = gr.Textbox()
    image_output = gr.Image()
    combined_output = [image_output, file_output]
    upload_button = gr.UploadButton(
        "Click to upload an Image",
        file_types=['images'],
        file_count='multiple',
    )

    def process_and_display_files(files):
        file_path, response, additional_line = process_uploaded_files(files)
        if response:
            file_output.update(response + additional_line)

    upload_button.upload(process_and_display_files, upload_button, combined_output)

    demo.launch(debug=True)
