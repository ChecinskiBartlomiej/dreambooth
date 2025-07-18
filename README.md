I implement dreambooth https://arxiv.org/abs/2208.12242 using a plushy monkey as my subject. Text to image diffusion model fine-tuned using dreambooth technique enables generating various novel photorealistic images of the subject contextualized in different scenes.

I prepared dataset consisting of 6 images of a plushy monkey and cropped them to 512x512 resolution. This can be seen in data directory.

<table>
  <tr>
    <td><img src="data/cropped/monke1.jpg" width="160"/></td>
    <td><img src="data/cropped/monke2.jpg" width="160"/></td>
    <td><img src="data/cropped/monke3.jpg" width="160"/></td>
  </tr>
  <tr>
    <td><img src="data/cropped/monke4.jpg" width="160"/></td>
    <td><img src="data/cropped/monke5.jpg" width="160"/></td>
    <td><img src="data/cropped/monke6.jpg" width="160"/></td>
  </tr>
</table>


I use train_dreambooth.py script from diffusers library: https://github.com/huggingface/diffusers/blob/main/examples/dreambooth/train_dreambooth.py

I use stable diffusion v1-5 as a base model. I fine tune CLIP-based text encoder to embedd new token "byn" which is a name of a plushy monkey I came up with. It is one token in tokenizer I use which is desired in dreambooth.

Because of that, I was not able to train it on my laptop because my GPU has only 8 VRAM which is not enough. I used ICM's supercomputer https://kdm.icm.edu.pl.

Below, I post images which I liked the most and corresponding prompts, these are cherry picked examples, I rejected most of images.

### byn plushy monkey exploring a futuristic space station interior, neon lights, cyberpunk vibe

<table>
  <tr>
    <td><img src="data/cropped/best/2/10.jpg" width="160"></td>
  </tr>

### byn plushy monkey discovering a treasure at the bottom of the ocean, shafts of sunlight and shimmering seashells

  <tr>
    <td><img src="data/cropped/best/3/4.jpg" width="160"></td>
  </tr>

### byn plushy monkey in ancient Mayan temple ruins overgrown with lush greenery, epic adventure feel

  <tr>
    <td><img src="data/cropped/best/4/1.jpg" width="160"></td>
    <td><img src="data/cropped/best/4/4.jpg" width="160"></td>
    <td><img src="data/cropped/best/4/9.jpg" width="160"></td>
  </tr>
</table>

