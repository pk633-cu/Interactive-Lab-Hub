#!/usr/bin/env bash

python3 -m piper \
  --model en_US-hfc_female-medium.onnx \
  --output-raw \
  -- "What is your zip code?" \
  | aplay -r 22050 -f S16_LE -t raw -

arecord -d 5 -f cd -c 1 -r 16000 zipcode_answer.wav
