import os, datetime

rss_file = "rss.xml"
news_folder = "news"

# Get all HTML files in the news folder
items = ""
for file in os.listdir(news_folder):
    if file.endswith(".html"):
        title = file.replace(".html", "").replace("-", " ").title()
        link = f"https://www.thevillagegist.com/news/{file}"
        date = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0100")
        items += f"""
        <item>
        <title>{title}</title>
        <link>{link}</link>
        <description>{title} — latest story from The Village Gist.</description>
        <pubDate>{date}</pubDate>
        <guid>{link}</guid>
        </item>
        """

rss_template = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
<title>The Village Gist News Network</title>
<link>https://www.thevillagegist.com</link>
<description>Local and National News from The Village Gist</description>
<language>en-us</language>
<copyright>© 2025 The Village Gist</copyright>
<image>
<url>https://www.thevillagegist.com/assets/img/logo.png</url>
<title>The Village Gist News Network</title>
<link>https://www.thevillagegist.com</link>
</image>
{items}
</channel>
</rss>"""

open(rss_file, "w").write(rss_template)
print("RSS feed updated ✅")
