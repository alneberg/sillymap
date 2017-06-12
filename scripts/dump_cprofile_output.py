import pstats
import argparse

def main(args):
    p = pstats.Stats(args.cprofile_result)
    p.sort_stats('cumulative').print_stats()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('cprofile_result')
    args = parser.parse_args()

    main(args)
