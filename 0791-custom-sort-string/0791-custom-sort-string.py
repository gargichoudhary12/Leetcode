class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        res = ''
        dict = collections.defaultdict(int)
        for index, v in enumerate(S):
            dict[v] = index
        #print(dict)
        T = sorted(T, key = lambda x :dict[x])
        return ''.join(i for i in T)