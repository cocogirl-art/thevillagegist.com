import os
import re
from datetime import datetime

# --- CONFIGURATION ---
SITE_NAME = "The Village Gist News Network"
SITE_URL = "https://www.thevillagegist.com"
SITE_DESCRIPTION = "Local and National News from The Village Gist"
LOGO_URL = "https://www.thevillagegist.com/images/logo.png"
NEWS_FOLDER = "news"
RSS_FILE = "rss.xml"
COPYRIGHT = "© 2025 The Village Gist"

# --- HTML META PARSING ---
def extract_meta(html_content):
    title_match = re.search(r"<title>(.*?)</title>", html_content, re.IGNORECASE | re.DOTALL)
    desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html_content, re.IGNORECASE)
    title = title_match.group(1).strip() if title_match else "Untitled Article"
    desc = desc_match.group(1).strip() if desc_match else "No description available."
    return title, desc

# --- RSS GENERATION ---
def generate_rss(news_items):
    rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
<title>{SITE_NAME}</title>
<link>{SITE_URL}</link>
<description>{SITE_DESCRIPTION}</description>
<language>en-us</language>
<copyright>{COPYRIGHT}</copyright>
<image>
<url>{LOGO_URL}</url>
<title>{SITE_NAME}</title>
<link>{SITE_URL}</link>
</image>
"""
    for item in news_items:
        rss += f"""
<item>
<title>{item['title']}</title>
<link>{item['link']}</link>
<description>{item['description']}</description>
<pubDate>{item['pubDate']}</pubDate>
<guid>{item['link']}</guid>
</item>"""
    rss += "\n</channel>\n</rss>"
    return rss

# --- MAIN SCRIPT ---
def main():
    news_items = []
    folder_path = os.path.join(os.getcwd(), NEWS_FOLDER)

    for file in sorted(os.listdir(folder_path), reverse=True):
        if file.endswith(".html"):
            file_path = os.path.join(folder_path, file)
            with open(file_path, "r", encoding="utf-8") as f:
                html_content = f.read()
                title, desc = extract_meta(html_content)
                link = f"{SITE_URL}/{NEWS_FOLDER}/{file}"
                pub_date = datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0100")
                news_items.append({
                    "title": title,
                    "description": desc,
                    "link": link,
                    "pubDate": pub_date
                })

    rss_content = generate_rss(news_items)
    with open(RSS_FILE, "w", encoding="utf-8") as rss_file:
        rss_file.write(rss_content)

    print(f"✅ RSS feed updated with {len(news_items)} items at {RSS_FILE}")

if __name__ == "__main__":
    main()
