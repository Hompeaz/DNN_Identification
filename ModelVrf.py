import argparse
from runs.modelops import modelvrf

def main():
    parser = argparse.ArgumentParser(description='PyTorch MNIST Example')
    parser.add_argument('--experiment', type=str, default='mnist', metavar='N',
                        help='experiment type, eg.(mnist)')
    
    parser.add_argument('--key-path', type=str, default='keys',
                        help='The key loaded path.')
    parser.add_argument('--model-path', type=str, default='',
                        help='The model loaded path.')
    parser.add_argument('--sig-path', type=str, default='signature.hex',
                        help='The signature loaded path.')
    parser.add_argument('--cov-path', type=str, default='cov_mat.pt',
                        help='The covariance loaded path.')
    
    
    parser.add_argument('--test-batch-size', type=int, default=1000, metavar='N',
                        help='input batch size for testing (default: 1000)')
    parser.add_argument('--no-cuda', action='store_true', default=False,
                        help='disables CUDA training')
    parser.add_argument('--no-mps', action='store_true', default=False,
                        help='disables macOS GPU training')
    args = parser.parse_args()
    
    modelvrf(args)
    
    
if __name__=='__main__':
    main()