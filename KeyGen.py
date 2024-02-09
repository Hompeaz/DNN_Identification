import argparse
from crypto.model_proof import keygen, store_keys

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Key Generation')
    parser.add_argument('--path', type=str, default='keys',
                        help='The key store path.')
    args = parser.parse_args()
    
    sk, Y = keygen()
    print("sk:")
    print(hex(sk))
    print("Y:")
    print(Y.to_hex())
    store_keys(sk,Y,args.path)