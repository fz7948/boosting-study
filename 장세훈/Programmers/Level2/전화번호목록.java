class 전화번호목록 {

    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/42577
        살짝 당황한 해시 문제
    
    */

    public boolean solution(String[] phone_book) {
        Set<String> set = new HashSet<>();
        Arrays.sort(phone_book, Comparator.comparingInt(String::length));
        for (String s : phone_book) {

            StringBuilder sb = new StringBuilder();
            for (char c : s.toCharArray()) {
                sb.append(c);
                if(set.contains(sb.toString())) return false;
            }

            set.add(s);
        }

        return true;
    }
}