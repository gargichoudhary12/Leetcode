class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand = sorted(hand)
        while hand:
            cur = hand[0]
            hand.remove(cur)
            for i in range(groupSize):
                if i == 0:
                    cur += 1
                    continue
                if cur not in hand:
                    return False
                hand.remove(cur)
                cur += 1
        return True
        