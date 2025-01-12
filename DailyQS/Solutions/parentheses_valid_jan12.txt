class Solution(object):
    def canBeValid(self, s, locked):
        if len(s)%2!=0:
            return False
        open_left = 0
        unlocked_left = 0
        for i in range(len(s)):
            if locked[i] == '0':
                unlocked_left += 1;
            elif s[i] == '(':
                open_left += 1
            else:
                open_left -= 1
            if open_left + unlocked_left < 0:
                return False

        open_right = 0
        unlocked_right = 0
        for i in range(len(s)-1,-1,-1):
            if locked[i] == '0':
                unlocked_right += 1;
            elif s[i] == ')':
                open_right += 1
            else:
                open_right -= 1
            if open_right + unlocked_right < 0:
                return False
        return True