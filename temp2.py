import torch
from PIL import Image
import requests
from lavis.models import load_model_and_preprocess

img_url = 'https://storage.googleapis.com/sfr-vision-language-research/LAVIS/assets/merlion.png' 
raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')   

device = torch.device("cuda") if torch.cuda.is_available() else "cpu"

# we associate a model with its preprocessors to make it easier for inference.
# model, vis_processors, _ = load_model_and_preprocess(
#    name="blip2_t5", model_type="pretrain_flant5xxl", is_eval=True, device=device
# )

# Other available models:
# 
model, vis_processors, _ = load_model_and_preprocess(
    name="blip2_opt", model_type="pretrain_opt2.7b", is_eval=True, device=device
)

# model, vis_processors, _ = load_model_and_preprocess(
#     name="blip2_opt", model_type="pretrain_opt6.7b", is_eval=True, device=device
# )
# model, vis_processors, _ = load_model_and_preprocess(
#     name="blip2_opt", model_type="caption_coco_opt2.7b", is_eval=True, device=device
# )
# model, vis_processors, _ = load_model_and_preprocess(
#     name="blip2_opt", model_type="caption_coco_opt6.7b", is_eval=True, device=device
# )
#
# model, vis_processors, _ = load_model_and_preprocess(
#     name="blip2_t5", model_type="pretrain_flant5xl", is_eval=True, device=device
# )
#
# model, vis_processors, _ = load_model_and_preprocess(
#     name="blip2_t5", model_type="caption_coco_flant5xl", is_eval=True, device=device
# )

image = vis_processors["eval"](raw_image).unsqueeze(0).to(device)

print(model.generate({"image": image}))
print("------------------------------------------------------------")

print(model.generate({"image": image}, use_nucleus_sampling=True, num_captions=3))
print("------------------------------------------------------------")

print(model.generate({"image": image, "prompt": "Clue: "}))
print("------------------------------------------------------------")

print(model.generate({
    "image": image,
    "prompt": "Question: which city is this? Answer: singapore. Question: why?"}))
print("------------------------------------------------------------")

context = [
    ("which city is this?", "singapore"),
    ("why?", "it has a statue of a merlion"),
]
question = "where is the name merlion coming from?"
template = "Question: {} Answer: {}."

prompt = " ".join([template.format(context[i][0], context[i][1]) for i in range(len(context))]) + " Question: " + question + " Answer:"

print(prompt)
print("------------------------------------------------------------")
print(model.generate(
    {
    "image": image,
    "prompt": prompt
    },
    use_nucleus_sampling=False,
))

