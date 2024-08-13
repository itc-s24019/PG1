import collections

data = 'すもももももももものうち'

# 通常の辞書を使用する方法
count_dic = {}
for v in data:
    if v in count_dic:
        count_dic[v] += 1
    else:
        count_dic[v] = 1
print(count_dic)

# defaultdictを使用する方法 (int)
count_dic = collections.defaultdict(int)
for v in data:
    count_dic[v] += 1
print(count_dic)

# defaultdictを使用する方法 (list)
count_dic = collections.defaultdict(list)
for v in data:
    count_dic[v].append(v)
print(count_dic)

# Counterを使用する方法
counter = collections.Counter(data)
print(counter)

# namedtupleを使用する方法
CharCount = collections.namedtuple('CharCount', ['char', 'count'])

mo = CharCount('も', 8)
print(mo)
print(mo.char, mo.count)

import collections
data = 'すもももももももものうち'
count = collections.Counter(data)
res_dict = collections.defaultdict(list)
for ch, cnt in count.items():
    res_dict[cnt].append(ch)
print(res_dict[1])


