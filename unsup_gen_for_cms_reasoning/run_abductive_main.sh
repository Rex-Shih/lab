#!/bin/bash

python3 dialogpt_main.py \
    --pretrained_model microsoft/DialoGPT-medium \
    --length 15 \
    --max_length 30 \
    --top_k 1 \
    --num_passes 20 \
    --num_backward_iters 20 \
    --stepsize 0.0003 \
    --mix_rate 0.88 \
    --temperature_first 1 \
    --temperature_backward 1 \
    --temperature_forward 1\
    --input_file ./data/abductive/augmentation.json  \
    --output_dir ./output/abductive/aug/dialogpt_medium \
