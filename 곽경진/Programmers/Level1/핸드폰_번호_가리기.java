
```
프로그래머스 - 핸드폰 번호가리기

    1. String 길이 -4 만큼 * 붙이기 
    2. substring으로 뒤에서 4자리 잘라서 붙이기 
    
```
class Solution {
    public String solution(String phone_number) {
        String answer = "";
        for (int i = 0 ; i < phone_number.length()-4 ; i++){
            answer += "*";
        }
        answer = answer + phone_number.substring(phone_number.length()-4, phone_number.length());
        return answer;
    }
}