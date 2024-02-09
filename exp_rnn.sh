CUDA_VISIBLE_DEVICES=3 python ModelGen.py --experiment mnist_rnn \
    --epochs 14 \
    --watermark \
    --save-model \
    --key-path keys \
    --sig-path signature.hex \
    --cov-path cov_mat.pt
CUDA_VISIBLE_DEVICES=3 python be_ModelVrf.py --experiment mnist_rnn \
    --check-num 100 \
    --test-batch-size 50