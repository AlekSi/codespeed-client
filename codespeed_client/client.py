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

    default_branch = "default"
    default_environment = platform.node()
    default_executable = sys.version.replace('\n', ' ')

    def __init__(self, root_url):
        self.url = urlparse.urljoin(root_url, '/result/add/json/')
        self.data = []

    def add_result(self, **kwargs):
        item = {
            'branch': self.default_branch,
            'environment': self.default_environment,
            'executable': self.default_executable
        }

        for k in kwargs:
            if k not in self.combined:
                raise KeyError("Unexpected key %r" % (k,))
            v = kwargs[k]
            if v is not None:
                item[k] = v

        missing = []
        for k in self.required:
            if k not in item:
                missing.append(k)
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
