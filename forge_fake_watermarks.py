import argparse
import torch
import csv
import io
from collections import OrderedDict
from crypto.model_proof import *
from crypto.encode import *

def main():
    parser = argparse.ArgumentParser(description='Forge Attack')
    parser.add_argument('--experiment', type=str, default='mnist',
                        help='The target experiment.')
    parser.add_argument('--keys', type=str, default='attacker_saves/keys/', metavar='N',
                        help='Attacker\'s key pair.')
    parser.add_argument('--target', type=str, default='signature.hex', metavar='N',
                        help='Target signature to forge')
    parser.add_argument('--target-model', type=str, default='watermarked.pt', metavar='N',
                        help='Target model to sign')
    parser.add_argument('--target-cov', type=str, default='cov_mat.pt', metavar='N',
                        help='Target model to sign')
    parser.add_argument('--num', type=int, default=100000,
                        help='Attempt times')
    parser.add_argument('--store-path', type=str, default='fake_signatures/',
                        help='Signature saving path.')
    args = parser.parse_args()
    
    pth = args.experiment + '/'
    
    sk = load_secret_key(args.keys)
    pk = load_public_key(args.keys)
    
    list = OrderedDict()
    sig_0, _ = load_sig(pth + args.target)
    mark_0 = markgen(sig_0)
    
    for i in range(args.num):
        print(f'# Epoch {i+1} #')
        r_bar, sig = sign_1()
        mark = markgen(sig)
        be = be_mark(mark_0, mark)
        print(f'bit error {be} \n')
        if be in list:
            list[be] += 1
        else:
            list[be] = 1
            model_params = torch.load('saves/'+pth+args.target_model)
            model_buffer = io.BytesIO()
            torch.save(model_params, model_buffer)
            
            cov = torch.load('saves/'+pth+args.target_cov)
            buffer = io.BytesIO()
            torch.save(cov, buffer)
            cov_mat = buffer.getvalue()
            
            r = sign_2(model_buffer, cov_mat, pk, sk, r_bar)
            store_sig(pth+args.store_path+'be-'+str(be)+'.sig', sig, r)
            #store_trapdoor(r_bar, args.store_path+'be-'+str(be)+'.trp')
    
    print(list)
    rows = []
    for i in range(512):
        if i in list:
            rows.append(list[i])
        else:
            rows.append(0)
    
    with open('hash.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows([rows])
            
if __name__ == '__main__':
    main()