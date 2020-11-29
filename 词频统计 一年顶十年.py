import jieba #引用jieba库 python第172页
txt = open("一年顶十年.txt", "r", encoding='utf-8').read() #打开一年顶十年.txt，只读模式，utf-8模式,一年顶十年文本由变量txt表示。
                                                           #python中的小括号( )：代表tuple元组数据类型，元组是一种不可变序列。
words = jieba.lcut(txt)  #第170页 jieba.lcut(s) 描述为精确模式，返回一个列表类型，建议使用。
counts = {}  
'''新建一个空字典使用一个字典类型counts=｛｝（键值对，用冒号：隔开）,统计单词出现的次数可采用如下代码：  counts[word] = counts[word] + 1
                python大括号{ }花括号：代表dict字典数据类型，字典是由键对值组组成。冒号':'分开键和值，逗号','隔开组
'''
for word in words:  
'''当遇到一个新词时，单词没有出现在字典结构中，则需要在字典中新建键值对：  counts[new_word] = a
                       for为遍历循环，可以便利任何序列，如list，tuple，迭代器等。
                       for的语句格式如下：for <变量> in <循环序列>：
                                                  【循环体】
                       解释：通过for循环依次将<循环序列>中的数据取出赋值给<变量>，再通过【循环体】进行处理。
'''
    if len(word) == 1: 
''' 排除单个字符的分词结果.
                           if语句代表“如果”。 如果 什么条件成立了，我们就做什么，a<42成立，执行缩进代码块内容。
                           内置函数，len(word),参数-word为对象；返回值，返回对象长度；
'''
        continue      # continue语句用来告诉python跳过当前循环的剩余语句，然后继续进行下一轮循环。
    else:             
''' 表示再次判断，是else if的简写，elif语句不能独立使用，可以在需要检查更多条件时，与if和else一同使用，
                          一个if语句中可以包含多个elif语句，但结尾只能有一个else语句。
'''
        counts[word] = counts.get(word,0) + 1  
''' 无论词是否在字典中，加入字典counts中的处理逻辑可以统一表示。
                                                   字典类型的counts.ger(word,0)方法表示：如果word在counts中，则返回
                                                   word对应的值，如果word不在counts中，则返回0。
                                                   python 字典（Dictinary）get()函数返回指定键的值。
                                                   get()方法语法：   dict.get（key, default=None）
                                                   key --字典中要查找的键。
                                                   default --如果指定键的值不存在时，返回该默认值。
                                                   返回值，返回指定的值，如果键不在字典中返回默认值None或者设置的默认值。
                                                   python中的中括号[ ]，代表list列表数据类型：
'''
items = list(counts.items())  # count()方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
                              # python 字典(Dictionary)items() 函数以列表返回可遍历的(键，值)元祖数组。
  items.sort(key=lambda x:x[1], reverse=True)  
''' sort()函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
    sort(d.items(),key=lambda x:x[1])中d.items()为待排序的对象；
    key=lambda x:x[1]为对前面的对象中的第二位数据（即value）的值进行排序。key=lambda 变量：变量[维数]。维数可以按照自己的需要进行设置。
    key=lambda 元素：元素[字段索引]
    比如 print(sorted(C,key=lambda x:x[2]))
    x:x[]字母可以随意修改，排序方式按照中括号[]里面的维度进行排序，[0]按照第一维排序，[2]按照第三维排序。
'''
for i in range(50):
    word, count = items[i]   
'''python中的变量不需要声明。每个变量再使用前都必需赋值，变量赋值以后该变量才会被创建。
                                python中，变量就是变量，它没有类型，他们所说的“类型”是变量所指的内存中对象的类型。
                                等号（=）运算符左边是一个变量名，等号（=）运算符右边是存储在变量中的值。
'''
    print ("{0:<10}{1:>5}".format(word,count)) 
'''  输出。{0:10}花括号代表一个字典槽位，槽位里左边代表键，右边代表值。
                                                   这个是format方法的格式控制。首先：'我的｛0｝叫｛1｝'.format(word,count),大括号里的数字
                                                   表示的是位置，就是0对应的Word，1对应的是count。
                                                   ：冒号是引导符号，后面的format是格式控制方法。
                                                   <表示左对齐，>表示右对齐，数字表示宽度。
                                                   同理，<10表示左对齐，并占10个位置，>5表示右对齐，占5个位置。
'''
                                                '''
