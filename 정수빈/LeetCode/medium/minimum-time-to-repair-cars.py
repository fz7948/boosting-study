class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def canRepairInTime(time):
            total_cars = 0
            for rank in ranks:
                total_cars += int((time // rank) ** 0.5)  # 주어진 시간 내에 수리할 수 있는 차량 수
            return total_cars >= cars  # 필요한 차량 수를 수리할 수 있는가?

        ranks.sort()
        left, right = 1, ranks[0] * cars * cars  # 최소 시간과 최대 시간 설정

        while left < right:
            mid = (left + right) // 2
            if canRepairInTime(mid):
                right = mid  # 가능한 경우 시간 줄이기
            else:
                left = mid + 1  # 불가능하면 시간 늘리기

        return left  # 최소 시간 반환
