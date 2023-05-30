import re

from lavis.common.registry import registry
from lavis.processors.base_processor import BaseProcessor
from lavis.processors.randaugment import RandomAugment
from omegaconf import OmegaConf
from torchvision import transforms
from torchvision.transforms.functional import InterpolationMode

from lavis.processors.blip_processors import *

caption = "this light is lit at night"

caption = re.sub(
            r"([.!\"()*#:;~])",
            " ",
            caption.lower(),
        )

print(caption)

caption = re.sub(
    r"\s{2,}",
    " ",
    caption,
)


print(caption)
caption = caption.rstrip("\n")

print(caption)
caption = caption.strip(" ")

print(caption)



text_processor = BlipClueinferenceProcessor

print(text_processor(caption))

#print(text_processor.__class__.__name__)