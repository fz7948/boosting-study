package 장세훈.LeetCode.medium;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class GroupAnagrams {
    /*
        49. Group Anagrams
        https://leetcode.com/problems/group-anagrams/

        key는 문자열, value는 List<String> 타입인 맵을 준비한다.
        입력된 문자열 배열을 순회하며 맵에 저장한다
          - key는 문자를 정렬한 값, value는 원래 문자열
            (그럼 애너그램끼리 묶을 수 있다.)
        맵의 value를 반환한다.
    */
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for (String str : strs) {
            char[] charArray = str.toCharArray();
            Arrays.sort(charArray);
            String key = String.valueOf(charArray);

            if (!map.containsKey(key)) {
                map.put(key, new ArrayList<>());
            }
            map.get(key).add(str);
        }

        return new ArrayList<>(map.values());
    }
}