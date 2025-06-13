import time
import torch
from diffusers import StableDiffusionPipeline

start_time = time.time()
pipeline = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-1", torch_dtype=torch.float16)
pipeline = pipeline.to('cuda')
prompt = "Generate an image of a orange cat. Ensure the cat is in full view in the image"
image = pipeline(prompt=prompt).images[0]
image.save("catcat.png", format="PNG")
end_time = time.time()
print(f"I am going mao. Time taken: {end_time - start_time} seconds")