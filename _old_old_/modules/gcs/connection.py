import os, argparse, time

parser = argparse.ArgumentParser()
parser.add_argument("--connect", help="Connection String", required=True)
args = parser.parse_args()

os.system(f"xterm -T xterm -fa 'Monospace' -fs 14 -e \"mavproxy.py --master={args.connect} --console --map --load-module horizon\"")
