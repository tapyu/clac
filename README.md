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
### Main packages used in this RPA

<!-- 1. **Selenium**:  Selenium is a web testing library. It is used to automate browser activities. -->
1. [**BeautifulSoup**](https://www.crummy.com/software/BeautifulSop/bs4/doc/): It is a  package for parsing HTML and XML documents. It creates parse trees that is helpful to extract the data easily.
1. [**PyAutoGUI**](https://pyautogui.readthedocs.io/en/latest/): It is a cross-platform  package that controls the mouse and keyboard to automate interactions with other applications. 

---
### FAQ
1. **Why CLAC isn't a Anki addon**? Because I do not have enough knowledge with [QT for py](https://doc.qt.io/qtforpython/) to turn CLAC an addons. The current approach to learn about Anki addon is [some poor references](https://www.reddit.com/r/Anki/comments/bae3yx/building_addons_without_reading_all_the_source/) or learning with the source code from other addons 😑. **I do not have time to do it**.

1. **How can I turn CLAC an addons**? If you are familiar with Anki addon development, you could exploit the web scraping performed on CLAC to collect the necessary information and create an Anki card using the Anki GUI itself. Just let me know making a pull request and let's work together 😄.

<!--
Useful links:
1. For request CLAC to a new Addon: https://forums.ankiweb.net/
1. About Python Web Scraping: https://www.edureka.co/blog/web-scraping-with-python/

-->
