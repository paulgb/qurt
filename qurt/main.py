
import logging
import argparse

from qurt import Qurt


class NotInRepoError(Exception):
    def __str__(self):
        return 'Not a git repo'


def main():
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument('--init', '-i', action='store_true')
    parser.add_argument('--export', '-e')
    parser.add_argument('--run', '-r')
    args = parser.parse_args()

    controller = Qurt()
    
    try:
        if args.init:
            # placeholder; nothing to initialize yet
            pass
        elif args.export:
            controller.export(args.export)
        elif args.run:
            controller.run(args.run)
        else:
            parser.print_help()

    except NotInRepoError:
        controller.log.error('Error: must be run inside a git repository')


if __name__ == '__main__':
    main()

