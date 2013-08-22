## iWi, a lightweight Markdown Wiki

**iWi** is a very simple system I use in order to view my [Markdown][1] documents.
**iWi** only renders a `.md` file, it does not permit to edit the pages. I originally wrote it for my own use, and thought it might be of use to others.

**iWi** has very little dependencies:

* [Flask][2], the fabulous `python` web development _microframework_
* [Markdown][3], a [markdown][1] module for `python`

It bundles [Twitter Bootstrap][4] so the articles do not look like _raw_ 1990-ish _HTML_, but are nicely styled instead.

*iWi* installation is quite straightforward, just `git clone` the project and make the application available through some [WSGI][5]. As an example, here's my [uWSGI][6] `.ini` file:

```
http = :9090
uid = imil
gid = wheel
chdir = /home/imil/www//iwi
wsgi-file = iwi.py
callable = app
processes = 1
threads = 2
daemonize = /home/imil/log/uwsgi.log
```

Enjoy!

[1]: http://daringfireball.net/projects/markdown/
[2]: http://flask.pocoo.org/
[3]: https://pypi.python.org/pypi/Markdown
[4]: http://getbootstrap.com/
[5]: http://en.wikipedia.org/wiki/Web_Server_Gateway_Interface
[6]: http://uwsgi-docs.readthedocs.org/en/latest/
