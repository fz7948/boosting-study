class 불량사용자 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/64064
        banid에 해당하는 userid를 각각 리스트에 담는다.
        각 리스트에 있는 userid들을 조합을 한다
     */

    Set<Set<String>> uniqueSet = new HashSet<>();

    public int solution(String[] user_id, String[] banned_id) {
        List<List<String>> matchedUsers = new ArrayList<>();

        for (String banned : banned_id) {
            String regex = banned.replace("*", ".");
            List<String> matched = new ArrayList<>();

            for (String user : user_id) {
                if (user.matches(regex))
                    matched.add(user);
            }

            matchedUsers.add(matched);
        }

        dfs(matchedUsers, new HashSet<>(), 0);
        return uniqueSet.size();
    }

    void dfs(List<List<String>> matchedUsers, Set<String> set, int depth) {
        if (matchedUsers.size() == depth) {
            uniqueSet.add(new HashSet<>(set));
            return;
        }

        for (String user : matchedUsers.get(depth)) {
            if (!set.contains(user)) {
                set.add(user);
                dfs(matchedUsers, set, depth + 1);
                set.remove(user);
            }
        }
    }

}