# #encoding:utf-8
# # __author__ = 'donghao'
# # __time__ = 2019/4/18 20:00
#
# def longestCommonPrefix(strs):
#     """获取最长前缀"""
#     mydict = {} #定义一个字典存储
#     for str in strs:
#         substr = str
#         str = ""   #定义接受的字符
#         for c in range(0,len(substr)):
#             str += substr[c]   #遍历后面拼接的字符串
#             if str not in mydict:
#                 mydict[str] = 1 #如果字典不存在
#             else:
#                 mydict[str] += 1 #如果字典存在
#     Maxlen = 0
#
#     #对字典进行处理，查出最长前缀
#     str = ""
#     for key,value in mydict.items():
#         if value >= Maxlen and len(key)>len(str):  #更新最大长度
#             str = key
#             Maxlen = value
#     return str if len(strs) == Maxlen else ''
#
# def main(strs):
#     longestCommonPrefix(strs)
#
# if __name__ == '__main__':
#     result1 = longestCommonPrefix(["flower", "flow", "flight"])
#     print("result1 is ",result1) #result1 is "fl"
#
#     result2 = longestCommonPrefix(["dog", "racecar", "car"])
#     print("result2 is ",result2) #result2 is ""
