# Guide

## Shortcuts

* Ctrl+\\ - Take high contrast screenshot

## Whisper Models

### What is a model?

The whisper models are Speech-To-Text (STT) modules that convert audio to text. There are 6 models, each on a balance of speed/accuracy. Typically, the smaller models are faster but less accurate, while the larger models are slower but more accurate. The models are compared below:

|  Size  | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
|:------:|:----------:|:------------------:|:------------------:|:-------------:|:--------------:|
|  tiny  |    39 M    |     `tiny.en`      |       `tiny`       |     ~1 GB     |      ~10x      |
|  base  |    74 M    |     `base.en`      |       `base`       |     ~1 GB     |      ~7x       |
| small  |   244 M    |     `small.en`     |      `small`       |     ~2 GB     |      ~4x       |
| medium |   769 M    |    `medium.en`     |      `medium`      |     ~5 GB     |      ~2x       |
| large  |   1550 M   |        N/A         |      `large`       |    ~10 GB     |       1x       |
| turbo  |   809 M    |        N/A         |      `turbo`       |     ~6 GB     |      ~8x       |

^ Table taken from [Whisper repository](https://github.com/openai/whisper/blob/c0d2f624c09dc18e709e37c2ad90c039a4eb72a2/README.md) on 12 March, 2026, under MIT License (see Licenses for MIT License text). Relative speeds on a A100 GPU, but you can run these on CPUs.

In short, `tiny` should be good for most lower-end computers. `base` is better for the medium end, and anything beyond `small` should be reserved for higher end PCs. `turbo`, however, is an exception, as it is faster while more accurate. You still need a lot of memory for it, but speeds should suffice for a medium-high end PC.

### Changing Models

To change the model, select the `Options` tab then select `Change Transcription Model`. There, you can select your preferred model. Model decisions will save.

### Clearing cache

To free up space on your computer, it is a good idea to clear your model cache. You can do this under `Help` then `Clear Model Cache`, but please note, there will be no confirmation and you will have to redownload the models.

## Resetting Preferences

To reset any preferences set, just click `Reset Preferences...`, also under `Help`. You will be asked confirmation. Once confirmed, the app will close after 5 seconds.
