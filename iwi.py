'''
A very basic Flask app to control my markdown files
'''

from flask import Flask, request, url_for, render_template
import markdown
import sys

# if the application is hidden behind a rewriting reverse proxy, append this
# path to static URLs
frontpath = '/iwi/'

app = Flask(__name__)

@app.route('/docs/<doc>', methods = ['GET'])
@app.route('/')
def index(doc='index.md'):
        if not doc.startswith('index'):
                doc = 'docs/{0}'.format(doc)
        try:
                with open(doc, 'r') as f:
                        md = f.read().decode('iso-8859-15') # .decode('utf-8')
                content = markdown.markdown(md, ['fenced_code'])
                return render_template('layout.html',
                                        content=content, frontpath=frontpath)
        except IOError:
                return ''

if __name__ == '__main__':
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = 5000
    app.run(host='0.0.0.0', port=int(port))
