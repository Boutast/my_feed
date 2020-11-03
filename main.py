import feedparser, sys, getopt
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

    def print_usage():
        print("0.0.2")
        return(0)

    def print_command():
        print("Commande")
        return (0)
    
    def add_feed():
        print("Add feed")
        return (0)

    def get_flag(arg):
        options = "hau"
        long_options = ["Help", "Add", "Usage", "usage", "add", "help"]
        try:
            arguments, values = getopt.getopt(arg, options, long_options)
            for currentArgument, currentValue in arguments:

                if currentArgument in ("-h", "-help", "-Help", "--h","--help", "--Help"):
                    Feed_rss.print_command()
                
                if currentArgument in ("-u", "-usage", "-Usage","--u", "--usage", "--Usage"):
                    Feed_rss.print_usage()

                if currentArgument in ("-a", "-add", "-Add", "--a", "--add", "--Add"):
                    Feed_rss.add_feed()

        except (getopt.error) as err:
            print (str(err))
            return (9)
        return (0)


if __name__ == "__main__":
    arg = sys.argv[1:]
    x = Feed_rss.get_flag(arg)
    if (x == 0):
        with open("./urls.txt") as file:
            while 1:
                data = file.readline()
                if (data == ""):
                    exit(0)
                else :
                    url = Feed_rss.set_rss(data)
                    compt = Feed_rss.get_all_entries(url)
                    entry = Feed_rss.get_rss(url, compt)