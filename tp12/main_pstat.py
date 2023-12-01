
import pstats

def main():
    stats = pstats.Stats('nth_prime.pstat')
    # print(stats.dump_stats())
    stats.print_stats()
    stats.sort_stats(pstats.SortKey.TIME).print_stats(3)

if __name__ == '__main__':
    main()
