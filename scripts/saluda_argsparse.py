#!/usr/bin/env python3
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", required=True)
args = parser.parse_args()
print(f'Hola {args.name} , benvingut! ')