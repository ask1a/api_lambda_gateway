# Code stub taken from https://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory

import os
import zipfile

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

base_dir = os.getcwd()

os.chdir('layers/pkgs_pd_sk_jlb')
zipf = zipfile.ZipFile('pkgs_pd_sk_jlb_lambda.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('python/', zipf)
zipf.close()
