This script should connect to the Upper Deck ePack API using your browser cookies and download a list of your current collection and save it as a CSV.  It's using the modules requests, browser-cookie3, tqdm, and tablib.

Search Filters:
Currently you need to specify the search filters you want to use manually in the script.  I've listed some common options below:
Base All Cards Filter = "o_u"
Autographed Cards = "auto"
Physical Cards = "phy"
Memorabilia = "mem"
Serial Numbered = "num"

To get the cards you are looking for you need to append the desired search onto the base filter with a comma, so autographed memorabilia cards would be "o_u,mem,auto", which you would then paste in the script on line 7, so it would look like search_filters = "o_u,mem,auto"
