class 스킬트리 {

    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/49993
     */

    public int solution(String skill, String[] skill_trees) {
        int answer = 0;

        for (String skillTree : skill_trees) {
            Set<Character> set = new HashSet<>();
            boolean isOk = true;

            for (char c : skill.toCharArray()) {
                if (skillTree.indexOf(c) != -1) {
                    set.add(c);
                }
            }

            int index = -1;
            for (int i = 0; i < set.size(); i++) {
                int skillIndex = skillTree.indexOf(skill.charAt(i));
                if (set.contains(skill.charAt(i)) && index < skillIndex) {
                    index = skillIndex;
                } else {
                    isOk = false;
                    break;
                }
            }

            if (isOk) answer++;
        }

        return answer;
    }
}