from utils.main_utils import run_clac_cli
import argparse

def parse_args():
    """ parse CLI arguments
    Parameters
    ---------- 
    args : :class: `list`
        A list of arguments; generally, this should be ``sys.argv``.

    Resturns
    ---------- 
    :class: `argpase.Namespace`
        An object returned by ``argparse.parse_args``.
     """
    parser = argparse.ArgumentParser(description='RPA to create language cards on Anki', prog='clac', usage='%(prog)s word_or_list [-y]', epilog='Do you want to help? Collabore on my project! :)')

    parser.add_argument('word_or_list', help='A word to sacrape or a line-separated .txt filename')
    parser.add_argument('-y', '--yes-rpa', help='A flag that indicates it should run the RPA as soon as it saves the when the word.', action='store_true') # optional argument
    parser.add_argument('-r', '--auto-remove', help='A flag that indicates ir should remove the folders used to save the .mp3 data', action='store_true') # TODO

    return parser.parse_args()

def main():
    args = parse_args()
    try:
        with open(args.word_or_list, 'r') as file:
            for line in file:
                run_clac_cli(line.rstrip(), args.yes_rpa) # the CLI argument is a line-separeted .txt file
    except FileNotFoundError:
        run_clac_cli(args.word_or_list, args.yes_rpa) # the CLI argument is a single word

if __name__ == '__main__':
    main()