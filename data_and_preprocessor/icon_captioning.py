import pandas as pd
import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# 读取保存的预测结果 CSV
df = pd.read_csv("/kaggle/input/lol-icon-prediction/icon_label_predictions.csv")  # 里面有 fname, prob_like

# 只要 prob_like > 0.7 的
df = df[df["prob_like"] > 0.7]

# BLIP 模型
device = "cuda" if torch.cuda.is_available() else "cpu"

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(device)

TRIGGER = "<lolicon>"

captions = []
for fname in df["fname"]:
    # print(fname)
    raw_image = Image.open(f"/kaggle/working/lol_profile_icons/{fname}").convert("RGB")
    inputs = processor(raw_image, return_tensors="pt").to(device)
    out = model.generate(**inputs, max_length=30)
    caption = processor.decode(out[0], skip_special_tokens=True)

    # 改进：加 trigger + 风格模板
    caption = f"a {TRIGGER} League of Legends style icon of {caption}"
    captions.append(caption)

df["caption"] = captions
df.to_csv("captions.csv", index=False)

