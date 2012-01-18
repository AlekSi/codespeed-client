import json
import platform
import sys

if sys.version_info[0] == 3:
    from urllib.parse import urlencode
    from urllib.parse import urljoin
    from urllib.request import urlopen
    from urllib.error import HTTPError, URLError
else:
    from urllib import urlencode
    from urlparse import urljoin
    from urllib2 import urlopen
    from urllib2 import HTTPError, URLError


class UploadError(IOError):
    pass


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

        try:
            pypy_version = '%d.%d.%d' % sys.pypy_version_info[:3]
        except AttributeError:
            pypy_version = None

        self.defaults = {
            'branch': 'default',
            'environment': platform.node().lower(),
            'executable': '%s %s' % (platform.python_implementation(), pypy_version or platform.python_version())
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
            code, body = int(f.getcode()), f.read()
            f.close()
        except HTTPError as e:
            raise UploadError(int(e.code), e.read())
        except URLError as e:
            raise UploadError(0, e.reason)

        return (code, body)
