package 장세훈.Programmers.Level1;

public class 지폐_접기 {

    /*
        [PCCE 기출문제] 9번 / 지폐 접기
        https://school.programmers.co.kr/learn/courses/30/lessons/340199

        지폐가 지갑에 들어갈 수 있는 크기인지 확인
          들어가지 못한다면 들어가질떄 까지 지폐의 가로, 세로 길이 중 긴 곳을 2로 나눔을 반복
     */

    public int solution(int[] wallet, int[] bill) {
        int answer = 0;
        while (!(wallet[0] >= bill[0] && wallet[1] >= bill[1]) &&
                !(wallet[0] >= bill[1] && wallet[1] >= bill[0])) {

            if (bill[0] >= bill[1]) bill[0] /= 2;
            else bill[1] /= 2;

            answer++;
        }

        return answer;
    }
}
