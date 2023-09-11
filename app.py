import json
from flask import Flask
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return f'API using Flask that empowers users to seamlessly install, uninstall, and retrieve a list of installed pip packages. This API eliminates the need for users to directly interact with the command line for managing their pip packages.<br> EndPoints<br><br>/list : Get list of all installed pip packages with version.<br>/install: Install packages that are required<br>/uninstall: Uninstall a specific pip package from Computer.<br><br>MIT License<br>Copyright (c) 2023 Shivam Kumar<br>Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:<br>The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.<br>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.'

@app.route('/list')
def show_all_package():
   command = f'pip list'
   process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
   result , error = process.communicate()
   res = str(result, 'UTF-8')
   print(res)
   res = res.replace('\n', '<br>')
   return res

@app.route('/search/<package>')
def search_package(package):
   url = "https://pypi.org/project/"
   url += f'{package}'
   return redirect(url, code=302)

@app.route('/install/<package>')
def install_package(package):
   os.system(f'pip install {package}')
   return f"Installed {package}"

@app.route('/uninstall/<package>')
def uninstall_package(package):
   os.system(f'pip uninstall -y {package}')
   return f"Uninstalled {package}"

