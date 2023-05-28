"""
 Copyright (c) 2022, salesforce.com, inc.
 All rights reserved.
 SPDX-License-Identifier: BSD-3-Clause
 For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause
"""

import json
import os
import re

from pycocoevalcap.bleu.bleu import Bleu

from lavis.common.dist_utils import main_process
from lavis.common.registry import registry
from lavis.tasks.base_task import BaseTask


@registry.register_task("reasoning")
class ReasonTask(BaseTask):
    def __init__(self, num_beams, max_len, min_len, evaluate, report_metric=True):
        super().__init__()

        self.num_beams = num_beams
        self.max_len = max_len
        self.min_len = min_len
        self.evaluate = evaluate

        self.report_metric = report_metric

    @classmethod
    def setup_task(cls, cfg):
        run_cfg = cfg.run_cfg

        num_beams = run_cfg.num_beams
        max_len = run_cfg.max_len
        min_len = run_cfg.min_len
        evaluate = run_cfg.evaluate

        report_metric = run_cfg.get("report_metric", True)

        return cls(
            num_beams=num_beams,
            max_len=max_len,
            min_len=min_len,
            evaluate=evaluate,
            report_metric=report_metric,
        )

    def valid_step(self, model, samples):
        results = []

        # run_cfg = slf.cfg.run_cfg
        captions = model.generate(
            samples,
            use_nucleus_sampling=False,
            num_beams=self.num_beams,
            max_length=self.max_len,
            min_length=self.min_len,
        )

        img_ids = samples["image_id"]
        for caption, img_id in zip(captions, img_ids):
            results.append({"caption": caption, "image_id": int(img_id)})

        return results

    def after_evaluation(self, val_result, split_name, epoch, **kwargs):
        eval_result_file = self.save_result(
            result=val_result,
            result_dir=registry.get_path("result_dir"),
            filename="{}_epoch{}".format(split_name, epoch),
            remove_duplicate="image_id",
        )

        if self.report_metric:
            metrics = self._report_metrics(
                eval_result_file=eval_result_file, split_name=split_name
            )
        else:
            metrics = {"agg_metrics": 0.0}

        return metrics

    @main_process
    def _report_metrics(self, eval_result_file, split_name):

        sherlock_root = '/net/nfs.cirrascale/mosaic/seungjuh/sherlock_dataset'
        sherlock_eval_file = os.path.join(sherlock_root, 'sherlock_val_with_split_idxs_v1_1.json')

        with open(sherlock_eval_file, 'r') as f:
            sherlock_eval = json.load(f)

        with open(eval_result_file, 'r') as f:
            eval_result = json.load(f)

        eval_image_id_to_inference = {}
        eval_image_id_to_clue = {}

        for i, d in enumerate(sherlock_eval):
            inference = d['targets']['inference']
            clue = d['inputs']['clue']
            eval_image_id_to_clue[i] = clue
            eval_image_id_to_inference[i] = inference

        bleu1_scorer = Bleu(1)
        bleu2_scorer = Bleu(2)
        bleu3_scorer = Bleu(3)

        pred_inference = {}
        pred_clue = {}
        gt_inference = {}
        gt_clue = {}

        for i, result in enumerate(eval_result):
            img_id = result['image_id']
            caption = result['caption']
            # ex: caption = 'Clue: xxx, Inference: xxx'
            inference = re.findall(r'Inference: (.*)', caption)
            if len(inference) == 0:
                inference = ''
            else:
                inference = inference[0]
            clue = re.findall(r'Clue: (.*)', caption)
            if len(clue) == 0:
                clue = ''
            else:
                clue = clue[0]

            pred_inference[i] = [inference]
            pred_clue[i] = [clue]

            eval_clue = eval_image_id_to_clue[int(img_id)]
            eval_inference = eval_image_id_to_inference[int(img_id)]
            gt_inference[i] = [eval_inference]
            gt_clue[i] = [eval_clue]

        bleu1_score = bleu1_scorer.compute_score(gt_inference, pred_inference)[0]
        bleu2_score = bleu2_scorer.compute_score(gt_inference, pred_inference)[0]
        bleu3_score = bleu3_scorer.compute_score(gt_inference, pred_inference)[0]
        return {'agg_metrics': {
            'bleu1': bleu1_score,
            'bleu2': bleu2_score,
            'bleu3': bleu3_score,
        }}
