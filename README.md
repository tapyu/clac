# CLAC
CLAC (Cards Language with Audio/examples from Collins dictionary) is a [RPA](https://repoman.pl/en/why-robots-cost-so-much/) written in Python for create a language card on Anki with audio/examples from [Collins](https://www.collinsdictionary.com/).

CLAC works on the following way:
1. Gather all text/audio information on Collins about the word that you are looking up. The information are:
    1. Meaning (Just the text).
    1. Different conjugations.
    1. Examples.
    1. Tag (verb, noun or phrasal verb...) (Just text)
1. Create a new card on Anki in with the following structure:
    1. Front:
        1. Audio and text of the word for different conjugations.
        1. Audio and text of an example
    1. back
        1. Text of the meaning
        1. Audio and text of 2 more examples


---
### Main packages used in this RPA

1. **Selenium**:  Selenium is a web testing library. It is used to automate browser activities.
1. **BeautifulSoup**: Beautiful Soup is a Python package for parsing HTML and XML documents. It creates parse trees that is helpful to extract the data easily.
1. **Pandas**: Pandas is a library used for data manipulation and analysis. It is used to extract the data and store it in the desired format.


---
### FAQ
1. **Why CLAC isn't a Anki addon**? Because I do not have knowledge enough with [QT for py](https://doc.qt.io/qtforpython/) to turn CLAC an addons. The current approach to learn about Anki addon is [some poor references](https://www.reddit.com/r/Anki/comments/bae3yx/building_addons_without_reading_all_the_source/) and learning with the source code from other addons (😑). **I do not have time to do it**.

1. **How can I turn CLAC an addons**? If you are familiar of anki addon development, you could use the first behavior of CLAC: Gather all text/audio information on Collins about the word that you are looking up. Then, you just add all this information in a new card on Anki.

<!--
Useful links:
1. For request CLAC to a new Addon: https://forums.ankiweb.net/
1. About Python Web Scraping: https://www.edureka.co/blog/web-scraping-with-python/

-->