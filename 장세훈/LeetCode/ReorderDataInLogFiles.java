package 장세훈.LeetCode;
import java.util.*;

class ReorderDataInLogFiles {
    /*
            937. Reorder Data in Log Files
            https://leetcode.com/problems/reorder-data-in-log-files/description/

            문자열 로그를 담을 리스트와 숫자 로그를 담을 리스트를 만들고 각각 로그를 넣는다.
            로그 식별값과 내용을 분리한다. 자바인 경우 String의 split 함수에 limit 값을 주면 쉽게 분리 가능하다.
            문자열 로그는 문제 조건에 맞게 정렬을 수행한다.
            정렬된 문자열 로그와 숫자 로그를 합쳐 리턴한다.
     */
    public String[] reorderLogFiles(String[] logs) {
        List<String> letterList = new ArrayList<>();
        List<String> digitList = new ArrayList<>();

        for (String log : logs) {
            if (Character.isDigit(log.split(" ")[1].charAt(0))) digitList.add(log);
            else letterList.add(log);
        }

        letterList.sort((s1, s2) -> {
            String[] split1 = s1.split(" ", 2);
            String[] split2 = s2.split(" ", 2);

            int compared = split1[1].compareTo(split2[1]);
            if (compared == 0)
                return split1[0].compareTo(split2[0]);
            else return compared;
        });

        letterList.addAll(digitList);
        return letterList.toArray(new String[0]);
    }
}
