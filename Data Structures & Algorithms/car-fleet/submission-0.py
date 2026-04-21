class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carSortedByPos=sorted(zip(position,speed), reverse=True)
        latest_ariv_time=float("-inf")
        fleet_count=0

        for pos,spd in carSortedByPos:
            remaining_dist=target-pos
            time_to_target=remaining_dist/spd

            if time_to_target> latest_ariv_time:
                latest_ariv_time=time_to_target
                fleet_count+=1
        return fleet_count
        









        # # Combine the position and speed into tuples and sort them based on position in descending order
        # cars_sorted_by_position = sorted(zip(position, speed), reverse=True)

        # latest_arrival_time = float('-inf')
        # fleet_count = 0

        # # Iterate over the sorted cars
        # for pos, spd in cars_sorted_by_position:
        #     remaining_distance = target - pos
        #     time_to_target = remaining_distance / spd

        #     # If the current car takes more time to reach the target than the latest bottleneck time,
        #     # it forms a new fleet
        #     if time_to_target > latest_arrival_time:
        #         latest_arrival_time = time_to_target
        #         fleet_count += 1

        # return fleet_count
