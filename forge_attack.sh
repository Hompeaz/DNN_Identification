
rm -rf saves/mnist_mlp/fake_signatures/*
python forge_fake_watermarks.py --experiment mnist_mlp
python ModelVrf.py --experiment mnist_mlp \
    --key-path attacker_saves/keys \
    --sig-path fake_signatures/`find saves/mnist_mlp/fake_signatures/* -type f -exec basename {} \; | sort | head -n 1`