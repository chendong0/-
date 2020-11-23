import jieba #引用jieba库 python第172页
txt = open("一年顶十年.txt", "r", encoding='utf-8').read() #打开一年顶十年.txt，只读模式，utf-8模式,一年顶十年文本由变量txt表示
words = jieba.lcut(txt)  #第170页 jieba.lcut(s) 描述为精确模式，返回一个列表类型，建议使用。
counts = {}  #使用一个字典类型counts=｛｝,统计单词出现的次数可采用如下代码：  counts[word] = counts[word] + 1
for word in words:  #当遇到一个新词时，单词没有出现在字典结构中，则需要在字典中新建键值对：  counts[new_word] = a
    if len(word) == 1: #排除单个字符的分词结果
        continue
    else:
        counts[word] = counts.get(word,0) + 1  ''' 无论词是否在字典中，加入字典counts中的处理逻辑可以统一表示。
                                                   字典类型的counts.ger(word,0)方法表示：如果word在counts中，则返回
                                                   word对应的值，如果word不在counts中，则返回0。
                                               '''
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(50):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word,count)) '''  输出。{0:10}花括号代表一个字典槽位，槽位里左边代表键，右边代表值。
                                                   这个是format方法的格式控制。首先：'我的｛0｝叫｛1｝'.format(word,count),大括号里的数字
                                                   表示的是位置，就是0对应的Word，1对应的是count。
                                                   ：冒号是引导符号，后面的format是格式控制方法。
                                                   <表示左对齐，>表示右对齐，数字表示宽度。
                                                   同理，<10表示左对齐，并占10个位置，>5表示右对齐，占5个位置。
                                                '''
