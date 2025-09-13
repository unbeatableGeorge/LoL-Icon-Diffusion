# 🎯 LoL Icon Diffusion — Text-to-Image with LoRA

An end-to-end text-to-image project: 

collect League of Legends profile icons → filter with CLIP + binary head → generate captions with BLIP → fine-tune Stable Diffusion with LoRA → generate high-quality icons **directly from text prompts**.

> **Highlights**  
> - Pure text-to-image: generate icons from prompts, not from input images  
> - Fully reproducible pipeline: data → labeling (filtering) → training → inference  
> - Transparent setup (thresholds, models, training parameters)

---

## 🔥 Sample Results (placeholders — replace with your outputs)

> Showcase your generated images with their text prompts


| Text Prompt | Generated Image                           |
|-------------|-------------------------------------------|
| *"a <lolicon> League of Legends style icon of a cartoon character with a cat face and a blue hair"* | <img src="assets/gen_1.png" width="120"/> |
| *"a <lolicon> League of Legends style icon of a dark knight in heavy armor"* | <img src="assets/gen_2.png" width="120"/> |
| *"a <lolicon> League of Legends style icon of a radiant archer with golden bow"* | <img src="assets/gen_3.png" width="120"/> |
| *"a <lolicon> League of Legends style icon of a cybernetic assassin with glowing red eyes"* | <img src="assets/gen_4.png" width="120"/> |
| *"a <lolicon> League of Legends style icon of a cartoon character with blue hair and a purple dress"* | <img src="assets/gen_5.png" width="120"/> |

More samples in `assets/gallery/`

## 🎨 More Samples

| ![](assets/gallery/sample_1.png)  | ![](assets/gallery/sample_2.png) | ![](assets/gallery/sample_3.png)  |
|-----------------------------------|----------------------------------|-----------------------------------|
| ![](assets/gallery/sample_4.png)  | ![](assets/gallery/sample_5.png) | ![](assets/gallery/sample_6.png)  |
| ![](assets/gallery/sample_7.png)  | ![](assets/gallery/sample_8.png) | ![](assets/gallery/sample_9.png)  |
| ![](assets/gallery/sample_10.png) | ![](assets/gallery/sample_11.png)| ![](assets/gallery/sample_12.jpg) |
| ![](assets/gallery/sample_13.jpg) | ![](assets/gallery/sample_14.png)| ![](assets/gallery/sample_15.png) |

---

## 🧭 Pipeline Overview

```mermaid
flowchart LR
  A[Download LoL Icons] --> B[CLIP + Binary Head\nFilter “liked” icons]
  B --> C[BLIP Auto-Captioning\nGenerate image-text pairs]
  C --> D[LoRA Fine-tune Stable Diffusion]
  D --> E[Text-to-Image Generation\nNew icons from prompts]
