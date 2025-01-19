class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        List = []
        for i in image:
            subList = []
            for j in i:
                if j == 0:
                    subList.append(1)
                else:
                    subList.append(0)
            List.append(subList[::-1])
        return List