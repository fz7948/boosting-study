class 가장큰수 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/42746?language=java
    */
    public String solution(int[] numbers) {
        StringBuilder sb = new StringBuilder();
        Arrays.stream(numbers).mapToObj(e -> e + "").sorted((o1, o2) -> (o2 + o1).compareTo(o1 + o2))
                .forEach(sb::append);

        return sb.charAt(0) == '0' ? "0" : sb.toString();
    }
}