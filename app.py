import json
from flask import Flask
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def show_all_package():
   command = f'pip list'
   process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
   result , error = process.communicate()
   res = str(result, 'UTF-8')
   print(res)
   res = res.replace('\n', '<br>')
   return res


@app.route('/install/<package>')
def install_package(package):
   os.system(f'pip install {package}')
   return f"Installed {package}"

@app.route('/uninstall/<package>')
def uninstall_package(package):
   os.system(f'pip uninstall -y {package}')
   return f"Uninstalled {package}"

if __name__ == '__main__':
    app.run()
