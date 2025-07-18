I implement dreambooth https://arxiv.org/abs/2208.12242 using a plushy monkey as my subject. Text to image diffusion model fine-tuned using dreambooth technique enables generating various novel photorealistic images of the subject contextualized in different scenes.

I prepared dataset consisting of 6 images of a plushy monkey and cropped them to 512x512 resolution. This can be seen in data directory.

![Opis alternatywny obrazka](data/cropped/monke1.jpg)
![Opis alternatywny obrazka](data/cropped/monke2.jpg)
![Opis alternatywny obrazka](data/cropped/monke3.jpg)
![Opis alternatywny obrazka](data/cropped/monke4.jpg)
![Opis alternatywny obrazka](data/cropped/monke5.jpg)
![Opis alternatywny obrazka](data/cropped/monke6.jpg)


I use train_dreambooth.py script from diffusers library: https://github.com/huggingface/diffusers/blob/main/examples/dreambooth/train_dreambooth.py

I use stable diffusion v1-5 as a base model. I fine tune CLIP-based text encoder to embedd new token "byn" which is a name of a plushy monkey I came up with. It is one token in tokenizer I use which is desired in dreambooth.

Because of that, I was not able to train it on my laptop because my GPU has only 8 VRAM which is not enough. I used ICM's supercomputer https://kdm.icm.edu.pl.

Below, I post images which I liked the most and corresponding prompts, these are cherry picked examples, I rejected most of images.




