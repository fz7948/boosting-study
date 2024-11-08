class 연속_부분_수열_합의_개수 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/131701
        연속 부분 수열 합의 개수
        
        원형 배열의 조건은 입력된 배열을 그대로 뒤에 똑같이 복사를 해서 구현한다.
        적절히 3중 for문으로 부분 수열의 합을 set(중복 제거용)에 담는다.
        set의 크기를 반환한다.
     */
    public int solution(int[] elements) {
        Set<Integer> set = new HashSet<>();
        int[] array = new int[elements.length * 2];

        for (int i = 0; i < array.length; i++) {
            array[i] = elements[i % elements.length];
        }

        for (int i = 0; i < array.length / 2; i++) {
            for (int j = 0; j < array.length - i; j++) {
                int sum = 0;
                for (int k = j; k <= i + j; k++) {
                    sum += array[k];
                }
                set.add(sum);
            }
        }

        return set.size();
    }
}