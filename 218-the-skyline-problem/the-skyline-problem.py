import heapq

class Solution:
    def getSkyline(self, buildings):
        # 1. Create events: (x, -height) for starts, (x, height) for ends
        # Using -height for starts ensures that at the same x:
        # - Higher buildings are processed first
        # - Starts are processed before ends
        events = []
        for L, R, H in buildings:
            events.append((L, -H))
            events.append((R, H))
        
        # Sort events by x-coordinate, then by height
        events.sort()
        
        # res stores the key points: [x, height]
        # live_heights is a max-heap (storing negative values for min-heap)
        res = [[0, 0]]
        live_heights = [0]
        
        # To handle building ends efficiently, we use a lazy-removal dictionary
        past_heights = {0: 1}
        
        for x, h in events:
            if h < 0:
                # Building starts: add height to heap
                h = -h
                past_heights[h] = past_heights.get(h, 0) + 1
                heapq.heappush(live_heights, -h)
            else:
                # Building ends: mark height for removal
                past_heights[h] -= 1
            
            # 2. Lazy remove: clean the top of the heap if that height is no longer "live"
            while -live_heights[0] in past_heights and past_heights[-live_heights[0]] == 0:
                heapq.heappop(live_heights)
            
            # 3. If the max height changed, this x is a key point
            curr_max = -live_heights[0]
            if res[-1][1] != curr_max:
                res.append([x, curr_max])
        
        # Remove the dummy [0, 0] point used for initialization
        return res[1:]
