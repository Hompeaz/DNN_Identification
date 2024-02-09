from __future__ import print_function
import argparse
from runs.modelops import modelgen

def main():
    parser = argparse.ArgumentParser(description='PyTorch Indentification Watermark Embedding Experiment.')
    parser.add_argument('--experiment', type=str, default='mnist', metavar='N',
                        help='experiment type, eg.(mnist)')
    parser.add_argument('--watermark', action='store_true', default=False,
                        help='enable model watermarking')
    parser.add_argument('--save-model', action='store_true', default=False,
                        help='For Saving the current Model')
    
    parser.add_argument('--key-path', type=str, default='keys',
                        help='The key loaded path.')
    parser.add_argument('--model-path', type=str, default='',
                        help='The model store path.')
    parser.add_argument('--sig-path', type=str, default='signature.hex',
                        help='The signature store path.')
    parser.add_argument('--cov-path', type=str, default='cov_mat.pt',
                        help='The covariance store path.')
    
    
    parser.add_argument('--batch-size', type=int, default=64, metavar='N',
                        help='input batch size for training (default: 64)')
    parser.add_argument('--test-batch-size', type=int, default=1000, metavar='N',
                        help='input batch size for testing (default: 1000)')
    parser.add_argument('--epochs', type=int, default=14, metavar='N',
                        help='number of epochs to train (default: 14)')
    parser.add_argument('--lr', type=float, default=1.0, metavar='LR',
                        help='learning rate (default: 1.0)')
    parser.add_argument('--gamma', type=float, default=0.7, metavar='M',
                        help='Learning rate step gamma (default: 0.7)')
    parser.add_argument('--no-cuda', action='store_true', default=False,
                        help='disables CUDA training')
    parser.add_argument('--no-mps', action='store_true', default=False,
                        help='disables macOS GPU training')
    parser.add_argument('--dry-run', action='store_true', default=False,
                        help='quickly check a single pass')
    parser.add_argument('--seed', type=int, default=1, metavar='S',
                        help='random seed (default: 1)')
    parser.add_argument('--log-interval', type=int, default=10, metavar='N',
                        help='how many batches to wait before logging training status')
    args = parser.parse_args()
    
    modelgen(args)
    
    
if __name__=='__main__':
    main()