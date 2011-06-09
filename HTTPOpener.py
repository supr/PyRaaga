from urllib2 import build_opener

class HTTPOpener(object):
    def __init__(self):
        ua_header = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.35 (KHTML, like Gecko) Chrome/13.0.761.0 Safari/534.35')]
        self.opener = build_opener()
        self.opener.addheaders = ua_header

    def open(self, url, headers = None):
        if headers:
            self.opener.addheaders = headers
        return self.opener.open(url)

    def close(self):
        return self.opener.close()

    def __del__(self):
        return self.opener.close()
