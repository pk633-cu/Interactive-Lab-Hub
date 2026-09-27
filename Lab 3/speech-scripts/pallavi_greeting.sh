#!/usr/bin/env bash

python3 -m piper \
  --model en_US-hfc_female-medium.onnx \
  --output-raw \
  -- "Hi Pallavi! Welcome back!" \
  | aplay -r 22050 -f S16_LE -t raw -
