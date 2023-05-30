# Experimental Results

## Fine-tuning OPT-2.7b BLIP-2 on Sherlock dataset

- Inference only
```bash
{"train_lr": "0.000", "train_loss": "1.082"}
{"val_bleu1": 0.1973673027601816, "val_bleu2": 0.10738339017020203, "val_bleu3": 0.06337779735679472, "val_agg_metrics": 0.1973673027601816, "val_best_epoch": 0}
{"train_lr": "0.000", "train_loss": "1.045"}
{"val_bleu1": 0.2054177779346287, "val_bleu2": 0.11552292648313325, "val_bleu3": 0.07090251688297855, "val_agg_metrics": 0.2054177779346287, "val_best_epoch": 1}
{"train_lr": "0.000", "train_loss": "0.981"}
{"val_bleu1": 0.19264960649408408, "val_bleu2": 0.10573017097463727, "val_bleu3": 0.06371767897264714, "val_agg_metrics": 0.19264960649408408, "val_best_epoch": 1}
{"train_lr": "0.000", "train_loss": "0.936"}
{"val_bleu1": 0.2086663304859838, "val_bleu2": 0.11842804025882887, "val_bleu3": 0.07344701887274359, "val_agg_metrics": 0.2086663304859838, "val_best_epoch": 3}
{"train_lr": "0.000", "train_loss": "0.885"}
{"val_bleu1": 0.2081978278210703, "val_bleu2": 0.11842636985026793, "val_bleu3": 0.07383837234889445, "val_agg_metrics": 0.2081978278210703, "val_best_epoch": 3}
```
- Ground-truth clue + Inference

- Clue + Inference
