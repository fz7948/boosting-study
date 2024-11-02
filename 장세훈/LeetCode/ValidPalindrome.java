package 장세훈.LeetCode;

public class ValidPalindrome {

    /*
        125. Valid Palindrome
        https://leetcode.com/problems/valid-palindrome/description/

        입련된 문자열을 정규식으로 알파벳과 숫자만 필터링하고 알파벳은 소문자로 만든다.
        변환된 문자열 기준으로 앞뒤 문자가 같은지 확인하며 순회한다.
     */
    public boolean isPalindrome(String s) {
        String str = s.replaceAll("[^A-Za-z0-9]", "").toLowerCase();

        for (int i = 0; i < str.length() / 2; i++) {
            if (str.charAt(i) != str.charAt(str.length() - 1 - i)) {
                return false;
            }
        }

        return true;
    }

}
