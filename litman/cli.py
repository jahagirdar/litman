"""Console script for litman."""
import argparse
import sys
from .mm import update_mindmap


def main():
    """Console script for litman."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "litman.cli.main")

    print(sys.argv[0])
    update_mindmap(sys.argv[1])

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
