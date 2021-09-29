class Solution:
    def maximum69Number(self, num: int) -> int:
        num = str(num)
        ind = num.find('6')
        if ind == -1:
            return int(num)
        else:
            return int(num[:ind] + '9' + num[ind + 1:])
