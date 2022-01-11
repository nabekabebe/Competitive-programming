class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = []
        for i in range(len(position)):
            cars.append([position[i],speed[i]])
        cars.sort(key=lambda x : x[0], reverse=True)
        
        prev = -2
        fleets = 0

        for pos, spd in cars:
            time = (target - pos) / spd
            if time > prev:
                fleets += 1
                prev = time
                
        return fleets
