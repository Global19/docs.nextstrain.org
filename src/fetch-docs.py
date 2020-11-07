#!/usr/bin/env python
import subprocess

edit_warning = '<!-- DONT EDIT THIS FILE OR YOU WILL LOSE YOUR CHANGES -->'
auspice_branch = 'migrate-docs'
auspice_url = f'https://raw.githubusercontent.com/nextstrain/auspice/{auspice_branch}/docs/'

docs = {
    f'{auspice_url}narratives/create-pdf.md': 'guides/communicate/create-pdf.md',
}

if __name__ == '__main__':
    for source_url, dest_path in docs.items():
        subprocess.check_call(['curl', source_url, '--compressed', '-o', dest_path])
