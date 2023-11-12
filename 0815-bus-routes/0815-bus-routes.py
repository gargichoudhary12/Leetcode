class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        buses = defaultdict(set)
        for bus, route in enumerate(routes):
            routes[bus] = set(route)
            for stop in route:
                buses[stop].add(bus)

        reachable = {source}
        old = set()

        steps = 0
        while reachable and target not in reachable:
            steps += 1
            newReachable = set()
            old.update(reachable)
            for bus in set().union(*[buses[stop] for stop in reachable]):
                newReachable.update(routes[bus].difference(old))
            reachable.clear()
            reachable = newReachable

        return -1 if target not in reachable else steps