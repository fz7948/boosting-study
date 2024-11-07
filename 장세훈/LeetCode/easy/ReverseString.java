package 장세훈.LeetCode.easy;

class ReverseString {

    /*
         344. Reverse String
         https://leetcode.com/problems/reverse-string/

         in-place with O(1) extra memory. 조건이 있는 문자열 뒤집는 문제이다.
         in-place는 입력된 데이터로만 활용해서 알고리즘을 풀라는 말이고,
         O(1)은 변수 하나를 허용한다는 뜻이다.

     */
    public void reverseString(char[] s) {
        for(int i = 0; i < s.length / 2; i++) {
            char temp = s[i];
            s[i] = s[s.length - i - 1];
            s[s.length - i - 1] = temp;
        }
    }
}