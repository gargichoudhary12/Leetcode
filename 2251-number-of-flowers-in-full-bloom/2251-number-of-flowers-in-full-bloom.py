class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        events = []
        for start, end in flowers:
            events.append((start, True))
            events.append((end + 1, False))
        
        events.sort()
        people_events = [(time, index) for index, time in enumerate(people)]
        people_events.sort()

        count = 0
        flower_idx = 0
        result = [0] * len(people)

        for person_time, person_idx in people_events:
            while flower_idx < len(events) and events[flower_idx][0] <= person_time:
                time, is_open = events[flower_idx]
                if is_open:
                    count += 1
                else:
                    count -= 1
                flower_idx += 1
            result[person_idx] = count
        
        return result