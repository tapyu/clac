# CLAC
CLAC (Cards Language with Audio/examples from Collins dictionary) is a [RPA](https://repoman.pl/en/why-robots-cost-so-much/#:~:text=What%20is%20RPA%3F) written in [Python](https://www.python.org/) to automatically create language cards on [Anki](https://apps.ankiweb.net/) with audio/examples from [Collins](https://www.collinsdictionary.com/).

CLAC works on the following way:
1. Gather all text/audio information on Collins about the word that you are looking up. The information are:
    1. Meaning (Just the text).
    1. Different conjugations.
    1. Examples.
    1. Tag (verb, noun, phrasal verb, etc...) (Just text)
1. Create a new card on Anki in with the following structure:
    1. Front:
        1. Audio and text of the word for different conjugations.
        1. Audio and text of an examples
    1. back
        1. Text of the meaning

---
### Installing

- `git clone https://github.com/tapyu/clac`

In the `clac/` folder, run

- `py -m pip install .`

To install the required packages.

Alternatively, you can create a virtual environment to separate the CLAC's package requirements from the rest of your system site packages. In this case, you should install the packages from the `pyproject.toml` file. It is recommended to use [Poetry](https://python-poetry.org/) to make the package dependency management.


---
### Usage

The following sintax follows [Git's Coding Guidelines](https://github.com/git/git/blob/master/Documentation/CodingGuidelines#:~:text=Writing%20Documentation)

<!-- `clac <word-or-list> [--yes-rpa|-y] [--auto-remove|-r]` -->
`clac <word-or-list> [--yes-rpa|-y]`

`clac [--help|-h]`


- `<word-or-list>`: A single word or a path to a line-separated `.txt` file in which each line is a single word. CLAC will first assume that the argument is a path. If it fails, the argument will be treated as a single word.
- `--yes-rpa|-y`: Optional argument to run the RPA as soon as it saves the word.
<!-- - `--auto-remove|-r`: Optional argument to remove the folders used to save the data. -->
- `--help|-h`: Show a help message.

If you have any question, check this [video tutorial](https://www.youtube.com/watch?v=9XNqNNM2AhI).

---
### FAQ
1. **Why CLAC isn't a Anki addon**? Because I do not have enough knowledge with [QT for py](https://doc.qt.io/qtforpython/) to turn CLAC an addons. The current approach to learn about Anki addon is [some poor references](https://www.reddit.com/r/Anki/comments/bae3yx/building_addons_without_reading_all_the_source/) or learning with the source code from other addons 😑. **I do not have time to do it**.

1. **How can I turn CLAC an addons**? If you are familiar with Anki addon development, you could exploit the web scraping performed on CLAC to collect the necessary information and create an Anki card using the Anki GUI itself. Just let me know making a pull request and let's work together 😄.

<!--
Useful links:
1. For request CLAC to a new Addon: https://forums.ankiweb.net/
1. About Python Web Scraping: https://www.edureka.co/blog/web-scraping-with-python/

-->
