CUDA_VISIBLE_DEVICES=1 python ModelGen.py --experiment mnist_mlp \
    --epochs 14 \
    --watermark \
    --save-model \
    --key-path keys \
    --sig-path signature.hex \
    --cov-path cov_mat.pt
CUDA_VISIBLE_DEVICES=1 python be_ModelVrf.py --experiment mnist_mlp \
    --check-num 100 \
    --test-batch-size 50