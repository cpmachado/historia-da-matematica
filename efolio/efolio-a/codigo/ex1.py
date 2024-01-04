"""
Program that computes pentagonal numbers until N.
Outputs in csv.
Columns:
    - k: iteration number, 1, ..., N
    - sk: extensive sum(e.g. s2 = "1 + 4")
    - pk: kth pentagonal number
"""
import argparse
import csv
import sys
from typing import Tuple, List


def pentagonal_dk(k: int) -> int:
    return 3 * k - 2


def pentagonal_extensive_sum(k: int) -> str:
    return " + ".join(map(str, (pentagonal_dk(i) for i in range(1, k + 1))))


def pentagonal(k: int) -> int:
    return int(k * (3 * k - 1) / 2)


def pentagonal_list(N: int) -> List[Tuple[int, int, int]]:
    return [(k, pentagonal_extensive_sum(k), pentagonal(k)) for k in range(1, N + 1)]


def main():
    parser = argparse.ArgumentParser(
        description="""
                Compute pentagonal numbers.
                Outputs in csv: index,extensive_sum,value
                example of extensive_sum: index=2 => 1 + 4
                """
    )
    parser.add_argument("N", help="Limit, it will compute 1,..., N", type=int)
    args = parser.parse_args()
    writer = csv.writer(sys.stdout)
    writer.writerow(("k", "sk", "pk"))
    writer.writerows(pentagonal_list(args.N))


if __name__ == "__main__":
    main()
