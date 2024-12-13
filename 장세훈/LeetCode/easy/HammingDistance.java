    /*
        https://leetcode.com/problems/hamming-distance/description/
        두 숫자의 이진수 표현에서 비트가 다른 위치의 개수
        xor을 연산 시 비트가 다르면 1을 반환 -> 1의 개수 카운트
     */
    public int hammingDistance(int x, int y) {
        return Integer.bitCount(x^y);
    }