class 숫자카드나누기 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/135807?language=java
        배열의 최소 공배수 구하기
     */

    public int solution(int[] arrayA, int[] arrayB) {
        int aGcd = arrayGcd(arrayA);
        int bGcd = arrayGcd(arrayB);

        int a = canDivided(aGcd, arrayB) ? 0 : aGcd;
        int b = canDivided(bGcd, arrayA) ? 0 : bGcd;

        return Math.max(a, b);
    }

    boolean canDivided(int n, int[] arr) {
        for (int a : arr) {
            if (a % n == 0)
                return true;
        }

        return false;
    }

    int arrayGcd(int[] arr) {
        int gcd = arr[0];

        for (int a : arr) {
            gcd = gcd(gcd, a);
        }

        return gcd;
    }

    int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }

        return a;
    }

}