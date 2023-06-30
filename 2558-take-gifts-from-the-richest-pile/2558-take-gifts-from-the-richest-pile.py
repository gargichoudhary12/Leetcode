class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        counter = 0
        while counter<k:
            gifts.sort(reverse=True)
            maxPile = gifts[0]
            maxPile = math.floor(maxPile**0.5)
            gifts[0] = maxPile
            counter+=1
        return sum(gifts)