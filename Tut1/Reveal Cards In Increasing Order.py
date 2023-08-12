#import deque from collections before coding
def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck = sorted(deck)[::-1]
        arr = deque()
        for i in deck:
            if arr:
                arr.appendleft(arr.pop())
            arr.appendleft(i)
        return arr
