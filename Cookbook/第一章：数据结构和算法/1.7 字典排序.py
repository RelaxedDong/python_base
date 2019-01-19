#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/19 21:51
# 问题
# 你想创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序。
#
# 解决方案
# 为了能控制一个字典中元素的顺序，你可以使用 collections 模块中的 OrderedDict 类。 在迭代操作的时候它会保持元素被插入时的顺序，示例如下：
from collections import OrderedDict
import json
d = OrderedDict()
d['a'] = 1
d['c'] = 3
d['d'] = 4
d['b'] = 2

for key in d:
    print(key,d[key])

end = json.dumps(d)
print(end)
# 当你想要构建一个将来需要序列化或编码成其他格式的映射的时候， OrderedDict 是非常有用的。 比如，你想精确控制以 JSON 编码后字段的顺序，你可以先使用 OrderedDict 来构建这样的数据：

# >>> import json
# >>> json.dumps(d)
# '{"foo": 1, "bar": 2, "spam": 3, "grok": 4}'
# >>>