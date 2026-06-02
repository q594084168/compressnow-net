def build_sitemap():
    import os
    urls = ["https://{DOMAIN}/"]
    for d in os.listdir('.'):
        fp = os.path.join(d, 'index.html')
        if os.path.isfile(fp) and not d.startswith('.'):
            urls.append("https://{DOMAIN}/" + d + "/")
    with open('sitemap.xml', 'w') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for u in urls:
            p = "1.0" if u.endswith("/") and u.count("/") == 3 else "0.8"
            f.write('  <url>\n')
            f.write('    <loc>' + u + '</loc>\n')
            f.write('    <changefreq>weekly</changefreq>\n')
            f.write('    <priority>' + p + '</priority>\n')
            f.write('  </url>\n')
        f.write('</urlset>\n')
    print("Sitemap: " + str(len(urls)) + " URLs")
