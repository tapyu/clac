from clac.utils.main_utils import run_clac_cli
import argparse, warnings, os, time

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
    parser = argparse.ArgumentParser(description='RPA to create language cards on Anki', prog='clac', usage='%(prog)s <word-or-list> [-y|--yes-rpa] [-r|--auto-remove]', epilog='Do you want to help? Collabore on my project! :)')

    parser.add_argument('word_or_list', help='A single word or a path to a line-separated .txt file in which each line is a single word. CLAC will first assume that the argument is a path. If it fails, the argument will be treated as a single word.')
    parser.add_argument('-y', '--yes-rpa', help='Optional argument to run the RPA as soon as it saves the word.', action='store_true') # optional argument
    # parser.add_argument('-r', '--auto-remove', help='Optional argument to remove the folders used to save the data.', action='store_true') # TODO

    return parser.parse_args()

def main():
    args = parse_args()
    if os.path.isfile(args.word_or_list): # word_or_list is treated as a txt file
        with open(args.word_or_list, 'r') as file:
            for line in file:
                try:
                    run_clac_cli(line.rstrip(), args.yes_rpa) # the CLI argument is a line-separeted .txt file
                except (ValueError,LookupError) as e:
                    with open('./failed_words.txt', 'a') as txt_file:
                        txt_file.write(f'{line} [{e.args[0]}]\n')
                    if type(e) == ValueError:
                        warnings.warn(f'The word {args.word_or_list} was found, but it did not have any meaning statement on the web site. This word was saved on ./failed_words.txt. Please, try another word')
                    else: # type(e) == LookupError
                        warnings.warn(f'The word {args.word_or_list} was not found. It was saved on ./failed_words.txt. Please, try another word')
                    time.sleep(2)
                    os.system('cls')

    else: # word_or_list is treated as a word
        try:
            run_clac_cli(args.word_or_list, args.yes_rpa) # the CLI argument is a single word
        except (ValueError,LookupError) as e:
                    with open('./failed_words.txt', 'a') as txt_file:
                        txt_file.write(f'{args.word_or_list} [{e.args[0]}]\n')
                    if type(e) == ValueError:
                        warnings.warn(f'The word {args.word_or_list} was found, but it did not have any meaning statement on the web site. This word was saved on ./failed_words.txt. Please, try another word')
                    else: # type(e) == LookupError
                        warnings.warn(f'The word {args.word_or_list} was not found. It was saved on ./failed_words.txt. Please, try another word')
                    input("Press Enter to continue...")

if __name__ == '__main__':
    main()
