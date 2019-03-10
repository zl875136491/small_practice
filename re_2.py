import re

def check(m):    # 判断匹配是否成功
    if m is not None:
        print(m.group())
    else:
        print(None)


# 字符集合 [ ]
m = re.match('[cr][23][dp][o2]', 'c3po')
check(m)

# 重复、特殊字符和子组
print()
patt = '\w+@(\w+\.)?\w+\.com'

# \w    匹配任何数字字母字符，与[A-Za-z0-9]相同，\W为反义
# ？    匹配前面出现的表达式零次或一次
# +     匹配前面出现的表达式一次或多次
# ()    匹配括号中的表达式，并封闭为子组

m = re.match(patt, 'nobody@xxx.com')
check(m)
m = re.match(patt, '875136491@qq.pp.com')
check(m)
# 例二可以看出，表达式容许.com前有一个或两个名字

# 接下来用*替换？，使得表达式允许任意数量的子域名存在
print()
patt2 = '\w+@(\w+\.)*\w+\.com'
# *     匹配前面出现的表达式零次或多次
m = re.match(patt2, 'nobody@xxx.yyy.zzz.ppp.qqq.com')
check(m)

# 匹配子组
print()
m = re.match('\w\w\w-\d\d\d', 'abc-123')
check(m)

m = re.match('\w\w\w-\d\d\d', 'abc-xyz')
check(m)

# 修改正则，使它能分别提取包含字母或数字的部分和仅含数字的部分
m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
print(m.groups())

# 开头、结尾、单词边界匹配
# 对于锚点型正则表达式操作符，主要被用于搜索而不是匹配
print()
m = re.search('^The', 'The end')            # 开头匹配
check(m)
m = re.search('^The', 'end. The')           # 不在开头
check(m)
m = re.search(r'\bthe', 'bite the dog')     # 在词边界
check(m)
m = re.search(r'\bthe', 'bitethe dog')      # 无边界
check(m)
m = re.search(r'\Bthe', 'bitethe dog')     # 匹配无边界
check(m)

# findall()找到每个匹配部分
print()
print(re.findall('car', 'carry the barcardi to the car'))
# 用sub()和subn()进行搜索和替换
# sub和subn一样，都是将某字符串中所有匹配正则表达式的部分进行替换。subn会额外返回一个替换次数的数字
print()
print(re.sub('X', 'Zhang Le', 'attn: X\n\nDear X,\n'))
print(re.subn('X', 'Zhang Le', 'attn: X\n\nDear X,\n'))

# 用split()分割
print()
print(re.split(':', 'str1:str2:str3'))
