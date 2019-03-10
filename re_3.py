import re
data = 'Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8'
# '^Mon|^Tue|^Wed|^The|^Fri|^Sat|^Sun'规则为必须以其中之一打头
# 可以用^()方法将日期字符串归为一个子组
patt = '^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)'
print(re.match(patt, data).group())
# 贪心模式
print()
# 首先 用搜索来匹配数字-数字-数字部分
patt2 = '\d+-\d+-\d+'
print(re.search(patt2, data).group())

# 如果用match方法的话，数字字符串在末尾，
# 所以用“.+”表示任意个字符集。后面再接上感兴趣的数字
patt3 = '.+\d+-\d+-\d+'
print(re.search(patt3, data).group())
# 但是我们只想要数字部分，所以用括号将数字部分分成子组

patt4 = '.+(\d+-\d+-\d+)'
print(re.search(patt4, data).groups())
# 这时没有得到1171590364-6-8，却只有4-6-8
# 因为1171590364的除去最后一位的前一部分被“+.”的默认贪心匹配
# 贪心模式会从字符串的起始开始抓取满足模式的足够长的最长串
# 而“\d+”仅需要一位即能完成匹配，所以“\d+”匹配了“4”，
# 而“+.”匹配了从开始到4的所有字符

# 贪心模式的一个解决办法就是用“?”，
# 可以把它放在 * + 或者 ？后面，
# 他的作用就是使得表达式匹配的越少越好

patt5 = '.+?(\d+-\d+-\d+)'
print(re.search(patt5, data).groups())
