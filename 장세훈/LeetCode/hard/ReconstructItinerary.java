import java.util.*;

class ReconstructItinerary {
    /*
        https://leetcode.com/problems/reconstruct-itinerary/description/
        332. Reconstruct Itinerary

        주어진 항공권으로 경로 만들기
        한 출발지에서 여러 목적지로 갈 수 있다면 사전순으로 방문
        모든 티켓은 한번만 사용해야 함

        Map<출발지, PriortyQueue<목적지>> 타입을 만들고,
        dfs로 최종 목적지를 찾아내며 answer에 추가
     */

    List<String> answer = new ArrayList<>();

    public List<String> findItinerary(List<List<String>> tickets) {
        Map<String, PriorityQueue<String>> map = new HashMap<>();

        for (List<String> ticket : tickets) {
            if (!map.containsKey(ticket.get(0)))
                map.put(ticket.getFirst(), new PriorityQueue<>());
            map.get(ticket.get(0)).add(ticket.get(1));
        }

        dfs(map, "JFK");

        return answer;
    }

    void dfs(Map<String, PriorityQueue<String>> map, String from) {
        PriorityQueue<String> destinations = map.get(from);

        while (destinations != null && !destinations.isEmpty()) {
            dfs(map, destinations.poll());
        }

        answer.addFirst(from);
    }
}