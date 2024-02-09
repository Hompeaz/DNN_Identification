from crypto.model_proof import *
from models.mnist.main import Net
import torch
import io

def test_signing():
    #KeyGen
    sk, Y = keygen()
    print("sk:")
    print(hex(sk))
    print("Y:")
    print(Y.to_hex())
    
    # Signing Phase 1
    r_bar, sig = sign_1()
    print("r_bar:")
    print(hex(r_bar))
    print("sig:")
    print(sig)
    print(sig.to_hex())
    
    model_params = torch.load('saves/mnist/regular.pt')
    model_buffer = io.BytesIO()
    torch.save(model_params, model_buffer)
    cov = torch.load('saves/mnist/cov_mat.pt')
    buffer = io.BytesIO()
    torch.save(cov, buffer)
    cov_bytes = buffer.getvalue()
    
    # Signing Phase 2
    r = sign_2(model_buffer, cov_bytes, Y, sk, r_bar)
    print("r:")
    print(hex(r))
    
    # Verification
    result = scheck(model_buffer, cov_bytes, Y, sig, r)
    print(result)


if __name__ == '__main__':
    test_signing()
