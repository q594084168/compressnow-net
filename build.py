#!/usr/bin/env python3
"""CompressNow Build v2 — Pillar guides + stripped boilerplate + noindex low-value pages"""

import os, json
from datetime import datetime
os.chdir(os.path.dirname(os.path.abspath(__file__)))

DOMAIN = "compressnow.net"
OUTPUT = "."
TODAY = datetime.now().strftime("%Y-%m-%d")

def w(path, content):
    full = os.path.join(OUTPUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

# ═══ Page Definitions ═══════════════════════════════

SIZES = [
    {"slug":"compress-image-to-10kb","size":"10 KB","title":"Compress Image to 10KB Online — Free, No Upload | CompressNow","desc":"Compress any image to exactly 10KB. Perfect for tiny icons, avatars, and strict file size limits. 100% browser-based, no upload needed.","use_cases":"UK passport photo digital submission (10KB max). Favicon and browser tab icons. Email signature logos. Forum avatar size limits. Tiny embedded images for HTML emails.","format_tip":"At 10KB, JPEG quality drops to ~30-40 — acceptable for thumbnails but not detailed photos. PNG is usually too large at this size unless the image has very few colors. Use JPEG for photos, PNG only for simple icons with <16 colors."},
    {"slug":"compress-image-to-20kb","size":"20 KB","title":"Compress Image to 20KB Online — Free, No Upload | CompressNow","desc":"Compress any image to exactly 20KB. Great for form submissions and strict upload limits. 100% browser-based, no upload needed.","use_cases":"Online visa application photo uploads. Government form ID photos. School project submission portals. Forum and community site avatars.","format_tip":"20KB is enough for a clear 200×200 JPEG at quality ~50. PNG only works for very simple graphics at this size. Use JPEG for photos — you'll get much better visual quality than PNG at the same file size."},
    {"slug":"compress-image-to-30kb","size":"30 KB","title":"Compress Image to 30KB Online — Free, No Upload | CompressNow","desc":"Compress any image to exactly 30KB. Ideal for government forms and ID uploads. 100% browser-based, no upload needed.","use_cases":"Certain embassy visa photo requirements. Online exam registration photos. Membership card photo uploads. Small web badges and buttons.","format_tip":"At 30KB, a 300×300 JPEG at quality ~55 looks crisp on screen. If your image has text, bump to PNG — but only if the color count is under 64. Otherwise JPEG will look sharper at this file size."},
    {"slug":"compress-image-to-40kb","size":"40 KB","title":"Compress Image to 40KB Online — Free, No Upload | CompressNow","desc":"Compress any image to exactly 40KB. Perfect for application forms and profile photos. 100% browser-based, no upload needed.","use_cases":"Job application portal photo uploads. Dating app profile pictures (many cap at 50KB). Small product thumbnail images for marketplace listings.","format_tip":"40KB is the sweet spot for a 400×400 headshot — JPEG quality ~65, looks great on screen. WebP at 40KB would look even better (equivalent to JPEG quality ~80) but check if your target platform supports WebP."},
    {"slug":"compress-image-to-50kb","size":"50 KB","title":"Compress Image to 50KB Online — Free, No Upload | CompressNow","desc":"Compress any image to exactly 50KB. Great for email attachments and web thumbnails. 100% browser-based, no upload needed.","use_cases":"Email attachment thumbnails (keep total under limit). LinkedIn profile photo upload. eBay gallery images. WordPress thumbnail sizes. Internal wiki/documentation images.","format_tip":"50KB is enough for a sharp 500×500 JPEG at quality ~70. If you need transparency (logos, icons), use PNG with a reduced color palette — posterize to 128 colors first, then compress."},
    {"slug":"compress-image-to-60kb","size":"60 KB","title":"Compress Image to 60KB Online — Free, No Upload | CompressNow","desc":"Compress any image to exactly 60KB. Ideal for resume photos and job applications. 100% browser-based, no upload needed.","use_cases":"Resume/CV photo attachments. Job board profile pictures. Online portfolio thumbnail images. E-commerce product gallery thumbnails.","format_tip":"60KB = 500×500 JPEG quality ~75 — near indistinguishable from original on screen. If the image is mostly solid colors (screenshots, diagrams), PNG may actually be smaller than JPEG at equivalent quality."},
    {"slug":"compress-image-to-75kb","size":"75 KB","title":"Compress Image to 75KB Online — Free, No Upload | CompressNow","desc":"Compress any image to exactly 75KB. Perfect for social media profiles and CMS uploads. 100% browser-based, no upload needed.","use_cases":"Social media profile pictures (Facebook, Twitter, Instagram). CMS user avatar uploads. Blog author bio photos. Online course platform profile images.","format_tip":"75KB at 600×600 JPEG quality ~80 = social-media ready. Consider WebP for the same visual quality at ~50KB — a 33% saving. Most modern CMS platforms (WordPress 5.8+, Shopify) support WebP."},
    {"slug":"compress-image-to-80kb","size":"80 KB","title":"Compress Image to 80KB Online — Free, No Upload | CompressNow","desc":"Compress any image to exactly 80KB. Great for blog headers and article images. 100% browser-based, no upload needed.","use_cases":"Blog post featured images. Article inline illustrations. Newsletter header graphics. Documentation screenshots.","format_tip":"80KB JPEG at 800px wide quality ~75 is the standard for blog images. If your image is a screenshot with text, PNG often produces a smaller file — screenshots compress exceptionally well with PNG's lossless algorithm."},
    {"slug":"compress-image-to-100kb","size":"100 KB","title":"100KB Image Compressor — Reduce to Exactly 100KB, Free & Instant | CompressNow","desc":"Compress any image to exactly 100KB. The most popular target size for web and email. 100% browser-based, no upload needed.","use_cases":"Most common web image target. Passport/visa photo upper limit for many countries. Product image for e-commerce (Amazon, Shopify recommend under 1MB but 100KB loads much faster). Blog post featured image. Email newsletter hero image.","format_tip":"100KB at 800×600 JPEG quality ~85 looks nearly identical to the original. If converting from PNG to JPEG at 100KB, you'll see a dramatic size reduction with minimal quality loss — PNG originals are often 500KB-2MB for the same image."},
    {"slug":"compress-image-to-150kb","size":"150 KB","title":"Compress Image to 150KB Online — Free, No Upload | CompressNow","desc":"Compress any image to exactly 150KB. Great for high-quality web images. 100% browser-based, no upload needed.","use_cases":"Higher-quality blog images. Portfolio website photos. Real estate listing photos. Restaurant menu images. Online store category banners.","format_tip":"150KB at 1000px wide JPEG quality ~85 — excellent for photography portfolios. WebP at the same file size gives quality equivalent to JPEG ~95. For images with gradients (skies, skin tones), JPEG at 150KB is nearly perfect."},
    {"slug":"compress-image-to-200kb","size":"200 KB","title":"Compress Image to 200KB Online — Free, No Upload | CompressNow","desc":"Compress any image to exactly 200KB. Perfect for product photos and portfolios. 100% browser-based, no upload needed.","use_cases":"E-commerce product photos (zoom-ready quality). Photography portfolio images. Instagram post uploads (pre-compress for quality control). Digital art commission deliveries.","format_tip":"200KB JPEG at 1200px quality ~90 is print-ready for web use. Google's PageSpeed Insights recommends images under 200KB for optimal LCP scores. This is the best balance of quality and performance for most web images."},
    {"slug":"compress-image-to-250kb","size":"250 KB","title":"Compress Image to 250KB Online — Free, No Upload | CompressNow","desc":"Compress any image to exactly 250KB. Ideal for detailed images with good quality. 100% browser-based, no upload needed.","use_cases":"High-detail product images (jewelry, textiles). Architecture and interior design photos. Travel blog full-width images. Online magazine illustrations.","format_tip":"250KB at 1600px wide JPEG quality ~85 — excellent for retina displays. At this size, the difference between JPEG and WebP narrows; both look great. Choose JPEG for universal compatibility, WebP if your CDN supports it."},
    {"slug":"compress-image-to-300kb","size":"300 KB","title":"Compress Image to 300KB Online — Free, No Upload | CompressNow","desc":"Compress any image to exactly 300KB. Great for presentations and documents. 100% browser-based, no upload needed.","use_cases":"PowerPoint/Keynote presentation images. PDF report embedded images. Digital document attachments. High-quality social media ads.","format_tip":"300KB JPEG at 2000px wide quality ~85 — suitable for most presentation screens. If embedding in a PDF, JPEG is preferred over PNG — PDF readers handle JPEG streams more efficiently, resulting in a smaller final document."},
    {"slug":"compress-image-to-400kb","size":"400 KB","title":"Compress Image to 400KB Online — Free, No Upload | CompressNow","desc":"Compress any image to exactly 400KB. Perfect for high-res web images. 100% browser-based, no upload needed.","use_cases":"Website hero banners. Full-width background images. High-resolution marketing materials. Print-on-demand product mockups.","format_tip":"400KB JPEG at 2000px wide quality ~90 — near-lossless for web viewing. For hero banners, consider using WebP with lossy compression at this size — you'll get 30% smaller files with no visible difference on screen."},
    {"slug":"compress-image-to-500kb","size":"500 KB","title":"Compress Image to 500KB Online — Free, No Upload | CompressNow","desc":"Compress any image to exactly 500KB. Great for detailed photos and prints. 100% browser-based, no upload needed.","use_cases":"Print-quality photos for online submission. High-res marketing assets. Magazine-quality digital images. Fine art reproduction for web galleries.","format_tip":"500KB JPEG at 2500px wide quality ~90 — good enough for 8×10\" prints at 250 DPI. For true print quality, consider TIFF or maximum-quality JPEG (2-5MB) instead. 500KB is the upper limit of what's practical for web delivery."},
    {"slug":"compress-image-to-1mb","size":"1 MB","title":"Compress Image to 1MB Online — Free, No Upload | CompressNow","desc":"Compress any image to exactly 1MB. Perfect for email limits and web uploads. 100% browser-based, no upload needed.","use_cases":"Email attachment limit for most providers (Gmail: 25MB total, keep individual images small). High-res social media uploads. Digital photo frame images. Cloud storage optimization.","format_tip":"1MB JPEG at 4000px wide quality ~85 — suitable for 4K displays. Most email providers cap individual attachments; 1MB per image lets you attach 20-25 photos in one email. For cloud storage, switching from PNG to JPEG at 1MB can save 80%+ space."},
    {"slug":"compress-image-to-2mb","size":"2 MB","title":"Compress Image to 2MB Online — Free, No Upload | CompressNow","desc":"Compress any image to exactly 2MB. Great for document uploads and portfolios. 100% browser-based, no upload needed.","use_cases":"Portfolio submissions with file size caps. PDF attachments with embedded images. Competition entry photo uploads. Archive-quality web images.","format_tip":"2MB is typically the max individual file size for many upload portals. JPEG at this size is near-lossless for most purposes. If your original is a 20MB TIFF or RAW, 2MB JPEG at quality ~92 preserves virtually all visible detail."},
    {"slug":"compress-image-to-5mb","size":"5 MB","title":"Compress Image to 5MB Online — Free, No Upload | CompressNow","desc":"Compress any image to exactly 5MB. Perfect for high-quality prints and archives. 100% browser-based, no upload needed.","use_cases":"High-quality print submission. Archive-quality digital preservation. Twitter/X image uploads (5MB limit). Professional photography delivery.","format_tip":"5MB JPEG at maximum resolution quality ~95 preserves 99%+ of visible detail. This is the upper limit for Twitter/X image uploads. If archiving, consider keeping the original RAW/TIFF and using this as the web-delivery version."},
]

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

FORMATS = [
    {"slug":"compress-png","format":"PNG","title":"PNG Compress — Reduce PNG Size Online Free | CompressNow","desc":"PNG compress online — reduce PNG file size without losing quality. Free, browser-based, instant. No upload needed."},
    {"slug":"compress-jpeg-without-losing-quality","format":"JPEG","title":"Compress JPEG Without Losing Quality — Free Online Tool","desc":"Compress JPEG photos while preserving quality. Smart compression for photos and images. Free, browser-based, instant."},
    {"slug":"compress-webp","format":"WebP","title":"Compress WebP Online — Reduce WebP File Size Free","desc":"Compress WebP images online. Reduce file size for faster web loading. Free, no upload, instant."},
    {"slug":"compress-icon-logo","format":"Icon/Logo","title":"Compress Icons & Logos Under 50KB — Free, No Quality Loss | CompressNow","desc":"Compress icons, logos, and favicons to tiny file sizes. Perfect for websites and apps. Free, browser-based."},
    {"slug":"compress-passport-photo","format":"Passport Photo","title":"Compress Passport Photo — Meet Size Requirements Free","desc":"Compress passport photos to meet government size requirements (10KB-100KB). Free, no upload, instant."},
    {"slug":"compress-screenshot","format":"Screenshot","title":"Compress Screenshot — Reduce Screenshot File Size Free","desc":"Compress screenshots for sharing and documentation. Reduce file size instantly. Free, browser-based, instant."},
    {"slug":"compress-scanned-document","format":"Scanned Document","title":"Compress Scanned Document — Reduce PDF/Image Size Free","desc":"Compress scanned documents for email and upload. Reduce file size while keeping text readable. Free, instant."},
    {"slug":"compress-signature-image","format":"Signature","title":"Compress Signature Image — Reduce to Under 50KB Free","desc":"Compress signature images for forms and documents. Meet strict file size limits. Free, no upload, instant."},
]

# === High-value special pages (keep, index) ===
SPECIAL = [
    {"slug":"bulk-image-compressor","title":"Bulk Compress Up to 20 Images — Fast, Free, No Quality Loss | CompressNow","desc":"Compress multiple images at once. Batch compression for PNG, JPEG, WebP. Free, browser-based, no upload needed."},
    {"slug":"compress-image-to-exact-kb","title":"Compress Image to Exact KB — Precise File Size Control","desc":"Compress images to any exact file size in KB. Precise control over output size. Free, browser-based, instant."},
    {"slug":"compress-image-under-50kb","title":"Compress Image Under 50KB — Ultra-Small File Size Free","desc":"Compress images to under 50KB. Perfect for forms, avatars, and strict limits. Free, no upload, instant."},
    {"slug":"reduce-image-size-for-upload","title":"Reduce Image Size for Upload — Meet File Size Limits","desc":"Reduce image file size to meet upload requirements. Works for any platform. Free, browser-based, instant."},
    {"slug":"compress-image-for-amazon-product-listing","title":"Compress Image for Amazon — Optimize Product Photos Free","desc":"Compress product images for Amazon listings. Meet Amazon's file size requirements. Free, browser-based, instant."},
    {"slug":"compress-image-for-ebay-listing","title":"Compress Image for eBay — Optimize Listing Photos","desc":"Compress product photos for eBay listings. Meet eBay's image requirements. Free, browser-based, instant."},
    {"slug":"compress-image-for-etsy-product-photo","title":"Compress Image for Etsy — Optimize Shop Photos","desc":"Compress product photos for Etsy listings. Meet Etsy's image requirements. Free, browser-based, instant."},
    {"slug":"compress-image-for-youtube-thumbnail","title":"Compress Image for YouTube Thumbnail — Optimize Thumbnails","desc":"Compress YouTube thumbnail images. Meet YouTube's requirements. Free, browser-based, instant."},
    {"slug":"compress-image-for-seo","title":"Compress Image for SEO — Improve Core Web Vitals","desc":"Compress images to improve SEO rankings. Faster page load, better Core Web Vitals. Free, instant."},
    {"slug":"compress-images-for-web","title":"Compress Images for Web — Optimize All Website Images","desc":"Batch compress images for web use. Improve page speed and SEO. Free, browser-based, instant."},
    {"slug":"compress-image-without-losing-quality","title":"Compress Image Without Losing Quality — Free Online Tool","desc":"Compress images while preserving visual quality. Smart compression algorithm. Free, browser-based, instant."},
    {"slug":"compressnow-vs-tinypng","title":"CompressNow vs TinyPNG — Which Is Better for You?","desc":"Compare CompressNow and TinyPNG. See which image compression tool fits your needs. Free comparison guide."},
]

# === Low-value long-tail pages (noindex) ===
# These are redundant keyword variants that compete with primary pages.
# Keep them accessible (they may have backlinks) but tell Google not to index.
NOINDEX_PAGES = [
    {"slug":"compress-photo-to-20kb","size":"20 KB","cat":"size"},
    {"slug":"compress-photo-to-50kb","size":"50 KB","cat":"size"},
    {"slug":"compress-photo-to-100kb","size":"100 KB","cat":"size"},
    {"slug":"compress-photo-to-200kb","size":"200 KB","cat":"size"},
    {"slug":"compress-photo-to-500kb","size":"500 KB","cat":"size"},
    {"slug":"image-compressor-to-100kb","size":"100 KB","cat":"size"},
    {"slug":"image-compressor-to-200kb","size":"200 KB","cat":"size"},
    {"slug":"image-compressor-to-500kb","size":"500 KB","cat":"size"},
    {"slug":"reduce-image-size-to-100kb","size":"100 KB","cat":"size"},
    {"slug":"convert-image-to-100kb","size":"100 KB","cat":"size"},
    # Redundant platform variants
    {"slug":"discord-image-compressor","cat":"platform"},
    {"slug":"discord-image-size-reducer","cat":"platform"},
    {"slug":"reduce-image-size-for-discord","cat":"platform"},
    {"slug":"compress-photo-for-discord","cat":"platform"},
    {"slug":"compress-jpg-for-discord","cat":"platform"},
    {"slug":"discord-avatar-size-reducer","cat":"platform"},
    {"slug":"discord-banner-image-compressor","cat":"platform"},
    {"slug":"discord-profile-image-compressor","cat":"platform"},
    {"slug":"whatsapp-image-compressor","cat":"platform"},
    {"slug":"whatsapp-image-optimizer","cat":"platform"},
    {"slug":"whatsapp-image-size-reducer","cat":"platform"},
    {"slug":"whatsapp-photo-size-reducer","cat":"platform"},
    {"slug":"whatsapp-profile-photo-compressor","cat":"platform"},
    {"slug":"whatsapp-dp-photo-compressor","cat":"platform"},
    {"slug":"compress-photo-for-whatsapp","cat":"platform"},
    {"slug":"compress-jpg-for-whatsapp","cat":"platform"},
    {"slug":"compress-png-for-whatsapp","cat":"platform"},
    {"slug":"reduce-image-size-for-whatsapp","cat":"platform"},
    {"slug":"email-image-optimizer","cat":"platform"},
    {"slug":"email-attachment-image-compressor","cat":"platform"},
    {"slug":"email-photo-size-reducer","cat":"platform"},
    {"slug":"compress-photo-for-email","cat":"platform"},
    {"slug":"compress-jpg-for-email","cat":"platform"},
    {"slug":"compress-png-for-email","cat":"platform"},
    {"slug":"reduce-image-size-for-email","cat":"platform"},
    {"slug":"instagram-image-size-reducer","cat":"platform"},
    {"slug":"optimize-image-for-instagram","cat":"platform"},
    {"slug":"compress-image-for-twitter-profile","cat":"platform"},
    {"slug":"compress-image-for-twitter-timeline-post","cat":"platform"},
    {"slug":"compress-image-for-linkedin-profile","cat":"platform"},
    {"slug":"compress-image-for-website-hero-banner","cat":"platform"},
    {"slug":"compress-image-for-website-thumbnail","cat":"platform"},
    {"slug":"compress-image-for-wordpress-media-library","cat":"platform"},
    {"slug":"compress-image-for-google-business-profile-listing","cat":"platform"},
    {"slug":"compress-image-for-google-drive-sharing","cat":"platform"},
    {"slug":"compress-image-for-google-forms","cat":"platform"},
    {"slug":"compress-image-for-pinterest-pin","cat":"platform"},
    {"slug":"compress-image-for-telegram-sticker","cat":"platform"},
    {"slug":"compress-image-for-real-estate-listing","cat":"platform"},
    {"slug":"compress-image-for-ecommerce-product-catalog","cat":"platform"},
    {"slug":"compress-image-for-online-marketplace-listing","cat":"platform"},
    {"slug":"compress-image-for-online-portfolio","cat":"platform"},
    {"slug":"compress-image-for-online-portfolio-gallery","cat":"platform"},
    {"slug":"compress-image-for-blog-featured-image","cat":"platform"},
    {"slug":"compress-image-for-blog-post-inline-image","cat":"platform"},
    {"slug":"compress-image-for-social-media-story","cat":"platform"},
    {"slug":"compress-image-for-newsletter-header","cat":"platform"},
    {"slug":"compress-image-for-email-marketing-campaign","cat":"platform"},
    {"slug":"compress-image-for-email-signature","cat":"platform"},
    {"slug":"compress-image-for-powerpoint-presentation","cat":"platform"},
    {"slug":"compress-image-for-pdf-attachment","cat":"platform"},
    {"slug":"compress-image-for-mobile-app-icon","cat":"platform"},
    {"slug":"compress-image-for-online-class-submission","cat":"platform"},
    {"slug":"compress-image-for-online-course-platform","cat":"platform"},
    {"slug":"compress-image-for-school-project-submission","cat":"platform"},
    {"slug":"compress-image-for-university-application","cat":"platform"},
    {"slug":"compress-image-for-resume-attachment","cat":"platform"},
    {"slug":"compress-image-for-avatar-profile-picture","cat":"platform"},
    {"slug":"compress-image-for-dating-app-profile","cat":"platform"},
    {"slug":"compress-image-for-travel-blog","cat":"platform"},
    {"slug":"compress-image-for-event-flyer","cat":"platform"},
    {"slug":"compress-image-for-print-flyer","cat":"platform"},
    {"slug":"compress-image-for-craigslist-ad","cat":"platform"},
    {"slug":"compress-image-for-reddit-post","cat":"platform"},
    {"slug":"compress-image-for-digital-art-commission","cat":"platform"},
    {"slug":"compress-image-for-medical-report","cat":"platform"},
    {"slug":"compress-image-for-google-ads-display","cat":"platform"},
    # Passport/visa variants (keep the primary FORMAT page, noindex these)
    {"slug":"compress-passport-photo-to-20kb","size":"20 KB","cat":"size"},
    {"slug":"compress-passport-photo-to-50kb","size":"50 KB","cat":"size"},
    {"slug":"compress-passport-photo-to-100kb","size":"100 KB","cat":"size"},
    {"slug":"passport-photo-compressor","cat":"platform"},
    {"slug":"compress-image-for-visa-application","cat":"platform"},
    {"slug":"compress-photo-for-visa","cat":"platform"},
    {"slug":"compress-image-for-immigration-form","cat":"platform"},
    {"slug":"photo-compressor-for-government-form","cat":"platform"},
    {"slug":"reduce-passport-photo-size","cat":"platform"},
    {"slug":"compress-image-for-online-application","cat":"platform"},
    {"slug":"compress-image-for-embassy-application","cat":"platform"},
    {"slug":"compress-image-for-id-card","cat":"platform"},
    {"slug":"compress-photo-for-id-card","cat":"platform"},
    {"slug":"resize-passport-photo-online","cat":"platform"},
    {"slug":"passport-image-size-reducer","cat":"platform"},
    {"slug":"compress-image-for-citizenship-application","cat":"platform"},
    {"slug":"compress-image-for-government-upload","cat":"platform"},
    {"slug":"passport-photo-under-100kb","size":"100 KB","cat":"size"},
    {"slug":"passport-photo-under-50kb","size":"50 KB","cat":"size"},
    # eCommerce variants
    {"slug":"shopify-image-compressor","cat":"platform"},
    {"slug":"ebay-photo-compressor","cat":"platform"},
    {"slug":"etsy-image-size-reducer","cat":"platform"},
    {"slug":"amazon-image-optimizer","cat":"platform"},
    {"slug":"product-image-compressor","cat":"platform"},
    {"slug":"product-photo-size-reducer","cat":"platform"},
    {"slug":"compress-product-photos","cat":"platform"},
    {"slug":"reduce-product-image-size","cat":"platform"},
    {"slug":"optimize-website-images","cat":"platform"},
    {"slug":"website-image-compressor","cat":"platform"},
    {"slug":"website-performance-image-compressor","cat":"platform"},
    {"slug":"website-speed-image-compressor","cat":"platform"},
    {"slug":"image-optimization-for-website","cat":"platform"},
    {"slug":"social-media-image-compressor","cat":"platform"},
    # AI variants (keep only the primary SPECIAL AI pages)
    {"slug":"compress-image-for-chatgpt","cat":"platform"},
    {"slug":"compress-image-for-claude","cat":"platform"},
    {"slug":"compress-image-for-gemini","cat":"platform"},
    {"slug":"compress-image-for-midjourney","cat":"platform"},
    {"slug":"compress-image-for-stable-diffusion","cat":"platform"},
    {"slug":"compress-image-for-ai-training","cat":"platform"},
    {"slug":"compress-image-for-ai-upload","cat":"platform"},
    {"slug":"compress-image-for-machine-learning","cat":"platform"},
    {"slug":"compress-image-for-multimodal-ai","cat":"platform"},
    {"slug":"compress-image-for-vision-models","cat":"platform"},
    {"slug":"ai-image-size-reducer","cat":"platform"},
    {"slug":"ai-image-upload-compressor","cat":"platform"},
    {"slug":"image-compressor-for-ai-tools","cat":"platform"},
    {"slug":"image-optimizer-for-ai","cat":"platform"},
    {"slug":"reduce-image-size-for-ai","cat":"platform"},
    {"slug":"reduce-image-size-for-ai-processing","cat":"platform"},
    {"slug":"compress-image-before-ai-upload","cat":"platform"},
    # JPEG/PNG/WEBP redundant variants
    {"slug":"compress-jpg-for-website","cat":"platform"},
    {"slug":"compress-png-for-website","cat":"platform"},
    {"slug":"compress-jpg-for-email","cat":"platform"},
    {"slug":"compress-jpg-for-whatsapp","cat":"platform"},
    # Other redundant variants
    {"slug":"compress-cover-photo","cat":"platform"},
    {"slug":"compress-hero-image","cat":"platform"},
    {"slug":"compress-image-for-online-store","cat":"platform"},
    {"slug":"compress-image-for-printing","cat":"platform"},  # duplicate of PLATFORMS entry
    {"slug":"compress-images-for-ecommerce","cat":"platform"},
    {"slug":"compress-listing-images","cat":"platform"},
    {"slug":"compress-profile-photo","cat":"platform"},
    {"slug":"optimize-ecommerce-images","cat":"platform"},
    {"slug":"web-image-optimizer","cat":"platform"},
    {"slug":"reduce-attachment-size","cat":"platform"},
    {"slug":"image-attachment-compressor","cat":"platform"},
    {"slug":"image-optimizer-online","cat":"platform"},
    {"slug":"compress-images-before-emailing","cat":"platform"},
    {"slug":"compress-blog-images","cat":"platform"},
    {"slug":"compress-catalog-images","cat":"platform"},
    {"slug":"compress-dataset-images","cat":"platform"},
    {"slug":"image-reducer-for-email","cat":"platform"},
    {"slug":"photo-compressor-for-email","cat":"platform"},
    {"slug":"resize-image-for-email","cat":"platform"},
    {"slug":"resize-image-for-instagram","cat":"platform"},
    {"slug":"resize-image-for-whatsapp","cat":"platform"},
    {"slug":"compress-image-under-1mb","cat":"special"},
    {"slug":"compress-image-under-200kb","cat":"special"},
    {"slug":"compress-image-under-500kb","cat":"special"},
    {"slug":"compress-image","cat":"special"},
]

# Keep these NOINDEX pages accessible (some may have backlinks) but with noindex meta
# Add title/desc from existing definitions where available

# Simplified: we'll build noindex pages with a stripped template

CONVERSIONS = [
    {"slug":"jpg-to-png","title":"Convert JPG to PNG Online — Free, Instant","desc":"Convert JPG/JPEG images to PNG format online. Preserve quality with lossless conversion. Free, browser-based, no upload."},
    {"slug":"png-to-jpg","title":"Convert PNG to JPG Online — Free, Instant","desc":"Convert PNG images to JPG/JPEG format online. Reduce file size significantly. Free, browser-based, no upload."},
    {"slug":"webp-to-jpg","title":"Convert WebP to JPG Online — Free, Instant","desc":"Convert WebP images to JPG/JPEG format. Universal compatibility. Free, browser-based, no upload needed."},
    {"slug":"webp-to-png","title":"Convert WebP to PNG Online — Free, Instant","desc":"Convert WebP images to PNG format with transparency preserved. Free, browser-based, no upload needed."},
    {"slug":"jpg-to-webp","title":"Convert JPG to WebP Online — Free, Instant","desc":"Convert JPG images to WebP format for smaller file sizes. Modern web format. Free, browser-based, no upload."},
    {"slug":"png-to-webp","title":"Convert PNG to WebP Online — Free, Instant","desc":"Convert PNG images to WebP format. 25-35% smaller than PNG. Free, browser-based, no upload needed."},
    {"slug":"heic-to-jpg","title":"Convert HEIC to JPG Online — Free, Instant","desc":"Convert HEIC (iPhone) photos to JPG format. Universal compatibility. Free, browser-based, no upload."},
    {"slug":"heic-to-png","title":"Convert HEIC to PNG Online — Free, Instant","desc":"Convert HEIC (iPhone) photos to PNG format. Lossless conversion. Free, browser-based, no upload."},
    {"slug":"avif-to-jpg","title":"Convert AVIF to JPG Online — Free, Instant","desc":"Convert AVIF images to JPG format. Universal compatibility. Free, browser-based, no upload."},
    {"slug":"avif-to-png","title":"Convert AVIF to PNG Online — Free, Instant","desc":"Convert AVIF images to PNG format with transparency. Free, browser-based, no upload."},
    {"slug":"free-image-converter","title":"Free Image Converter — JPG, PNG, WebP, HEIC Online","desc":"Convert between all major image formats. JPG, PNG, WebP, HEIC, AVIF. Free, browser-based, no upload."},
    {"slug":"convert-photo-format","title":"Convert Photo Format Online — Free Image Converter","desc":"Convert photos between JPG, PNG, WebP, and more. Free, browser-based, no upload needed."},
    {"slug":"image-file-converter","title":"Image File Converter — Free Online Format Conversion","desc":"Convert image files between formats. JPG, PNG, WebP, HEIC. Free, browser-based, instant."},
    {"slug":"image-format-converter","title":"Image Format Converter — Free Online Tool","desc":"Convert images between all major formats. Free, browser-based, instant conversion."},
    {"slug":"jpg-converter-online","title":"JPG Converter Online — Free Image Conversion Tool","desc":"Convert images to and from JPG format. Free, browser-based, instant conversion."},
    {"slug":"png-converter-online","title":"PNG Converter Online — Free Image Conversion Tool","desc":"Convert images to and from PNG format. Free, browser-based, instant conversion."},
    {"slug":"webp-converter-online","title":"WebP Converter Online — Free Image Conversion Tool","desc":"Convert images to and from WebP format. Free, browser-based, instant conversion."},
]

# ═══ Assemble ALL_SCENARIOS ════════════════════════

ALL_SCENARIOS = []
SEEN_SLUGS = set()

def add_scenario(s):
    if s["slug"] not in SEEN_SLUGS:
        SEEN_SLUGS.add(s["slug"])
        ALL_SCENARIOS.append(s)

for s in SIZES:
    s["cat"] = "size"
    add_scenario(s)
for s in PLATFORMS:
    s["cat"] = "platform"
    add_scenario(s)
for s in FORMATS:
    s["cat"] = "format"
    add_scenario(s)
for s in SPECIAL:
    s["cat"] = "special"
    add_scenario(s)
for s in CONVERSIONS:
    s["cat"] = "conversion"
    add_scenario(s)

# De-duplicate NOINDEX against ALL_SCENARIOS
NOINDEX_FINAL = []
for s in NOINDEX_PAGES:
    if s["slug"] not in SEEN_SLUGS:
        NOINDEX_FINAL.append(s)

print(f"[OK] Indexed pages: {len(ALL_SCENARIOS)} | Noindex pages: {len(NOINDEX_FINAL)}")

# ═══ Platform-specific enrichment ══════════════════

PLATFORM_DATA = {
    "discord": {
        "name": "Discord", "limit": "8MB (free) / 25MB (Nitro)", "formats": "PNG, JPG, GIF, WebP",
        "faq": [
            ("What's Discord's image upload limit?", "Free users: 8MB per file. Nitro Basic: 50MB. Nitro: 500MB."),
            ("Will my images look blurry after compression?", "Our smart compression algorithm reduces file size while preserving clarity. For screenshots and photos, the difference is nearly invisible."),
            ("Can I compress animated GIFs for Discord?", "Yes. Upload a GIF and the tool compresses it while preserving animation."),
        ],
        "tips": "Discord supports PNG, JPG, GIF, and WebP. If your screenshot is over 8MB, use JPG compression for the smallest file size.",
    },
    "whatsapp": {
        "name": "WhatsApp", "limit": "16MB", "formats": "JPG, PNG, GIF",
        "faq": [
            ("What's WhatsApp's image size limit?", "WhatsApp limits individual file sharing to 16MB."),
            ("How do I send HD photos without compression?", "Choose 'Send as Document' to preserve original quality — but the file must still be under 16MB."),
        ],
        "tips": "WhatsApp auto-compresses large images, often degrading quality. Pre-compress with our tool instead — you control the quality.",
    },
    "email": {
        "name": "Email", "limit": "25MB (Gmail) / 20MB (Outlook)", "formats": "JPG, PNG, GIF, BMP",
        "faq": [
            ("What's the email attachment size limit?", "Gmail: 25MB. Outlook: 20MB. Yahoo: 25MB."),
            ("Can I compress multiple images for one email?", "Yes. Upload multiple images and the tool compresses them one by one."),
        ],
        "tips": "Gmail caps attachments at 25MB. To send 10-20 images in one email, compress each to 200KB-500KB.",
    },
    "instagram": {
        "name": "Instagram", "limit": "30MB (photos)", "formats": "JPG, PNG",
        "faq": [
            ("What are the best image dimensions for Instagram?", "Square: 1080x1080px. Portrait: 1080x1350px. Landscape: 1080x566px."),
            ("Does Instagram compress uploaded images?", "Yes, Instagram auto-compresses all uploads. Pre-compressing lets you control quality."),
        ],
        "tips": "Instagram recommends 1080px width. Pre-compress to under 1MB for the best quality-to-size ratio.",
    },
    "facebook": {
        "name": "Facebook", "limit": "10MB (photos)", "formats": "JPG, PNG, GIF, BMP",
        "faq": [
            ("What's Facebook's image size limit?", "Photos: 10MB. File sharing: 25MB."),
        ],
        "tips": "Facebook recommends 2048px width. Compress to under 1MB for fast uploads with great display quality.",
    },
    "twitter": {
        "name": "Twitter/X", "limit": "5MB (images) / 15MB (GIF)", "formats": "JPG, PNG, GIF, WebP",
        "faq": [
            ("What's Twitter's image size limit?", "Images: 5MB. GIFs: 15MB."),
        ],
        "tips": "Twitter recommends 16:9 or 1:1 aspect ratio. PNG preserves more detail; JPG is smaller.",
    },
    "linkedin": {
        "name": "LinkedIn", "limit": "10MB (photos)", "formats": "JPG, PNG, GIF",
        "faq": [
            ("What size should my LinkedIn profile photo be?", "Recommended: 400x400px. Minimum: 200x200px."),
        ],
        "tips": "LinkedIn is a professional platform — your headshot quality matters. Compress to under 500KB while keeping it crisp.",
    },
    "pinterest": {
        "name": "Pinterest", "limit": "20MB", "formats": "JPG, PNG, GIF",
        "faq": [
            ("What's the best image size for Pinterest?", "Use a 2:3 aspect ratio, with a recommended width of 1000px."),
        ],
        "tips": "Pinterest recommends vertical images (2:3 ratio). Compress to under 1MB for best results.",
    },
    "tiktok": {
        "name": "TikTok", "limit": "2MB (avatar) / 10MB (video cover)", "formats": "JPG, PNG",
        "faq": [
            ("What size should a TikTok avatar be?", "Recommended: 200x200px, under 2MB."),
        ],
        "tips": "TikTok is a vertical-first platform — use 9:16 aspect ratio images.",
    },
    "youtube": {
        "name": "YouTube", "limit": "2MB (thumbnail) / 6MB (channel icon)", "formats": "JPG, PNG, GIF, BMP",
        "faq": [
            ("What size should YouTube thumbnails be?", "Recommended: 1280x720px, minimum width 640px."),
        ],
        "tips": "YouTube thumbnails significantly impact CTR. Use 1280x720px JPG, keeping files under 1MB.",
    },
    "website": {
        "name": "Website", "limit": "Recommend <200KB per image", "formats": "JPG, PNG, WebP, GIF, SVG",
        "faq": [
            ("How large should website images be?", "Google recommends under 200KB per image. Hero images can go up to 500KB."),
            ("Does image size affect SEO?", "Yes. Large images slow down page loads, hurting Google rankings."),
        ],
        "tips": "Use WebP format, keep images under 200KB, and implement lazy loading for best Core Web Vitals.",
    },
    "wordpress": {
        "name": "WordPress", "limit": "Depends on host (usually 2-10MB)", "formats": "JPG, PNG, GIF, WebP, SVG",
        "faq": [
            ("Does WordPress auto-compress images?", "Yes, WordPress generates multiple thumbnail sizes. But the original upload is not compressed."),
        ],
        "tips": "WordPress recommends images no wider than 2048px. WebP format offers better compression.",
    },
    "shopify": {
        "name": "Shopify", "limit": "20MB", "formats": "JPG, PNG, GIF, WebP",
        "faq": [
            ("What size should Shopify product images be?", "Recommended: 2048x2048px, square aspect ratio."),
        ],
        "tips": "Shopify recommends square product images at 2048x2048px. Compress to under 200KB for faster page loads.",
    },
    "amazon": {
        "name": "Amazon", "limit": "10MB", "formats": "JPG, PNG, GIF",
        "faq": [
            ("What size should Amazon product images be?", "Main image: minimum 1000x1000px, recommended 2000x2000px."),
        ],
        "tips": "Amazon requires pure white background. Use 2000x2000px JPG, keeping files under 1MB.",
    },
    "ebay": {
        "name": "eBay", "limit": "7MB", "formats": "JPG, PNG, GIF, BMP",
        "faq": [
            ("What size should eBay product images be?", "Minimum 500x500px, recommended 1600x1600px."),
        ],
        "tips": "eBay recommends white background and minimum 500x500px. Use 1600x1600px JPG under 1MB.",
    },
    "etsy": {
        "name": "Etsy", "limit": "20MB", "formats": "JPG, PNG, GIF",
        "faq": [
            ("What size should Etsy product images be?", "Recommended: 2000x2000px, square aspect ratio."),
        ],
        "tips": "Etsy recommends square images at 2000x2000px. Compress to under 1MB for faster page loads.",
    },
    "passport": {
        "name": "Passport/Visa", "limit": "Typically 50KB-500KB", "formats": "JPG, PNG",
        "faq": [
            ("What size should passport photos be?", "Requirements vary: US passport photos are 2x2 inches (51x51mm), UK are 35x45mm."),
            ("What's the passport photo file size limit?", "Varies by agency, typically 50KB-500KB."),
        ],
        "tips": "Passport photo requirements vary by country. Check your specific requirements first, then set the target file size accordingly.",
    },
    "seo": {
        "name": "SEO", "limit": "Recommended <200KB per image", "formats": "JPG, PNG, WebP",
        "faq": [
            ("Does image size affect SEO?", "Yes. Large images slow down page loads, hurting Core Web Vitals and search rankings."),
            ("Does WebP help with SEO?", "Yes. WebP files are 25-35% smaller than JPEG at the same quality."),
        ],
        "tips": "Google recommends LCP under 2.5 seconds. Compressing images is one of the most effective ways to improve LCP.",
    },
    "ecommerce": {
        "name": "E-commerce", "limit": "Depends on platform (usually 10-20MB)", "formats": "JPG, PNG, WebP",
        "faq": [
            ("How large should product images be?", "Minimum 1000x1000px, with file sizes between 200KB-500KB."),
            ("Do product images affect sales?", "Yes. High-quality product images can increase conversion rates by 30% or more."),
        ],
        "tips": "Product image quality directly impacts conversions. Compress to 200KB-500KB per image for best results.",
    },
    "ai": {
        "name": "AI Tools", "limit": "Depends on tool (usually 10-20MB)", "formats": "JPG, PNG, WebP, GIF",
        "faq": [
            ("What's ChatGPT's image upload limit?", "ChatGPT Plus: 20MB per image. Free tier limits are lower."),
        ],
        "tips": "AI tools have image upload limits. Compress to under 10MB using JPG or PNG format.",
    },
    "bulk": {
        "name": "Bulk Compression", "limit": "Up to 20 images at once", "formats": "PNG, JPG, JPEG, WebP",
        "faq": [
            ("How many images can I compress at once?", "Up to 20 images. All processing is done locally in your browser."),
            ("Are my images safe?", "Yes. 100% browser-based processing. Your images never leave your device."),
        ],
        "tips": "Batch compression is perfect for e-commerce sellers, bloggers, and webmasters optimizing entire site assets.",
    },
}

# ═══ Generic enrichment fallback ═══════════════════

ENRICHMENT = {
    "size": {
        "tips": "Compressing to a precise KB size is ideal for government forms, passport photos, job applications, and email attachments. Our tool uses smart compression algorithms — all processing happens locally in your browser.",
        "faq": [
            ("Can you compress to an exact file size?", "Yes. Upload your image and the tool compresses to the target size. Adjust the quality slider if needed."),
            ("How's the quality after compressing to 100KB?", "100KB keeps most images looking sharp. For passport photos and avatars, it's virtually indistinguishable."),
            ("Can I batch-compress to the same size?", "Yes. Use our Bulk Image Compressor — upload up to 20 images at once."),
        ],
    },
    "platform": {
        "tips": "Each platform has different image size and format requirements. Our tool optimizes compression for your target platform automatically.",
        "faq": [
            ("Will the compressed image display correctly?", "Yes. The format stays the same; the image displays normally on any device."),
        ],
    },
    "format": {
        "tips": "Different formats have different strengths: PNG for graphics/transparency, JPEG for photos, WebP for modern web. Our tool picks the optimal method automatically.",
        "faq": [
            ("What's the difference between JPG and PNG?", "JPG uses lossy compression — smaller files, best for photos. PNG uses lossless compression — larger files, supports transparency."),
            ("What's the advantage of WebP?", "WebP files are 25-35% smaller than JPEG at the same quality level."),
        ],
    },
    "special": {
        "tips": "All processing happens locally in your browser — your images never leave your device, ensuring complete privacy.",
        "faq": [
            ("Are my images uploaded to a server?", "No. All processing is done locally in your browser."),
        ],
    },
    "conversion": {
        "tips": "PNG supports transparency (best for graphics), JPG is smaller (best for photos), WebP is the modern web format.",
        "faq": [
            ("Will quality drop after conversion?", "Converting from lossless (PNG) to lossy (JPG) may cause minor quality loss."),
        ],
    },
}

# ═══ Get content for a scenario ════════════════════

def get_content(s):
    slug = s.get("slug", "")
    for key, data in PLATFORM_DATA.items():
        if key in slug:
            return data
    cat = s.get("cat", "special")
    return ENRICHMENT.get(cat, ENRICHMENT["special"])

# ═══ Reusable style block ═════════════════════════

STYLE_BLOCK = """
        :root{--primary:#4F46E5;--primary-dark:#4338CA;--bg:#F8FAFC;--card-bg:#FFFFFF;--text:#1E293B;--text-secondary:#64748B;--border:#E2E8F0;--radius:12px}
        *{box-sizing:border-box;margin:0;padding:0}
        body{font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:var(--bg);color:var(--text);line-height:1.6}
        .container{max-width:960px;margin:0 auto;padding:0 24px}
        header{background:#1E293B;color:#F1F5F9;padding:16px 0;box-shadow:0 2px 8px rgba(0,0,0,.15)}
        header .container{display:flex;justify-content:space-between;align-items:center}
        header nav{display:flex;gap:24px}header nav a{color:#94A3B8;text-decoration:none;font-size:.9rem;font-weight:500}header nav a:hover{color:#fff}
        .scene-hero{padding:40px 0 24px;text-align:center}
        .scene-hero h1{font-size:2rem;font-weight:800;margin-bottom:12px;line-height:1.3}
        @media(max-width:640px){.scene-hero h1{font-size:1.5rem}}
        .subtitle{color:var(--text-secondary);max-width:560px;margin:0 auto}
        .tool-area{max-width:700px;margin:0 auto 24px;padding:0 24px}
        .btn-row{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-bottom:24px}
        .btn{padding:12px 28px;border:none;border-radius:8px;font-size:1rem;font-weight:600;cursor:pointer;font-family:inherit}.btn:active{transform:scale(.97)}
        .btn-primary{background:var(--primary);color:#fff}.btn-primary:hover{background:var(--primary-dark)}
        .btn-secondary{background:var(--card-bg);color:var(--text);border:1px solid var(--border)}
        .scene-body{max-width:700px;margin:0 auto;padding:0 24px 40px}
        .scene-body h2{font-size:1.25rem;margin:32px 0 12px;color:#1E293B}
        .scene-body p{color:#475569;margin-bottom:12px;font-size:1rem;line-height:1.7}
        .scene-body ul{color:#475569;margin-bottom:16px;padding-left:24px;line-height:1.7}
        .scene-body li{margin-bottom:4px}
        .faq-section{padding:40px 0;text-align:left}.faq-section h2{font-size:1.5rem;margin-bottom:24px;text-align:center}
        .faq-item{margin-bottom:20px}.faq-item h3{font-size:1rem;margin-bottom:6px;color:var(--primary)}
        .faq-item p{color:var(--text-secondary);font-size:.9rem}
        .related-tools{background:#F8FAFC;border-top:1px solid #E2E8F0;padding:40px 0}
        .related-tools .container{max-width:960px;margin:0 auto;padding:0 24px}
        .related-tools h2{font-size:1.5rem;margin-bottom:20px;text-align:center}
        .related-tools ul{list-style:none;display:grid;grid-template-columns:repeat(2,1fr);gap:12px;max-width:600px;margin:0 auto}
        @media(max-width:640px){.related-tools ul{grid-template-columns:1fr}}
        .related-tools a{color:#4F46E5;text-decoration:none;font-weight:500;padding:10px 16px;display:block;background:#fff;border-radius:8px;border:1px solid #E2E8F0;transition:all .15s}
        .related-tools a:hover{border-color:#4F46E5;box-shadow:0 2px 8px rgba(79,70,229,0.12)}
        .breadcrumb{font-size:.85rem;color:#64748B;padding:16px 0;max-width:960px;margin:0 auto}
        .breadcrumb a{color:#4F46E5;text-decoration:none}.breadcrumb a:hover{text-decoration:underline}
        .guide-cta{max-width:700px;margin:0 auto 40px;padding:20px 24px;background:#EEF2FF;border:1px solid #C7D2FE;border-radius:12px;text-align:center}
        .guide-cta p{color:#4338CA;font-size:.95rem;margin:0}
        .guide-cta a{color:#4F46E5;font-weight:700;text-decoration:underline}
        footer{background:#1E293B;color:#94A3B8;padding:32px 0;text-align:center;font-size:.85rem}
        footer a{color:#CBD5E1;text-decoration:none}
"""

TOOL_JS = """
    const IS_CONVERSION = {is_conv};
    const TARGET_KB = {target_kb};
    const TARGET_BYTES = TARGET_KB * 1024;
    const CONVERT_TO = IS_CONVERSION ? '{convert_to}' : '';
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
    downloadBtn.addEventListener('click', () => {{ if(!resultBlob) return; const a = document.createElement('a'); a.href = resultUrl; const ext = CONVERT_TO || 'jpg'; const name = fileInput.files[0].name.replace(/\\.[^.]+$/, '') + '.' + ext; a.download = name; a.click(); }});
    function formatSize(bytes) {{ if(bytes < 1024) return bytes + ' B'; if(bytes < 1048576) return (bytes/1024).toFixed(1) + ' KB'; return (bytes/1048576).toFixed(2) + ' MB'; }}
    function handleFile(file) {{
        if(file.type==="image/heic"||file.name.match(/\\.heic$/i)){{loadHeicDecoder().then(()=>convertHeic(file));return;}}
        if(!file.type.match(/^image\\/(png|jpeg|webp)$/)) {{ errorMsg.textContent = 'Please upload a PNG, JPEG, or WebP image.'; errorMsg.style.display = 'block'; return; }}
        errorMsg.style.display = 'none';
        const reader = new FileReader();
        reader.onload = e => {{
            const img = new Image();
            img.onload = () => {{
                originalPreview.src = e.target.result;
                dropZone.style.display = 'none';
                previewArea.style.display = 'block';
                progressBar.style.display = 'block';
                progressFill.style.width = '30%';
                if(IS_CONVERSION) convertImage(img);
                else compressImage(img, file.type);
            }};
            img.src = e.target.result;
        }};
        reader.readAsDataURL(file);
    }}
    function compressImage(img, mime) {{
        const canvas = document.createElement('canvas');
        canvas.width = img.width;
        canvas.height = img.height;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(img, 0, 0);
        progressFill.style.width = '60%';
        const quality = currentMode === 'quality' ? parseInt(document.getElementById('qualitySlider').value)/100 : 0.75;
        canvas.toBlob(blob => {{
            progressFill.style.width = '90%';
            finishCompression(blob, img, 'image/jpeg');
        }}, 'image/jpeg', quality);
    }}
    function convertImage(img) {{
        const canvas = document.createElement('canvas');
        canvas.width = img.width;
        canvas.height = img.height;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(img, 0, 0);
        progressFill.style.width = '60%';
        const mime = CONVERT_TO === 'jpg' ? 'image/jpeg' : 'image/' + CONVERT_TO;
        canvas.toBlob(blob => {{
            progressFill.style.width = '90%';
            finishCompression(blob, img, mime);
        }}, mime, 0.85);
    }}
    function finishCompression(blob, img, mime) {{
        if(currentMode === 'exact' && !IS_CONVERSION) {{
            const targetKB = parseInt(document.getElementById('targetKB').value) || 100;
            const targetBytes = targetKB * 1024;
            if(blob.size > targetBytes) {{
                const ratio = targetBytes / blob.size;
                const canvas2 = document.createElement('canvas');
                canvas2.width = img.width;
                canvas2.height = img.height;
                const ctx2 = canvas2.getContext('2d');
                ctx2.drawImage(img, 0, 0);
                const q = Math.max(0.01, Math.min(1.0, ratio * 0.85));
                canvas2.toBlob(finalBlob => {{
                    resultBlob = finalBlob;
                    resultUrl = URL.createObjectURL(finalBlob);
                    showResult(finalBlob, img);
                }}, 'image/jpeg', q);
                return;
            }}
        }}
        resultBlob = blob;
        resultUrl = URL.createObjectURL(blob);
        showResult(blob, img);
    }}
    function showResult(blob, img) {{
        compressedPreview.src = resultUrl;
        progressBar.style.display = 'none';
        stats.innerHTML = '<strong>Original:</strong> ' + formatSize(img.src.length) + ' → <strong>Compressed:</strong> ' + formatSize(blob.size) + ' (' + (100-blob.size/img.src.length*100).toFixed(1) + '% smaller)';
    }}
    function loadHeicDecoder() {{
        if(window.heic2any) return Promise.resolve();
        return new Promise((resolve, reject) => {{
            const script = document.createElement('script');
            script.src = 'https://cdn.jsdelivr.net/npm/heic2any@0.0.4/dist/heic2any.min.js';
            script.onload = resolve;
            script.onerror = () => {{ errorMsg.textContent = 'HEIC decoder failed to load. Try a different format.'; errorMsg.style.display = 'block'; reject(); }};
            document.head.appendChild(script);
        }});
    }}
    function convertHeic(file) {{
        const reader = new FileReader();
        reader.onload = e => {{
            window.heic2any({{blob: file, toType: 'image/jpeg'}}).then(jpgBlob => {{
                const img = new Image();
                img.onload = () => {{
                    originalPreview.src = URL.createObjectURL(jpgBlob);
                    dropZone.style.display = 'none';
                    previewArea.style.display = 'block';
                    progressBar.style.display = 'block';
                    progressFill.style.width = '30%';
                    if(IS_CONVERSION) convertImage(img);
                    else compressImage(img, 'image/jpeg');
                }};
                img.src = URL.createObjectURL(jpgBlob);
            }}).catch(() => {{ errorMsg.textContent = 'HEIC conversion failed. Try converting to JPG first.'; errorMsg.style.display = 'block'; }});
        }};
        reader.readAsDataURL(file);
    }}
    function switchMode(mode) {{
        const exactBtn = document.getElementById('modeExact');
        const qualityBtn = document.getElementById('modeQuality');
        const exactDiv = document.getElementById('exactControls');
        const qualityDiv = document.getElementById('qualityControls');
        if(mode === 'quality') {{
            exactBtn.style.background = 'var(--card-bg)'; exactBtn.style.color = 'var(--text)';
            qualityBtn.style.background = 'var(--primary)'; qualityBtn.style.color = '#fff';
            exactDiv.style.display = 'none'; qualityDiv.style.display = 'block';
        }} else {{
            exactBtn.style.background = 'var(--primary)'; exactBtn.style.color = '#fff';
            qualityBtn.style.background = 'var(--card-bg)'; qualityBtn.style.color = 'var(--text)';
            exactDiv.style.display = 'block'; qualityDiv.style.display = 'none';
        }}
        currentMode = mode;
    }}
    let currentMode = 'exact';
"""

# ═══ Build scenario page (tools pages) ═════════════

def build_scene_page(s, noindex=False):
    content = get_content(s)
    slug = s["slug"]
    cat = s.get("cat", "special")
    size_val = s.get("size", "")
    title = s.get("title", "CompressNow")
    desc = s.get("desc", "")
    
    # Dynamic target label
    if cat == "size" and size_val:
        target_label = size_val
    elif cat == "platform":
        s_lower = slug.lower()
        if "discord" in s_lower: target_label = "Under 8MB"
        elif "email" in s_lower: target_label = "Under 1MB"
        elif "whatsapp" in s_lower: target_label = "Under 1MB"
        elif "twitter" in s_lower: target_label = "Under 5MB"
        elif "instagram" in s_lower: target_label = "Under 5MB"
        elif "facebook" in s_lower: target_label = "Under 5MB"
        else: target_label = "Web-Optimized"
    elif cat == "format": target_label = "Web-Optimized"
    else: target_label = "100 KB"

    # Use case text — unique per page from data definitions
    use_cases_text = s.get("use_cases", "")
    if not use_cases_text:
        if cat == "size" and size_val:
            use_cases_text = f"Compress images to exactly {size_val} for passport photos, visa applications, online forms, email attachments, forum avatars, and any website requiring strict file size limits."
        elif cat == "platform":
            pname = s.get("platform", slug.replace("compress-image-for-","").replace("-"," ").title())
            use_cases_text = f"Compress images for {pname} — meet platform upload limits, share photos faster, and save storage space."
        else:
            use_cases_text = "Compress images for websites, apps, social media, email, and any platform with file size restrictions."

    # Format tip — unique per page
    format_tip = s.get("format_tip", "")
    if not format_tip:
        format_tip = content.get('tips', 'Compress images to exact sizes while maintaining visual quality. All processing happens locally in your browser.')
    
    # Page-specific Pro Tip (not cross-site)
    page_tip = content.get('tips', '')
    
    # Dynamic What to Expect table
    if cat == "size" and size_val:
        kb_str = size_val.replace(" KB","").replace(" MB","000")
        try: kbi = int(kb_str)
        except: kbi = 100
        if kbi <= 100: table_smartphone = f"~{kbi} KB"; table_dslr = f"~{kbi} KB"
        elif kbi <= 500: table_smartphone = f"~{kbi} KB"; table_dslr = f"~{kbi} KB"
        else: table_smartphone = f"~{kbi//1000} MB"; table_dslr = f"~{kbi//1000} MB"
        table_screenshot = table_smartphone
    else:
        table_smartphone = "~100 KB"; table_dslr = "~200 KB"; table_screenshot = "~100 KB"

    # What to Expect table quality notes
    if cat == "size" and size_val:
        try: kbi2 = int(size_val.replace(" KB","").replace(" MB","000"))
        except: kbi2 = 100
        q_smartphone = "[OK] Good" if kbi2 >= 50 else "⚠️ May lose detail" if kbi2 >= 20 else "🔴 Noticeable loss"
        q_dslr = "⚠️ May lose detail" if kbi2 < 200 else "[OK] Good" if kbi2 < 500 else "[OK] Excellent"
        q_screenshot = "[OK] Perfect" if kbi2 >= 30 else "⚠️ Text may blur"
    else:
        q_smartphone = "[OK] Good"; q_dslr = "⚠️ May lose detail"; q_screenshot = "[OK] Perfect"

    # FAQ
    faq_html = ""
    for q, a in content.get("faq", [])[:5]:
        faq_html += f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>'

    # Related tools
    related_slugs = []
    if cat == "size":
        nearby = [s2 for s2 in SIZES if s2["slug"] != slug][:3]
        related_slugs.extend([s2["slug"] for s2 in nearby])
        related_slugs.extend(["compress-image-for-email", "compress-image-for-discord", "bulk-image-compressor"])
    elif cat == "platform":
        related_slugs.extend(["compress-image-to-100kb", "compress-image-to-50kb", "compress-image-to-200kb"])
        other = [s2["slug"] for s2 in PLATFORMS if s2["slug"] != slug][:2]
        related_slugs.extend(other)
    elif cat == "format":
        related_slugs.extend(["jpg-to-png", "png-to-jpg", "webp-to-jpg", "compress-image-to-100kb", "compress-image-to-50kb"])
    elif cat == "conversion":
        other = [s2["slug"] for s2 in CONVERSIONS if s2["slug"] != slug][:3]
        related_slugs.extend(other)
        related_slugs.extend(["compress-image-to-100kb", "compress-image-to-50kb"])
    else:
        related_slugs.extend(["compress-image-to-100kb", "compress-image-to-50kb", "compress-image-for-email", "compress-image-for-discord", "bulk-image-compressor"])

    related_html = ""
    for rs in related_slugs[:6]:
        r = next((s2 for s2 in ALL_SCENARIOS if s2["slug"] == rs), None)
        if r:
            related_html += f'<li><a href="/{r["slug"]}/">{r["title"].split("—")[0].strip()}</a></li>'

    # JS values
    is_conv = "true" if cat == "conversion" else "false"
    tk = size_val.replace(" KB","").replace(" MB","000") if size_val else "100"
    try: tk = int(tk)
    except: tk = 100
    convert_to = slug.split("-to-")[1] if "-to-" in slug else "png"
    the_js = TOOL_JS.format(is_conv=is_conv, target_kb=tk, convert_to=convert_to)
    
    robots_meta = 'noindex, follow' if noindex else 'index, follow'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <link rel="apple-touch-icon" href="/favicon.svg">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="msvalidate.01" content="1F14EEA4478F7A176F2E0451992C984C">
    <meta name="description" content="{desc}">
    <meta name="robots" content="{robots_meta}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://{DOMAIN}/{slug}/">
    <link rel="canonical" href="https://{DOMAIN}/{slug}/">
    <title>{title}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preload" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet"></noscript>
    <script>
        // Lazy load Google Analytics after page load
        window.addEventListener('load', function() {{
            var script = document.createElement('script');
            script.src = 'https://www.googletagmanager.com/gtag/js?id=G-Z9NW1GSG04';
            script.async = true;
            document.head.appendChild(script);
            window.dataLayer = window.dataLayer || [];
            function gtag(){{{{dataLayer.push(arguments);}}}}
            gtag('js', new Date());
            gtag('config', 'G-Z9NW1GSG04');
        }});
    </script>
    <style>{STYLE_BLOCK}</style>
    <script type="application/ld+json">
    {json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in content.get('faq',[])[:4]]}, ensure_ascii=False)}
    </script>
    <script type="application/ld+json">
    {{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://{DOMAIN}/"}}, {{"@type": "ListItem", "position": 2, "name": "{title.split('—')[0].strip()}", "item": "https://{DOMAIN}/{slug}/"}}]}}
    </script>
</head>
<body>
    <header>
        <div class="container">
            <a href="/" style="color:#fff;text-decoration:none;font-size:1.2rem;font-weight:700">CompressNow</a>
            <nav>
                <a href="/">Home</a>
                <a href="/guides/how-to-compress-images/">Guides</a>
                <a href="#faq">FAQ</a>
            </nav>
        </div>
    </header>
    <main>
        <div class="breadcrumb"><a href="/">Home</a> / {title.split('—')[0].strip()}</div>
        <section class="scene-hero">
            <h1>{title.split('—')[0].strip()}</h1>
            <p class="subtitle">{desc}</p>
        </section>
        <section class="tool-area">
            <div style="display:flex;gap:8px;justify-content:center;margin-bottom:16px;flex-wrap:wrap"><button id="modeExact" class="mode-btn active" onclick="switchMode('exact')" style="padding:8px 16px;border-radius:8px;border:1px solid var(--border);cursor:pointer;font-weight:600;background:var(--primary);color:#fff">🎯 Target Size (KB)</button><button id="modeQuality" class="mode-btn" onclick="switchMode('quality')" style="padding:8px 16px;border-radius:8px;border:1px solid var(--border);cursor:pointer;font-weight:600;background:var(--card-bg);color:var(--text)">🎚️ Quality Slider</button></div><div id="exactControls"><div style="display:flex;gap:8px;align-items:center;justify-content:center;flex-wrap:wrap"><input type="number" id="targetKB" value="100" min="1" max="5000" style="width:80px;padding:8px 12px;border:1px solid var(--border);border-radius:8px;font-size:1rem;text-align:center"><span style="color:var(--text-secondary)">KB</span></div></div><div id="qualityControls" style="display:none;max-width:400px;margin:0 auto"><input type="range" id="qualitySlider" min="1" max="100" value="75" style="width:100%;accent-color:var(--primary)"><div style="display:flex;justify-content:space-between;font-size:.75rem;color:var(--text-secondary)"><span>Smallest file</span><span id="qualityLabel">75%</span><span>Best quality</span></div></div><div id="dropZone" style="border:2px dashed var(--border);border-radius:var(--radius);padding:40px 20px;text-align:center;cursor:pointer;background:var(--card-bg);transition:all .2s">
                <p style="font-size:2rem;margin-bottom:8px">📁</p>
                <p style="font-weight:600;margin-bottom:4px">Drop image here or click to upload</p>
                <p style="color:var(--text-secondary);font-size:.85rem">Supports PNG, JPEG, WebP, HEIC</p>
                <input type="file" id="fileInput" accept="image/*" style="display:none">
            </div>
            <div id="previewArea" style="display:none;margin-top:20px">
                <div style="position:relative;width:100%;max-width:500px;margin:0 auto 16px;overflow:hidden;border-radius:8px;border:1px solid var(--border)">
                    <img id="compressedPreview" alt="Compressed image preview showing quality after compression" style="width:100%;display:block">
                    <div style="position:absolute;top:0;left:0;width:50%;height:100%;overflow:hidden;border-right:2px solid #4F46E5">
                        <img id="originalPreview" alt="Original image before compression" style="width:500px;max-width:500px;display:block;position:absolute;top:0;left:0">
                    </div>
                    <div id="sliderHandle" style="position:absolute;top:0;bottom:0;left:50%;width:4px;background:#4F46E5;cursor:ew-resize;z-index:2;transform:translateX(-2px)"></div>
                    <div id="sliderLabel" style="position:absolute;top:8px;left:calc(50% - 24px);background:#4F46E5;color:#fff;padding:2px 8px;border-radius:4px;font-size:11px;font-weight:600;z-index:3;pointer-events:none">◄ ►</div>
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
            <h2>What to Expect</h2>
            <div style="background:var(--card-bg);border:1px solid var(--border);border-radius:8px;overflow:hidden;margin:20px 0"><table style="width:100%;border-collapse:collapse;font-size:.9rem"><thead><tr style="background:#F1F5F9"><th style="padding:12px;text-align:left">Image Type</th><th style="padding:12px;text-align:left">Typical Before</th><th style="padding:12px;text-align:left">Typical After ({target_label})</th><th style="padding:12px;text-align:left">Quality</th></tr></thead><tbody><tr><td style="padding:12px;border-top:1px solid var(--border)">Smartphone Photo</td><td style="padding:12px;border-top:1px solid var(--border)">~3-5 MB</td><td style="padding:12px;border-top:1px solid var(--border)">{table_smartphone}</td><td style="padding:12px;border-top:1px solid var(--border);color:#16A34A">{q_smartphone}</td></tr><tr><td style="padding:12px;border-top:1px solid var(--border)">DSLR Photo</td><td style="padding:12px;border-top:1px solid var(--border)">~8-15 MB</td><td style="padding:12px;border-top:1px solid var(--border)">{table_dslr}</td><td style="padding:12px;border-top:1px solid var(--border);color:#EAB308">{q_dslr}</td></tr><tr><td style="padding:12px;border-top:1px solid var(--border)">Screenshot</td><td style="padding:12px;border-top:1px solid var(--border)">~500 KB-2 MB</td><td style="padding:12px;border-top:1px solid var(--border)">{table_screenshot}</td><td style="padding:12px;border-top:1px solid var(--border);color:#16A34A">{q_screenshot}</td></tr><tr><td style="padding:12px;border-top:1px solid var(--border)">Logo/Icon</td><td style="padding:12px;border-top:1px solid var(--border)">~50-200 KB</td><td style="padding:12px;border-top:1px solid var(--border)">~30-50 KB</td><td style="padding:12px;border-top:1px solid var(--border);color:#16A34A">[OK] Excellent</td></tr></tbody></table></div>
            
            <h2>When to Compress to {target_label}</h2>
            <p>{use_cases_text}</p>
            
            <h2>Format Tips for {target_label}</h2>
            <p>{format_tip}</p>

            <div style="background:#FFF7ED;border:1px solid #FED7AA;border-radius:8px;padding:16px;margin-top:20px">
                <p style="color:#C2410C;font-size:.9rem;margin:0"><strong>💡 Pro Tip:</strong> {page_tip}</p>
            </div>

            <h2>Learn More About Image Optimization</h2>
            <p>Want to dive deeper into image compression? Check out these authoritative resources:</p>
            <ul style="color:var(--text-secondary);font-size:.9rem;line-height:1.8">
                <li><a href="https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/image-optimization" target="_blank" rel="noopener noreferrer" style="color:var(--primary);text-decoration:none">Google Developers — Image Optimization Guide</a></li>
                <li><a href="https://web.dev/fast/#optimize-your-images" target="_blank" rel="noopener noreferrer" style="color:var(--primary);text-decoration:none">Web.dev — Fast Image Optimization</a></li>
                <li><a href="https://developers.google.com/speed/webp" target="_blank" rel="noopener noreferrer" style="color:var(--primary);text-decoration:none">Google — WebP Image Format</a></li>
            </ul>
        </section>
        <div class="guide-cta">
            <p>[GUIDE] New to image compression? Read our <a href="/guides/how-to-compress-images/">Complete Guide to Image Compression</a> — learn how to choose the right format, size, and quality for any use case.</p>
        </div>
        <section class="faq-section" id="faq">
            <div class="container">
                <h2>Frequently Asked Questions</h2>
                {faq_html}
            </div>
        </section>
        <section class="related-tools" id="related">
            <div class="container">
                <h2>Related Tools</h2>
                <ul>{related_html}</ul>
            </div>
        </section>
    </main>
    <footer>
        <div class="container">
            <p>&copy; 2026 CompressNow. All rights reserved. | <a href="/">Home</a> | <a href="/guides/how-to-compress-images/">Compression Guide</a> | <a href="/guides/image-formats-compared/">Format Guide</a> | <a href="#faq">FAQ</a></p>
            <p style="margin-top:8px;font-size:.8rem;color:#94A3B8">Also try: <a href="https://resizenow.net" style="color:#64748B">ResizeNow</a> (image resizer) · All processing happens locally in your browser. Your data is never uploaded.</p>
        </div>
    </footer>
    <script>{the_js}</script>
</body>
</html>"""

# ═══ Build homepage ═══════════════════════════════

def build_home():
    all_sizes = "".join(f'<a href="/{s["slug"]}/" class="card">{s["size"]}</a>' for s in SIZES)
    size_cards = f'<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:12px;max-width:820px;margin:0 auto"><a href="/bulk-image-compressor/" class="card" style="background:#EEF2FF;border-color:var(--primary);font-weight:700;text-align:center">📦 Bulk (20 images)</a>{all_sizes}</div>'
    platform_cards = "".join(f'<a href="/{s["slug"]}/" class="card">{s["platform"]}</a>' for s in PLATFORMS[:8])
    conversion_cards = "".join(f'<a href="/{s["slug"]}/" class="card">{s["title"].split("—")[0].strip()}</a>' for s in CONVERSIONS[:6])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <link rel="apple-touch-icon" href="/favicon.svg">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="msvalidate.01" content="1F14EEA4478F7A176F2E0451992C984C">
    <meta name="description" content="Free image compressor — compress to exact size from 10KB to 5MB. 100% browser-based, no upload. PNG, JPEG, WebP, HEIC supported. Free forever.">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://{DOMAIN}/">
    <meta property="og:title" content="Free Image Compressor — Compress to Exact Size (10KB–5MB), No Upload | CompressNow">
    <meta property="og:description" content="Compress images to any exact size from 10KB to 5MB. 100% browser-based, no upload. Free forever.">
    <meta property="og:url" content="https://{DOMAIN}/">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary_large_image">
    <title>Free Image Compressor — Compress to Exact Size (10KB–5MB), No Upload | CompressNow</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preload" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet"></noscript>
    <script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"CompressNow","url":"https://{DOMAIN}","description":"Free online image compression tool. Compress PNG, JPEG, WebP images to exact file sizes."}}</script>
    <script type="application/ld+json">{{"@context":"https://schema.org","@type":"WebApplication","name":"CompressNow","url":"https://{DOMAIN}","applicationCategory":"UtilityApplication","operatingSystem":"All","offers":{{"@type":"Offer","price":"0","priceCurrency":"USD"}}}}</script>
    <script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{{"@type":"Question","name":"How does CompressNow work?","acceptedAnswer":{{"@type":"Answer","text":"Upload your image, set your target file size, and our tool compresses it instantly. Everything happens in your browser — no upload to server."}}}},{{"@type":"Question","name":"Is CompressNow free?","acceptedAnswer":{{"@type":"Answer","text":"Yes, completely free. No signup, no watermarks, no limits."}}}},{{"@type":"Question","name":"Is my image uploaded to a server?","acceptedAnswer":{{"@type":"Answer","text":"No. All processing happens locally in your browser. Your images never leave your device."}}}}]}}</script>
    <script>
        // Lazy load Google Analytics after page load
        window.addEventListener('load', function() {{
            var script = document.createElement('script');
            script.src = 'https://www.googletagmanager.com/gtag/js?id=G-Z9NW1GSG04';
            script.async = true;
            document.head.appendChild(script);
            window.dataLayer = window.dataLayer || [];
            function gtag(){{{{dataLayer.push(arguments);}}}}
            gtag('js', new Date());
            gtag('config', 'G-Z9NW1GSG04');
        }});
    </script>
    <style>
        {STYLE_BLOCK}
        .hero{{padding:60px 0 40px;text-align:center}}
        .hero h1{{font-size:2.5rem;font-weight:800;margin-bottom:16px;line-height:1.2}}
        .hero p{{color:var(--text-secondary);font-size:1.1rem;max-width:600px;margin:0 auto}}
        .section{{padding:40px 0}}.section h2{{font-size:1.5rem;margin-bottom:20px;text-align:center}}
        .grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;max-width:700px;margin:0 auto}}
        @media(max-width:640px){{.grid{{grid-template-columns:repeat(2,1fr)}}.hero h1{{font-size:1.8rem}}}}
        .card{{padding:16px;background:var(--card-bg);border:1px solid var(--border);border-radius:8px;text-align:center;text-decoration:none;color:var(--text);font-weight:600;font-size:.9rem;transition:all .15s}}
        .card:hover{{border-color:var(--primary);box-shadow:0 2px 8px rgba(79,70,229,0.12)}}
    </style>
</head>
<body>
    <header>
        <div class="container">
            <a href="/" style="color:#fff;text-decoration:none;font-size:1.2rem;font-weight:700">CompressNow</a>
            <nav>
                <a href="/">Home</a>
                <a href="/guides/how-to-compress-images/">Guides</a>
                <a href="#faq">FAQ</a>
                <a href="#sizes">Sizes</a>
            </nav>
        </div>
    </header>
    <main>
        <section class="hero">
            <h1>Compress Images to Exact Size — 10KB to 5MB | CompressNow</h1>
            <p>18 exact target sizes. 100% browser-based, no upload. PNG, JPEG, WebP, HEIC supported. Compress to any size from 10KB to 5MB.</p>
            <div style="display:flex;gap:32px;justify-content:center;margin-top:24px;flex-wrap:wrap">
                <div style="text-align:center"><div style="font-size:2rem;font-weight:800;color:var(--primary)">18</div><div style="font-size:.85rem;color:var(--text-secondary)">Target Sizes</div></div>
                <div style="text-align:center"><div style="font-size:2rem;font-weight:800;color:var(--primary)">100%</div><div style="font-size:.85rem;color:var(--text-secondary)">Browser-Based</div></div>
                <div style="text-align:center"><div style="font-size:2rem;font-weight:800;color:var(--primary)">0</div><div style="font-size:.85rem;color:var(--text-secondary)">Uploads to Server</div></div>
                <div style="text-align:center"><div style="font-size:2rem;font-weight:800;color:var(--primary)">4</div><div style="font-size:.85rem;color:var(--text-secondary)">Formats</div></div>
            </div>
        </section>
        <section class="tool-area">
            <div style="display:flex;gap:8px;justify-content:center;margin-bottom:16px;flex-wrap:wrap"><button id="modeExact" class="mode-btn active" onclick="switchMode('exact')" style="padding:8px 16px;border-radius:8px;border:1px solid var(--border);cursor:pointer;font-weight:600;background:var(--primary);color:#fff">🎯 Target Size (KB)</button><button id="modeQuality" class="mode-btn" onclick="switchMode('quality')" style="padding:8px 16px;border-radius:8px;border:1px solid var(--border);cursor:pointer;font-weight:600;background:var(--card-bg);color:var(--text)">🎚️ Quality Slider</button></div><div id="exactControls"><div style="display:flex;gap:8px;align-items:center;justify-content:center;flex-wrap:wrap"><input type="number" id="targetKB" value="100" min="1" max="5000" style="width:80px;padding:8px 12px;border:1px solid var(--border);border-radius:8px;font-size:1rem;text-align:center"><span style="color:var(--text-secondary)">KB</span></div></div><div id="qualityControls" style="display:none;max-width:400px;margin:0 auto"><input type="range" id="qualitySlider" min="1" max="100" value="75" style="width:100%;accent-color:var(--primary)"><div style="display:flex;justify-content:space-between;font-size:.75rem;color:var(--text-secondary)"><span>Smallest file</span><span id="qualityLabel">75%</span><span>Best quality</span></div></div><div id="dropZone" style="border:2px dashed var(--border);border-radius:var(--radius);padding:40px 20px;text-align:center;cursor:pointer;background:var(--card-bg);transition:all .2s">
                <p style="font-size:2rem;margin-bottom:8px">📁</p>
                <p style="font-weight:600;margin-bottom:4px">Drop image here or click to upload</p>
                <p style="color:var(--text-secondary);font-size:.85rem">Supports PNG, JPEG, WebP, HEIC</p>
                <input type="file" id="fileInput" accept="image/*" style="display:none">
            </div>
            <div id="previewArea" style="display:none;margin-top:20px">
                <div style="position:relative;width:100%;max-width:500px;margin:0 auto 16px;overflow:hidden;border-radius:8px;border:1px solid var(--border)">
                    <img id="compressedPreview" alt="Compressed image preview showing quality after compression" style="width:100%;display:block">
                    <div style="position:absolute;top:0;left:0;width:50%;height:100%;overflow:hidden;border-right:2px solid #4F46E5">
                        <img id="originalPreview" alt="Original image before compression" style="width:500px;max-width:500px;display:block;position:absolute;top:0;left:0">
                    </div>
                    <div id="sliderHandle" style="position:absolute;top:0;bottom:0;left:50%;width:4px;background:#4F46E5;cursor:ew-resize;z-index:2;transform:translateX(-2px)"></div>
                    <div id="sliderLabel" style="position:absolute;top:8px;left:calc(50% - 24px);background:#4F46E5;color:#fff;padding:2px 8px;border-radius:4px;font-size:11px;font-weight:600;z-index:3;pointer-events:none">◄ ►</div>
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
            {size_cards}
        </section>
        <section class="section">
            <h2>Compress by Platform</h2>
            <div class="grid">{platform_cards}</div>
        </section>
        <section class="section">
            <h2>Convert Image Format</h2>
            <div class="grid">{conversion_cards}</div>
        </section>
        <section class="section" style="padding:48px 0;background:#fff">
            <div class="container" style="max-width:960px;margin:0 auto;padding:0 24px">
                <h2 style="font-size:1.5rem;font-weight:800;text-align:center;margin-bottom:16px">Why Compress to an Exact Size?</h2>
                <p style="color:var(--text-secondary);max-width:650px;margin:0 auto 32px;text-align:center;line-height:1.7">Most image compressors give you a quality slider and hope for the best. CompressNow lets you pick a <strong>precise target</strong> — 10KB, 50KB, 100KB, 500KB — and hit it exactly. That matters when you're dealing with strict upload limits: passport photos must be under 100KB, email attachments under 25MB, and Discord avatars under 8MB.</p>
                <h2 style="font-size:1.5rem;font-weight:800;text-align:center;margin-bottom:24px">How It Works</h2>
                <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px;max-width:800px;margin:0 auto 40px">
                    <div style="text-align:center;padding:24px;background:var(--bg);border-radius:12px"><div style="font-size:2.5rem;margin-bottom:12px">①</div><h3 style="font-weight:700;margin-bottom:8px">Upload</h3><p style="color:var(--text-secondary);font-size:.9rem">Drop your image or click to upload. PNG, JPEG, WebP, HEIC — all supported.</p></div>
                    <div style="text-align:center;padding:24px;background:var(--bg);border-radius:12px"><div style="font-size:2.5rem;margin-bottom:12px">②</div><h3 style="font-weight:700;margin-bottom:8px">Pick Your Size</h3><p style="color:var(--text-secondary);font-size:.9rem">Choose any target from 10KB to 5MB. Our algorithm hits it with surgical precision.</p></div>
                    <div style="text-align:center;padding:24px;background:var(--bg);border-radius:12px"><div style="font-size:2.5rem;margin-bottom:12px">③</div><h3 style="font-weight:700;margin-bottom:8px">Download</h3><p style="color:var(--text-secondary);font-size:.9rem">Get your compressed image instantly. No signup, no upload, 100% free.</p></div>
                </div>
                <h2 style="font-size:1.5rem;font-weight:800;text-align:center;margin-bottom:24px">Typical Results</h2>
                <div style="max-width:700px;margin:0 auto;background:var(--bg);border-radius:12px;overflow:hidden">
                    <table style="width:100%;border-collapse:collapse;font-size:.9rem">
                        <thead><tr style="background:#EEF2FF"><th style="padding:14px;text-align:left">Image Type</th><th style="padding:14px;text-align:left">Original Size</th><th style="padding:14px;text-align:left">After (100KB Target)</th><th style="padding:14px;text-align:left">Reduction</th></tr></thead>
                        <tbody>
                            <tr style="border-top:1px solid var(--border)"><td style="padding:14px">📱 Smartphone Photo</td><td style="padding:14px">~4.2 MB</td><td style="padding:14px">~98 KB</td><td style="padding:14px;color:#16A34A">97.7% smaller</td></tr>
                            <tr style="border-top:1px solid var(--border)"><td style="padding:14px">📷 DSLR Image</td><td style="padding:14px">~12 MB</td><td style="padding:14px">~487 KB</td><td style="padding:14px;color:#16A34A">96.0% smaller</td></tr>
                            <tr style="border-top:1px solid var(--border)"><td style="padding:14px">🖥 Screenshot</td><td style="padding:14px">~1.8 MB</td><td style="padding:14px">~102 KB</td><td style="padding:14px;color:#16A34A">94.3% smaller</td></tr>
                            <tr style="border-top:1px solid var(--border)"><td style="padding:14px">🌐 WebP Image</td><td style="padding:14px">~2.3 MB</td><td style="padding:14px">~78 KB</td><td style="padding:14px;color:#16A34A">96.6% smaller</td></tr>
                        </tbody>
                    </table>
                </div>
                <div style="text-align:center;margin-top:24px">
                    <p style="color:var(--text-secondary);font-size:.9rem">[GUIDE] Want to understand image compression in depth? Read our <a href="/guides/how-to-compress-images/" style="color:var(--primary);font-weight:600">Complete Guide to Image Compression</a></p>
                </div>
            </div>
        </section>
        <section class="faq-section" id="faq">
            <div class="container">
                <h2>Frequently Asked Questions</h2>
                <div class="faq-item"><h3>How does CompressNow work?</h3><p>Upload your image, set your target file size, and our tool compresses it instantly. Everything happens in your browser — no upload to server.</p></div>
                <div class="faq-item"><h3>Is CompressNow free?</h3><p>Yes, completely free. No signup, no watermarks, no limits. Compress as many images as you need.</p></div>
                <div class="faq-item"><h3>What image formats are supported?</h3><p>PNG, JPEG, and WebP are fully supported. Our tool applies format-specific compression for optimal results.</p></div>
                <div class="faq-item"><h3>Is my image uploaded to a server?</h3><p>No. All processing happens locally in your browser. Your images never leave your device, ensuring complete privacy.</p></div>
            </div>
        </section>
    </main>
    <footer>
        <div class="container">
            <p>&copy; 2026 CompressNow. All rights reserved. | <a href="/">Home</a> | <a href="/guides/how-to-compress-images/">Compression Guide</a> | <a href="/guides/image-formats-compared/">Format Guide</a> | <a href="#faq">FAQ</a></p>
            <p style="margin-top:8px;font-size:.8rem;color:#94A3B8">Also try: <a href="https://resizenow.net" style="color:#64748B">ResizeNow</a> (image resizer) · All processing happens locally in your browser. Your data is never uploaded.</p>
        </div>
    </footer>
    <script>
    {TOOL_JS.format(is_conv="false", target_kb=100, convert_to="jpg")}
    document.getElementById('qualitySlider').addEventListener('input', function() {{ document.getElementById('qualityLabel').textContent = this.value + '%'; }});
    </script>
</body>
</html>"""
    return html

# ═══ Pillar Guide Pages ═══════════════════════════

def build_guide_page(slug, title, desc, body_html, faq_items):
    faq_html = ""
    for q, a in faq_items:
        faq_html += f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="msvalidate.01" content="1F14EEA4478F7A176F2E0451992C984C">
    <meta name="description" content="{desc}">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://{DOMAIN}/{slug}/">
    <link rel="canonical" href="https://{DOMAIN}/{slug}/">
    <title>{title}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preload" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet"></noscript>
    <script>
        // Lazy load Google Analytics after page load
        window.addEventListener('load', function() {{
            var script = document.createElement('script');
            script.src = 'https://www.googletagmanager.com/gtag/js?id=G-Z9NW1GSG04';
            script.async = true;
            document.head.appendChild(script);
            window.dataLayer = window.dataLayer || [];
            function gtag(){{{{dataLayer.push(arguments);}}}}
            gtag('js', new Date());
            gtag('config', 'G-Z9NW1GSG04');
        }});
    </script>
    <style>
        {STYLE_BLOCK}
        .guide-hero{{padding:48px 0 32px;text-align:center;background:#fff;border-bottom:1px solid var(--border)}}
        .guide-hero h1{{font-size:2.2rem;font-weight:800;margin-bottom:16px;line-height:1.3}}
        .guide-body{{max-width:720px;margin:0 auto;padding:40px 24px 40px}}
        .guide-body h2{{font-size:1.4rem;font-weight:700;margin:36px 0 16px;color:#1E293B}}
        .guide-body h3{{font-size:1.15rem;font-weight:600;margin:24px 0 10px;color:#334155}}
        .guide-body p{{color:#475569;margin-bottom:16px;font-size:1rem;line-height:1.8}}
        .guide-body ul,.guide-body ol{{color:#475569;margin-bottom:20px;padding-left:28px;line-height:1.8}}
        .guide-body li{{margin-bottom:6px}}
        .guide-body table{{width:100%;border-collapse:collapse;margin:20px 0;font-size:.9rem}}
        .guide-body th{{background:#F1F5F9;padding:12px;text-align:left;font-weight:600;border-bottom:2px solid var(--border)}}
        .guide-body td{{padding:12px;border-bottom:1px solid var(--border)}}
        .guide-body strong{{color:#1E293B}}
        .guide-cta-box{{max-width:720px;margin:0 auto 48px;padding:24px 32px;background:#EEF2FF;border:2px solid #C7D2FE;border-radius:12px;text-align:center}}
        .guide-cta-box h3{{color:#4338CA;margin-bottom:8px}}
        .guide-cta-box a{{color:#4F46E5;font-weight:700}}
    </style>
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"Article","headline":"{title}","description":"{desc}","datePublished":"{TODAY}","dateModified":"{TODAY}","author":{{"@type":"Organization","name":"CompressNow"}},"publisher":{{"@type":"Organization","name":"CompressNow","url":"https://{DOMAIN}"}}}}
    </script>
    <script type="application/ld+json">
    {{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://{DOMAIN}/"}}, {{"@type": "ListItem", "position": 2, "name": "Guides", "item": "https://{DOMAIN}/guides/"}}, {{"@type": "ListItem", "position": 3, "name": "{title.split('—')[0].strip()}", "item": "https://{DOMAIN}/{slug}/"}}]}}
    </script>
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{','.join(['{"@type":"Question","name":"'+q.replace('"','\\"')+'","acceptedAnswer":{"@type":"Answer","text":"'+a.replace('"','\\"')+'"}}' for q,a in faq_items])}]}}
    </script>
</head>
<body>
    <header>
        <div class="container">
            <a href="/" style="color:#fff;text-decoration:none;font-size:1.2rem;font-weight:700">CompressNow</a>
            <nav>
                <a href="/">Home</a>
                <a href="/guides/how-to-compress-images/">Guides</a>
                <a href="#faq">FAQ</a>
            </nav>
        </div>
    </header>
    <main>
        <div class="breadcrumb"><a href="/">Home</a> / <a href="/guides/">Guides</a> / {title.split('—')[0].strip()}</div>
        <section class="guide-hero">
            <div class="container">
                <h1>{title}</h1>
                <p class="subtitle" style="max-width:600px">{desc}</p>
            </div>
        </section>
        <article class="guide-body">
            {body_html}
        </article>
        <div class="guide-cta-box">
            <h3>Ready to compress your images?</h3>
            <p style="color:#475569;margin-bottom:12px">Try our free online image compressor — 18 target sizes, 100% browser-based, no upload.</p>
            <a href="/" style="display:inline-block;padding:12px 28px;background:var(--primary);color:#fff;border-radius:8px;font-weight:600;text-decoration:none">Start Compressing →</a>
        </div>
        <section class="faq-section" id="faq">
            <div class="container">
                <h2>Frequently Asked Questions</h2>
                {faq_html}
            </div>
        </section>
    </main>
    <footer>
        <div class="container">
            <p>&copy; 2026 CompressNow. All rights reserved. | <a href="/">Home</a> | <a href="/guides/how-to-compress-images/">Compression Guide</a> | <a href="/guides/image-formats-compared/">Format Guide</a></p>
            <p style="margin-top:8px;font-size:.8rem;color:#94A3B8">All processing happens locally in your browser. Your data is never uploaded.</p>
        </div>
    </footer>
</body>
</html>"""

# ═══ Pillar 1: Complete Guide to Image Compression ═══

PILLAR1_BODY = """
<p>Image compression is one of the most impactful things you can do for your website's performance — yet most people treat it as an afterthought. In this guide, we'll walk through <strong>everything you need to know about image compression</strong>: how it works, which format to choose, what file size to target, and how to compress images without killing quality.</p>

<h2>What Is Image Compression?</h2>
<p>Image compression is the process of reducing an image's file size while attempting to preserve its visual quality. There are two fundamental approaches:</p>

<h3>Lossy Compression</h3>
<p>Lossy compression permanently removes some image data to achieve smaller files. It works by discarding details the human eye is unlikely to notice — subtle color variations, high-frequency textures, and metadata. <strong>JPEG is the most common lossy format.</strong> A JPEG at quality 85 is typically 5-10x smaller than the original with no visible difference on screen.</p>

<h3>Lossless Compression</h3>
<p>Lossless compression reduces file size without discarding any image data. It works by finding patterns and redundancies in the data and encoding them more efficiently. <strong>PNG uses lossless compression.</strong> The trade-off: PNG files are typically 3-10x larger than JPEG for the same photograph.</p>

<h2>Why Image Size Matters</h2>
<p>Uncompressed or poorly compressed images are the #1 cause of slow-loading web pages. Here's why that matters:</p>

<ul>
<li><strong>Core Web Vitals:</strong> Google's LCP (Largest Contentful Paint) metric measures how fast the main content loads. Large images directly hurt this score — and poor Core Web Vitals hurt your search rankings.</li>
<li><strong>User Experience:</strong> 53% of mobile users abandon a site that takes longer than 3 seconds to load. Every 100KB of unnecessary image weight costs you visitors.</li>
<li><strong>Bandwidth Costs:</strong> If you're serving images from a CDN or cloud storage, every uncompressed megabyte costs real money in bandwidth.</li>
<li><strong>Conversion Rates:</strong> Amazon found that every 100ms of page load delay cost them 1% in revenue. For e-commerce, image optimization is revenue optimization.</li>
</ul>

<h2>How to Choose the Right Image Format</h2>

<table>
<thead><tr><th>Format</th><th>Compression</th><th>Best For</th><th>Not Good For</th><th>Browser Support</th></tr></thead>
<tbody>
<tr><td><strong>JPEG</strong></td><td>Lossy</td><td>Photos, web images, social media</td><td>Text, logos, graphics with sharp edges</td><td>100% (all browsers)</td></tr>
<tr><td><strong>PNG</strong></td><td>Lossless</td><td>Logos, icons, screenshots, graphics with transparency</td><td>Photos (files will be huge)</td><td>100%</td></tr>
<tr><td><strong>WebP</strong></td><td>Both</td><td>Websites — 25-35% smaller than JPEG/PNG</td><td>Legacy apps that don't support it</td><td>97%+ (all modern browsers)</td></tr>
<tr><td><strong>AVIF</strong></td><td>Both</td><td>Next-gen web — even smaller than WebP</td><td>Older browsers (Safari < 16)</td><td>~93%</td></tr>
<tr><td><strong>HEIC</strong></td><td>Both</td><td>iPhone photos (default format)</td><td>Web use (convert to JPEG/WebP first)</td><td>Safari only for web</td></tr>
</tbody>
</table>

<p><strong>Rule of thumb:</strong> Use JPEG for photos, PNG for graphics with transparency or text, and WebP whenever browser support allows — it's the best all-around web format today.</p>

<h2>How to Choose the Right File Size</h2>
<p>Different use cases demand different file sizes. Here's a practical guide:</p>

<table>
<thead><tr><th>Target Size</th><th>Best For</th><th>Example Use Cases</th></tr></thead>
<tbody>
<tr><td><strong>10-30KB</strong></td><td>Tiny icons, favicons, email signature logos</td><td>Browser tab icons, forum avatars, HTML email graphics</td></tr>
<tr><td><strong>50-100KB</strong></td><td>Web thumbnails, profile photos, passport/visa photos</td><td>Blog post featured images, LinkedIn headshots, government form uploads</td></tr>
<tr><td><strong>150-300KB</strong></td><td>Product photos, portfolio images, blog inline images</td><td>E-commerce product galleries, photography portfolios, article illustrations</td></tr>
<tr><td><strong>500KB-1MB</strong></td><td>High-quality web images, email attachments</td><td>Website hero banners, marketing materials, presentation images</td></tr>
<tr><td><strong>2-5MB</strong></td><td>Print-quality submissions, archives</td><td>Print-on-demand files, competition entries, archival copies</td></tr>
</tbody>
</table>

<p><strong>For most web images, target 100-200KB.</strong> This gives you a great balance of quality and loading speed. Google's PageSpeed Insights recommends keeping images under 200KB for optimal LCP scores.</p>

<h2>Step-by-Step: Compress Any Image with CompressNow</h2>
<ol>
<li><strong>Upload your image</strong> — drag and drop or click to select. Supports PNG, JPEG, WebP, and HEIC.</li>
<li><strong>Pick your target size</strong> — choose from 18 preset sizes (10KB to 5MB) or use the quality slider for manual control.</li>
<li><strong>Review the result</strong> — use the before/after comparison slider to check quality.</li>
<li><strong>Download</strong> — save the compressed image. No signup, no upload to any server.</li>
</ol>

<h2>Common Image Compression Mistakes</h2>
<ul>
<li><strong>Over-compressing:</strong> Pushing a photo down to 10KB will make it look terrible. Match the target size to the use case.</li>
<li><strong>Wrong format:</strong> Using PNG for photos produces files 5-10x larger than JPEG at the same visual quality.</li>
<li><strong>Not pre-compressing for platforms:</strong> Instagram, Twitter, and WhatsApp all apply their own compression. If you upload an already-large file, you're letting their algorithm decide your quality. Pre-compress to control the result.</li>
<li><strong>Ignoring dimensions:</strong> A 6000×4000 pixel image will always be large, even with aggressive compression. Resize to the actual display size first, then compress.</li>
<li><strong>Compressing already-compressed images:</strong> Re-compressing a JPEG creates generation loss — each pass degrades quality. Always work from the original when possible.</li>
</ul>

<h2>Compression for Specific Platforms</h2>
<p>Every major platform has its own file size limits and image requirements. We've built dedicated tools for many of them:</p>
<ul>
<li><a href="/compress-image-for-discord/">Discord</a> — 8MB free tier limit</li>
<li><a href="/compress-image-for-email/">Email</a> — 20-25MB provider limits</li>
<li><a href="/compress-image-for-whatsapp/">WhatsApp</a> — 16MB limit, but pre-compress for quality control</li>
<li><a href="/compress-image-for-instagram/">Instagram</a> — auto-compresses; pre-compress for best results</li>
<li><a href="/compress-image-for-twitter/">Twitter/X</a> — 5MB image limit</li>
<li><a href="/compress-image-for-website/">Websites</a> — keep images under 200KB for best Core Web Vitals</li>
</ul>
"""

PILLAR1_FAQ = [
    ("What's the best image format for the web?", "WebP offers the best compression-to-quality ratio for web use — files are 25-35% smaller than JPEG at the same visual quality. If you need universal compatibility, JPEG is the safest choice."),
    ("How much should I compress my images?", "For most websites, target 100-200KB per image. Hero banners can go up to 500KB. Product photos: 200-500KB. Thumbnails: 20-50KB."),
    ("Does compression reduce image quality?", "Light to moderate compression is virtually invisible to the human eye. A JPEG at quality 80-85 looks identical to the original on screen but is 5-10x smaller."),
    ("What's the difference between resizing and compressing?", "Resizing changes the pixel dimensions (e.g., 4000×3000 → 800×600). Compression reduces the file size in bytes while keeping the same dimensions. For best results, do both — resize to display size, then compress."),
    ("Can I compress images without uploading them to a server?", "Yes. CompressNow does all processing locally in your browser using the Canvas API — your images never leave your device."),
    ("Should I use WebP or AVIF?", "WebP is the safe bet today — 97%+ browser support, excellent compression. AVIF is even better (20-30% smaller than WebP) but has slightly lower browser support (~93%). Use WebP for now, consider AVIF in 2026+."),
]

# ═══ Pillar 2: Image Formats Compared ═════════════

PILLAR2_BODY = """
<p>Choosing the right image format is the single most important decision in image optimization. Use the wrong format and you'll either have bloated files or visible quality loss — sometimes both. This guide compares <strong>JPEG, PNG, WebP, AVIF, and HEIC</strong> across every dimension that matters: file size, quality, transparency, browser support, and best use cases.</p>

<h2>Format Comparison at a Glance</h2>

<table>
<thead><tr><th>Feature</th><th>JPEG</th><th>PNG</th><th>WebP</th><th>AVIF</th><th>HEIC</th></tr></thead>
<tbody>
<tr><td><strong>Compression Type</strong></td><td>Lossy</td><td>Lossless</td><td>Both</td><td>Both</td><td>Both</td></tr>
<tr><td><strong>Transparency</strong></td><td>❌ No</td><td>[OK] Yes</td><td>[OK] Yes</td><td>[OK] Yes</td><td>[OK] Yes</td></tr>
<tr><td><strong>Animation</strong></td><td>❌ No</td><td>❌ No (APNG exists)</td><td>[OK] Yes</td><td>[OK] Yes</td><td>❌ No</td></tr>
<tr><td><strong>Relative Size*</strong></td><td>1.0× (baseline)</td><td>3-10× larger</td><td>0.65-0.75×</td><td>0.45-0.55×</td><td>0.5-0.7×</td></tr>
<tr><td><strong>Max Color Depth</strong></td><td>8-bit (16.7M)</td><td>8-bit / 16-bit</td><td>8-bit</td><td>12-bit</td><td>16-bit</td></tr>
<tr><td><strong>HDR Support</strong></td><td>❌ No</td><td>❌ No</td><td>❌ No</td><td>[OK] Yes</td><td>[OK] Yes</td></tr>
<tr><td><strong>Browser Support</strong></td><td>100%</td><td>100%</td><td>~97%</td><td>~93%</td><td>Safari only</td></tr>
<tr><td><strong>Best For</strong></td><td>Photos, web</td><td>Logos, icons, UI</td><td>Modern web</td><td>Next-gen web</td><td>Apple ecosystem</td></tr>
</tbody>
</table>
<p style="font-size:.85rem;color:var(--text-secondary)">* Relative size for the same photographic image at equivalent visual quality. JPEG at quality 85 = baseline 1.0×.</p>

<h2>JPEG: The Universal Workhorse</h2>
<p>JPEG (Joint Photographic Experts Group) has been the standard for photographic images since 1992 — and for good reason. It offers <strong>excellent compression for photos</strong> with universal compatibility. Every browser, every app, every device supports JPEG.</p>
<h3>When to Use JPEG</h3>
<ul><li>Photographs and photo-realistic images</li><li>Web images where universal compatibility is paramount</li><li>Email attachments (every email client displays JPEG)</li><li>Social media uploads</li></ul>
<h3>When NOT to Use JPEG</h3>
<ul><li>Logos or icons with sharp edges (compression artifacts are visible)</li><li>Images with text (text becomes blurry in JPEG)</li><li>Images requiring transparency (JPEG doesn't support it)</li><li>Screenshots of UI (PNG is much better for this)</li></ul>

<h2>PNG: The Graphics Specialist</h2>
<p>PNG (Portable Network Graphics) uses lossless compression — every pixel is preserved exactly. This makes it <strong>perfect for graphics, logos, and text</strong>, but terrible for photographs where file sizes balloon to 3-10× the JPEG equivalent.</p>
<h3>When to Use PNG</h3>
<ul><li>Logos and brand marks</li><li>Icons and UI elements</li><li>Screenshots (especially of text-heavy interfaces)</li><li>Images requiring transparent backgrounds</li><li>Graphics with sharp edges and solid colors</li></ul>
<h3>When NOT to Use PNG</h3>
<ul><li>Photographs (use JPEG or WebP — files will be 5-10× smaller)</li><li>Large hero images (PNG will be megabytes)</li><li>Email attachments (JPEG is much smaller for photos)</li></ul>

<h2>WebP: The Modern All-Rounder</h2>
<p>Developed by Google and released in 2010, WebP has become the <strong>best general-purpose web image format</strong>. It supports both lossy and lossless compression, transparency, and animation — all at file sizes 25-35% smaller than JPEG and 25% smaller than PNG.</p>
<h3>When to Use WebP</h3>
<ul><li>Website images (WordPress, Shopify, and most CMS platforms support it)</li><li>Anywhere you currently use JPEG — WebP will be smaller at the same quality</li><li>Animated images (as a replacement for GIF)</li><li>Images with transparency that need smaller files than PNG</li></ul>
<h3>When NOT to Use WebP</h3>
<ul><li>Email (most email clients don't display WebP)</li><li>Apps that don't explicitly support it</li><li>When you need 100% browser compatibility</li></ul>

<h2>AVIF: The Future</h2>
<p>AVIF (AV1 Image File Format) is the newest contender, offering <strong>20-30% smaller files than WebP</strong> at equivalent quality, plus HDR support and 12-bit color depth. It's the best format technically — but browser support is still catching up.</p>
<h3>When to Use AVIF</h3>
<ul><li>Cutting-edge web projects where you can serve fallback formats</li><li>HDR image delivery</li><li>When every byte counts (mobile-first experiences)</li></ul>
<h3>When NOT to Use AVIF</h3>
<ul><li>Safari versions before 16 (use WebP fallback)</li><li>Email, social media, or any context where compatibility matters more than size</li></ul>

<h2>HEIC: The iPhone Native</h2>
<p>HEIC (High Efficiency Image Container) is Apple's default photo format since iOS 11. It offers excellent compression (50% smaller than JPEG) but has <strong>virtually no web browser support</strong> outside Safari. For web use, always convert HEIC to JPEG or WebP.</p>

<h2>Which Format Should You Use? Decision Guide</h2>
<ol>
<li><strong>Is it a photo for the web?</strong> → Use WebP with JPEG fallback, or JPEG for simplicity.</li>
<li><strong>Is it a logo, icon, or graphic with transparency?</strong> → Use PNG. Consider WebP if you need smaller files.</li>
<li><strong>Is it for email?</strong> → Use JPEG. Email clients don't support WebP.</li>
<li><strong>Is it for a cutting-edge web project?</strong> → Use AVIF with WebP/JPEG fallback.</li>
<li><strong>Is it from an iPhone?</strong> → Convert HEIC to JPEG or WebP before using on the web.</li>
</ol>

<p>You can convert between all these formats using our free <a href="/free-image-converter/">image format converter</a> — no upload, 100% browser-based.</p>
"""

PILLAR2_FAQ = [
    ("What's the best image format overall?", "WebP strikes the best balance of file size, quality, and browser support for web use in 2026. For universal compatibility, JPEG is still the safest choice."),
    ("Is PNG always better quality than JPEG?", "PNG is lossless, so it preserves every pixel exactly — but the files are much larger. For photos, a high-quality JPEG (85+) looks identical to a PNG on screen while being 5-10× smaller."),
    ("Should I convert all my images to WebP?", "For website use, yes — WebP will reduce your total image payload by 25-35%. For email and social media, stick with JPEG since those platforms don't support WebP uploads."),
    ("Does converting PNG to JPEG reduce quality?", "Converting from PNG (lossless) to JPEG (lossy) will cause some quality loss, but at quality 85+ it's usually invisible on screen while reducing file size by 80-95%."),
    ("Can I use AVIF everywhere yet?", "Not yet. Safari added AVIF support in version 16 (2022), but ~7% of browsers still don't support it. If you use AVIF, always provide WebP or JPEG fallback."),
    ("Why does my iPhone take HEIC photos?", "HEIC offers better compression than JPEG — Apple switched to it as the default format in iOS 11 to save storage space. You can change this in Settings > Camera > Formats."),
]

# ═══ Pillar 3: Image Compression for SEO ══════════

PILLAR3_BODY = """
<p>Image compression isn't just about saving disk space — <strong>it directly impacts your Google search rankings</strong>. Google's Core Web Vitals measure how fast your pages load, and oversized images are the most common cause of poor scores. This guide explains exactly how image compression affects SEO and what you can do about it.</p>

<h2>How Image Size Affects SEO</h2>
<p>Google uses three Core Web Vitals metrics to evaluate page experience:</p>
<ul>
<li><strong>LCP (Largest Contentful Paint):</strong> How fast the main content loads. Target: under 2.5 seconds. <strong>Large hero images are the #1 cause of poor LCP.</strong></li>
<li><strong>INP (Interaction to Next Paint):</strong> How fast the page responds to user input. Less directly affected by images.</li>
<li><strong>CLS (Cumulative Layout Shift):</strong> Visual stability. Images without width/height attributes cause layout shifts.</li>
</ul>
<p>Google has confirmed that Core Web Vitals are <strong>direct ranking signals</strong>. A page that fails LCP because of a 5MB hero image will rank lower than an otherwise identical page with a 200KB hero image.</p>

<h2>How Much Do Images Slow Down Your Site?</h2>
<p>Images typically account for <strong>50-70% of a web page's total weight</strong>. On an average e-commerce product page, images are 2-5MB. Compressed to 200KB each, that drops to 0.5-1MB — a 70-80% reduction in page weight.</p>
<p>That translates directly to faster load times. Google's own research shows:</p>
<ul>
<li>Going from 1s to 3s load time increases bounce probability by 32%</li>
<li>Going from 1s to 5s increases bounce probability by 90%</li>
<li>Every 0.1s improvement in load time can increase conversion rates by up to 8% (e-commerce)</li>
</ul>

<h2>Step-by-Step: Optimize Images for SEO</h2>
<ol>
<li><strong>Choose the right format:</strong> WebP for modern browsers, JPEG for universal compatibility, PNG only for graphics.</li>
<li><strong>Compress to the right size:</strong> Target 100-200KB for most images. Hero images: under 500KB. Thumbnails: under 50KB.</li>
<li><strong>Resize to display dimensions:</strong> Don't serve a 4000px-wide image in a 800px-wide container. Resize first.</li>
<li><strong>Use responsive images:</strong> The <code>&lt;picture&gt;</code> element with <code>srcset</code> lets you serve different sizes for mobile vs desktop.</li>
<li><strong>Add width and height attributes:</strong> This prevents CLS (layout shift) as images load.</li>
<li><strong>Lazy-load below-the-fold images:</strong> <code>loading="lazy"</code> tells the browser to defer off-screen images.</li>
<li><strong>Use a CDN:</strong> Serving images from a CDN reduces latency for users far from your origin server.</li>
</ol>

<h2>Real-World Before/After: Image Optimization Case Study</h2>
<p>Here's what happens when you optimize a typical blog post page with 5 images:</p>

<table>
<thead><tr><th>Metric</th><th>Before (Uncompressed)</th><th>After (Compressed)</th><th>Improvement</th></tr></thead>
<tbody>
<tr><td>Total image weight</td><td>12.4 MB</td><td>0.9 MB</td><td style="color:#16A34A">92.7% reduction</td></tr>
<tr><td>Page load time (3G)</td><td>6.2 seconds</td><td>1.8 seconds</td><td style="color:#16A34A">71% faster</td></tr>
<tr><td>LCP score</td><td>4.1s (fails)</td><td>1.9s (passes)</td><td style="color:#16A34A">Passes Core Web Vitals</td></tr>
<tr><td>PageSpeed score</td><td>42/100</td><td>89/100</td><td style="color:#16A34A">+47 points</td></tr>
</tbody>
</table>

<h2>Google's Image Guidelines for SEO</h2>
<ul>
<li>Use supported formats: JPEG, PNG, WebP, SVG, GIF, BMP</li>
<li>Optimize images for speed — Google explicitly recommends compression</li>
<li>Use descriptive filenames (not IMG_0047.jpg)</li>
<li>Add alt text to every image (accessibility + SEO signal)</li>
<li>Create an image sitemap or ensure images are in your regular sitemap</li>
<li>Use structured data for product images, recipes, and videos</li>
</ul>

<h2>Testing Your Image Optimization</h2>
<p>After compressing your images, verify the results:</p>
<ul>
<li><strong>Google PageSpeed Insights:</strong> <a href="https://pagespeed.web.dev/" rel="nofollow">pagespeed.web.dev</a> — tests LCP and flags oversized images</li>
<li><strong>Google Search Console:</strong> The Core Web Vitals report shows which pages need improvement</li>
<li><strong>WebPageTest:</strong> <a href="https://www.webpagetest.org/" rel="nofollow">webpagetest.org</a> — detailed waterfall view of image loading</li>
</ul>

<p>For an image-specific tool, use our <a href="/compress-image-for-pagespeed/">PageSpeed image compressor</a> — it targets the exact file sizes that help you pass Core Web Vitals.</p>
"""

PILLAR3_FAQ = [
    ("Does image compression affect SEO?", "Yes, directly. Large images slow down page loads, which hurts your Core Web Vitals scores. Poor Core Web Vitals = lower Google rankings."),
    ("What's the ideal image size for SEO?", "Google recommends keeping images under 200KB where possible. Hero images can be larger (up to 500KB), but anything above 1MB will likely hurt your LCP score."),
    ("Does WebP help with SEO?", "Yes. WebP files are 25-35% smaller than JPEG at the same quality, which means faster page loads and better Core Web Vitals — both positive SEO signals."),
    ("Should I use lazy loading for images?", "Yes, for images below the fold. Use loading='lazy' on img tags for images that aren't visible on initial page load. Don't lazy-load your hero image (above the fold) — it needs to load immediately for good LCP."),
    ("Do image alt tags affect SEO?", "Yes. Alt text helps Google understand image content and is a factor in image search rankings. It's also essential for accessibility."),
    ("How often should I audit my site's images?", "Run a PageSpeed Insights test monthly, and check Google Search Console's Core Web Vitals report weekly. Re-compress any images flagged as oversized."),
]

# ═══ Build sitemap ═══════════════════════════════

def build_sitemap():
    urls = ['https://' + DOMAIN + '/']
    urls += ['https://' + DOMAIN + '/' + s['slug'] + '/' for s in ALL_SCENARIOS]
    urls += [
        'https://' + DOMAIN + '/guides/how-to-compress-images/',
        'https://' + DOMAIN + '/guides/image-formats-compared/',
        'https://' + DOMAIN + '/guides/image-compression-for-seo/',
    ]
    # NOTE: NOINDEX pages are NOT included in the sitemap
    
    entries = []
    for u in urls:
        entries.append(f"""  <url>
    <loc>{u}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{'1.0' if u.endswith(DOMAIN+'/') else '0.9' if '/guides/' in u else '0.8'}</priority>
  </url>""")
    
    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(entries)}
</urlset>"""
    w("sitemap.xml", sitemap)
    return len(entries)

# ═══ Build robots.txt ═══════════════════════════

def build_robots():
    robots = f"""User-agent: *
Allow: /
Disallow: /deploy_out/

User-agent: GPTBot
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

Sitemap: https://{DOMAIN}/sitemap.xml
"""
    w("robots.txt", robots)

# ═══ Build llms.txt ═══════════════════════════

def build_llms_txt():
    llms = f"""# CompressNow
> Free online image compression tool — compress to exact sizes from 10KB to 5MB, 100% browser-based.

## Tools
- Image Compressor: https://{DOMAIN}/
- Bulk Compressor: https://{DOMAIN}/bulk-image-compressor/
- Format Converter: https://{DOMAIN}/free-image-converter/

## Guides
- How to Compress Images: https://{DOMAIN}/guides/how-to-compress-images/
- Image Formats Compared: https://{DOMAIN}/guides/image-formats-compared/
- Image Compression for SEO: https://{DOMAIN}/guides/image-compression-for-seo/

## Key Pages
"""
    for s in SIZES[:5]:
        llms += f"- {s['title'].split('—')[0].strip()}: https://{DOMAIN}/{s['slug']}/\n"
    for s in PLATFORMS[:5]:
        llms += f"- {s['title'].split('—')[0].strip()}: https://{DOMAIN}/{s['slug']}/\n"
    w("llms.txt", llms)

# ═══ Main ═══════════════════════════════════════

def validate_scenarios(data, name="数据"):
    required = ['slug', 'title', 'desc']
    for i, s in enumerate(data):
        for f in required:
            if f not in s:
                raise KeyError(f"{name}[{i}] 缺字段 '{f}' — 标题: {s.get('title', 'N/A')}")
    print(f"[OK] {name} validation passed: {len(data)} items")

if __name__ == "__main__":
    validate_scenarios(ALL_SCENARIOS, "ALL_SCENARIOS")
    
    # 1. Build homepage
    w("index.html", build_home())
    print("[PAGE] Homepage built")
    
    # 2. Build indexed scenario pages
    for s in ALL_SCENARIOS:
        w(f"{s['slug']}/index.html", build_scene_page(s))
    print(f"[PAGE] {len(ALL_SCENARIOS)} indexed scenario pages built")
    
    # 3. Build noindex pages (thin content, but keep accessible)
    for s in NOINDEX_FINAL:
        # Use a stripped template for noindex pages
        cat = s.get("cat", "special")
        size_val = s.get("size", "")
        title = s.get("title", "")
        if not title:
            slug_readable = s["slug"].replace("-", " ").title()
            title = f"{slug_readable} — Free Online | CompressNow"
        desc = s.get("desc", f"Compress images with CompressNow. Free, browser-based, instant.")
        
        # Build a stripped page with noindex
        content = ENRICHMENT.get(cat, ENRICHMENT["special"])
        faq_html = ""
        for q, a in content.get("faq", [])[:3]:
            faq_html += f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>'

        page = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><meta name="robots" content="noindex, follow"><meta name="description" content="{desc}"><link rel="canonical" href="https://{DOMAIN}/compress-image-to-100kb/"><title>{title}</title><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet"><script async src="https://www.googletagmanager.com/gtag/js?id=G-Z9NW1GSG04"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag("js",new Date());gtag("config","G-Z9NW1GSG04");</script><style>{STYLE_BLOCK}</style></head><body><header><div class="container"><a href="/" style="color:#fff;text-decoration:none;font-size:1.2rem;font-weight:700">CompressNow</a><nav><a href="/">Home</a><a href="/guides/how-to-compress-images/">Guides</a></nav></div></header><main><section class="scene-hero"><h1>{title}</h1><p class="subtitle">Compress images to exact sizes — free, browser-based, no upload. Try our main <a href="/compress-image-to-100kb/" style="color:var(--primary)">100KB compressor</a> or visit the <a href="/" style="color:var(--primary)">homepage</a> for all options.</p></section><section style="text-align:center;padding:40px 0"><a href="/" class="btn btn-primary">Go to CompressNow Home →</a></section></main><footer><div class="container"><p>&copy; 2026 CompressNow. | <a href="/">Home</a> | <a href="/guides/how-to-compress-images/">Guides</a></p></div></footer></body></html>"""
        w(f"{s['slug']}/index.html", page)
    print(f"[PAGE] {len(NOINDEX_FINAL)} noindex pages built")
    
    # 4. Build pillar guide pages
    w("guides/how-to-compress-images/index.html", build_guide_page(
        "guides/how-to-compress-images",
        "How to Compress Images — Complete Guide (2026) | CompressNow",
        "Learn everything about image compression: lossy vs lossless, how to choose the right format (JPEG, PNG, WebP, AVIF), what file size to target for web/email/social, and how to compress without losing quality.",
        PILLAR1_BODY,
        PILLAR1_FAQ
    ))
    print("[PAGE] Guide 1: How to Compress Images")
    
    w("guides/image-formats-compared/index.html", build_guide_page(
        "guides/image-formats-compared",
        "JPEG vs PNG vs WebP vs AVIF — Image Formats Compared (2026) | CompressNow",
        "Complete comparison of image formats: JPEG, PNG, WebP, AVIF, and HEIC. File size, quality, transparency, browser support, and when to use each format.",
        PILLAR2_BODY,
        PILLAR2_FAQ
    ))
    print("[PAGE] Guide 2: Image Formats Compared")
    
    w("guides/image-compression-for-seo/index.html", build_guide_page(
        "guides/image-compression-for-seo",
        "Image Compression for SEO — Improve Core Web Vitals & Rankings | CompressNow",
        "How image compression impacts SEO: Core Web Vitals, page speed, Google rankings. Step-by-step optimization guide with real before/after case study.",
        PILLAR3_BODY,
        PILLAR3_FAQ
    ))
    print("[PAGE] Guide 3: Image Compression for SEO")
    
    # 5. Build sitemap, robots.txt, llms.txt
    sitemap_count = build_sitemap()
    build_robots()
    build_llms_txt()
    
    print(f"\n[OK] Build Complete — {1 + len(ALL_SCENARIOS) + len(NOINDEX_FINAL) + 3} pages total")
    print(f"   [STATS] Indexed: {1 + len(ALL_SCENARIOS) + 3} | Noindex: {len(NOINDEX_FINAL)}")
    print(f"   [MAP]  Sitemap: {sitemap_count} URLs")
    print(f"   [GUIDE] Guides: 3 pillar pages")
