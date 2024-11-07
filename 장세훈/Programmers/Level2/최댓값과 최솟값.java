

/*
    최댓값과 최솟값
    https://school.programmers.co.kr/learn/courses/30/lessons/12939?language=java
    
    입력된 문자열 리스트를 split와 stream으로 정렬된 정수 리스트를 만듬.
    맨 앞, 맨 뒤 숫자를 리턴한다.
*/

public String solution(String s) {
    List<Integer> list = Arrays.stream(s.split(" ")).map(Integer::parseInt).sorted().t
    return list.get(0) + " " + list.get(list.size() - 1);
}