class JadenCase {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/12951
     */
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        boolean isFirst = true;

        for (char c : s.toCharArray()) {
            if (Character.isAlphabetic(c)) {
                if (isFirst)
                    c = Character.toUpperCase(c);
                else
                    c = Character.toLowerCase(c);
                isFirst = false;
            } else isFirst = c == ' ';

            sb.append(c);
        }

        return sb.toString();
    }
}