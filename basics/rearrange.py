import argparse
import random

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("words", help="Shuffle given strings", type=str, nargs='+')
    return parser.parse_args()

def rearrange_words(words):
    random.shuffle(words)
    for word in words:
        print(word, end=" ")

if __name__ == '__main__':
    args = parse_args()
    rearrange_words(args.words)