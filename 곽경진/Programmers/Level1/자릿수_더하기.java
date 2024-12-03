
```
프로그래머스 - 자릿수 더하기 
    1. 숫자를 Stirng 으로 변환
    2. String 을 char 로 분해 
    3. getNumericValue 매서드로 int 전환후 합산
```
import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        
        for ( char c : (n+"").toCharArray()) {
            answer += Character.getNumericValue(c);
        }

        return answer;
    }
}