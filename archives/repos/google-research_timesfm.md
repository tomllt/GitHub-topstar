# TimesFM

TimesFM (Time Series Foundation Model) is a pretrained time-series foundation
model developed by Google Research for time-series forecasting.

*   Paper:
    [A decoder-only foundation model for time-series forecasting](https://arxiv.org/abs/2310.10688),
    ICML 2024.
*   All checkpoints:
    [TimesFM Hugging Face Collection](https://huggingface.co/collections/google/timesfm-release-66e4be5fdb56e960c1e482a6).
*   [Google Research blog](https://research.google/blog/a-decoder-only-foundation-model-for-time-series-forecasting/).
*   [TimesFM in BigQuery](https://cloud.google.com/bigquery/docs/timesfm-model):
    an official Google product.

This open version is not an officially supported Google product.

**Latest Model Version:** TimesFM 2.5

**Archived Model Versions:**

-   1.0 and 2.0: relevant code archived in the sub directory `v1`. You can `pip
    install timesfm==1.3.0` to install an older version of this package to load
    them.

## Update - Mar. 19, 2026

Huge shoutout to [@borealBytes](https://github.com/borealBytes) for adding the support for [AGENTS](https://github.com/google-research/timesfm/blob/master/AGENTS.md)! TimesFM [SKILL.md](https://github.com/google-research/timesfm/tree/master/timesfm-forecasting) is out.

## Update - Oct. 29, 2025

Added back the covariate support through XReg for TimesFM 2.5.


## Update - Sept. 15, 2025

TimesFM 2.5 is out!

Comparing to TimesFM 2.0, this new 2.5 model:

-   uses 200M parameters, down from 500M.
-   supports up to 16k context length, up from 2048.
-   supports continuous quantile forecast up to 1k horizon via an optional 30M
    quantile head.
-   gets rid of the `frequency` indicator.
-   has a couple of new forecasting flags.

Along with the model upgrade we have also upgraded the inference API. This repo
will be under construction over the next few weeks to

1.  add support for an upcoming Flax version of the model (faster inference).
2.  add back covariate support.
3.  populate more docstri

... (truncated)