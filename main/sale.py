from huggingface_hub import hf_hub_download

model_id = "runwayml/stable-diffusion-inpainting"
hf_hub_download(repo_id=model_id, filename="model.safetensors", cache_dir=cache_dir)
    