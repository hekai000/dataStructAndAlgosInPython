# KMP算法

## 算法思想

匹配时，利用模式串的pnext数组，目标串不回溯；

## 复杂度

O(n)

## 代码

```
    def getNext(self, needle):
        i, k, m = 0, -1, len(needle)
        pNext = [-1] * m
        while(i<m-1):
            if k==-1 or needle[i] == needle[k]:
                i, k = i+1, k+1
                pNext[i] = k
            else:
                k = pNext[k]
        return pNext

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not len(needle):
            return 0
        pnext = self.getNext(needle)
        j, i = 0, 0
        n, m = len(haystack), len(needle)
        while j<n and i<m:
            if i == -1 or haystack[j] == needle[i]:
                j, i = j+1, i+1
            else:
                i = pnext[i]
        if i==m:
            return j-i
        return -1
```

## 参考资料

[从头到尾彻底理解KMP（2014年8月22日版）](https://blog.csdn.net/v_july_v/article/details/7041827)

[知乎如何理解KMP](https://www.zhihu.com/question/21923021)