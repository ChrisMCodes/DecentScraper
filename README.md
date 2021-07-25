# DecentScraper
A webscraper starter for anyone who wants to use it.

This scraper takes a URL and class to scrape (ids, elements, and more will come later -- feel free to add them!),
then returns the count of results, a printout of the results, and an options menu that allows you to exit or export the results to a .txt or .csv file.

Right now, the .txt and .csv save to the current working directory. I may add some filesystem options to work around that in future iterations.

## Random Options

This also tells a joke that Ronald Reagan claims was popular in the USSR and has a recursive Fibonacci sequence for your entertainment.
These are features to keep you entertained while you're working on scraping.

## Usage

Use this however you want, wherever you want. My hope is that it will get into the hands of new developers who can tailor it to their very-early-career freelancing needs.

## Credit/Citations

Feel free to credit me if you use this or share it, but I'm wayyyy too lazy to pursue you if you don't (also I don't care), so no pressure.

## Other Soviet Jokes?

Yes, I know plenty. I won't work them into this just yet, but maybe I'll randomize a few in the future?

## Known issues?

This starter has very limited scope and does little to check the validity of URLs. More may come soon -- it was just a fun, quick project tonight -- but it should be useful as starter code even if you have more to add.

### Why don't the file writing classes inherit from a parent class?!

They used to. Then I trimmed the parent class down so much that it was pretty impractical to keep it. 

### HOW DO I GET THE NECESSARY IMPORTS?

Open your Command prompt, PowerShell, or Terminal (CLI environment, for you geeks):

try typing this:

pip install bs4
(many/most of you would benefit from using _pip**3** install bs4_ instead, but I didn't want to make assumptions)

I think that's the only external module I used. Too lazy to double-check. Feel free to let me know if I'm mistaken.
