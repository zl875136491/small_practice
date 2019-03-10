from random import randint, choice
from string import ascii_lowercase
from time import ctime
maxint = 32767254

doms = ('com', 'edu', 'net', 'org', 'gov')

for i in range(randint(5,10)):
    dtint = randint(0, maxint -1)
    dtstr = ctime(dtint)
    shorter = randint(4, 7)
    em = ''
    for j in range(shorter):
        em += choice(ascii_lowercase)

    longer = randint(shorter, 12)
    dn = ''
    for j in range(longer):
        dn += choice(ascii_lowercase)

    print('%s::%s@%s.%s::%d-%d-%d' % (dtstr, em, dn, choice(doms), dtint, shorter, longer))