#!/usr/bin/env python3
"""CompressNow Build — Image compressor, fix SEO + expand pages"""

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

DOMAIN = "compressnow.net"
OUTPUT = "."

def w(path, content):
    full = os.path.join(OUTPUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

# ═══ Page Definitions ═══════════════════════════════

# Exact size pages
SIZES = [
    {"slug":"compress-image-to-10kb","size":"10 KB","title":"Compress Image to 10KB Online — Free, No Upload","desc":"Compress any image to exactly 10KB. Perfect for tiny icons, avatars, and strict file size limits. 100% browser-based, no upload needed."},
    {"slug":"compress-image-to-20kb","size":"20 KB","title":"Compress Image to 20KB Online — Free, No Upload","desc":"Compress any image to exactly 20KB. Great for form submissions and strict upload limits. 100% browser-based, no upload needed."},
    {"slug":"compress-image-to-30kb","size":"30 KB","title":"Compress Image to 30KB Online — Free, No Upload","desc":"Compress any image to exactly 30KB. Ideal for government forms and ID uploads. 100% browser-based, no upload needed."},
    {"slug":"compress-image-to-40kb","size":"40 KB","title":"Compress Image to 40KB Online — Free, No Upload","desc":"Compress any image to exactly 40KB. Perfect for application forms and profile photos. 100% browser-based, no upload needed."},
    {"slug":"compress-image-to-50kb","size":"50 KB","title":"Compress Image to 50KB Online — Free, No Upload","desc":"Compress any image to exactly 50KB. Great for email attachments and web thumbnails. 100% browser-based, no upload needed."},
    {"slug":"compress-image-to-60kb","size":"60 KB","title":"Compress Image to 60KB Online — Free, No Upload","desc":"Compress any image to exactly 60KB. Ideal for resume photos and job applications. 100% browser-based, no upload needed."},
    {"slug":"compress-image-to-75kb","size":"75 KB","title":"Compress Image to 75KB Online — Free, No Upload","desc":"Compress any image to exactly 75KB. Perfect for social media profiles and CMS uploads. 100% browser-based, no upload needed."},
    {"slug":"compress-image-to-80kb","size":"80 KB","title":"Compress Image to 80KB Online — Free, No Upload","desc":"Compress any image to exactly 80KB. Great for blog headers and article images. 100% browser-based, no upload needed."},
    {"slug":"compress-image-to-100kb","size":"100 KB","title":"Compress Image to 100KB Online — Free, No Upload","desc":"Compress any image to exactly 100KB. The most popular target size for web and email. 100% browser-based, no upload needed."},
    {"slug":"compress-image-to-150kb","size":"150 KB","title":"Compress Image to 150KB Online — Free, No Upload","desc":"Compress any image to exactly 150KB. Great for high-quality web images. 100% browser-based, no upload needed."},
    {"slug":"compress-image-to-200kb","size":"200 KB","title":"Compress Image to 200KB Online — Free, No Upload","desc":"Compress any image to exactly 200KB. Perfect for product photos and portfolios. 100% browser-based, no upload needed."},
    {"slug":"compress-image-to-250kb","size":"250 KB","title":"Compress Image to 250KB Online — Free, No Upload","desc":"Compress any image to exactly 250KB. Ideal for detailed images with good quality. 100% browser-based, no upload needed."},
    {"slug":"compress-image-to-300kb","size":"300 KB","title":"Compress Image to 300KB Online — Free, No Upload","desc":"Compress any image to exactly 300KB. Great for presentations and documents. 100% browser-based, no upload needed."},
    {"slug":"compress-image-to-400kb","size":"400 KB","title":"Compress Image to 400KB Online — Free, No Upload","desc":"Compress any image to exactly 400KB. Perfect for high-res web images. 100% browser-based, no upload needed."},
    {"slug":"compress-image-to-500kb","size":"500 KB","title":"Compress Image to 500KB Online — Free, No Upload","desc":"Compress any image to exactly 500KB. Great for detailed photos and prints. 100% browser-based, no upload needed."},
    {"slug":"compress-image-to-1mb","size":"1 MB","title":"Compress Image to 1MB Online — Free, No Upload","desc":"Compress any image to exactly 1MB. Perfect for email limits and web uploads. 100% browser-based, no upload needed."},
    {"slug":"compress-image-to-2mb","size":"2 MB","title":"Compress Image to 2MB Online — Free, No Upload","desc":"Compress any image to exactly 2MB. Great for document uploads and portfolios. 100% browser-based, no upload needed."},
    {"slug":"compress-image-to-5mb","size":"5 MB","title":"Compress Image to 5MB Online — Free, No Upload","desc":"Compress any image to exactly 5MB. Perfect for high-quality prints and archives. 100% browser-based, no upload needed."},
]

# Platform/scene pages
PLATFORMS = [
    {"slug":"compress-image-for-email","platform":"Email","title":"Compress Image for Email — Reduce Attachment Size Free","desc":"Compress images to fit email attachment limits. Reduce file size for Gmail, Outlook, Yahoo. Free, no upload, instant."},
    {"slug":"compress-image-for-whatsapp","platform":"WhatsApp","title":"Compress Image for WhatsApp — Send Photos Faster","desc":"Compress images for WhatsApp sharing. Reduce file size without losing quality. Free, browser-based, instant."},
    {"slug":"compress-image-for-instagram","platform":"Instagram","title":"Compress Image for Instagram — Optimize Photos Free","desc":"Compress images for Instagram posts and stories. Perfect file size every time. Free, no upload needed."},
    {"slug":"compress-image-for-facebook","platform":"Facebook","title":"Compress Image for Facebook — Faster Uploads Free","desc":"Compress images for Facebook posts and profiles. Reduce upload time. Free, browser-based, instant."},
    {"slug":"compress-image-for-discord","platform":"Discord","title":"Compress Image for Discord — Bypass Size Limits Free","desc":"Compress images for Discord uploads. Bypass the 8MB/25MB file size limit. Free, no upload, instant."},
    {"slug":"compress-image-for-twitter","platform":"Twitter","title":"Compress Image for Twitter/X — Optimize Photos Free","desc":"Compress images for Twitter/X posts. Meet the 5MB image limit. Free, browser-based, instant."},
    {"slug":"compress-image-for-linkedin","platform":"LinkedIn","title":"Compress Image for LinkedIn — Professional Photos Free","desc":"Compress images for LinkedIn profiles and posts. Optimize for professional display. Free, no upload needed."},
    {"slug":"compress-image-for-website","platform":"Website","title":"Compress Image for Website — Speed Up Page Load Free","desc":"Compress images for faster website loading. Improve Core Web Vitals and SEO. Free, browser-based, instant."},
    {"slug":"compress-image-for-pagespeed","platform":"PageSpeed","title":"Compress Image for Google PageSpeed — Pass Core Web Vitals","desc":"Compress images to pass Google PageSpeed Insights. Reduce LCP and improve performance score. Free, instant."},
    {"slug":"compress-image-for-slack","platform":"Slack","title":"Compress Image for Slack — Share Screenshots Faster","desc":"Compress images for Slack channels and DMs. Reduce file size for faster sharing. Free, no upload needed."},
    {"slug":"compress-image-for-teams","platform":"Teams","title":"Compress Image for Microsoft Teams — Optimize Attachments","desc":"Compress images for Teams chats and channels. Meet file size limits. Free, browser-based, instant."},
    {"slug":"compress-image-for-wordpress","platform":"WordPress","title":"Compress Image for WordPress — Speed Up Your Site Free","desc":"Compress images for WordPress uploads. Improve site speed and SEO. Free, no upload, instant."},
    {"slug":"compress-image-for-resume","platform":"Resume","title":"Compress Image for Resume — Fit Photo Under 100KB","desc":"Compress your resume photo to meet size requirements. Perfect for job applications. Free, browser-based, instant."},
    {"slug":"compress-image-for-printing","platform":"Printing","title":"Compress Image for Printing — Reduce File Size Free","desc":"Compress images for print submissions. Meet file size requirements while maintaining quality. Free, instant."},
    {"slug":"compress-product-photo-for-shopify","platform":"Shopify","title":"Compress Product Photo for Shopify — Optimize Store Images","desc":"Compress product photos for Shopify stores. Faster loading = more sales. Free, browser-based, instant."},
    {"slug":"compress-image-for-tiktok","platform":"TikTok","title":"Compress Image for TikTok — Optimize Thumbnails Free","desc":"Compress images for TikTok thumbnails and profiles. Perfect file size every time. Free, no upload needed."},
]

# Format pages
FORMATS = [
    {"slug":"compress-png","format":"PNG","title":"Compress PNG Online — Reduce PNG File Size Free","desc":"Compress PNG images online without losing quality. Reduce file size instantly in your browser. Free, no upload needed."},
    {"slug":"compress-jpeg-without-losing-quality","format":"JPEG","title":"Compress JPEG Without Losing Quality — Free Online Tool","desc":"Compress JPEG photos while preserving quality. Smart compression for photos and images. Free, browser-based, instant."},
    {"slug":"compress-webp","format":"WebP","title":"Compress WebP Online — Reduce WebP File Size Free","desc":"Compress WebP images online. Reduce file size for faster web loading. Free, no upload, instant."},
    {"slug":"compress-icon-logo","format":"Icon/Logo","title":"Compress Icon and Logo Images — Reduce Size Under 50KB","desc":"Compress icons, logos, and favicons to tiny file sizes. Perfect for websites and apps. Free, browser-based."},
    {"slug":"compress-passport-photo","format":"Passport Photo","title":"Compress Passport Photo — Meet Size Requirements Free","desc":"Compress passport photos to meet government size requirements (10KB-100KB). Free, no upload, instant."},
    {"slug":"compress-screenshot","format":"Screenshot","title":"Compress Screenshot — Reduce Screenshot File Size Free","desc":"Compress screenshots for sharing and documentation. Reduce file size instantly. Free, browser-based, instant."},
    {"slug":"compress-scanned-document","format":"Scanned Document","title":"Compress Scanned Document — Reduce PDF/Image Size Free","desc":"Compress scanned documents for email and upload. Reduce file size while keeping text readable. Free, instant."},
    {"slug":"compress-signature-image","format":"Signature","title":"Compress Signature Image — Reduce to Under 50KB Free","desc":"Compress signature images for forms and documents. Meet strict file size limits. Free, no upload, instant."},
]

# Special pages
SPECIAL = [
    {"slug":"bulk-image-compressor","title":"Bulk Image Compressor — Compress Multiple Images Free","desc":"Compress multiple images at once. Batch compression for PNG, JPEG, WebP. Free, browser-based, no upload needed."},
    {"slug":"compress-image-to-exact-kb","title":"Compress Image to Exact KB — Precise File Size Control","desc":"Compress images to any exact file size in KB. Precise control over output size. Free, browser-based, instant."},
    {"slug":"compress-image-under-50kb","title":"Compress Image Under 50KB — Ultra-Small File Size Free","desc":"Compress images to under 50KB. Perfect for forms, avatars, and strict limits. Free, no upload, instant."},
    {"slug":"reduce-image-size-for-upload","title":"Reduce Image Size for Upload — Meet File Size Limits","desc":"Reduce image file size to meet upload requirements. Works for any platform. Free, browser-based, instant."},
    # Existing pages from original site
    {"slug":"compress-image-for-amazon-product-listing","title":"Compress Image for Amazon — Optimize Product Photos Free","desc":"Compress product images for Amazon listings. Meet Amazon's file size requirements. Free, browser-based, instant."},
    {"slug":"compress-image-for-avatar-profile-picture","title":"Compress Image for Avatar — Reduce Profile Picture Size","desc":"Compress avatar and profile pictures to small file sizes. Perfect for social media and forums. Free, instant."},
    {"slug":"compress-image-for-blog-featured-image","title":"Compress Image for Blog — Optimize Featured Images","desc":"Compress blog featured images for faster loading. Improve SEO and user experience. Free, browser-based."},
    {"slug":"compress-image-for-blog-post-inline-image","title":"Compress Blog Post Images — Optimize Inline Photos","desc":"Compress inline images for blog posts. Reduce page load time. Free, no upload, instant."},
    {"slug":"compress-image-for-craigslist-ad","title":"Compress Image for Craigslist — Meet Upload Limits","desc":"Compress images for Craigslist ads. Meet file size requirements. Free, browser-based, instant."},
    {"slug":"compress-image-for-dating-app-profile","title":"Compress Image for Dating Apps — Optimize Profile Photos","desc":"Compress profile photos for Tinder, Bumble, Hinge. Perfect file size every time. Free, instant."},
    {"slug":"compress-image-for-digital-art-commission","title":"Compress Image for Digital Art — Share Portfolio Work","desc":"Compress digital art for online portfolios and commissions. Reduce file size while preserving quality. Free."},
    {"slug":"compress-image-for-ebay-listing","title":"Compress Image for eBay — Optimize Listing Photos","desc":"Compress product photos for eBay listings. Meet eBay's image requirements. Free, browser-based, instant."},
    {"slug":"compress-image-for-ecommerce-product-catalog","title":"Compress Image for E-commerce — Optimize Product Catalog","desc":"Compress product images for e-commerce catalogs. Faster loading = more sales. Free, browser-based."},
    {"slug":"compress-image-for-email-marketing-campaign","title":"Compress Image for Email Marketing — Optimize Newsletter","desc":"Compress images for email marketing campaigns. Reduce load time and improve deliverability. Free, instant."},
    {"slug":"compress-image-for-email-signature","title":"Compress Image for Email Signature — Tiny File Size","desc":"Compress email signature images to under 10KB. Fast loading in every email client. Free, browser-based."},
    {"slug":"compress-image-for-etsy-product-photo","title":"Compress Image for Etsy — Optimize Shop Photos","desc":"Compress product photos for Etsy listings. Meet Etsy's image requirements. Free, browser-based, instant."},
    {"slug":"compress-image-for-event-flyer","title":"Compress Image for Event Flyer — Share Digitally","desc":"Compress event flyers for email and social media sharing. Reduce file size while keeping text sharp. Free."},
    {"slug":"compress-image-for-google-ads-display","title":"Compress Image for Google Ads — Meet Display Requirements","desc":"Compress images for Google Ads display campaigns. Meet file size limits. Free, browser-based, instant."},
    {"slug":"compress-image-for-google-business-profile-listing","title":"Compress Image for Google Business — Optimize Listings","desc":"Compress images for Google Business Profile. Meet Google's image requirements. Free, browser-based."},
    {"slug":"compress-image-for-google-drive-sharing","title":"Compress Image for Google Drive — Save Storage Space","desc":"Compress images before uploading to Google Drive. Save storage space. Free, no upload, instant."},
    {"slug":"compress-image-for-google-forms","title":"Compress Image for Google Forms — Meet Upload Limits","desc":"Compress images for Google Forms file upload questions. Meet size limits. Free, browser-based, instant."},
    {"slug":"compress-image-for-linkedin-profile","title":"Compress Image for LinkedIn — Optimize Profile Photos","desc":"Compress profile and banner images for LinkedIn. Professional quality, optimized size. Free, instant."},
    {"slug":"compress-image-for-medical-report","title":"Compress Image for Medical Report — Reduce File Size","desc":"Compress medical report images for digital submission. Meet file size requirements. Free, browser-based."},
    {"slug":"compress-image-for-mobile-app-icon","title":"Compress Image for App Icon — Optimize Mobile Icons","desc":"Compress app icons for mobile development. Meet platform requirements. Free, no upload, instant."},
    {"slug":"compress-image-for-newsletter-header","title":"Compress Image for Newsletter — Optimize Header Images","desc":"Compress newsletter header images for email campaigns. Faster loading, better engagement. Free, instant."},
    {"slug":"compress-image-for-online-class-submission","title":"Compress Image for Online Class — Meet Submission Limits","desc":"Compress images for online class submissions. Meet file size requirements. Free, browser-based, instant."},
    {"slug":"compress-image-for-online-course-platform","title":"Compress Image for Online Course — Optimize Course Materials","desc":"Compress images for online course platforms. Faster loading for students. Free, browser-based, instant."},
    {"slug":"compress-image-for-online-marketplace-listing","title":"Compress Image for Marketplace — Optimize Listings","desc":"Compress images for online marketplace listings. Meet platform requirements. Free, browser-based, instant."},
    {"slug":"compress-image-for-online-portfolio","title":"Compress Image for Portfolio — Showcase Your Work","desc":"Compress images for online portfolios. Fast loading galleries. Free, no upload, instant."},
    {"slug":"compress-image-for-online-portfolio-gallery","title":"Compress Image for Portfolio Gallery — Optimize Gallery","desc":"Compress images for portfolio galleries. Reduce load time while maintaining quality. Free, instant."},
    {"slug":"compress-image-for-pdf-attachment","title":"Compress Image for PDF — Reduce PDF File Size","desc":"Compress images before adding to PDF documents. Reduce overall PDF size. Free, browser-based, instant."},
    {"slug":"compress-image-for-pinterest-pin","title":"Compress Image for Pinterest — Optimize Pin Images","desc":"Compress images for Pinterest pins. Meet Pinterest's image requirements. Free, browser-based, instant."},
    {"slug":"compress-image-for-powerpoint-presentation","title":"Compress Image for PowerPoint — Reduce Presentation Size","desc":"Compress images for PowerPoint presentations. Reduce file size for email sharing. Free, instant."},
    {"slug":"compress-image-for-print-flyer","title":"Compress Image for Print Flyer — Optimize for Print","desc":"Compress images for print flyers. Balance quality and file size. Free, browser-based, instant."},
    {"slug":"compress-image-for-real-estate-listing","title":"Compress Image for Real Estate — Optimize Property Photos","desc":"Compress property photos for real estate listings. Fast loading, great quality. Free, browser-based."},
    {"slug":"compress-image-for-reddit-post","title":"Compress Image for Reddit — Optimize Post Images","desc":"Compress images for Reddit posts. Meet Reddit's image requirements. Free, browser-based, instant."},
    {"slug":"compress-image-for-resume-attachment","title":"Compress Image for Resume — Optimize Resume Photos","desc":"Compress profile photos for resumes and CVs. Meet application file size limits. Free, instant."},
    {"slug":"compress-image-for-school-project-submission","title":"Compress Image for School Project — Meet Submission Limits","desc":"Compress images for school project submissions. Meet file size requirements. Free, browser-based."},
    {"slug":"compress-image-for-social-media-story","title":"Compress Image for Social Media Story — Optimize Stories","desc":"Compress images for Instagram, Facebook, and Snapchat stories. Perfect file size. Free, instant."},
    {"slug":"compress-image-for-telegram-sticker","title":"Compress Image for Telegram Sticker — Meet Size Limits","desc":"Compress images for Telegram stickers. Meet Telegram's 512KB limit. Free, browser-based, instant."},
    {"slug":"compress-image-for-travel-blog","title":"Compress Image for Travel Blog — Optimize Travel Photos","desc":"Compress travel photos for blog posts. Faster loading, better SEO. Free, no upload, instant."},
    {"slug":"compress-image-for-twitter-profile","title":"Compress Image for Twitter Profile — Optimize Profile Photos","desc":"Compress profile and header images for Twitter/X. Meet platform requirements. Free, browser-based."},
    {"slug":"compress-image-for-twitter-timeline-post","title":"Compress Image for Twitter Post — Optimize Timeline Images","desc":"Compress images for Twitter/X timeline posts. Meet the 5MB limit. Free, browser-based, instant."},
    {"slug":"compress-image-for-university-application","title":"Compress Image for University Application — Meet Requirements","desc":"Compress images for university applications. Meet document upload limits. Free, browser-based, instant."},
    {"slug":"compress-image-for-website-hero-banner","title":"Compress Image for Website Hero Banner — Optimize Banners","desc":"Compress hero banner images for websites. Faster page load, better Core Web Vitals. Free, instant."},
    {"slug":"compress-image-for-website-thumbnail","title":"Compress Image for Website Thumbnail — Optimize Thumbnails","desc":"Compress website thumbnail images. Reduce file size for faster loading. Free, browser-based, instant."},
    {"slug":"compress-image-for-wordpress-media-library","title":"Compress Image for WordPress Media Library — Save Space","desc":"Compress images for WordPress media library. Save server storage space. Free, browser-based, instant."},
    {"slug":"compress-image-for-youtube-thumbnail","title":"Compress Image for YouTube Thumbnail — Optimize Thumbnails","desc":"Compress YouTube thumbnail images. Meet YouTube's requirements. Free, browser-based, instant."},
]

# Format conversion pages
CONVERSIONS = [
    {"slug":"jpg-to-png","title":"Convert JPG to PNG Online — Free, Instant","desc":"Convert JPG/JPEG images to PNG format online. Preserve quality with lossless conversion. Free, browser-based, no upload."},
    {"slug":"png-to-jpg","title":"Convert PNG to JPG Online — Free, Instant","desc":"Convert PNG images to JPG/JPEG format online. Reduce file size significantly. Free, browser-based, no upload."},
    {"slug":"webp-to-jpg","title":"Convert WebP to JPG Online — Free, Instant","desc":"Convert WebP images to JPG/JPEG format. Universal compatibility. Free, browser-based, no upload needed."},
    {"slug":"webp-to-png","title":"Convert WebP to PNG Online — Free, Instant","desc":"Convert WebP images to PNG format with transparency preserved. Free, browser-based, no upload needed."},
    {"slug":"jpg-to-webp","title":"Convert JPG to WebP Online — Free, Instant","desc":"Convert JPG images to WebP format for smaller file sizes. Modern web format. Free, browser-based, no upload."},
    {"slug":"png-to-webp","title":"Convert PNG to WebP Online — Free, Instant","desc":"Convert PNG images to WebP format. 25-35% smaller than PNG. Free, browser-based, no upload needed."},
]

ALL_SCENARIOS = []

for s in SIZES:
    s["cat"] = "size"
    ALL_SCENARIOS.append(s)
for s in PLATFORMS:
    s["cat"] = "platform"
    ALL_SCENARIOS.append(s)
for s in FORMATS:
    s["cat"] = "format"
    ALL_SCENARIOS.append(s)
for s in SPECIAL:
    s["cat"] = "special"
    ALL_SCENARIOS.append(s)
for s in CONVERSIONS:
    s["cat"] = "conversion"
    ALL_SCENARIOS.append(s)

# ═══ Enrichment ════════════════════════════════════

ENRICHMENT = {
    "size": {
        "how_to": [
            "Upload or drag your image into the tool above.",
            "Set the target file size (the tool will auto-detect the optimal compression level).",
            "Click 'Compress' and download your compressed image instantly."
        ],
        "tips": "Compressing to an exact KB size is useful for government forms, passport photos, job applications, and CMS uploads that enforce strict file size limits. Our tool uses smart binary search compression to hit your target size precisely."
    },
    "platform": {
        "how_to": [
            "Upload your image using the tool above.",
            "The tool automatically applies platform-optimized compression settings.",
            "Download the compressed image and upload it to your platform."
        ],
        "tips": "Each platform has different image size and quality requirements. Our tool optimizes compression specifically for the platform you choose, balancing file size and visual quality."
    },
    "format": {
        "how_to": [
            "Upload your image (PNG, JPEG, or WebP).",
            "Our tool applies format-specific compression algorithms for optimal results.",
            "Download the compressed image — quality preserved, file size reduced."
        ],
        "tips": "Different image formats compress differently. PNG is best for graphics and transparency, JPEG for photos, and WebP for modern web. Our tool uses the best compression method for each format."
    },
    "special": {
        "how_to": [
            "Upload one or more images using the tool above.",
            "Configure compression settings (quality, target size, format).",
            "Download all compressed images at once."
        ],
        "tips": "Bulk compression saves time when you have multiple images to process. Our tool processes everything locally in your browser — your images never leave your device."
    },
    "conversion": {
        "how_to": [
            "Upload your image using the tool above.",
            "The tool automatically converts to the target format.",
            "Download the converted image instantly."
        ],
        "tips": "Different formats serve different purposes: PNG supports transparency and is best for graphics, JPEG is ideal for photos with small file sizes, WebP offers the best compression for modern web browsers."
    }
}

# ═══ Page Template ═════════════════════════════════

def build_scene_page(s):
    e = ENRICHMENT.get(s["cat"], ENRICHMENT["special"])
    how_to_html = "".join(f"<p>Step {i+1}: {step}</p>" for i, step in enumerate(e["how_to"]))

    # Structured internal linking by user intent
    slug = s["slug"]
    cat = s["cat"]
    related_slugs = []

    # For size pages: link to nearby sizes + popular platforms + conversions
    if cat == "size":
        size_val = s.get("size", "100 KB").replace(" KB","").replace(" MB","000")
        try: size_num = int(size_val)
        except: size_num = 100
        # Nearby sizes
        nearby = [s2 for s2 in SIZES if s2["slug"] != slug and abs(int(s2.get("size","100 KB").replace(" KB","").replace(" MB","000")) - size_num) <= size_num]
        related_slugs.extend([s2["slug"] for s2 in nearby[:2]])
        # Popular platforms
        related_slugs.extend(["compress-image-for-email", "compress-image-for-discord", "compress-image-for-whatsapp"])
        # Conversion
        related_slugs.append("jpg-to-png")

    # For platform pages: link to common sizes + other platforms + conversions
    elif cat == "platform":
        related_slugs.extend(["compress-image-to-100kb", "compress-image-to-50kb", "compress-image-to-200kb"])
        other_platforms = [s2["slug"] for s2 in PLATFORMS if s2["slug"] != slug]
        related_slugs.extend(other_platforms[:2])
        related_slugs.append("png-to-jpg")

    # For format pages: link to conversions + sizes + platforms
    elif cat == "format":
        related_slugs.extend(["jpg-to-png", "png-to-jpg", "webp-to-jpg"])
        related_slugs.extend(["compress-image-to-100kb", "compress-image-to-50kb"])
        related_slugs.append("compress-image-for-website")

    # For special pages: link to sizes + platforms
    elif cat == "special":
        related_slugs.extend(["compress-image-to-100kb", "compress-image-to-50kb", "compress-image-to-200kb"])
        related_slugs.extend(["compress-image-for-email", "compress-image-for-discord"])
        related_slugs.append("jpg-to-png")

    # For conversion pages: link to other conversions + sizes
    elif cat == "conversion":
        other_conv = [s2["slug"] for s2 in CONVERSIONS if s2["slug"] != slug]
        related_slugs.extend(other_conv[:3])
        related_slugs.extend(["compress-image-to-100kb", "compress-image-to-50kb"])
        related_slugs.append("compress-image-for-website")

    # Build related HTML
    related_html = ""
    for rs in related_slugs[:6]:
        r = next((s2 for s2 in ALL_SCENARIOS if s2["slug"] == rs), None)
        if r:
            related_html += f'<li><a href="/{r["slug"]}/">{r["title"].split("—")[0].strip()}</a></li>'

    # Cross-site links
    cross_links = """<p>Need to compress images for other tools? Try <a href="https://cvbuild-ai.com">CVBuild-AI</a> for resume content, <a href="https://messagegen-ai.com">MessageGen-AI</a> for email writing, and <a href="https://tonemodifier.com">ToneModifier</a> for tone adjustment.</p>"""

    title = s["title"]
    desc = s["desc"]
    slug = s["slug"]

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{desc}">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://{DOMAIN}/{slug}/">
    <link rel="canonical" href="https://{DOMAIN}/{slug}/">
    <title>{title}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-Z9NW1GSG04"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag("js",new Date());gtag("config","G-Z9NW1GSG04");</script>
    <style>
        :root{{--primary:#4F46E5;--primary-dark:#4338CA;--bg:#F8FAFC;--card-bg:#FFFFFF;--text:#1E293B;--text-secondary:#64748B;--border:#E2E8F0;--radius:12px}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:var(--bg);color:var(--text);line-height:1.6}}
.container{{max-width:960px;margin:0 auto;padding:0 24px}}
header{{background:#1E293B;color:#F1F5F9;padding:16px 0;box-shadow:0 2px 8px rgba(0,0,0,.15)}}
header .container{{display:flex;justify-content:space-between;align-items:center}}
header nav{{display:flex;gap:24px}}header nav a{{color:#94A3B8;text-decoration:none;font-size:.9rem;font-weight:500}}header nav a:hover{{color:#fff}}
.subtitle{{color:var(--text-secondary);max-width:560px;margin:0 auto}}
.tool-area{{max-width:700px;margin:0 auto 24px;padding:0 24px}}
.tool-area textarea{{width:100%;border:2px dashed var(--border);border-radius:var(--radius);padding:20px;font-family:'Consolas',monospace;font-size:14px;resize:vertical;background:var(--card-bg);min-height:200px}}
.tool-area textarea:focus{{outline:none;border-color:var(--primary);border-style:solid}}
.btn-row{{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-bottom:24px}}
.btn{{padding:12px 28px;border:none;border-radius:8px;font-size:1rem;font-weight:600;cursor:pointer;font-family:inherit}}.btn:active{{transform:scale(.97)}}
.btn-primary{{background:var(--primary);color:#fff}}.btn-primary:hover{{background:var(--primary-dark)}}
.btn-secondary{{background:var(--card-bg);color:var(--text);border:1px solid var(--border)}}
.output-area{{margin-top:16px;background:var(--card-bg);border:1px solid var(--border);border-radius:var(--radius);padding:20px;min-height:80px;word-break:break-all;display:none}}
.error-msg{{color:#DC2626;font-size:.85rem;margin-top:8px;display:none}}
.faq-section{{padding:40px 0;text-align:left}}.faq-section h2{{font-size:1.5rem;margin-bottom:24px;text-align:center}}
.faq-item{{margin-bottom:20px}}.faq-item h3{{font-size:1rem;margin-bottom:6px;color:var(--primary)}}
.faq-item p{{color:var(--text-secondary);font-size:.9rem}}
footer{{background:#1E293B;color:#94A3B8;padding:32px 0;text-align:center;font-size:.85rem}}
footer a{{color:#CBD5E1;text-decoration:none}}
        .scene-hero{{padding:40px 0 24px;text-align:center}}
        .scene-hero h1{{font-size:2rem;font-weight:800;margin-bottom:12px;line-height:1.3}}
        @media(max-width:640px){{.scene-hero h1{{font-size:1.5rem}}}}
        .scene-body{{max-width:700px;margin:0 auto;padding:0 24px 40px}}
        .scene-body h2{{font-size:1.25rem;margin:32px 0 12px;color:#1E293B}}
        .scene-body p{{color:#475569;margin-bottom:12px;font-size:1rem;line-height:1.7}}
        .related-tools{{background:#F8FAFC;border-top:1px solid #E2E8F0;padding:40px 0}}
        .related-tools .container{{max-width:960px;margin:0 auto;padding:0 24px}}
        .related-tools h2{{font-size:1.5rem;margin-bottom:20px;text-align:center}}
        .related-tools ul{{list-style:none;display:grid;grid-template-columns:repeat(2,1fr);gap:12px;max-width:600px;margin:0 auto}}
        @media(max-width:640px){{.related-tools ul{{grid-template-columns:1fr}}}}
        .related-tools a{{color:#4F46E5;text-decoration:none;font-weight:500;padding:10px 16px;display:block;background:#fff;border-radius:8px;border:1px solid #E2E8F0;transition:all .15s}}
        .related-tools a:hover{{border-color:#4F46E5;box-shadow:0 2px 8px rgba(79,70,229,0.12)}}
        .breadcrumb{{font-size:.85rem;color:#64748B;padding:16px 0;max-width:960px;margin:0 auto}}
        .breadcrumb a{{color:#4F46E5;text-decoration:none}}.breadcrumb a:hover{{text-decoration:underline}}
        .cross-site{{max-width:700px;margin:0 auto 40px;padding:20px;background:#F5F0FF;border-left:3px solid #4F46E5;border-radius:0 8px 8px 0}}
        .cross-site strong{{color:#4F46E5}}
        .cross-site a{{color:#4F46E5;font-weight:600}}
    </style>
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{{"@type": "Question", "name": "Can I compress an image to {s.get('size', 'exact')} online?", "acceptedAnswer": {{"@type": "Answer", "text": "Yes. Upload your image and our tool automatically compresses it to the target size. 100% browser-based, no upload to server."}}}}, {{"@type": "Question", "name": "Is this tool free?", "acceptedAnswer": {{"@type": "Answer", "text": "Yes, completely free. No signup, no watermarks, no limits."}}}}, {{"@type": "Question", "name": "Is my image uploaded to a server?", "acceptedAnswer": {{"@type": "Answer", "text": "No. All processing happens locally in your browser. Your images never leave your device."}}}}]
    }}
    </script>
    <script type="application/ld+json">
    {{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://{DOMAIN}/"}}, {{"@type": "ListItem", "position": 2, "name": "{title.split('—')[0].strip()}", "item": "https://{DOMAIN}/{slug}/"}}]}}
    </script>
    <script type="application/ld+json">
    {{"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "{title}", "url": "https://{DOMAIN}/{slug}/", "description": "{desc}", "applicationCategory": "UtilityApplication", "operatingSystem": "All", "offers": {{"@type": "Offer", "price": "0", "priceCurrency": "USD"}}}}
    </script>
</head>
<body>
    <header>
        <div class="container">
            <a href="/" class="logo">Compressnow</a>
            <nav>
                <a href="/">Home</a>
                <a href="#faq">FAQ</a>
                <a href="#related">Related Tools</a>
            </nav>
        </div>
    </header>
    <main>
        <div class="breadcrumb"><a href="/">Home</a> / {title.split('—')[0].strip()}</div>
        <section class="scene-hero">
            <h1>{title}</h1>
            <p class="subtitle">{desc}</p>
        </section>
        <section class="tool-area">
            <div id="dropZone" style="border:2px dashed var(--border);border-radius:var(--radius);padding:40px 20px;text-align:center;cursor:pointer;background:var(--card-bg);transition:all .2s">
                <p style="font-size:2rem;margin-bottom:8px">📁</p>
                <p style="font-weight:600;margin-bottom:4px">Drop image here or click to upload</p>
                <p style="color:var(--text-secondary);font-size:.85rem">Supports PNG, JPEG, WebP</p>
                <input type="file" id="fileInput" accept="image/*" style="display:none">
            </div>
            <div id="previewArea" style="display:none;margin-top:20px">
                <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px">
                    <div style="text-align:center"><p style="font-size:.8rem;color:var(--text-secondary);margin-bottom:8px">Original</p><img id="originalPreview" style="max-width:100%;border-radius:8px;border:1px solid var(--border)"></div>
                    <div style="text-align:center"><p style="font-size:.8rem;color:var(--text-secondary);margin-bottom:8px">Compressed</p><img id="compressedPreview" style="max-width:100%;border-radius:8px;border:1px solid var(--border)"></div>
                </div>
                <div id="stats" style="background:var(--card-bg);border:1px solid var(--border);border-radius:8px;padding:16px;margin-bottom:16px;font-size:.9rem"></div>
                <div class="btn-row">
                    <button class="btn btn-primary" id="downloadBtn">⬇ Download Compressed</button>
                    <button class="btn btn-secondary" id="resetBtn">🔄 Compress Another</button>
                </div>
            </div>
            <div id="progressBar" style="display:none;margin-top:16px;background:var(--border);border-radius:8px;overflow:hidden;height:8px"><div id="progressFill" style="background:var(--primary);height:100%;width:0%;transition:width .3s"></div></div>
            <p class="error-msg" id="errorMsg"></p>
        </section>
        <section class="scene-body">
            <h2>About This Tool</h2>
            <p>{desc}</p>
            <h2>How to Use</h2>
            {how_to_html}
            <h2>Tips</h2>
            <p>{e['tips']}</p>
        </section>
        <div class="cross-site">
            <strong>Pro Tip</strong> — After compressing your image, use <a href="https://cvbuild-ai.com">CVBuild-AI</a> to build your resume, <a href="https://messagegen-ai.com">MessageGen-AI</a> to write professional emails, and <a href="https://tonemodifier.com">ToneModifier</a> to perfect your tone.
        </div>
        <section class="faq-section" id="faq">
            <div class="container">
                <h2>Frequently Asked Questions</h2>
                <div class="faq-item">
                    <h3>Can I compress an image to {s.get('size', 'exact')} online?</h3>
                    <p>Yes. Upload your image and our tool automatically compresses it to the target size. 100% browser-based, no upload to server.</p>
                </div>
                <div class="faq-item">
                    <h3>Is this tool free?</h3>
                    <p>Yes, completely free. No signup, no watermarks, no limits.</p>
                </div>
                <div class="faq-item">
                    <h3>Is my image uploaded to a server?</h3>
                    <p>No. All processing happens locally in your browser. Your images never leave your device.</p>
                </div>
            </div>
        </section>
        <section class="related-tools" id="related">
            <div class="container">
                <h2>Related Tools</h2>
                <ul>
                    {related_html}
                </ul>
            </div>
        </section>
    </main>
    <footer>
        <div class="container">
            <p>&copy; 2026 Compressnow. All rights reserved. | <a href="/">Home</a> | <a href="#faq">FAQ</a></p>
            <p style="margin-top:8px">All processing happens locally in your browser. Your data is never uploaded.</p>
        </div>
    </footer>
    <script>
    const IS_CONVERSION = {"true" if s.get("cat") == "conversion" else "false"};
    const TARGET_KB = {s.get('size', '100').replace(' KB','').replace(' MB','000')};
    const TARGET_BYTES = TARGET_KB * 1024;
    const CONVERT_TO = IS_CONVERSION ? '{s.get("slug","").split("-to-")[1] if "-to-" in s.get("slug","") else "png"}' : '';
    const dropZone = document.getElementById('dropZone');
    const fileInput = document.getElementById('fileInput');
    const previewArea = document.getElementById('previewArea');
    const originalPreview = document.getElementById('originalPreview');
    const compressedPreview = document.getElementById('compressedPreview');
    const stats = document.getElementById('stats');
    const downloadBtn = document.getElementById('downloadBtn');
    const resetBtn = document.getElementById('resetBtn');
    const progressBar = document.getElementById('progressBar');
    const progressFill = document.getElementById('progressFill');
    const errorMsg = document.getElementById('errorMsg');
    let resultBlob = null;
    let resultUrl = null;
    dropZone.addEventListener('click', () => fileInput.click());
    dropZone.addEventListener('dragover', e => {{ e.preventDefault(); dropZone.style.borderColor = 'var(--primary)'; dropZone.style.background = '#F5F3FF'; }});
    dropZone.addEventListener('dragleave', () => {{ dropZone.style.borderColor = 'var(--border)'; dropZone.style.background = 'var(--card-bg)'; }});
    dropZone.addEventListener('drop', e => {{ e.preventDefault(); dropZone.style.borderColor = 'var(--border)'; dropZone.style.background = 'var(--card-bg)'; if(e.dataTransfer.files.length) handleFile(e.dataTransfer.files[0]); }});
    fileInput.addEventListener('change', () => {{ if(fileInput.files.length) handleFile(fileInput.files[0]); }});
    resetBtn.addEventListener('click', () => {{ previewArea.style.display = 'none'; dropZone.style.display = 'block'; fileInput.value = ''; if(resultUrl) URL.revokeObjectURL(resultUrl); resultBlob = null; resultUrl = null; errorMsg.style.display = 'none'; }});
    downloadBtn.addEventListener('click', () => {{ if(!resultBlob) return; const a = document.createElement('a'); a.href = resultUrl; const ext = CONVERT_TO || 'jpg'; const name = fileInput.files[0].name.replace(/\.[^.]+$/, '') + '.' + ext; a.download = name; a.click(); }});
    function formatSize(bytes) {{ if(bytes < 1024) return bytes + ' B'; if(bytes < 1048576) return (bytes/1024).toFixed(1) + ' KB'; return (bytes/1048576).toFixed(2) + ' MB'; }}
    function handleFile(file) {{ if(!file.type.match(/^image\/(png|jpeg|webp)$/)) {{ errorMsg.textContent = 'Please upload a PNG, JPEG, or WebP image.'; errorMsg.style.display = 'block'; return; }} errorMsg.style.display = 'none'; const reader = new FileReader(); reader.onload = e => {{ const img = new Image(); img.onload = () => {{ originalPreview.src = e.target.result; dropZone.style.display = 'none'; previewArea.style.display = 'block'; progressBar.style.display = 'block'; progressFill.style.width = '30%'; if(IS_CONVERSION) convertImage(img); else compressImage(img, file.type); }}; img.src = e.target.result; }}; reader.readAsDataURL(file); }}
    function convertImage(img) {{ const canvas = document.createElement('canvas'); canvas.width = img.width; canvas.height = img.height; const ctx = canvas.getContext('2d'); ctx.drawImage(img, 0, 0); progressFill.style.width = '60%'; const mimeMap = {{'png':'image/png','jpg':'image/jpeg','jpeg':'image/jpeg','webp':'image/webp'}}; const mime = mimeMap[CONVERT_TO] || 'image/jpeg'; const quality = mime === 'image/png' ? undefined : 0.92; canvas.toBlob(blob => {{ resultBlob = blob; showResult(blob, img.width, img.height); }}, mime, quality); }}
    function compressImage(img, type) {{ const canvas = document.createElement('canvas'); canvas.width = img.width; canvas.height = img.height; const ctx = canvas.getContext('2d'); ctx.drawImage(img, 0, 0); progressFill.style.width = '60%'; const mimeType = type === 'image/png' ? 'image/png' : type === 'image/webp' ? 'image/webp' : 'image/jpeg'; if(mimeType === 'image/png') {{ canvas.toBlob(blob => {{ resultBlob = blob; showResult(blob, img.width, img.height); }}, mimeType); }} else {{ let low = 0.01, high = 1.0, bestBlob = null; function tryQuality(q) {{ canvas.toBlob(blob => {{ if(!blob) {{ showResult(bestBlob || new Blob(), img.width, img.height); return; }} if(blob.size <= TARGET_BYTES * 1.05) {{ bestBlob = blob; low = q; }} else {{ high = q; }} if(high - low < 0.01) {{ resultBlob = bestBlob || blob; showResult(resultBlob, img.width, img.height); }} else {{ progressFill.style.width = (60 + (1 - (high-low)) * 30) + '%'; tryQuality((low + high) / 2); }} }}, mimeType, q); }} tryQuality(0.7); }} }}
    function showResult(blob, w, h) {{ if(resultUrl) URL.revokeObjectURL(resultUrl); resultBlob = blob; resultUrl = URL.createObjectURL(blob); compressedPreview.src = resultUrl; progressFill.style.width = '100%'; setTimeout(() => progressBar.style.display = 'none', 500); const originalSize = fileInput.files[0].size; const resultSize = blob.size; const change = ((1 - resultSize/originalSize) * 100).toFixed(1); const label = IS_CONVERSION ? 'Converted' : 'Compressed'; stats.innerHTML = '<div style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px"><div><strong>Original:</strong> ' + formatSize(originalSize) + '</div><div><strong>' + label + ':</strong> ' + formatSize(resultSize) + '</div><div><strong>Change:</strong> ' + change + '%</div><div><strong>Dimensions:</strong> ' + w + ' x ' + h + '</div></div>'; }}
    </script>
</body>
</html>"""


# ═══ Build Homepage ═════════════════════════════════

def build_home():
    # Size cards
    size_cards = "".join(f'<a href="/{s["slug"]}/" class="card">{s["size"]}</a>' for s in SIZES[:9])
    # Platform cards
    platform_cards = "".join(f'<a href="/{s["slug"]}/" class="card">{s["platform"]}</a>' for s in PLATFORMS[:8])
    # Conversion cards
    conversion_cards = "".join(f'<a href="/{s["slug"]}/" class="card">{s["title"].split("—")[0].strip()}</a>' for s in CONVERSIONS)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Compress images to exact 100KB/200KB/500KB online. 100% browser-based, no upload needed. Support PNG, JPEG, WebP. Free forever.">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://{DOMAIN}/">
    <meta property="og:title" content="Compress Image to Exact KB Online — Free, No Upload | CompressNow">
    <meta property="og:description" content="Compress images to exact 100KB/200KB/500KB online. 100% browser-based, no upload needed. Support PNG, JPEG, WebP. Free forever.">
    <meta property="og:url" content="https://{DOMAIN}/">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary_large_image">
    <title>Compress Image to Exact KB Online — Free, No Upload | CompressNow</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"CompressNow","url":"https://{DOMAIN}","description":"Free online image compression tool. Compress PNG, JPEG, WebP images to exact file sizes."}}</script>
    <script type="application/ld+json">{{"@context":"https://schema.org","@type":"WebApplication","name":"CompressNow","url":"https://{DOMAIN}","applicationCategory":"UtilityApplication","operatingSystem":"All","offers":{{"@type":"Offer","price":"0","priceCurrency":"USD"}}}}</script>
    <script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{{"@type":"Question","name":"How does CompressNow work?","acceptedAnswer":{{"@type":"Answer","text":"Upload your image, set your target file size, and our tool compresses it instantly. Everything happens in your browser — no upload to server."}}}},{{"@type":"Question","name":"Is CompressNow free?","acceptedAnswer":{{"@type":"Answer","text":"Yes, completely free. No signup, no watermarks, no limits. Compress as many images as you need."}}}},{{"@type":"Question","name":"What image formats are supported?","acceptedAnswer":{{"@type":"Answer","text":"PNG, JPEG, and WebP are fully supported. Our tool applies format-specific compression for optimal results."}}}},{{"@type":"Question","name":"Is my image uploaded to a server?","acceptedAnswer":{{"@type":"Answer","text":"No. All processing happens locally in your browser. Your images never leave your device, ensuring complete privacy."}}}}]}}</script>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-Z9NW1GSG04"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag("js",new Date());gtag("config","G-Z9NW1GSG04");</script>
    <style>
        :root{{--primary:#4F46E5;--primary-dark:#4338CA;--bg:#F8FAFC;--card-bg:#FFFFFF;--text:#1E293B;--text-secondary:#64748B;--border:#E2E8F0;--radius:12px}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:var(--bg);color:var(--text);line-height:1.6}}
.container{{max-width:960px;margin:0 auto;padding:0 24px}}
header{{background:#1E293B;color:#F1F5F9;padding:16px 0;box-shadow:0 2px 8px rgba(0,0,0,.15)}}
header .container{{display:flex;justify-content:space-between;align-items:center}}
header nav{{display:flex;gap:24px}}header nav a{{color:#94A3B8;text-decoration:none;font-size:.9rem;font-weight:500}}header nav a:hover{{color:#fff}}
.hero{{padding:60px 0 40px;text-align:center}}
.hero h1{{font-size:2.5rem;font-weight:800;margin-bottom:16px;line-height:1.2}}
.hero p{{color:var(--text-secondary);font-size:1.1rem;max-width:600px;margin:0 auto}}
.tool-area{{max-width:700px;margin:0 auto 40px;padding:0 24px}}
.tool-area textarea{{width:100%;border:2px dashed var(--border);border-radius:var(--radius);padding:20px;font-family:'Consolas',monospace;font-size:14px;resize:vertical;background:var(--card-bg);min-height:200px}}
.tool-area textarea:focus{{outline:none;border-color:var(--primary);border-style:solid}}
.btn-row{{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-bottom:24px}}
.btn{{padding:12px 28px;border:none;border-radius:8px;font-size:1rem;font-weight:600;cursor:pointer;font-family:inherit}}.btn:active{{transform:scale(.97)}}
.btn-primary{{background:var(--primary);color:#fff}}.btn-primary:hover{{background:var(--primary-dark)}}
.btn-secondary{{background:var(--card-bg);color:var(--text);border:1px solid var(--border)}}
.output-area{{margin-top:16px;background:var(--card-bg);border:1px solid var(--border);border-radius:var(--radius);padding:20px;min-height:80px;word-break:break-all;display:none}}
.error-msg{{color:#DC2626;font-size:.85rem;margin-top:8px;display:none}}
.section{{padding:40px 0}}.section h2{{font-size:1.5rem;margin-bottom:20px;text-align:center}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;max-width:700px;margin:0 auto}}
@media(max-width:640px){{.grid{{grid-template-columns:repeat(2,1fr)}}.hero h1{{font-size:1.8rem}}}}
.card{{padding:16px;background:var(--card-bg);border:1px solid var(--border);border-radius:8px;text-align:center;text-decoration:none;color:var(--text);font-weight:600;font-size:.9rem;transition:all .15s}}
.card:hover{{border-color:var(--primary);box-shadow:0 2px 8px rgba(79,70,229,0.12)}}
.faq-section{{padding:40px 0;text-align:left}}.faq-section h2{{font-size:1.5rem;margin-bottom:24px;text-align:center}}
.faq-item{{margin-bottom:20px}}.faq-item h3{{font-size:1rem;margin-bottom:6px;color:var(--primary)}}
.faq-item p{{color:var(--text-secondary);font-size:.9rem}}
.cross-site{{max-width:700px;margin:0 auto 40px;padding:20px;background:#F5F0FF;border-left:3px solid #4F46E5;border-radius:0 8px 8px 0}}
.cross-site strong{{color:#4F46E5}}.cross-site a{{color:#4F46E5;font-weight:600}}
footer{{background:#1E293B;color:#94A3B8;padding:32px 0;text-align:center;font-size:.85rem}}
footer a{{color:#CBD5E1;text-decoration:none}}
    </style>
</head>
<body>
    <header>
        <div class="container">
            <a href="/" class="logo">Compressnow</a>
            <nav>
                <a href="/">Home</a>
                <a href="#faq">FAQ</a>
                <a href="#sizes">Sizes</a>
            </nav>
        </div>
    </header>
    <main>
        <section class="hero">
            <h1>Compress Image to Exact KB Online</h1>
            <p>Free, no upload, 100% browser-based. Support PNG, JPEG, WebP. Compress to 100KB, 200KB, 500KB, or any size you need.</p>
        </section>
        <section class="tool-area">
            <div id="dropZone" style="border:2px dashed var(--border);border-radius:var(--radius);padding:40px 20px;text-align:center;cursor:pointer;background:var(--card-bg);transition:all .2s">
                <p style="font-size:2rem;margin-bottom:8px">📁</p>
                <p style="font-weight:600;margin-bottom:4px">Drop image here or click to upload</p>
                <p style="color:var(--text-secondary);font-size:.85rem">Supports PNG, JPEG, WebP</p>
                <input type="file" id="fileInput" accept="image/*" style="display:none">
            </div>
            <div id="previewArea" style="display:none;margin-top:20px">
                <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px">
                    <div style="text-align:center"><p style="font-size:.8rem;color:var(--text-secondary);margin-bottom:8px">Original</p><img id="originalPreview" style="max-width:100%;border-radius:8px;border:1px solid var(--border)"></div>
                    <div style="text-align:center"><p style="font-size:.8rem;color:var(--text-secondary);margin-bottom:8px">Compressed</p><img id="compressedPreview" style="max-width:100%;border-radius:8px;border:1px solid var(--border)"></div>
                </div>
                <div id="stats" style="background:var(--card-bg);border:1px solid var(--border);border-radius:8px;padding:16px;margin-bottom:16px;font-size:.9rem"></div>
                <div class="btn-row">
                    <button class="btn btn-primary" id="downloadBtn">⬇ Download Compressed</button>
                    <button class="btn btn-secondary" id="resetBtn">🔄 Compress Another</button>
                </div>
            </div>
            <div id="progressBar" style="display:none;margin-top:16px;background:var(--border);border-radius:8px;overflow:hidden;height:8px"><div id="progressFill" style="background:var(--primary);height:100%;width:0%;transition:width .3s"></div></div>
            <p class="error-msg" id="errorMsg"></p>
        </section>
        <section class="section" id="sizes">
            <h2>Compress by Target Size</h2>
            <div class="grid">{size_cards}</div>
        </section>
        <section class="section">
            <h2>Compress by Platform</h2>
            <div class="grid">{platform_cards}</div>
        </section>
        <section class="section">
            <h2>Convert Image Format</h2>
            <div class="grid">{conversion_cards}</div>
        </section>
        <div class="cross-site">
            <strong>Pro Tip</strong> — After compressing your image, use <a href="https://cvbuild-ai.com">CVBuild-AI</a> to build your resume, <a href="https://messagegen-ai.com">MessageGen-AI</a> to write professional emails, and <a href="https://tonemodifier.com">ToneModifier</a> to perfect your tone.
        </div>
        <section class="faq-section" id="faq">
            <div class="container">
                <h2>Frequently Asked Questions</h2>
                <div class="faq-item">
                    <h3>How does CompressNow work?</h3>
                    <p>Upload your image, set your target file size, and our tool compresses it instantly. Everything happens in your browser — no upload to server.</p>
                </div>
                <div class="faq-item">
                    <h3>Is CompressNow free?</h3>
                    <p>Yes, completely free. No signup, no watermarks, no limits. Compress as many images as you need.</p>
                </div>
                <div class="faq-item">
                    <h3>What image formats are supported?</h3>
                    <p>PNG, JPEG, and WebP are fully supported. Our tool applies format-specific compression for optimal results.</p>
                </div>
                <div class="faq-item">
                    <h3>Is my image uploaded to a server?</h3>
                    <p>No. All processing happens locally in your browser. Your images never leave your device, ensuring complete privacy.</p>
                </div>
            </div>
        </section>
    </main>
    <footer>
        <div class="container">
            <p>&copy; 2026 Compressnow. All rights reserved. | <a href="/">Home</a> | <a href="#faq">FAQ</a></p>
            <p style="margin-top:8px">All processing happens locally in your browser. Your data is never uploaded.</p>
        </div>
    </footer>
    <script>
    const IS_CONVERSION = {"true" if s.get("cat") == "conversion" else "false"};
    const TARGET_KB = {s.get('size', '100').replace(' KB','').replace(' MB','000')};
    const TARGET_BYTES = TARGET_KB * 1024;
    const CONVERT_TO = IS_CONVERSION ? '{s.get("slug","").split("-to-")[1] if "-to-" in s.get("slug","") else "png"}' : '';
    const dropZone = document.getElementById('dropZone');
    const fileInput = document.getElementById('fileInput');
    const previewArea = document.getElementById('previewArea');
    const originalPreview = document.getElementById('originalPreview');
    const compressedPreview = document.getElementById('compressedPreview');
    const stats = document.getElementById('stats');
    const downloadBtn = document.getElementById('downloadBtn');
    const resetBtn = document.getElementById('resetBtn');
    const progressBar = document.getElementById('progressBar');
    const progressFill = document.getElementById('progressFill');
    const errorMsg = document.getElementById('errorMsg');
    let resultBlob = null;
    let resultUrl = null;
    dropZone.addEventListener('click', () => fileInput.click());
    dropZone.addEventListener('dragover', e => {{ e.preventDefault(); dropZone.style.borderColor = 'var(--primary)'; dropZone.style.background = '#F5F3FF'; }});
    dropZone.addEventListener('dragleave', () => {{ dropZone.style.borderColor = 'var(--border)'; dropZone.style.background = 'var(--card-bg)'; }});
    dropZone.addEventListener('drop', e => {{ e.preventDefault(); dropZone.style.borderColor = 'var(--border)'; dropZone.style.background = 'var(--card-bg)'; if(e.dataTransfer.files.length) handleFile(e.dataTransfer.files[0]); }});
    fileInput.addEventListener('change', () => {{ if(fileInput.files.length) handleFile(fileInput.files[0]); }});
    resetBtn.addEventListener('click', () => {{ previewArea.style.display = 'none'; dropZone.style.display = 'block'; fileInput.value = ''; if(resultUrl) URL.revokeObjectURL(resultUrl); resultBlob = null; resultUrl = null; errorMsg.style.display = 'none'; }});
    downloadBtn.addEventListener('click', () => {{ if(!resultBlob) return; const a = document.createElement('a'); a.href = resultUrl; const ext = CONVERT_TO || 'jpg'; const name = fileInput.files[0].name.replace(/\.[^.]+$/, '') + '.' + ext; a.download = name; a.click(); }});
    function formatSize(bytes) {{ if(bytes < 1024) return bytes + ' B'; if(bytes < 1048576) return (bytes/1024).toFixed(1) + ' KB'; return (bytes/1048576).toFixed(2) + ' MB'; }}
    function handleFile(file) {{ if(!file.type.match(/^image\/(png|jpeg|webp)$/)) {{ errorMsg.textContent = 'Please upload a PNG, JPEG, or WebP image.'; errorMsg.style.display = 'block'; return; }} errorMsg.style.display = 'none'; const reader = new FileReader(); reader.onload = e => {{ const img = new Image(); img.onload = () => {{ originalPreview.src = e.target.result; dropZone.style.display = 'none'; previewArea.style.display = 'block'; progressBar.style.display = 'block'; progressFill.style.width = '30%'; if(IS_CONVERSION) convertImage(img); else compressImage(img, file.type); }}; img.src = e.target.result; }}; reader.readAsDataURL(file); }}
    function convertImage(img) {{ const canvas = document.createElement('canvas'); canvas.width = img.width; canvas.height = img.height; const ctx = canvas.getContext('2d'); ctx.drawImage(img, 0, 0); progressFill.style.width = '60%'; const mimeMap = {{'png':'image/png','jpg':'image/jpeg','jpeg':'image/jpeg','webp':'image/webp'}}; const mime = mimeMap[CONVERT_TO] || 'image/jpeg'; const quality = mime === 'image/png' ? undefined : 0.92; canvas.toBlob(blob => {{ resultBlob = blob; showResult(blob, img.width, img.height); }}, mime, quality); }}
    function compressImage(img, type) {{ const canvas = document.createElement('canvas'); canvas.width = img.width; canvas.height = img.height; const ctx = canvas.getContext('2d'); ctx.drawImage(img, 0, 0); progressFill.style.width = '60%'; const mimeType = type === 'image/png' ? 'image/png' : type === 'image/webp' ? 'image/webp' : 'image/jpeg'; if(mimeType === 'image/png') {{ canvas.toBlob(blob => {{ resultBlob = blob; showResult(blob, img.width, img.height); }}, mimeType); }} else {{ let low = 0.01, high = 1.0, bestBlob = null; function tryQuality(q) {{ canvas.toBlob(blob => {{ if(!blob) {{ showResult(bestBlob || new Blob(), img.width, img.height); return; }} if(blob.size <= TARGET_BYTES * 1.05) {{ bestBlob = blob; low = q; }} else {{ high = q; }} if(high - low < 0.01) {{ resultBlob = bestBlob || blob; showResult(resultBlob, img.width, img.height); }} else {{ progressFill.style.width = (60 + (1 - (high-low)) * 30) + '%'; tryQuality((low + high) / 2); }} }}, mimeType, q); }} tryQuality(0.7); }} }}
    function showResult(blob, w, h) {{ if(resultUrl) URL.revokeObjectURL(resultUrl); resultBlob = blob; resultUrl = URL.createObjectURL(blob); compressedPreview.src = resultUrl; progressFill.style.width = '100%'; setTimeout(() => progressBar.style.display = 'none', 500); const originalSize = fileInput.files[0].size; const resultSize = blob.size; const change = ((1 - resultSize/originalSize) * 100).toFixed(1); const label = IS_CONVERSION ? 'Converted' : 'Compressed'; stats.innerHTML = '<div style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px"><div><strong>Original:</strong> ' + formatSize(originalSize) + '</div><div><strong>' + label + ':</strong> ' + formatSize(resultSize) + '</div><div><strong>Change:</strong> ' + change + '%</div><div><strong>Dimensions:</strong> ' + w + ' x ' + h + '</div></div>'; }}
    </script>
</body>
</html>"""
    w("index.html", html)
    print("🏠 index.html")


# ═══ Build Sitemap ══════════════════════════════════

def build_sitemap():
    urls = [f"https://{DOMAIN}/"]
    for s in ALL_SCENARIOS:
        urls.append(f"https://{DOMAIN}/{s['slug']}/")
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        p = "1.0" if u == f"https://{DOMAIN}/" else "0.8"
        xml += f"  <url><loc>{u}</loc><priority>{p}</priority></url>\n"
    xml += "</urlset>"
    w("sitemap.xml", xml)
    print(f"📄 sitemap.xml ({len(urls)} URLs)")


# ═══ Build robots.txt ═══════════════════════════════

def build_robots():
    w("robots.txt", f"User-agent: *\nAllow: /\nSitemap: https://{DOMAIN}/sitemap.xml\n")
    print("🤖 robots.txt")


# ═══ Main ═══════════════════════════════════════════

if __name__ == "__main__":
    build_home()
    print(f"\n📄 {len(ALL_SCENARIOS)} Scenario Pages:")
    for s in ALL_SCENARIOS:
        w(f"{s['slug']}/index.html", build_scene_page(s))
        print(f"  📄 {s['slug']}/")
    build_sitemap()
    build_robots()
    print(f"\n✅ Build Complete — {1 + len(ALL_SCENARIOS) + 3} pages")
