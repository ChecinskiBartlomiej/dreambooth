I implemented [DreamBooth](https://arxiv.org/abs/2208.12242), using a plush monkey as the subject.  
Fine‑tuning a text‑to‑image diffusion model with DreamBooth lets me generate novel, photorealistic pictures of the monkey in a wide range of scenes.

The dataset contains six 512 × 512 crops of the plush monkey (see the `data/` directory).

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

I trained with the `train_dreambooth.py` script from 🤗 Diffusers  
(<https://github.com/huggingface/diffusers/blob/main/examples/dreambooth/train_dreambooth.py>)  
using **Stable Diffusion v1‑5** as the base model.

The CLIP text encoder was fine‑tuned to embed a new token **“byn”** – the name I gave the plush monkey.  
Because “byn” is a single token in the tokenizer, it works well for DreamBooth.

Training would not fit into my laptop‑GPU (8 GB VRAM), so I ran the job on the ICM supercomputer  
(<https://kdm.icm.edu.pl>).

Below are my favourite generations and their prompts (cherry‑picked – most images were discarded).

### byn plush monkey exploring a futuristic space‑station interior, neon lights, cyberpunk vibe
<table>
  <tr><td><img src="best/2/10.png" width="160"></td></tr>
</table>

---

### byn plush monkey discovering treasure on the ocean floor, shafts of sunlight, shimmering seashells
<table>
  <tr><td><img src="best/3/4.png" width="160"></td></tr>
</table>

---

### byn plush monkey in overgrown Mayan temple ruins, epic adventure feel
<table>
  <tr>
    <td><img src="best/4/1.png"  width="160"></td>
    <td><img src="best/4/4.png"  width="160"></td>
    <td><img src="best/4/9.png"  width="160"></td>
  </tr>
</table>

---

### byn plush monkey having tea in a Victorian parlour, elegant porcelain cups, warm lamplight
<table>
  <tr><td><img src="best/5/9.png" width="160"></td></tr>
</table>

---

### byn plush monkey dressed as a pirate on deck, billowing sails and crashing waves, comic‑book style
<table>
  <tr><td><img src="best/6/8.png" width="160"></td></tr>
</table>

---

### byn plush monkey dancing at a masked ball in a Baroque ballroom, ornate décor, crystal chandeliers
<table>
  <tr>
    <td><img src="best/7/6.png" width="160"></td>
    <td><img src="best/7/9.png" width="160"></td>
  </tr>
</table>

---

### byn plush monkey tagging graffiti on a city street at night, colourful murals, lamppost glow
<table>
  <tr><td><img src="best/8/1.png" width="160"></td></tr>
</table>

---

### byn plush monkey cooking in a professional kitchen, steam rising from pots, documentary realism
<table>
  <tr>
    <td><img src="best/10/3.png"  width="160"></td>
    <td><img src="best/10/7.png"  width="160"></td>
    <td><img src="best/10/10.png" width="160"></td>
  </tr>
</table>

---

### byn plush monkey trekking across snow‑capped mountains, bright sunlight, wide‑angle landscape
<table>
  <tr>
    <td><img src="best/11/7.png" width="160"></td>
    <td><img src="best/11/8.png" width="160"></td>
    <td><img src="best/11/9.png" width="160"></td>
  </tr>
</table>

---

### byn plush monkey sitting on a stone pier by a misty lake at dawn, serene mood
<table>
  <tr>
    <td><img src="best/12/8.png"  width="160"></td>
    <td><img src="best/12/10.png" width="160"></td>
  </tr>
</table>

---

### byn plush monkey enjoying a sunset at an amusement park, carousel lights, dreamy bokeh
<table>
  <tr>
    <td><img src="best/16/1.png" width="160"></td>
    <td><img src="best/16/2.png" width="160"></td>
    <td><img src="best/16/6.png" width="160"></td>
  </tr>
</table>

---

### byn plush monkey as a knight on horseback outside a medieval castle, epic fantasy art
<table>
  <tr>
    <td><img src="best/18/1.png"  width="160"></td>
    <td><img src="best/18/10.png" width="160"></td>
  </tr>
</table>

---

### byn plush monkey standing on a desert dune beneath a rising moon, dramatic shadows, minimalist
<table>
  <tr><td><img src="best/19/1.png" width="160"></td></tr>
</table>

---

### byn plush monkey DJ‑ing in a techno club, pulsing lasers, dynamic crowd shot
<table>
  <tr>
    <td><img src="best/21/1.png" width="160"></td>
    <td><img src="best/21/5.png" width="160"></td>
    <td><img src="best/21/9.png" width="160"></td>
  </tr>
</table>

---

### byn plush monkey walking on Mars in an astronaut suit, red rocks and dust, photorealistic render
<table>
  <tr>
    <td><img src="best/24/2.png" width="160"></td>
    <td><img src="best/24/4.png" width="160"></td>
  </tr>
</table>
