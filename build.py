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

# Additional long-tail pages (batch 1)
EXTRA = [
    # File size variants (photo)
    {"slug":"compress-photo-to-20kb","title":"Compress Photo to 20KB — Reduce Picture Size Free","desc":"Compress photos to exactly 20KB. Perfect for forms and strict upload limits. Free, browser-based, instant.","cat":"size","size":"20 KB"},
    {"slug":"compress-photo-to-50kb","title":"Compress Photo to 50KB — Reduce Picture Size Free","desc":"Compress photos to exactly 50KB. Great for email and web thumbnails. Free, browser-based, instant.","cat":"size","size":"50 KB"},
    {"slug":"compress-photo-to-100kb","title":"Compress Photo to 100KB — Reduce Picture Size Free","desc":"Compress photos to exactly 100KB. Most popular target size. Free, browser-based, instant.","cat":"size","size":"100 KB"},
    {"slug":"compress-photo-to-200kb","title":"Compress Photo to 200KB — Reduce Picture Size Free","desc":"Compress photos to exactly 200KB. Great for product photos. Free, browser-based, instant.","cat":"size","size":"200 KB"},
    {"slug":"compress-photo-to-500kb","title":"Compress Photo to 500KB — Reduce Picture Size Free","desc":"Compress photos to exactly 500KB. Good quality, smaller size. Free, browser-based, instant.","cat":"size","size":"500 KB"},
    # File size variants (image-compressor)
    {"slug":"image-compressor-to-100kb","title":"Image Compressor to 100KB — Free Online Tool","desc":"Compress any image to 100KB instantly. Free online image compressor, no upload needed.","cat":"size","size":"100 KB"},
    {"slug":"image-compressor-to-200kb","title":"Image Compressor to 200KB — Free Online Tool","desc":"Compress any image to 200KB instantly. Free online image compressor, no upload needed.","cat":"size","size":"200 KB"},
    {"slug":"image-compressor-to-500kb","title":"Image Compressor to 500KB — Free Online Tool","desc":"Compress any image to 500KB instantly. Free online image compressor, no upload needed.","cat":"size","size":"500 KB"},
    # File size variants (reduce/convert)
    {"slug":"reduce-image-size-to-100kb","title":"Reduce Image Size to 100KB — Free Online Tool","desc":"Reduce image file size to 100KB. Free, browser-based, instant compression.","cat":"size","size":"100 KB"},
    {"slug":"convert-image-to-100kb","title":"Convert Image to 100KB — Free Online Tool","desc":"Convert any image to 100KB file size. Free, browser-based, instant.","cat":"size","size":"100 KB"},

    # Passport/Visa/Government
    {"slug":"compress-passport-photo-to-20kb","title":"Compress Passport Photo to 20KB — Meet Requirements","desc":"Compress passport photo to 20KB for government applications. Free, browser-based, instant.","cat":"size","size":"20 KB"},
    {"slug":"compress-passport-photo-to-50kb","title":"Compress Passport Photo to 50KB — Meet Requirements","desc":"Compress passport photo to 50KB for visa and ID applications. Free, browser-based, instant.","cat":"size","size":"50 KB"},
    {"slug":"compress-passport-photo-to-100kb","title":"Compress Passport Photo to 100KB — Meet Requirements","desc":"Compress passport photo to 100KB for online applications. Free, browser-based, instant.","cat":"size","size":"100 KB"},
    {"slug":"passport-photo-compressor","title":"Passport Photo Compressor — Free Online Tool","desc":"Compress passport photos to meet government size requirements. Free, no upload, instant.","cat":"platform"},
    {"slug":"compress-image-for-visa-application","title":"Compress Image for Visa Application — Meet Size Limits","desc":"Compress photos for visa applications. Meet embassy file size requirements. Free, instant.","cat":"platform"},
    {"slug":"compress-photo-for-visa","title":"Compress Photo for Visa — Meet Embassy Requirements","desc":"Compress visa photos to required file size. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-image-for-immigration-form","title":"Compress Image for Immigration Form — Meet Upload Limits","desc":"Compress images for immigration form uploads. Meet government requirements. Free, instant.","cat":"platform"},
    {"slug":"photo-compressor-for-government-form","title":"Photo Compressor for Government Forms — Free Tool","desc":"Compress photos for government form submissions. Meet strict file size limits. Free, instant.","cat":"platform"},
    {"slug":"reduce-passport-photo-size","title":"Reduce Passport Photo Size — Free Online Tool","desc":"Reduce passport photo file size for online submissions. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-image-for-online-application","title":"Compress Image for Online Application — Meet Limits","desc":"Compress images for online job/application submissions. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-image-for-embassy-application","title":"Compress Image for Embassy Application — Meet Requirements","desc":"Compress images for embassy applications. Meet strict file size limits. Free, instant.","cat":"platform"},
    {"slug":"compress-image-for-id-card","title":"Compress Image for ID Card — Meet Size Requirements","desc":"Compress photos for ID card applications. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-photo-for-id-card","title":"Compress Photo for ID Card — Free Online Tool","desc":"Compress ID card photos to required size. Free, browser-based, instant.","cat":"platform"},
    {"slug":"resize-passport-photo-online","title":"Resize Passport Photo Online — Free Tool","desc":"Resize passport photos to meet government dimensions. Free, browser-based, instant.","cat":"platform"},
    {"slug":"passport-image-size-reducer","title":"Passport Image Size Reducer — Free Online Tool","desc":"Reduce passport image file size for online submissions. Free, no upload, instant.","cat":"platform"},
    {"slug":"compress-image-for-citizenship-application","title":"Compress Image for Citizenship Application — Free","desc":"Compress photos for citizenship applications. Meet government requirements. Free, instant.","cat":"platform"},
    {"slug":"compress-image-for-government-upload","title":"Compress Image for Government Upload — Meet Limits","desc":"Compress images for government portal uploads. Free, browser-based, instant.","cat":"platform"},
    {"slug":"passport-photo-under-100kb","title":"Passport Photo Under 100KB — Free Online Compressor","desc":"Compress passport photos to under 100KB. Meet online application limits. Free, instant.","cat":"size","size":"100 KB"},
    {"slug":"passport-photo-under-50kb","title":"Passport Photo Under 50KB — Free Online Compressor","desc":"Compress passport photos to under 50KB. Meet strict government limits. Free, instant.","cat":"size","size":"50 KB"},

    # Discord extended
    {"slug":"discord-image-compressor","title":"Discord Image Compressor — Free Online Tool","desc":"Compress images for Discord uploads. Bypass file size limits. Free, browser-based, instant.","cat":"platform"},
    {"slug":"discord-image-size-reducer","title":"Discord Image Size Reducer — Free Online Tool","desc":"Reduce image file size for Discord. Free, no upload, instant.","cat":"platform"},
    {"slug":"reduce-image-size-for-discord","title":"Reduce Image Size for Discord — Free Tool","desc":"Reduce image size to meet Discord's upload limits. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-photo-for-discord","title":"Compress Photo for Discord — Free Online Tool","desc":"Compress photos for Discord sharing. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-png-for-discord","title":"Compress PNG for Discord — Free Online Tool","desc":"Compress PNG images for Discord uploads. Free, browser-based, instant.","cat":"format"},
    {"slug":"compress-jpg-for-discord","title":"Compress JPG for Discord — Free Online Tool","desc":"Compress JPG images for Discord uploads. Free, browser-based, instant.","cat":"format"},
    {"slug":"compress-screenshot-for-discord","title":"Compress Screenshot for Discord — Free Tool","desc":"Compress screenshots for Discord sharing. Free, browser-based, instant.","cat":"platform"},
    {"slug":"discord-avatar-size-reducer","title":"Discord Avatar Size Reducer — Free Online Tool","desc":"Reduce Discord avatar image size. Free, browser-based, instant.","cat":"platform"},
    {"slug":"discord-profile-image-compressor","title":"Discord Profile Image Compressor — Free Tool","desc":"Compress Discord profile images. Free, browser-based, instant.","cat":"platform"},
    {"slug":"discord-banner-image-compressor","title":"Discord Banner Image Compressor — Free Tool","desc":"Compress Discord banner images. Free, browser-based, instant.","cat":"platform"},

    # Email extended
    {"slug":"compress-photo-for-email","title":"Compress Photo for Email — Free Online Tool","desc":"Compress photos for email attachments. Free, browser-based, instant.","cat":"platform"},
    {"slug":"reduce-image-size-for-email","title":"Reduce Image Size for Email — Free Tool","desc":"Reduce image size for email attachments. Free, browser-based, instant.","cat":"platform"},
    {"slug":"email-attachment-image-compressor","title":"Email Attachment Image Compressor — Free Tool","desc":"Compress images for email attachments. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-jpg-for-email","title":"Compress JPG for Email — Free Online Tool","desc":"Compress JPG images for email. Free, browser-based, instant.","cat":"format"},
    {"slug":"compress-png-for-email","title":"Compress PNG for Email — Free Online Tool","desc":"Compress PNG images for email. Free, browser-based, instant.","cat":"format"},
    {"slug":"compress-screenshot-for-email","title":"Compress Screenshot for Email — Free Tool","desc":"Compress screenshots for email sharing. Free, browser-based, instant.","cat":"platform"},
    {"slug":"resize-image-for-email","title":"Resize Image for Email — Free Online Tool","desc":"Resize images for email attachments. Free, browser-based, instant.","cat":"platform"},
    {"slug":"email-image-optimizer","title":"Email Image Optimizer — Free Online Tool","desc":"Optimize images for email delivery. Free, browser-based, instant.","cat":"platform"},
    {"slug":"reduce-attachment-size","title":"Reduce Attachment Size — Free Online Tool","desc":"Reduce email attachment file size. Free, browser-based, instant.","cat":"platform"},
    {"slug":"image-attachment-compressor","title":"Image Attachment Compressor — Free Tool","desc":"Compress image attachments for email. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-images-before-emailing","title":"Compress Images Before Emailing — Free Tool","desc":"Compress images before sending via email. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-image-under-1mb","title":"Compress Image Under 1MB — Free Online Tool","desc":"Compress images to under 1MB for email. Free, browser-based, instant.","cat":"size","size":"1 MB"},
    {"slug":"compress-image-under-500kb","title":"Compress Image Under 500KB — Free Online Tool","desc":"Compress images to under 500KB. Free, browser-based, instant.","cat":"size","size":"500 KB"},
    {"slug":"compress-image-under-200kb","title":"Compress Image Under 200KB — Free Online Tool","desc":"Compress images to under 200KB. Free, browser-based, instant.","cat":"size","size":"200 KB"},
    {"slug":"photo-compressor-for-email","title":"Photo Compressor for Email — Free Online Tool","desc":"Compress photos for email attachments. Free, browser-based, instant.","cat":"platform"},
    {"slug":"image-reducer-for-email","title":"Image Reducer for Email — Free Online Tool","desc":"Reduce image size for email. Free, browser-based, instant.","cat":"platform"},
    {"slug":"email-photo-size-reducer","title":"Email Photo Size Reducer — Free Tool","desc":"Reduce photo size for email. Free, browser-based, instant.","cat":"platform"},
]

# Batch 2: WhatsApp, Social Media, Website Optimization
EXTRA2 = [
    # WhatsApp extended
    {"slug":"whatsapp-image-compressor","title":"WhatsApp Image Compressor — Free Online Tool","desc":"Compress images for WhatsApp sharing. Free, browser-based, instant.","cat":"platform"},
    {"slug":"reduce-image-size-for-whatsapp","title":"Reduce Image Size for WhatsApp — Free Tool","desc":"Reduce image size for WhatsApp. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-photo-for-whatsapp","title":"Compress Photo for WhatsApp — Free Online Tool","desc":"Compress photos for WhatsApp. Free, browser-based, instant.","cat":"platform"},
    {"slug":"whatsapp-image-size-reducer","title":"WhatsApp Image Size Reducer — Free Tool","desc":"Reduce WhatsApp image file size. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-jpg-for-whatsapp","title":"Compress JPG for WhatsApp — Free Online Tool","desc":"Compress JPG images for WhatsApp. Free, browser-based, instant.","cat":"format"},
    {"slug":"compress-png-for-whatsapp","title":"Compress PNG for WhatsApp — Free Online Tool","desc":"Compress PNG images for WhatsApp. Free, browser-based, instant.","cat":"format"},
    {"slug":"resize-image-for-whatsapp","title":"Resize Image for WhatsApp — Free Online Tool","desc":"Resize images for WhatsApp sharing. Free, browser-based, instant.","cat":"platform"},
    {"slug":"whatsapp-profile-photo-compressor","title":"WhatsApp Profile Photo Compressor — Free Tool","desc":"Compress WhatsApp profile photos. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-image-before-sending-whatsapp","title":"Compress Image Before Sending WhatsApp — Free","desc":"Compress images before sending on WhatsApp. Free, browser-based, instant.","cat":"platform"},
    {"slug":"whatsapp-image-optimizer","title":"WhatsApp Image Optimizer — Free Online Tool","desc":"Optimize images for WhatsApp. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-screenshot-for-whatsapp","title":"Compress Screenshot for WhatsApp — Free Tool","desc":"Compress screenshots for WhatsApp sharing. Free, browser-based, instant.","cat":"platform"},
    {"slug":"whatsapp-dp-photo-compressor","title":"WhatsApp DP Photo Compressor — Free Tool","desc":"Compress WhatsApp display picture. Free, browser-based, instant.","cat":"platform"},
    {"slug":"whatsapp-photo-size-reducer","title":"WhatsApp Photo Size Reducer — Free Tool","desc":"Reduce WhatsApp photo file size. Free, browser-based, instant.","cat":"platform"},

    # Social Media extended
    {"slug":"compress-image-for-threads","title":"Compress Image for Threads — Free Online Tool","desc":"Compress images for Threads posts. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-image-for-x","title":"Compress Image for X/Twitter — Free Online Tool","desc":"Compress images for X/Twitter posts. Free, browser-based, instant.","cat":"platform"},
    {"slug":"social-media-image-compressor","title":"Social Media Image Compressor — Free Tool","desc":"Compress images for any social media platform. Free, browser-based, instant.","cat":"platform"},
    {"slug":"resize-image-for-instagram","title":"Resize Image for Instagram — Free Online Tool","desc":"Resize images for Instagram posts and stories. Free, browser-based, instant.","cat":"platform"},
    {"slug":"instagram-image-size-reducer","title":"Instagram Image Size Reducer — Free Tool","desc":"Reduce image size for Instagram. Free, browser-based, instant.","cat":"platform"},
    {"slug":"optimize-image-for-instagram","title":"Optimize Image for Instagram — Free Tool","desc":"Optimize images for Instagram uploads. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-profile-photo","title":"Compress Profile Photo — Free Online Tool","desc":"Compress profile photos for any platform. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-cover-photo","title":"Compress Cover Photo — Free Online Tool","desc":"Compress cover/banner photos. Free, browser-based, instant.","cat":"platform"},

    # Website Optimization extended
    {"slug":"website-image-compressor","title":"Website Image Compressor — Free Online Tool","desc":"Compress images for websites. Improve loading speed. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-image-for-seo","title":"Compress Image for SEO — Free Online Tool","desc":"Compress images for better SEO rankings. Free, browser-based, instant.","cat":"platform"},
    {"slug":"image-optimization-for-website","title":"Image Optimization for Website — Free Tool","desc":"Optimize images for website performance. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-images-for-web","title":"Compress Images for Web — Free Online Tool","desc":"Compress images for web publishing. Free, browser-based, instant.","cat":"platform"},
    {"slug":"web-image-optimizer","title":"Web Image Optimizer — Free Online Tool","desc":"Optimize images for web. Free, browser-based, instant.","cat":"platform"},
    {"slug":"website-speed-image-compressor","title":"Website Speed Image Compressor — Free Tool","desc":"Compress images to speed up website. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-image-without-losing-quality","title":"Compress Image Without Losing Quality — Free","desc":"Compress images while preserving quality. Free, browser-based, instant.","cat":"format"},
    {"slug":"optimize-website-images","title":"Optimize Website Images — Free Online Tool","desc":"Optimize all website images for speed. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-hero-image","title":"Compress Hero Image — Free Online Tool","desc":"Compress hero banner images for websites. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-blog-images","title":"Compress Blog Images — Free Online Tool","desc":"Compress images for blog posts. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-png-for-website","title":"Compress PNG for Website — Free Online Tool","desc":"Compress PNG images for websites. Free, browser-based, instant.","cat":"format"},
    {"slug":"compress-jpg-for-website","title":"Compress JPG for Website — Free Online Tool","desc":"Compress JPG images for websites. Free, browser-based, instant.","cat":"format"},
    {"slug":"image-optimizer-online","title":"Image Optimizer Online — Free Tool","desc":"Optimize images online for free. Browser-based, instant.","cat":"format"},
    {"slug":"website-performance-image-compressor","title":"Website Performance Image Compressor — Free","desc":"Compress images for website performance. Free, browser-based, instant.","cat":"platform"},
]

# Batch 3: E-commerce, Format Conversion extended, AI Upload
EXTRA3 = [
    # E-commerce extended
    {"slug":"product-image-compressor","title":"Product Image Compressor — Free Online Tool","desc":"Compress product images for e-commerce. Free, browser-based, instant.","cat":"platform"},
    {"slug":"amazon-image-optimizer","title":"Amazon Image Optimizer — Free Online Tool","desc":"Optimize images for Amazon listings. Free, browser-based, instant.","cat":"platform"},
    {"slug":"shopify-image-compressor","title":"Shopify Image Compressor — Free Online Tool","desc":"Compress images for Shopify stores. Free, browser-based, instant.","cat":"platform"},
    {"slug":"ebay-photo-compressor","title":"eBay Photo Compressor — Free Online Tool","desc":"Compress photos for eBay listings. Free, browser-based, instant.","cat":"platform"},
    {"slug":"etsy-image-size-reducer","title":"Etsy Image Size Reducer — Free Tool","desc":"Reduce image size for Etsy listings. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-catalog-images","title":"Compress Catalog Images — Free Online Tool","desc":"Compress product catalog images. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-product-photos","title":"Compress Product Photos — Free Online Tool","desc":"Compress product photos for e-commerce. Free, browser-based, instant.","cat":"platform"},
    {"slug":"optimize-ecommerce-images","title":"Optimize E-commerce Images — Free Tool","desc":"Optimize images for e-commerce stores. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-image-for-online-store","title":"Compress Image for Online Store — Free Tool","desc":"Compress images for online stores. Free, browser-based, instant.","cat":"platform"},
    {"slug":"reduce-product-image-size","title":"Reduce Product Image Size — Free Tool","desc":"Reduce product image file size. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-listing-images","title":"Compress Listing Images — Free Online Tool","desc":"Compress marketplace listing images. Free, browser-based, instant.","cat":"platform"},
    {"slug":"product-photo-size-reducer","title":"Product Photo Size Reducer — Free Tool","desc":"Reduce product photo file size. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-images-for-ecommerce","title":"Compress Images for E-commerce — Free Tool","desc":"Compress images for e-commerce platforms. Free, browser-based, instant.","cat":"platform"},

    # Format Conversion extended
    {"slug":"heic-to-jpg","title":"Convert HEIC to JPG Online — Free, Instant","desc":"Convert HEIC/HEIF photos to JPG format. Free, browser-based, no upload.","cat":"conversion"},
    {"slug":"heic-to-png","title":"Convert HEIC to PNG Online — Free, Instant","desc":"Convert HEIC/HEIF photos to PNG format. Free, browser-based, no upload.","cat":"conversion"},
    {"slug":"avif-to-jpg","title":"Convert AVIF to JPG Online — Free, Instant","desc":"Convert AVIF images to JPG format. Free, browser-based, no upload.","cat":"conversion"},
    {"slug":"avif-to-png","title":"Convert AVIF to PNG Online — Free, Instant","desc":"Convert AVIF images to PNG format. Free, browser-based, no upload.","cat":"conversion"},
    {"slug":"image-format-converter","title":"Image Format Converter — Free Online Tool","desc":"Convert between any image format. Free, browser-based, instant.","cat":"conversion"},
    {"slug":"free-image-converter","title":"Free Image Converter — Online Format Conversion","desc":"Free online image format converter. No upload needed.","cat":"conversion"},
    {"slug":"batch-image-converter","title":"Batch Image Converter — Convert Multiple Images Free","desc":"Convert multiple images at once. Free, browser-based, instant.","cat":"conversion"},
    {"slug":"convert-photo-format","title":"Convert Photo Format — Free Online Tool","desc":"Convert photo formats online. Free, browser-based, instant.","cat":"conversion"},
    {"slug":"jpg-converter-online","title":"JPG Converter Online — Free Format Conversion","desc":"Convert images to/from JPG format. Free, browser-based.","cat":"conversion"},
    {"slug":"png-converter-online","title":"PNG Converter Online — Free Format Conversion","desc":"Convert images to/from PNG format. Free, browser-based.","cat":"conversion"},
    {"slug":"webp-converter-online","title":"WebP Converter Online — Free Format Conversion","desc":"Convert images to/from WebP format. Free, browser-based.","cat":"conversion"},
    {"slug":"image-file-converter","title":"Image File Converter — Free Online Tool","desc":"Convert image files between formats. Free, browser-based, instant.","cat":"conversion"},

    # AI Upload scenarios
    {"slug":"compress-image-for-chatgpt","title":"Compress Image for ChatGPT — Free Online Tool","desc":"Compress images for ChatGPT uploads. Meet file size limits. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-image-for-claude","title":"Compress Image for Claude — Free Online Tool","desc":"Compress images for Claude AI uploads. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-image-for-gemini","title":"Compress Image for Gemini — Free Online Tool","desc":"Compress images for Google Gemini uploads. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-image-for-ai-upload","title":"Compress Image for AI Upload — Free Tool","desc":"Compress images for AI tool uploads. Free, browser-based, instant.","cat":"platform"},
    {"slug":"reduce-image-size-for-ai","title":"Reduce Image Size for AI — Free Online Tool","desc":"Reduce image size for AI processing. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-screenshot-for-chatgpt","title":"Compress Screenshot for ChatGPT — Free Tool","desc":"Compress screenshots for ChatGPT. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-image-before-ai-upload","title":"Compress Image Before AI Upload — Free Tool","desc":"Compress images before uploading to AI tools. Free, browser-based, instant.","cat":"platform"},
    {"slug":"image-compressor-for-ai-tools","title":"Image Compressor for AI Tools — Free Online","desc":"Compress images for AI tools. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-image-for-midjourney","title":"Compress Image for Midjourney — Free Online Tool","desc":"Compress images for Midjourney. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-image-for-stable-diffusion","title":"Compress Image for Stable Diffusion — Free","desc":"Compress images for Stable Diffusion. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-image-for-ai-training","title":"Compress Image for AI Training — Free Tool","desc":"Compress images for AI model training datasets. Free, browser-based, instant.","cat":"platform"},
    {"slug":"reduce-image-size-for-ai-processing","title":"Reduce Image Size for AI Processing — Free","desc":"Reduce image size for AI processing. Free, browser-based, instant.","cat":"platform"},
    {"slug":"ai-image-upload-compressor","title":"AI Image Upload Compressor — Free Online Tool","desc":"Compress images for AI uploads. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-dataset-images","title":"Compress Dataset Images — Free Online Tool","desc":"Compress images for machine learning datasets. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-image-for-machine-learning","title":"Compress Image for Machine Learning — Free","desc":"Compress images for ML training. Free, browser-based, instant.","cat":"platform"},
    {"slug":"image-optimizer-for-ai","title":"Image Optimizer for AI — Free Online Tool","desc":"Optimize images for AI tools. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-image-for-vision-models","title":"Compress Image for Vision Models — Free Tool","desc":"Compress images for AI vision models. Free, browser-based, instant.","cat":"platform"},
    {"slug":"compress-image-for-multimodal-ai","title":"Compress Image for Multimodal AI — Free Tool","desc":"Compress images for multimodal AI systems. Free, browser-based, instant.","cat":"platform"},
    {"slug":"ai-image-size-reducer","title":"AI Image Size Reducer — Free Online Tool","desc":"Reduce image size for AI applications. Free, browser-based, instant.","cat":"platform"},
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
for s in EXTRA:
    if "cat" not in s:
        s["cat"] = "special"
    ALL_SCENARIOS.append(s)
for s in EXTRA2:
    if "cat" not in s:
        s["cat"] = "special"
    ALL_SCENARIOS.append(s)
for s in EXTRA3:
    if "cat" not in s:
        s["cat"] = "special"
    ALL_SCENARIOS.append(s)

# ═══ Enrichment ════════════════════════════════════

# ═══ Platform-specific content database ════════════════
PLATFORM_DATA = {
    "discord": {
        "name": "Discord",
        "limit": "8MB (free) / 25MB (Nitro)",
        "formats": "PNG, JPG, GIF, WebP",
        "about": "Discord免费用户上传文件限制为8MB，Nitro用户为25MB。当你的截图、GIF动图或高清照片超过限制时，会被提示'文件过大'。本工具可以将图片压缩到8MB以下，让你顺利发送。",
        "faq": [
            ("Discord的图片上传限制是多少？", "Discord免费用户单个文件限制为8MB，Nitro Basic为50MB，Nitro为500MB。超过限制的图片需要压缩后才能上传。"),
            ("压缩后图片会模糊吗？", "我们的智能压缩算法在减小文件大小的同时尽可能保持图片清晰度。对于截图和照片，压缩后几乎看不出区别。"),
            ("支持哪些图片格式？", "支持PNG、JPG、JPEG、GIF和WebP格式。压缩后会自动保留原始格式。"),
            ("GIF动图也能压缩吗？", "可以。上传GIF文件后，工具会自动压缩到目标大小，同时保留动画效果。"),
        ],
        "how_to": [
            "点击上方的上传区域，选择你要发送的图片或截图",
            "工具会自动将图片压缩到8MB以下（Discord免费用户限制）",
            "点击下载按钮，将压缩后的图片保存到本地",
            "打开Discord，将压缩后的图片拖入聊天窗口发送",
        ],
        "tips": "Discord支持PNG、JPG、GIF、WebP格式。如果你的截图超过8MB，建议使用JPG格式压缩，文件会更小。Nitro用户可以上传最大50MB的文件，但压缩后发送速度更快。",
    },
    "whatsapp": {
        "name": "WhatsApp",
        "limit": "16MB",
        "formats": "JPG, PNG, GIF",
        "about": "WhatsApp单张图片发送限制为16MB。高清照片通常超过这个限制，导致发送失败或被自动压缩变模糊。使用本工具预先压缩图片，可以在保持清晰度的同时确保发送成功。",
        "faq": [
            ("WhatsApp图片大小限制是多少？", "WhatsApp单个文件发送限制为16MB。超过此大小的图片会被自动压缩，但压缩后质量可能下降。"),
            ("怎么发送高清图片不被压缩？", "在WhatsApp设置中可以选择'以文档方式发送'来保持原图质量，但文件仍需小于16MB。使用我们的工具压缩到16MB以下即可。"),
            ("WhatsApp状态视频也能压缩吗？", "本工具支持图片压缩。视频压缩请使用专门的视频压缩工具。"),
            ("压缩后的图片在手机上能正常显示吗？", "可以。压缩后的图片格式不变，在任何设备上都能正常显示。"),
        ],
        "how_to": [
            "选择你要发送的图片，上传到上方工具",
            "工具自动将图片压缩到16MB以下",
            "下载压缩后的图片到手机",
            "打开WhatsApp聊天窗口，选择压缩后的图片发送",
        ],
        "tips": "WhatsApp会自动压缩大图片，但压缩后质量会明显下降。建议先用我们的工具压缩到合适大小，再发送，这样可以控制压缩质量。",
    },
    "email": {
        "name": "Email",
        "limit": "25MB (Gmail) / 20MB (Outlook) / 25MB (Yahoo)",
        "formats": "JPG, PNG, GIF, BMP",
        "about": "大多数邮箱的附件大小限制在20-25MB之间（Gmail 25MB，Outlook 20MB，Yahoo 25MB）。当你要发送多张图片或高清照片时，很容易超过限制。本工具可以将图片压缩到合适的大小，让你顺利发送邮件附件。",
        "faq": [
            ("邮箱附件大小限制是多少？", "Gmail为25MB，Outlook为20MB，Yahoo为25MB。超过限制的邮件会被退回。"),
            ("压缩后图片质量会下降吗？", "轻微压缩几乎看不出区别。如果需要发送高清图片，建议压缩到200KB-500KB之间。"),
            ("可以一次压缩多张图片吗？", "可以。上传多张图片后，工具会逐个压缩，然后打包下载。"),
            ("压缩后的图片能打印吗？", "可以。只要压缩后的分辨率足够（建议300DPI以上），打印效果不会有明显差别。"),
        ],
        "how_to": [
            "将需要发送的图片上传到上方工具",
            "工具自动将每张图片压缩到合适的大小",
            "下载压缩后的图片",
            "在邮件客户端中添加压缩后的图片作为附件发送",
        ],
        "tips": "Gmail附件限制为25MB，Outlook为20MB。如果要发送多张图片，建议每张压缩到200KB-500KB之间，这样可以同时发送10-20张图片而不超过限制。",
    },
    "instagram": {
        "name": "Instagram",
        "limit": "30MB (照片) / 650MB (视频)",
        "formats": "JPG, PNG",
        "about": "Instagram支持JPG和PNG格式的图片上传，建议分辨率为1080x1080像素（正方形）或1080x1350像素（竖版）。虽然Instagram会自动压缩图片，但预先压缩可以确保上传速度更快，画质更可控。",
        "faq": [
            ("Instagram图片最佳尺寸是多少？", "正方形帖子建议1080x1080像素，竖版建议1080x1350像素，横版建议1080x566像素。"),
            ("Instagram会自动压缩图片吗？", "是的，Instagram会自动压缩上传的图片。预先压缩可以控制最终质量。"),
            ("Stories和Reels的图片尺寸一样吗？", "Stories和Reels建议使用1080x1920像素（9:16比例）。"),
            ("上传失败怎么办？", "如果上传失败，可能是图片太大或格式不支持。使用我们的工具压缩后重试。"),
        ],
        "how_to": [
            "将照片上传到上方工具",
            "工具自动压缩到Instagram推荐的大小",
            "下载压缩后的照片",
            "打开Instagram，选择压缩后的照片上传",
        ],
        "tips": "Instagram建议图片宽度为1080像素。如果图片太大，Instagram会自动压缩，但可能导致画质下降。预先压缩到1MB以内可以获得最佳效果。",
    },
    "facebook": {
        "name": "Facebook",
        "limit": "10MB (照片) / 25MB (文件)",
        "formats": "JPG, PNG, GIF, BMP",
        "about": "Facebook照片上传限制为10MB，文件分享限制为25MB。高清照片通常超过10MB限制，上传时会被自动压缩。使用本工具预先压缩，可以控制图片质量，同时加快上传速度。",
        "faq": [
            ("Facebook图片大小限制是多少？", "照片上传限制为10MB，文件分享限制为25MB。"),
            ("Facebook会压缩上传的图片吗？", "是的，Facebook会自动压缩图片。预先压缩可以控制最终质量。"),
            ("封面照片和头像有什么尺寸要求？", "封面照片建议820x312像素，头像建议170x170像素。"),
            ("相册上传有数量限制吗？", "单次最多可上传100张照片。"),
        ],
        "how_to": [
            "将照片上传到上方工具",
            "工具自动压缩到Facebook推荐的大小",
            "下载压缩后的照片",
            "在Facebook中选择压缩后的照片上传",
        ],
        "tips": "Facebook建议照片宽度为2048像素以获得最佳显示效果。但如果文件太大，上传速度会很慢。建议压缩到1MB以内。",
    },
    "twitter": {
        "name": "Twitter/X",
        "limit": "5MB (图片) / 15MB (GIF)",
        "formats": "JPG, PNG, GIF, WebP",
        "about": "Twitter/X的图片上传限制为5MB，GIF限制为15MB。超过限制的图片无法上传。本工具可以将图片压缩到5MB以下，让你顺利发布。",
        "faq": [
            ("Twitter图片大小限制是多少？", "单张图片限制为5MB，GIF限制为15MB。"),
            ("Twitter支持哪些图片格式？", "支持JPG、PNG、GIF和WebP格式。"),
            ("Twitter会压缩上传的图片吗？", "是的，Twitter会自动压缩图片，特别是JPG格式。预先压缩可以控制质量。"),
            ("怎么上传高清图片？", "使用PNG格式上传可以保留更多细节，但文件会更大。"),
        ],
        "how_to": [
            "将图片上传到上方工具",
            "工具自动压缩到5MB以下",
            "下载压缩后的图片",
            "在Twitter/X中发布压缩后的图片",
        ],
        "tips": "Twitter建议图片比例为16:9或1:1。PNG格式保留更多细节但文件更大，JPG格式文件更小但可能有压缩痕迹。",
    },
    "linkedin": {
        "name": "LinkedIn",
        "limit": "10MB (照片) / 20MB (文件)",
        "formats": "JPG, PNG, GIF",
        "about": "LinkedIn照片上传限制为10MB，文件分享限制为20MB。专业头像和封面照片需要在限制内保持高质量。本工具可以帮助你压缩图片，同时保持专业外观。",
        "faq": [
            ("LinkedIn头像尺寸是多少？", "建议400x400像素，最小为200x200像素。"),
            ("LinkedIn封面照片尺寸是多少？", "个人封面建议1584x396像素，公司封面建议1128x191像素。"),
            ("帖子图片有什么要求？", "建议宽度为1200像素，比例为1.91:1或1:1。"),
            ("LinkedIn会压缩图片吗？", "是的，LinkedIn会自动压缩图片。预先压缩可以控制质量。"),
        ],
        "how_to": [
            "将照片上传到上方工具",
            "工具自动压缩到LinkedIn推荐的大小",
            "下载压缩后的照片",
            "在LinkedIn中上传压缩后的照片",
        ],
        "tips": "LinkedIn是专业社交平台，头像和封面照片的质量很重要。建议压缩到500KB以内，同时保持清晰度。",
    },
    "pinterest": {
        "name": "Pinterest",
        "limit": "20MB",
        "formats": "JPG, PNG, GIF",
        "about": "Pinterest图片上传限制为20MB。Pinterest是图片驱动的平台，图片质量很重要。本工具可以帮助你压缩图片到合适大小，同时保持高质量。",
        "faq": [
            ("Pinterest图片最佳尺寸是多少？", "建议比例为2:3，推荐宽度为1000像素。"),
            ("Pinterest支持哪些格式？", "支持JPG、PNG和GIF格式。"),
            ("怎么让Pin获得更多曝光？", "使用高质量、竖版图片，添加详细描述和关键词。"),
            ("Pinterest会压缩图片吗？", "是的，Pinterest会自动压缩图片。预先压缩可以控制质量。"),
        ],
        "how_to": [
            "将图片上传到上方工具",
            "工具自动压缩到合适大小",
            "下载压缩后的图片",
            "在Pinterest中创建新Pin并上传压缩后的图片",
        ],
        "tips": "Pinterest建议使用竖版图片（2:3比例），宽度至少1000像素。压缩到1MB以内可以获得最佳效果。",
    },
    "tiktok": {
        "name": "TikTok",
        "limit": "2MB (头像) / 10MB (视频封面)",
        "formats": "JPG, PNG",
        "about": "TikTok头像上传限制为2MB，视频封面限制为10MB。本工具可以帮助你压缩图片到合适大小。",
        "faq": [
            ("TikTok头像尺寸是多少？", "建议200x200像素，文件大小不超过2MB。"),
            ("TikTok视频封面尺寸是多少？", "建议1080x1920像素，文件大小不超过10MB。"),
            ("TikTok支持哪些图片格式？", "支持JPG和PNG格式。"),
            ("怎么制作吸引人的封面？", "使用高清图片，添加文字说明，保持与视频内容相关。"),
        ],
        "how_to": [
            "将图片上传到上方工具",
            "工具自动压缩到TikTok限制以内",
            "下载压缩后的图片",
            "在TikTok中上传压缩后的图片",
        ],
        "tips": "TikTok是竖屏平台，建议使用9:16比例的图片。头像建议200x200像素，视频封面建议1080x1920像素。",
    },
    "youtube": {
        "name": "YouTube",
        "limit": "2MB (缩略图) / 6MB (频道头像)",
        "formats": "JPG, PNG, GIF, BMP",
        "about": "YouTube缩略图上传限制为2MB，频道头像限制为6MB。高质量的缩略图可以提高视频点击率。本工具可以帮助你压缩图片到合适大小。",
        "faq": [
            ("YouTube缩略图尺寸是多少？", "建议1280x720像素，最小宽度为640像素。"),
            ("YouTube频道头像尺寸是多少？", "建议800x800像素，显示为圆形。"),
            ("YouTube频道封面尺寸是多少？", "建议2560x1440像素，安全区域为1546x423像素。"),
            ("缩略图文件大小限制是多少？", "限制为2MB，建议使用JPG格式。"),
        ],
        "how_to": [
            "将缩略图或头像上传到上方工具",
            "工具自动压缩到YouTube限制以内",
            "下载压缩后的图片",
            "在YouTube Studio中上传压缩后的图片",
        ],
        "tips": "YouTube缩略图对视频点击率影响很大。建议使用1280x720像素的JPG格式，文件控制在1MB以内。",
    },
    "website": {
        "name": "Website",
        "limit": "无固定限制（建议单张<200KB）",
        "formats": "JPG, PNG, WebP, GIF, SVG",
        "about": "网站图片加载速度直接影响用户体验和SEO排名。Google建议单张图片控制在200KB以内，使用WebP格式可以获得更好的压缩效果。本工具可以帮助你优化网站图片，提高页面加载速度。",
        "faq": [
            ("网站图片应该多大？", "Google建议单张图片控制在200KB以内。Hero图片可以稍大，但不要超过500KB。"),
            ("WebP格式有什么优势？", "WebP格式比JPG小25-35%，比PNG小25%，同时保持相同质量。"),
            ("图片大小会影响SEO吗？", "是的。图片过大会导致页面加载慢，影响Google排名。Google Core Web Vitals会评估图片加载性能。"),
            ("怎么批量压缩网站图片？", "使用我们的工具逐个压缩，或者使用WordPress插件自动压缩。"),
        ],
        "how_to": [
            "将网站图片上传到上方工具",
            "工具自动压缩到Web优化大小",
            "下载压缩后的图片",
            "将压缩后的图片上传到网站服务器",
        ],
        "tips": "Google Core Web Vitals会评估图片加载性能。建议使用WebP格式，单张图片控制在200KB以内，使用懒加载技术。",
    },
    "wordpress": {
        "name": "WordPress",
        "limit": "取决于主机（通常2-10MB）",
        "formats": "JPG, PNG, GIF, WebP, SVG",
        "about": "WordPress默认图片上传限制取决于主机设置，通常为2-10MB。大型图片会占用服务器空间，影响网站加载速度。本工具可以帮助你压缩图片到合适大小。",
        "faq": [
            ("WordPress图片上传限制是多少？", "取决于主机设置，通常为2-10MB。可以在php.ini中修改upload_max_filesize。"),
            ("WordPress会自动压缩图片吗？", "是的，WordPress会自动生成不同尺寸的缩略图。但原图不会被压缩。"),
            ("有什么WordPress插件可以自动压缩？", "推荐ShortPixel、Imagify、Smush等插件。"),
            ("怎么恢复WordPress压缩前的图片？", "如果使用了插件压缩，通常可以恢复。如果是手动压缩，需要重新上传原图。"),
        ],
        "how_to": [
            "将图片上传到上方工具",
            "工具自动压缩到WordPress推荐的大小",
            "下载压缩后的图片",
            "在WordPress媒体库中上传压缩后的图片",
        ],
        "tips": "WordPress建议图片宽度不超过2048像素。使用WebP格式可以获得更好的压缩效果，但需要主机支持。",
    },
    "shopify": {
        "name": "Shopify",
        "limit": "20MB",
        "formats": "JPG, PNG, GIF, WebP",
        "about": "Shopify产品图片上传限制为20MB。高质量的产品图片可以提高转化率，但文件太大会影响页面加载速度。本工具可以帮助你压缩产品图片到合适大小。",
        "faq": [
            ("Shopify产品图片尺寸是多少？", "建议2048x2048像素，正方形比例。"),
            ("Shopify会压缩产品图片吗？", "是的，Shopify会自动生成不同尺寸的缩略图。但原图不会被压缩。"),
            ("产品图片应该用什么格式？", "建议使用JPG格式，文件更小。PNG格式适合需要透明背景的图片。"),
            ("怎么提高产品图片加载速度？", "压缩图片到200KB以内，使用懒加载，使用CDN加速。"),
        ],
        "how_to": [
            "将产品图片上传到上方工具",
            "工具自动压缩到Shopify推荐的大小",
            "下载压缩后的图片",
            "在Shopify后台上传压缩后的产品图片",
        ],
        "tips": "Shopify建议产品图片为正方形，2048x2048像素。压缩到200KB以内可以提高页面加载速度，提高转化率。",
    },
    "amazon": {
        "name": "Amazon",
        "limit": "10MB",
        "formats": "JPG, PNG, GIF",
        "about": "Amazon产品图片上传限制为10MB。Amazon要求主图为白色背景，最小1000x1000像素。高质量的产品图片可以提高转化率。本工具可以帮助你压缩产品图片到合适大小。",
        "faq": [
            ("Amazon产品图片尺寸是多少？", "主图最小1000x1000像素，建议2000x2000像素。"),
            ("Amazon主图有什么要求？", "必须是白色背景，产品占图片85%以上，不能有文字或水印。"),
            ("Amazon支持哪些图片格式？", "支持JPG、PNG和GIF格式。建议使用JPG格式。"),
            ("可以上传多少张产品图片？", "最多可以上传9张产品图片，其中1张为主图。"),
        ],
        "how_to": [
            "将产品图片上传到上方工具",
            "工具自动压缩到Amazon推荐的大小",
            "下载压缩后的图片",
            "在Amazon Seller Central上传压缩后的产品图片",
        ],
        "tips": "Amazon要求主图为白色背景，最小1000x1000像素。建议使用2000x2000像素的JPG格式，文件控制在1MB以内。",
    },
    "ebay": {
        "name": "eBay",
        "limit": "7MB",
        "formats": "JPG, PNG, GIF, BMP",
        "about": "eBay产品图片上传限制为7MB。eBay建议使用白色背景，最小500x500像素。高质量的产品图片可以提高销售。本工具可以帮助你压缩产品图片到合适大小。",
        "faq": [
            ("eBay产品图片尺寸是多少？", "最小500x500像素，建议1600x1600像素。"),
            ("eBay主图有什么要求？", "建议白色背景，产品占图片85%以上。"),
            ("eBay支持哪些图片格式？", "支持JPG、PNG、GIF和BMP格式。"),
            ("可以上传多少张产品图片？", "最多可以上传12张产品图片。"),
        ],
        "how_to": [
            "将产品图片上传到上方工具",
            "工具自动压缩到eBay推荐的大小",
            "下载压缩后的图片",
            "在eBay Seller Hub上传压缩后的产品图片",
        ],
        "tips": "eBay建议使用白色背景，最小500x500像素。建议使用1600x1600像素的JPG格式，文件控制在1MB以内。",
    },
    "etsy": {
        "name": "Etsy",
        "limit": "20MB",
        "formats": "JPG, PNG, GIF",
        "about": "Etsy产品图片上传限制为20MB。Etsy建议使用正方形比例，最小2000x2000像素。高质量的产品图片可以提高销售。本工具可以帮助你压缩产品图片到合适大小。",
        "faq": [
            ("Etsy产品图片尺寸是多少？", "建议2000x2000像素，正方形比例。"),
            ("Etsy支持哪些图片格式？", "支持JPG、PNG和GIF格式。"),
            ("Etsy会压缩产品图片吗？", "是的，Etsy会自动生成不同尺寸的缩略图。"),
            ("可以上传多少张产品图片？", "最多可以上传10张产品图片。"),
        ],
        "how_to": [
            "将产品图片上传到上方工具",
            "工具自动压缩到Etsy推荐的大小",
            "下载压缩后的图片",
            "在Etsy Shop Manager上传压缩后的产品图片",
        ],
        "tips": "Etsy建议使用正方形比例，2000x2000像素。压缩到1MB以内可以提高页面加载速度。",
    },
    "passport": {
        "name": "Passport/Visa",
        "limit": "通常50KB-500KB",
        "formats": "JPG, PNG",
        "about": "护照、签证和政府申请通常要求照片在50KB-500KB之间。不同国家和机构有不同的尺寸和文件大小要求。本工具可以将照片精确压缩到要求的大小。",
        "faq": [
            ("护照照片尺寸是多少？", "中国护照照片尺寸为33mm×48mm，美国护照照片尺寸为2x2英寸（51x51mm）。"),
            ("护照照片文件大小限制是多少？", "不同机构要求不同，通常在50KB-500KB之间。"),
            ("护照照片有什么要求？", "通常要求白色背景，正面免冠，不能戴眼镜，表情自然。"),
            ("可以用手机拍护照照片吗？", "可以，但需要确保光线均匀，背景白色，面部清晰。"),
        ],
        "how_to": [
            "拍摄或扫描护照照片",
            "将照片上传到上方工具",
            "设置目标文件大小（如100KB）",
            "下载压缩后的照片，用于申请提交",
        ],
        "tips": "不同国家和机构对护照照片的要求不同。建议先查看具体要求，然后设置相应的目标文件大小。通常要求白色背景，正面免冠。",
    },
    "seo": {
        "name": "SEO",
        "limit": "建议单张<200KB",
        "formats": "JPG, PNG, WebP",
        "about": "图片大小直接影响网站加载速度，而加载速度是Google排名的重要因素。Google Core Web Vitals会评估LCP（最大内容绘制）指标，大图片会导致LCP变差。本工具可以帮助你压缩图片，提高SEO排名。",
        "faq": [
            ("图片大小会影响SEO吗？", "是的。图片过大会导致页面加载慢，影响Google Core Web Vitals评分，从而影响排名。"),
            ("什么是Core Web Vitals？", "Core Web Vitals是Google评估网站用户体验的指标，包括LCP（加载速度）、FID（交互延迟）、CLS（布局偏移）。"),
            ("WebP格式对SEO有帮助吗？", "是的。WebP格式比JPG小25-35%，可以显著提高页面加载速度。"),
            ("怎么批量压缩网站图片？", "使用我们的工具逐个压缩，或者使用WordPress插件自动压缩。"),
        ],
        "how_to": [
            "将网站图片上传到上方工具",
            "工具自动压缩到SEO推荐的大小",
            "下载压缩后的图片",
            "将压缩后的图片上传到网站",
        ],
        "tips": "Google Core Web Vitals建议LCP小于2.5秒。压缩图片是提高LCP最有效的方法之一。建议使用WebP格式，单张图片控制在200KB以内。",
    },
    "ecommerce": {
        "name": "E-commerce",
        "limit": "取决于平台（通常10-20MB）",
        "formats": "JPG, PNG, WebP",
        "about": "电商平台的产品图片质量直接影响转化率。高质量图片可以提高30%以上的转化率，但文件太大会影响页面加载速度。本工具可以帮助你压缩产品图片到合适大小。",
        "faq": [
            ("产品图片应该多大？", "建议至少1000x1000像素，文件控制在200KB-500KB之间。"),
            ("产品图片用什么格式最好？", "JPG格式适合大多数产品图片，PNG格式适合需要透明背景的图片。"),
            ("怎么提高产品图片质量？", "使用良好的光线，白色背景，多角度拍摄，后期适当调整。"),
            ("产品图片会影响销售吗？", "是的。高质量的产品图片可以提高30%以上的转化率。"),
        ],
        "how_to": [
            "将产品图片上传到上方工具",
            "工具自动压缩到电商平台推荐的大小",
            "下载压缩后的图片",
            "在电商平台上上传压缩后的产品图片",
        ],
        "tips": "产品图片质量直接影响转化率。建议使用白色背景，多角度拍摄，压缩到200KB-500KB之间。",
    },
    "ai": {
        "name": "AI Tools",
        "limit": "取决于工具（通常10-20MB）",
        "formats": "JPG, PNG, WebP, GIF",
        "about": "AI工具如ChatGPT、Claude、Gemini等通常有图片上传限制。大图片会导致上传失败或处理速度变慢。本工具可以帮助你压缩图片到AI工具的限制以内。",
        "faq": [
            ("ChatGPT图片上传限制是多少？", "ChatGPT Plus用户单张图片限制为20MB，免费用户限制更小。"),
            ("Claude图片上传限制是多少？", "Claude单张图片限制为10MB。"),
            ("压缩后图片会影响AI识别吗？", "轻微压缩不会影响AI识别。但如果压缩过度，可能会影响细节识别。"),
            ("AI工具支持哪些图片格式？", "大多数AI工具支持JPG、PNG、WebP和GIF格式。"),
        ],
        "how_to": [
            "将图片上传到上方工具",
            "工具自动压缩到AI工具的限制以内",
            "下载压缩后的图片",
            "在AI工具中上传压缩后的图片",
        ],
        "tips": "AI工具通常有图片上传限制。建议压缩到10MB以内，使用JPG或PNG格式。如果需要AI识别细节，不要过度压缩。",
    },
    "format": {
        "name": "Format Conversion",
        "limit": "无固定限制",
        "formats": "JPG, PNG, WebP, GIF, BMP, TIFF",
        "about": "不同的图片格式有不同的特点：JPG适合照片，PNG适合图形和透明图片，WebP是现代网页的最佳选择。本工具可以帮你在不同格式之间转换，同时压缩文件大小。",
        "faq": [
            ("JPG和PNG有什么区别？", "JPG是有损压缩，文件更小；PNG是无损压缩，支持透明，文件更大。"),
            ("WebP格式有什么优势？", "WebP比JPG小25-35%，比PNG小25%，同时保持相同质量。"),
            ("什么时候用PNG格式？", "需要透明背景、图形、图标、截图时使用PNG格式。"),
            ("什么时候用JPG格式？", "照片、不需要透明背景的图片使用JPG格式。"),
        ],
        "how_to": [
            "将图片上传到上方工具",
            "选择目标格式（JPG、PNG、WebP等）",
            "工具自动转换并压缩",
            "下载转换后的图片",
        ],
        "tips": "JPG适合照片，PNG适合图形和透明图片，WebP是现代网页的最佳选择。根据用途选择合适的格式。",
    },
}

# Generic enrichment for pages without specific platform data
ENRICHMENT = {
    "size": {
        "how_to": [
            "上传或拖拽图片到上方工具区域",
            "工具会自动压缩到目标文件大小",
            "点击下载按钮保存压缩后的图片",
        ],
        "tips": "压缩到精确的KB大小适用于政府表格、护照照片、求职申请等有严格文件大小限制的场景。我们的工具使用智能压缩算法，可以精确命中目标大小。",
        "faq": [
            ("可以压缩到精确的文件大小吗？", "可以。上传图片后，工具会自动压缩到目标大小。如果第一次没达到目标，可以手动调整质量参数。"),
            ("压缩后图片质量会下降吗？", "轻微压缩几乎看不出区别。如果需要极小的文件大小，可能会有轻微质量损失。"),
            ("支持哪些图片格式？", "支持PNG、JPG、JPEG、WebP格式。压缩后会自动保留原始格式。"),
        ],
    },
    "platform": {
        "how_to": [
            "点击上方的上传区域，选择要压缩的图片",
            "工具会自动压缩到平台要求的大小",
            "点击下载按钮保存压缩后的图片",
            "将压缩后的图片上传到对应平台",
        ],
        "tips": "每个平台对图片大小和格式有不同的要求。我们的工具会根据目标平台自动优化压缩参数，在文件大小和图片质量之间找到最佳平衡。",
        "faq": [
            ("平台图片大小限制是多少？", "不同平台有不同的限制。请查看上方工具区域的说明，或访问平台官网了解具体要求。"),
            ("压缩后图片能正常显示吗？", "可以。压缩后的图片格式不变，在任何设备和平台上都能正常显示。"),
            ("支持哪些图片格式？", "支持PNG、JPG、JPEG、WebP格式。压缩后会自动保留原始格式。"),
        ],
    },
    "format": {
        "how_to": [
            "上传图片（PNG、JPEG或WebP格式）",
            "工具会自动应用格式特定的压缩算法",
            "下载压缩后的图片，质量保持不变",
        ],
        "tips": "不同图片格式有不同的压缩特性：PNG适合图形和透明图片，JPEG适合照片，WebP是现代网页的最佳选择。我们的工具会根据格式自动选择最佳压缩方法。",
        "faq": [
            ("JPG和PNG有什么区别？", "JPG是有损压缩，文件更小；PNG是无损压缩，支持透明，文件更大。"),
            ("WebP格式有什么优势？", "WebP比JPG小25-35%，比PNG小25%，同时保持相同质量。"),
            ("压缩后格式会改变吗？", "不会。压缩后会保留原始格式。如果需要转换格式，请使用格式转换工具。"),
        ],
    },
    "special": {
        "how_to": [
            "上传一张或多张图片到上方工具",
            "设置压缩参数（质量、目标大小、格式）",
            "点击压缩按钮，等待处理完成",
            "下载所有压缩后的图片",
        ],
        "tips": "批量压缩可以节省大量时间。我们的工具在浏览器本地处理，图片不会上传到服务器，确保隐私安全。",
        "faq": [
            ("可以一次压缩多少张图片？", "没有数量限制。但建议每次不超过20张，以确保浏览器性能。"),
            ("压缩后图片会上传到服务器吗？", "不会。所有处理都在浏览器本地完成，您的图片永远不会离开您的设备。"),
            ("压缩后图片质量会下降吗？", "轻微压缩几乎看不出区别。如果需要极小的文件大小，可能会有轻微质量损失。"),
        ],
    },
    "conversion": {
        "how_to": [
            "上传图片到上方工具",
            "工具会自动转换为目标格式",
            "下载转换后的图片",
        ],
        "tips": "不同格式有不同的用途：PNG支持透明，适合图形；JPG适合照片，文件更小；WebP是现代网页的最佳选择，压缩率最高。",
        "faq": [
            ("转换后质量会下降吗？", "从无损格式（PNG）转为有损格式（JPG）可能会有轻微质量损失。从有损转无损不会提高质量。"),
            ("可以批量转换格式吗？", "可以。上传多张图片后，工具会逐个转换，然后打包下载。"),
            ("WebP格式兼容性好吗？", "现代浏览器都支持WebP格式。如果需要兼容旧浏览器，建议使用JPG或PNG。"),
        ],
    },
}

def get_content(s):
    """Get platform-specific or generic content for a scenario page."""
    slug = s.get("slug", "")
    cat = s.get("cat", "special")

    # Try to find platform-specific content
    for key, data in PLATFORM_DATA.items():
        if key in slug:
            return data

    # Return generic content based on category
    return ENRICHMENT.get(cat, ENRICHMENT["special"])

# ═══ Page Template ═════════════════════════════════

def build_scene_page(s):
    # Get platform-specific or generic content
    content = get_content(s)
    how_to_html = "".join(f"<p>Step {i+1}: {step}</p>" for i, step in enumerate(content["how_to"]))

    # Generate FAQ HTML from content
    faq_html = ""
    for q, a in content.get("faq", []):
        faq_html += f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>'

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
        "mainEntity": [{','.join('{{"@type":"Question","name":"'+q+'","acceptedAnswer":{{"@type":"Answer","text":"'+a+'"}}}}' for q, a in content.get('faq', [])[:4])}]
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
            <p>{content.get('about', desc)}</p>
            <h2>How to Use</h2>
            {how_to_html}
            <h2>Tips</h2>
            <p>{content.get('tips', '')}</p>
        </section>
        <div class="cross-site">
            <strong>Pro Tip</strong> — After compressing your image, use <a href="https://cvbuild-ai.com">CVBuild-AI</a> to build your resume, <a href="https://messagegen-ai.com">MessageGen-AI</a> to write professional emails, and <a href="https://tonemodifier.com">ToneModifier</a> to perfect your tone.
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
