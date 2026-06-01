import zipfile, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with zipfile.ZipFile('C:/Users/Administrator/Desktop/compressnow-deploy.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
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

print('\nDone! File saved to Desktop: compressnow-deploy.zip')
