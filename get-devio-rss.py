import feedparser

RSS_URL = "https://feed.classmethod.jp/blog/daily.rss"

result = feedparser.parse(RSS_URL)
 
for entry in result['entries']:
    print("title:", entry.title)
    print("link: ", entry.link)
