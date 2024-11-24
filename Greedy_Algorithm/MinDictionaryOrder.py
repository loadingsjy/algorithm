# 给定一个全是小写字母的字符串str，删除多余字符，使得每种字符只保留一个，并让最终结果字符串的字典序最小。



def MinDictionaryOrder(s):
  if not s or len(s) == 1:
    return s
  mapping = dict()
  for c in s:
    if c in mapping.keys():
      mapping[c] += 1
    else:
      mapping[c] = 1
      
  minACSIIIndex = 0
  for i in range(len(s)):
    mapping[s[i]] -= 1
    if mapping[s[i]] == 0:
      break
    else:
      minACSIIIndex = i if ord(s[i]) < ord(s[minACSIIIndex]) else minACSIIIndex

  return s[minACSIIIndex] + MinDictionaryOrder(s[minACSIIIndex+1:].replace(s[minACSIIIndex], ''))
  
# 时间复杂度：O(k*n), k为字符种类数，n为字符串长度。
# 空间复杂度：O(k), 存储映射表。

  
  
if __name__ == '__main__':
  s = 'abccba'
  print(MinDictionaryOrder(s)) # Output: 'abc'
  
  s = 'cbbaaabccba'
  print(MinDictionaryOrder(s)) # Output: 'abc'
    