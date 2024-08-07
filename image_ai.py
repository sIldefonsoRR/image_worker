import requests
import logging
import io
from PIL import Image
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer


class Image_AI:
    def __init__(self,
                 api_key,
                 stability_url='https://api.stability.ai/v2beta/stable-image/generate/core') -> None:
        """
        Initialize the Image_AI class with the provided API key and Stability AI API URL.
        Args:
        api_key (str): The API key required for accessing the Stability AI API.
        stability_url (str): The URL of the Stability AI API endpoint for generating images.
                        Defaults to 'https://api.stability.ai/v2beta/stable-image/generate/core'.
        Returns:
        None
        Raises:
        No specific exceptions are raised.
        """
        self.stability_url = stability_url
        self.api_key = api_key

    def generate_image_from_prompt(self, prompt):
        """
        Generate an image based on the provided prompt using the Stability AI API.
        Args:
        prompt (str): The prompt for generating the image.
        Returns:
        bytes: The content of the generated image in webp format.
        Raises:
        Any exceptions raised by the requests.post method when interacting with the Stability AI API
        """
        headers = {
            'authorization': f'Bearer {self.api_key}',
            'accept': 'image/*',
            }
        files = {
            'prompt': (None, prompt),
            'output_format': (None, 'webp'),
            }
        response = requests.post(self.stability_url,
                                 headers=headers,
                                 files=files)
        return response.content

    def describe_image(self, image_bytes):
        """
        Generate a textual description of an image using the VisionEncoderDecoderModel from the transformers library.
        Args:
            image_bytes (bytes): The content of the image in bytes format.
        Returns:
            str: The textual description of the image generated by the model.
        Raises:
            No specific exceptions are raised within the method.
        """
        logging.getLogger("transformers").setLevel(logging.ERROR)
        model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
        image_processor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
        tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
        image = Image.open(io.BytesIO(image_bytes))
        pixel_values = image_processor(images=image, return_tensors="pt").pixel_values
        output_ids = model.generate(pixel_values, max_length=50, num_beams=4,
                                    early_stopping=True)[0]
        caption = tokenizer.decode(output_ids, skip_special_tokens=True)
        return caption
