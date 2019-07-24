import feedparser
import urllib.request
import os
from feedgen.feed import FeedGenerator
fg = FeedGenerator()
fg.load_extension('podcast')

fg.title('The Edition')
fg.description('A collection of podcasts')
fg.link(href="http://example.com/podcast.xml")

os.chdir("mp3")

# We want a dictionary of podcasts we're interested in getting each day.
feeds = {"Up First": "https://www.npr.org/rss/podcast.php?id=510318",
        "Story of the Day": "https://www.npr.org/templates/rss/podlayer.php?id=1090",
        "The Daily": "https://rss.art19.com/the-daily",
        "The Journal": "https://video-api.wsj.com/podcast/rss/wsj/the-journal",
        "Tech News Briefing": "https://video-api.wsj.com/podcast/rss/wsj/tech-news-briefing"}

podcasts = []

# Let's get the links to download the MP3 files.
for feed in feeds.values():
    d = feedparser.parse(feed)
    links = d.entries[0]['links']
    for link in links:
        podcasts.append(link['href'])

# Now we'll download each MP3 and name the filename by a number
i = 0
for podcast in podcasts:
    urllib.request.urlretrieve(podcast, filename=str(i)+".mp3")
    i+=1

# Some cleanup from the previous day
if os.path.isfile("edition.mp3"):
    os.remove("edition.mp3")
if os.path.isfile("/var/www/html/edition.mp3"):
    os.remove("/var/www/html/edition.mp3")

# We need a list of the MP3's we just downloaded
files = os.listdir()

# Constructing our FFMPEG command
count = 1
ff_command = "ffmpeg -i 'concat:"
for filen in files:
    ff_command += filen
    if count < len(files):
        ff_command += "|"
    count+=1

ff_command += "' -acodec copy edition.mp3 -y"
os.system(ff_command)

# Delete the MP3's and move our finished one to the web
for filen in files:
    os.remove(filen)
os.rename("edition.mp3", "/var/www/html/edition.mp3")

# Construct our RSS feed
fe = fg.add_entry()
fe.id("http://thirdprong.com/edition.mp3")
fe.title('The Edition')
fe.description('A collection of podcasts')
fe.link(href="http://example.com/podcast.xml")
fe.enclosure("http://example.com/edition.mp3", 0, "audio/mpeg")
fg.rss_str(pretty=True)
fg.rss_file('podcast.xml')

# Move the feed file to the web
os.rename("podcast.xml", "/var/www/html/podcast.xml")
