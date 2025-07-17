#!/usr/bin/env python3
import subprocess
import sys
from accelerate.utils import write_basic_config
from pathlib import Path

def main():

    write_basic_config()
    cwd = Path(__file__).resolve().parent

    instance_data_dir = cwd / "data" / "cropped"
    output_dir = cwd / "model"
    class_dir = cwd / "data" / "class_images"

    for d in (instance_data_dir, output_dir, class_dir):
        d.mkdir(parents=True, exist_ok=True)

    cmd = [
        "accelerate", "launch", "train_dreambooth.py",
        "--pretrained_model_name_or_path", "runwayml/stable-diffusion-v1-5",
        "--instance_data_dir", str(instance_data_dir),
        "--instance_prompt", "a photo of byn plushy monkey",
        "--with_prior_preservation",
        "--prior_loss_weight", "1.0",
        "--class_data_dir", str(class_dir),
        "--class_prompt", "a photo of a plushy monkey",
        "--output_dir", str(output_dir),
        "--resolution", "512",
        "--train_batch_size", "1",
        "--gradient_accumulation_steps", "1",
        "--learning_rate", "2e-6",
        "--lr_scheduler", "constant",
        "--lr_warmup_steps", "0",
        "--max_train_steps", "400",
        "--gradient_checkpointing",
        "--train_text_encoder"
    ]

    print("Starting training:\n", " ".join(cmd), "\n")
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print("Training error:", e, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()