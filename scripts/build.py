from twrpdtgen.device_tree import DeviceTree
import argparse
import os
from pathlib import Path
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Auto-Twrp-Builder")
    parser.add_argument('-i', '--input', type=str, default='', help='Recovery/Boot Image')
    parser.add_argument('-o', '--output', type=str, default='', help='Output path')
    args = parser.parse_args()
    if not args.input or not args.output:
        parser.print_help()
        exit()
    if not os.path.exists(args.output):
        os.makedirs(args.output, exist_ok=True)
    device_tree = DeviceTree(Path(args.input))
    if os.getenv('GITHUB_OUTPUT', ''):
        with open(os.getenv('GITHUB_OUTPUT', ''), 'w') as f:
            f.write(f'DEVICE_NAME={device_tree.device_info.manufacturer}\n')
            f.write(f'MAKEFILE_NAME=omni_{device_tree.device_info.codename}\n')
            f.write(f'DEVICE_PATH={os.path.basename(args.output) / device_tree.device_info.manufacturer / device_tree.device_info.codename}')
    device_tree.dump_to_folder(Path(args.output))
