class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:        
        smoothedImg = [[img[i][j] for j in range(len(img[0]))] for i in range(len(img))]        
        for i in range(len(img)):
            for j in range(len(img[0])):
                size = 1
                if i - 1 != -1:
                    size += 1
                    smoothedImg[i][j] += img[i - 1][j]
                if i - 1 != -1 and j - 1 != -1:
                    size += 1
                    smoothedImg[i][j] += img[i - 1][j - 1]
                if i - 1 != -1 and j + 1 != len(img[0]):
                    size += 1
                    smoothedImg[i][j] += img[i - 1][j + 1]
                if j - 1 != -1:
                    size += 1
                    smoothedImg[i][j] += img[i][j - 1]
                if i + 1 != len(img) and j - 1 != -1:
                    size += 1
                    smoothedImg[i][j] += img[i + 1][j - 1]
                if j + 1 != len(img[0]):
                    size += 1
                    smoothedImg[i][j] += img[i][j + 1]
                if i + 1 != len(img):
                    size += 1
                    smoothedImg[i][j] += img[i + 1][j]
                if i + 1 != len(img) and j + 1 != len(img[0]):
                    size += 1
                    smoothedImg[i][j] += img[i + 1][j + 1]
                smoothedImg[i][j] //= size
        
        return smoothedImg