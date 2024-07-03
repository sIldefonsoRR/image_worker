import settings
import os
from image_ai import Image_AI


api_key = settings.STABILITY_API_KEY
stability_url = settings.STABILITY_URL

prompt = 'A renascentist style painting with a plane, a crane, a car a man and a tree!'
folder_name = 'outputs'
file_name = 'output_001.webp'
file_output = os.path.join(folder_name, file_name)


# RUN
worker = Image_AI(api_key)
# image_content = worker.generate_image_from_prompt(prompt)
# with open(file_output, 'wb') as f:
#     f.write(image_content)

file_input = os.path.join(folder_name, file_name)
with open(file_input, "rb") as fr:
    image = fr.read()
result = worker.describe_image(image)
print(f"Image analysis: {result}")
