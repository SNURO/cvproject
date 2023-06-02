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
```bash
{"train_lr": "0.000", "train_loss": "0.945"}
{"val_clue_bleu1": 1.8175235682089387e-28, "val_clue_bleu2": 1.7517567424624873e-28, "val_clue_bleu3": 1.691642096628027e-28, "val_inference_bleu1": 0.1963154892079481, "val_inference_bleu2": 0.1080322061241011, "val_inference_bleu3": 0.06390138039092025, "val_agg_metrics": 0.1963154892079481, "val_best_epoch": 0}
{"train_lr": "0.000", "train_loss": "0.902"}
{"val_clue_bleu1": 3.218732254165068e-09, "val_clue_bleu2": 3.086556223767389e-09, "val_clue_bleu3": 2.9637488906021445e-09, "val_inference_bleu1": 0.18199119577191228, "val_inference_bleu2": 0.09970203523766452, "val_inference_bleu3": 0.058454102252679, "val_agg_metrics": 0.18199119577191228, "val_best_epoch": 0}
{"train_lr": "0.000", "train_loss": "0.869"}
{"val_clue_bleu1": 9.282474759903057e-11, "val_clue_bleu2": 8.872343326427603e-11, "val_clue_bleu3": 8.450901294378361e-11, "val_inference_bleu1": 0.18450844268471497, "val_inference_bleu2": 0.10194447314410296, "val_inference_bleu3": 0.06082592000609539, "val_agg_metrics": 0.18450844268471497, "val_best_epoch": 0}
{"train_lr": "0.000", "train_loss": "0.830"}
{"val_clue_bleu1": 2.051241649640662e-12, "val_clue_bleu2": 1.959955553048053e-12, "val_clue_bleu3": 1.8699479194338133e-12, "val_inference_bleu1": 0.1762687516673842, "val_inference_bleu2": 0.09840852075647018, "val_inference_bleu3": 0.05938827322819933, "val_agg_metrics": 0.1762687516673842, "val_best_epoch": 0}
{"train_lr": "0.000", "train_loss": "0.795"}
{"val_clue_bleu1": 3.0239829700849085e-13, "val_clue_bleu2": 2.89485403246524e-13, "val_clue_bleu3": 2.7676150317570337e-13, "val_inference_bleu1": 0.1795021815081653, "val_inference_bleu2": 0.10030196514266712, "val_inference_bleu3": 0.060416292552839146, "val_agg_metrics": 0.1795021815081653, "val_best_epoch": 0}
```

- Clue + Inference
```bash
{"train_lr": "0.000", "train_loss": "0.887"}
{"val_clue_bleu1": 0.30543605678830893, "val_clue_bleu2": 0.19290512864077242, "val_clue_bleu3": 0.13027816848801715, "val_inference_bleu1": 0.21969925665793294, "val_inference_bleu2": 0.13169165678474468, "val_inference_bleu3": 0.08290917445522264, "val_agg_metrics": 0.21969925665793294, "val_best_epoch": 0}
{"train_lr": "0.000", "train_loss": "0.852"}
{"val_clue_bleu1": 0.32678590918310363, "val_clue_bleu2": 0.2104841412705765, "val_clue_bleu3": 0.1433125272343687, "val_inference_bleu1": 0.22985973215395114, "val_inference_bleu2": 0.14121514719503445, "val_inference_bleu3": 0.09175994336877036, "val_agg_metrics": 0.22985973215395114, "val_best_epoch": 1}
{"train_lr": "0.000", "train_loss": "0.818"}
{"val_clue_bleu1": 0.3439080428976107, "val_clue_bleu2": 0.22577713127035673, "val_clue_bleu3": 0.15663953455065024, "val_inference_bleu1": 0.2270343837821426, "val_inference_bleu2": 0.14199028834287727, "val_inference_bleu3": 0.09309017077559595, "val_agg_metrics": 0.2270343837821426, "val_best_epoch": 1}
{"train_lr": "0.000", "train_loss": "0.787"}
{"val_clue_bleu1": 0.3487682589690668, "val_clue_bleu2": 0.23042114089931442, "val_clue_bleu3": 0.16028498541721217, "val_inference_bleu1": 0.2359607533254298, "val_inference_bleu2": 0.1471094390304837, "val_inference_bleu3": 0.09651452607373451, "val_agg_metrics": 0.2359607533254298, "val_best_epoch": 3}
{"train_lr": "0.000", "train_loss": "0.763"}
{"val_clue_bleu1": 0.3435918945738982, "val_clue_bleu2": 0.2270446337676239, "val_clue_bleu3": 0.15835586067821583, "val_inference_bleu1": 0.23897510793556867, "val_inference_bleu2": 0.15072598278830485, "val_inference_bleu3": 0.10063867862100798, "val_agg_metrics": 0.23897510793556867, "val_best_epoch": 4}
```
