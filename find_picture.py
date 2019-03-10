import urllib
import requests


import socket

weburl = 'https://ii.hywly.com/a/1/'
image_url = []
# elite = ['16593 49', '16636 64', '16637 62', '16639 47','16660 65',
#          '16661 52', '16666 40', '16681 46', '16752 67', '16759 63']

k = 0
for i in range(16759, 16760):          # 16764~16800
    for j in range(45, 64):
        print(weburl+str(i)+'/'+str(j)+'.jpg')
        socket.setdefaulttimeout(5)
        try:
            urllib.request.urlretrieve(weburl + str(i) + '/' + str(j) + '.jpg', "D:\ckc\\%s.jpg" % (str(i) + ' ' + str(j)))
        except socket.timeout:
            count = 1
            while count <= 5:
                try:
                    urllib.request.urlretrieve(weburl + str(i) + '/' + str(j) + '.jpg',
                                        "D:\ckb\\%s.jpg" % (str(i) + ' ' + str(j)))
                    break
                except socket.timeout:
                    err_info = 'Reloading for %d time' % count if count == 1 else 'Reloading for %d times' % count
                    print(err_info)
                    count += 1
            if count > 5:
                print("downloading picture fialed!")











