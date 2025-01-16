class 다른비트 {
   /*
        https://school.programmers.co.kr/learn/courses/30/lessons/77885
        비트연산으로 풀어야하는건 알았는데 못품.
    */

    public long[] solution(long[] numbers) {
        long[] answer = new long[numbers.length];

        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] % 2 == 0)
                answer[i] = numbers[i] + 1;
            else {
                answer[i] = numbers[i] + ((numbers[i] ^ (numbers[i] + 1)) >> 2) + 1;
            }
        }

        return answer;
    }
}