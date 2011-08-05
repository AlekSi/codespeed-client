import json
import platform
import sys

if platform.python_version_tuple()[0] == '3':
    from urllib.parse import urlencode
    from urllib.parse import urljoin
    from urllib.request import urlopen
    from urllib.error import HTTPError, URLError
else:
    from urllib import urlencode
    from urlparse import urljoin
    from urllib2 import urlopen
    from urllib2 import HTTPError, URLError


class Client(object):
    required = ('benchmark', 'commitid', 'project', 'result_value')
    combined = required + ('branch', 'environment', 'executable', 'revision_date',
                           'result_date', 'min', 'max', 'std_dev')

    @classmethod
    def _update(cls, item, kwargs):
        for k, v in kwargs.items():
            if k not in cls.combined:
                raise KeyError("Unexpected key %r" % (k,))
            if v is not None:
                item[k] = v

    def __init__(self, root_url, **kwargs):
        """
        kwargs passed there are defaults
        """

        self.url = urljoin(root_url, '/result/add/json/')
        self.data = []

        self.defaults = {
            'branch': 'default',
            'environment': platform.node(),
            'executable': sys.version.replace('\n', ' ')
        }
        self._update(self.defaults, kwargs)

    def add_result(self, **kwargs):
        """
        kwargs passed there overwrite defaults
        """

        item = self.defaults.copy()
        self._update(item, kwargs)

        missing = [k for k in self.required if k not in item]
        if missing:
            raise KeyError("Missing keys: %r" % missing)

        self.data.append(item)

    def upload_results(self):
        data, self.data = self.data, []
        try:
            f = urlopen(self.url, urlencode({'json': json.dumps(data)}).encode('ascii'))
            ok, code, body = True, f.getcode(), f.read()
            f.close()
        except HTTPError as e:
            ok, code, body = False, e.code, e.read()
        except URLError as e:
            ok, code, body = False, 'xxx', e.reason

        return (ok, code, body)
