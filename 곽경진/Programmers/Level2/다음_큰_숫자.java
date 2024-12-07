/*
프로그래머스 다음_큰_숫자

    1. 2진수의 1갯수 구하기 
    2. n 보다 크면서 1의 갯수가 같아야 하므로 nextNumber 증가 
    3. 1의 갯수가 같을때 숫자 리턴 
*/

class Solution {
    public int solution(int n) {
        int bit = Integer.bitCount(n);
        int nextNumber = n + 1;
        
        while(Integer.bitCount(nextNumber) != bit){
            nextNumber++;
        }
        
        return nextNumber;
    }
}