import re


def check(m):    # 判断匹配是否成功
    if m is not None:
        print(m.group())
    else:
        print(None)


# 即使字符串比模式要长，但从字符串开头有一个匹配成功，
print(re.match('foo', 'food on the table').group())

# 上面的例子中，如果匹配失败，会引发一个'NoneType' object has no attribute 'group'的错误
# 所以先前使用check()来做判断

# search()会检查参数字符串任意位置的地方给定正则表达式模式的匹配情况
m = re.search('food', 'seafood')
if m is not None:
    print(m.group())

# 管道
print()
bt = 'bat|bet|bit'

m = re.match(bt, 'bat')
check(m)

m = re.search(bt, 'he bit me!')
check(m)

# 句点匹配任何字符（换行符除外）
print()
anyend = '.end'
m = re.match(anyend, 'bend')
check(m)

m = re.match(anyend, '/nend')
check(m)

m = re.search(anyend, 'the end...')
check(m)

# 搜索包含句点的表达式
print()
patt = '3.14'
pi_patt = '3\.14'
m = re.match(patt, '3.14')
check(m)

m = re.match(patt, '3014')
check(m)

m = re.match(pi_patt, '3.14')
check(m)

m = re.match(pi_patt, '3014')
check(m)
