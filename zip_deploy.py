import zipfile, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'deploy')
os.makedirs(OUTPUT_DIR, exist_ok=True)
with zipfile.ZipFile(os.path.join(OUTPUT_DIR, 'compressnow-deploy.zip'), 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk('.'):
        if '.git' in root:
            continue
        for f in files:
            if f == 'build.py' or f == 'zip_deploy.py' or f.endswith('.zip'):
                continue
            filepath = os.path.join(root, f)
            arcname = filepath[2:] if filepath.startswith('./') else filepath
            zf.write(filepath, arcname)
            print(f'  Added: {arcname}')

print(f'\nDone! File saved to: {os.path.join(OUTPUT_DIR, "compressnow-deploy.zip")}')
