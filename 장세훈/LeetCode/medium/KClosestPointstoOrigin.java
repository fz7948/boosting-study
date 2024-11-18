/*
    https://leetcode.com/problems/k-closest-points-to-origin/description/
    973. K Closest Points to Origin

    xy 좌표 점들이 주어지고, 원점으로 부터 거리가 가까운 순으로 k개를 추출하는 문제.
    
    원점과의 거리순으로 정렬하는 우선순위 큐를 생성.
    주어진 좌표를 큐에 넣고 k 개수만큼 뽑아냄.
*/

class KClosestPointstoOrigin {
    public int[][] kClosest(int[][] points, int k) {
        int[][] answer = new int[k][];
        PriorityQueue<int[]> pq = new PriorityQueue<>((arr1, arr2) -> {
            int a = arr1[0] * arr1[0] + arr1[1] * arr1[1];
            int b = arr2[0] * arr2[0] + arr2[1] * arr2[1];
            return a - b;
        });

        pq.addAll(Arrays.asList(points));

        for (int i = 0; i < k; i++) {
            answer[i] = pq.poll();
        }

        return answer;
    }
}