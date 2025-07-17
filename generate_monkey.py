import torch
from diffusers import StableDiffusionPipeline
import matplotlib.pyplot as plt
from pathlib import Path

cwd = Path(__file__).resolve().parent
model_dir = cwd / "model"

pipe = StableDiffusionPipeline.from_pretrained(
    model_dir,
    torch_dtype=torch.float16,
    local_files_only=True,
)
pipe = pipe.to("cuda")

prompt = "a dramatic film noir scene: byn plushy monkey in a fedora, smoke-filled alley, high contrast lighting"

images = pipe([prompt]*8, num_inference_steps=100, guidance_scale=10).images

fig, axs = plt.subplots(2, 4, figsize=(12, 12))
for ax, img in zip(axs.flatten(), images):
    ax.imshow(img)
    ax.axis("off")

plt.tight_layout()
plt.show()

