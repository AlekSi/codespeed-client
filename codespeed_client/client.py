import json
import platform
import urllib
import urllib2
import urlparse
import sys

class Client(object):
    required = ('benchmark', 'commitid', 'project', 'result_value')
    combined = required + ('branch', 'environment', 'executable', 'revision_date',
                           'result_date', 'min', 'max', 'std_dev')

    @classmethod
    def _update(cls, item, kwargs):
        for k, v in kwargs.iteritems():
            if k not in cls.combined:
                raise KeyError("Unexpected key %r" % (k,))
            if v is not None:
                item[k] = v

    def __init__(self, root_url, **kwargs):
        self.url = urlparse.urljoin(root_url, '/result/add/json/')
        self.data = []

        self.defaults = {
            'branch': 'default',
            'environment': platform.node(),
            'executable': sys.version.replace('\n', ' ')
        }
        self._update(self.defaults, kwargs)

    def add_result(self, **kwargs):
        item = self.defaults.copy()
        self._update(item, kwargs)

        missing = [k for k in self.required if k not in item]
        if missing:
            raise KeyError("Missing keys: %r" % missing)

        self.data.append(item)

    def upload_results(self):
        data, self.data = self.data, []
        try:
            f = urllib2.urlopen(self.url, urllib.urlencode({'json': json.dumps(data)}))
            ok, code, body = True, f.getcode(), f.read()
            f.close()
        except urllib2.HTTPError as e:
            ok, code, body = False, e.code, e.read()
        except urllib2.URLError as e:
            ok, code, body = False, 'xxx', e.reason

        return (ok, code, body)
