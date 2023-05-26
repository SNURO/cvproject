## Installation

1. (Optional) Creating conda environment

```bash
conda create -n lavis python=3.8
conda activate lavis
```

    
2. Or, for development, you may build from source

```bash
git clone https://github.com/salesforce/LAVIS.git
cd LAVIS
pip install -e .
```

3. Official tutorial documents는 docs 폴더를 참고하세요

## Dataset download

1. Sherlock dataset은 json (train, eval) 및 VCR, VisualGenome dataset 이미지들로 구성되어 있습니다.

2. ``lavis/datasets/download_scripts/download_vg.sh`` 에서 주석에 따라 경로를 변경한 뒤 실행하면 지정한 root data folder 안에 필요한 파일들이 다운로드 됩니다.

3. 최종적으로 root directory 하위에는 다음과 같은 구조가 만들어지면 됩니다.
```
├── sherlock_dataset
│   ├── sherlock_train_v1_1.json
│   ├── sherlock_val_with_split_idxs_v1_1.json
├── vcr1images
│   ├── lsmdc_0001_American_Beauty
│   ├── ...
└── vg
    └── images
        ├── VG_100K
	        ├── ...
        ├── VG_100K_2
	        ├── ...
```

## Model Zoo
```python
from lavis.models import model_zoo
print(model_zoo)
# ==================================================
# Architectures                  Types
# ==================================================
# ...
# blip2_opt                      pretrain_opt2.7b, pretrain_opt6.7b, caption_coco_opt2.7b, caption_coco_opt6.7b
# blip2_t5                       pretrain_flant5xl, pretrain_flant5xl_vitL, pretrain_flant5xxl, caption_coco_flant5xl
# blip2_feature_extractor        pretrain, pretrain_vitL, coco
# blip2                          pretrain, pretrain_vitL, coco
# blip2_image_text_matching      pretrain, pretrain_vitL, coco
# blip2_t5_instruct              flant5xl, flant5xxl
# blip2_vicuna_instruct          vicuna7b, vicuna13b
# ...
```

## Training outline 

1. ``run_scripts/blip2/train/train_caption_sherlock.sh``를 실행합니다. ``--nproc_per_node``를 실행 환경에 맞게 조절하여 사용할 distributed run에 사용할 gpu를 조절합니다.
```bash
python -m torch.distributed.run --nproc_per_node=1 train.py --cfg-path lavis/projects/blip2/train/caption_sherlock_ft.yaml
```

2. Training configuration은 ``lavis/projects/blip2/train/caption_sherlock_ft.yaml``에 위치합니다.
```yaml
model:
  arch: blip2_opt   # LLM decoder only architecture
  model_type: caption_coco_opt2.7b  #가장 작은 decoder model 입니다
  load_finetuned: False
  use_grad_checkpoint: True
  freeze_vit: True  #24gb vram에서는 True로 해야 동작합니다. 실험 환경에 맞게 조절하세요. default code는 False로 setting 되어 있었습니다. 

...

run:
  task: captioning
  # optimizer
  lr_sched: "linear_warmup_cosine_lr"
  init_lr: 1e-5     #hyperparameter tuning 
  min_lr: 0
  warmup_lr: 1e-8
  warmup_steps: 1000
  weight_decay: 0.05
  max_epoch: 5
  batch_size_train: 8
  batch_size_eval: 8
  num_workers: 4
  accum_grad_iters: 1

  ...

  device: "cuda"
  world_size: 1
  dist_url: "env://"
  distributed: False    #다수의 gpu 사용 시 실험 환경에 맞게 조절
```

3. 코드를 실행하기 전에 각 실험 환경에 맞게 directory들을 수정해야 합니다. 프로젝트 내부의 모든 코드에서 root directory에 해당하는 ``'/gallery_tate/wonjae.roh'`` 부분을 ``Dataset Download #2``에서 설정한 dataset root directory로 수정해주세요.

4. Sherlock Dataset에 해당하는 Custom Dataset class는 ``lavis/datasets/datasets/sherlock_dataset.py``에 정의되어 있습니다. 실험 setting이 변경되거나 수정되어야 한다면 ``__getitem__`` method를 수정해야 합니다. Dataset class는 내부에 ``self.annotation``에서 ``.json``파일에 대한 정보를 가지고 있습니다. Sherlock dataset의 ``.json``파일의 구조는 다음과 같습니다. 
```json
{"inputs": 
    {"image": 
        {"url":"http://s3-us-west-2.amazonaws.com/ai2-rowanz/vcr1images/movieclips_Neruda/iQrYqaPeMlc@17.jpg", "width": 1920, "height": 816}, 
    "bboxes": [{"height": 486, "width": 1907, "left": 13, "top": 330}, 
            {"height": 326, "width": 1908, "left": 12, "top": 4}], 
    "clue": "snow on the ground and in the trees", 
    "confidence": 3.0, 
    "obs_idx": 0}, 
"targets": 
    {"inference": "It recently snowed."}, 
"instance_id": "2f34bb38723c3ad5d5142091be91a846"}

```

## TODO
* evaluation (metric: bleu scores, etc..)