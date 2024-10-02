
# Import required libraries
from diffusers import StableDiffusionInpaintPipeline
import torch
from PIL import Image
import requests
from io import BytesIO
import numpy as np

# Load the image
image_url = "https://drive.google.com/uc?export=download&id=17FCAXI5mS2Iof9NWQAmg68H2rGK0xTIc"
response = requests.get(image_url)
original_image = Image.open(BytesIO(response.content)).convert("RGB")

# Resize the canvas to 1280x1280 and center the original image
new_size = (1280, 1280)
new_image = Image.new("RGB", new_size)
new_image.paste(original_image, (128, 128))

# Load the stable diffusion inpainting model
pipe = StableDiffusionInpaintPipeline.from_pretrained("runwayml/stable-diffusion-inpainting", torch_dtype=torch.float16).to("cuda")

# Prepare the mask indicating the regions to outpaint (128 pixels on each side)
mask = Image.new("L", new_size, 0)
mask.paste(255, (0, 0, 1280, 128))  # Top
mask.paste(255, (0, 1152, 1280, 1280))  # Bottom
mask.paste(255, (0, 0, 128, 1280))  # Left
mask.paste(255, (1152, 0, 1280, 1280))  # Right

# Generate the outpainted image
outpainted_image = pipe(prompt="", image=new_image, mask_image=mask).images[0]

# Save the outpainted image
outpainted_image.save("outpainted_image.png")

# Display the outpainted image
outpainted_image.show()
