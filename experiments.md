# Experimental Results

## Fine-tuning OPT-2.7b BLIP-2 on Sherlock dataset

- Inference only
```bash
{"train_lr": "0.000", "train_loss": "1.082"}
{"val_inference_bleu1": 0.1973673027601816, "val_inference_bleu2": 0.10738339017020203, "val_inference_bleu3": 0.06337779735679472, "val_agg_metrics": 0.1973673027601816, "val_best_epoch": 0}
{"train_lr": "0.000", "train_loss": "1.045"}
{"val_inference_bleu1": 0.2054177779346287, "val_inference_bleu2": 0.11552292648313325, "val_inference_bleu3": 0.07090251688297855, "val_agg_metrics": 0.2054177779346287, "val_best_epoch": 1}
{"train_lr": "0.000", "train_loss": "0.981"}
{"val_inference_bleu1": 0.19264960649408408, "val_inference_bleu2": 0.10573017097463727, "val_inference_bleu3": 0.06371767897264714, "val_agg_metrics": 0.19264960649408408, "val_best_epoch": 1}
{"train_lr": "0.000", "train_loss": "0.936"}
{"val_inference_bleu1": 0.2086663304859838, "val_inference_bleu2": 0.11842804025882887, "val_inference_bleu3": 0.07344701887274359, "val_agg_metrics": 0.2086663304859838, "val_best_epoch": 3}
{"train_lr": "0.000", "train_loss": "0.885"}
{"val_inference_bleu1": 0.2081978278210703, "val_inference_bleu2": 0.11842636985026793, "val_inference_bleu3": 0.07383837234889445, "val_agg_metrics": 0.2081978278210703, "val_best_epoch": 3}
```
- Ground-truth clue + Inference

- Clue + Inference
```bash
{"train_lr": "0.000", "train_loss": "0.887"}
{"val_clue_bleu1": 0.30543605678830893, "val_clue_bleu2": 0.19290512864077242, "val_clue_bleu3": 0.13027816848801715, "val_inference_bleu1": 0.21969925665793294, "val_inference_bleu2": 0.13169165678474468, "val_inference_bleu3": 0.08290917445522264, "val_agg_metrics": 0.21969925665793294, "val_best_epoch": 0}
