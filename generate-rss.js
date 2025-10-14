const fs = require('fs');

// Load your articles list
const articles = JSON.parse(fs.readFileSync('articles.json', 'utf8'));

// Build RSS XML
const rss = `
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>TheVillageGist News Network</title>
    <link>https://thevillagegist.com/</link>
    <description>Latest local news from Ewatto, Esan, and Edo State.</description>
    <language>en-us</language>
    <lastBuildDate>${new Date().toUTCString()}</lastBuildDate>

    ${articles
      .map(
        (a) => `
    <item>
      <title>${a.title}</title>
      <link>${a.link}</link>
      <description>${a.description}</description>
      <pubDate>${new Date(a.pubDate).toUTCString()}</pubDate>
    </item>`
      )
      .join('\n')}
  </channel>
</rss>
`;

// Save new rss.xml
fs.writeFileSync('rss.xml', rss);
console.log('✅ RSS feed updated successfully!');
