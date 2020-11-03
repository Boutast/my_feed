import feedparser
from termcolor import colored

class Feed_rss:
    def set_rss(url):
        feed = feedparser.parse(url)
        return (feed)

    def get_all_entries(feed):
        all_entries = len(feed.entries)
        return(all_entries)

    def get_rss(feed, compt):
        print ('Number of RSS posts :', compt, '\n')
        x = 0
        while (x < compt):
            entry = feed.entries[x]
            print (colored('Title :', 'green'), entry.title, '\n\n',
            colored(entry.link, 'blue'), '\n')
            x += 1
        return (0)

if __name__ == "__main__":
    with open("~/Perso/Confinement/Day01/urls.txt") as file:
        while 1:
            data = file.readline()
            if (data == ""):
                exit(0)
            else :
                url = Feed_rss.set_rss(data)
                compt = Feed_rss.get_all_entries(url)
                entry = Feed_rss.get_rss(url, compt)
import feedparser
from termcolor import colored

class Feed_rss:
    def set_rss(url):
        feed = feedparser.parse(url)
        return (feed)

    def get_all_entries(feed):
        all_entries = len(feed.entries)
        return(all_entries)

    def get_rss(feed, compt):
        print ('Number of RSS posts :', compt, '\n')
        x = 0
        while (x < compt):
            entry = feed.entries[x]
            print (colored('Title :', 'green'), entry.title, '\n\n',
            colored(entry.link, 'blue'), '\n')
            x += 1
        return (0)

if __name__ == "__main__":
    with open("~/Perso/Confinement/Day01/urls.txt") as file:
        while 1:
            data = file.readline()
            if (data == ""):
                exit(0)
            else :
                url = Feed_rss.set_rss(data)
                compt = Feed_rss.get_all_entries(url)
                entry = Feed_rss.get_rss(url, compt)
