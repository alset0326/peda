import re
import progressbar
import pickle
import requests
import zlib

reply = requests.get('http://ascii.mastervb.net/')
# <option value="xhelvi.flf">xhelvi.flf</option>
pattern = re.compile('<option value="(\S+)">\S+</option>')
m = pattern.findall(reply.text)

print 'start!!'
l = []
p = progressbar.ProgressBar(maxval=len(m)).start()
for index, option in enumerate(m):
    p.update(index + 1)
    try:
        reply = requests.get('http://ascii.mastervb.net/figlet.ajax.php', params={'message': 'GDB-PEDA',
                                                                                  'rtol': 'undefined',
                                                                                  'old_layout': 'undefined',
                                                                                  'font': str(option),
                                                                                  'html_mode': 'undefined'},
                             proxies={"http": "http://127.0.0.1:8118"})
        t = str(reply.text)
        image = t[t.index('<pre>') + 5:t.index('</pre>')]
        l.append(image)
    except:
        print 'missing option: %s' % option
open('logos', 'wb').write(zlib.compress(pickle.dumps(l)))
p.finish()
