import requests
from PIL import Image #PIL = Python Image Library
from transformers import AutoProcessor, BlipForConditionalGeneration

#1.
#Load the pretrained processor and model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

#2.
# Load your image, DONT FORGET TO WRITE YOUR IMAGE NAME
img_path = "snow-leopard.png"
# convert it into an RGB format 
image = Image.open(img_path).convert('RGB')


#3. Process the image
text = "the image of"
inputs = processor(images=image, text=text, return_tensors="pt")


#4.
# Generate a caption for the image
outputs = model.generate(**inputs, max_length=50)


#5.
# Decode the generated tokens to text
caption = processor.decode(outputs[0], skip_special_tokens=True)
# Print the caption
print(caption)








