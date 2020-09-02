import argparse
import os
from config import Config
import modules.preprocess as preprocess
from modules.algorithm import Algorithm

def main():
    parser = argparse.ArgumentParser(description='Concept expansion with snippet')
    parser.add_argument('-task', type=str, choices=['extract', 'expand'], required=True)
    parser.add_argument('-input_text', '-it', type=str, help='the text file for concept extraction task')
    parser.add_argument('-input_seed', '-is', type=str, help='the seed file for concept extraction | expansion task')
    parser.add_argument('-language', '-l', type=str, choices=['zh', 'en'], required=True)
    parser.add_argument('-snippet_source', '-ss', default='baidu', type=str, choices=['baidu', 'google', 'bing'])
    parser.add_argument('-no_seed', '-ns', action='store_true', default=False, help='every candidate in text will be a seed')
    parser.add_argument('-algorithm', '-a', type=str, default='graph_propagation', choices=['graph_propagation', 'average_distance', 'tf_idf', 'pagerank'])
    parser.add_argument('-result_path', '-r', type=str, default='tmp/result.txt')
    parser.add_argument('-cpu', action='store_true', default=False)
    args = parser.parse_args()
    if not args.input_text and args.task == 'extract':
        raise Exception('concept extraction task need input_text')
    if not args.input_seed and args.task == 'expand':
        raise Exception('concept expansion task need input_seed')
    if not args.no_seed and not args.input_seed:
        raise Exception('seed config error')
    config = Config(args.task, args.input_text, args.input_seed, args.language, args.snippet_source, args.no_seed, args.algorithm, args.result_path, args.cpu)
    preprocess.get_candidates(config)
    algorithm = Algorithm(config)
    algorithm.get_result()

if __name__ == '__main__':
    main()