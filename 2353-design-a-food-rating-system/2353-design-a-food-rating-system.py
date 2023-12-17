from sortedcontainers import SortedSet
class Item:
	# name --> food 
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
    
    def __lt__(self, other):
        if self.rating == other.rating:
            return self.name > other.name
        return self.rating < other.rating
    

from collections import defaultdict
    
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.ratingSystem = defaultdict(lambda : SortedSet())
        self.itemMap = {}
        self.foodMap = {}
        for i in range(len(cuisines)):
            cur = Item(foods[i], ratings[i])
            self.ratingSystem[cuisines[i]].add(cur)
            self.itemMap[foods[i]] = cur
            self.foodMap[foods[i]] = cuisines[i]
            
        

    def changeRating(self, food: str, newRating: int) -> None:
        curC = self.foodMap[food]
        curItem = self.itemMap[food]
        newItem = Item(food, newRating)
        self.ratingSystem[curC].discard(curItem)
        self.ratingSystem[curC].add(newItem)
        self.itemMap[food] = newItem
        

    def highestRated(self, cuisine: str) -> str:
        return self.ratingSystem[cuisine][-1].name