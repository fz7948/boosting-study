/* 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/59415 */

-- 방법 1 : ordered by 활용
SELECT DATETIME
FROM ANIMAL_INS
ORDER BY DATETIME DESC
LIMIT 1;

-- 방법 2 : max 활용
SELECT MAX(DATETIME)
WHERE ANIMAL_INS;