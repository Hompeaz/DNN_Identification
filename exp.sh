python ModelGen.py --experiment mnist_mlp \
    --epochs 14 \
    --watermark \
    --save-model \
    --key-path keys \
    --sig-path signature.hex \
    --cov-path cov_mat.pt
python ModelGen.py --experiment mnist \
    --epochs 14 \
    --watermark \
    --save-model \
    --key-path keys \
    --sig-path signature.hex \
    --cov-path cov_mat.pt
python ModelGen.py --experiment mnist_rnn \
    --epochs 14 \
    --watermark \
    --save-model \
    --key-path keys \
    --sig-path signature.hex \
    --cov-path cov_mat.pt
python be_ModelVrf.py --experiment mnist_mlp \
    --check-num 10 \
    --test-batch-size 50
python be_ModelVrf.py --experiment mnist \
    --check-num 10 \
    --test-batch-size 50
python be_ModelVrf.py --experiment mnist_rnn \
    --check-num 10 \
    --test-batch-size 50