from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image
import torch

processor = ViTImageProcessor.from_pretrained(
    "google/vit-base-patch16-224"
)
model = ViTForImageClassification.from_pretrained(
    "google/vit-base-patch16-224"
)

def classify_image(image_file):
    image = Image.open(image_file)
    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = logits.argmax(-1).item()
    label = model.config.id2label[predicted_class]
    return label
