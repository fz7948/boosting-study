/* 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131697 */

-- 방법 1 : ordered by 활용
SELECT PRICE AS MAX_PRICE
FROM PRODUCT
ORDER BY PRICE DESC
LIMIT 1;

-- 방법 2 : max 활용
SELECT MAX(PRICE) AS MAX_PRICE
FROM PRODUCT;
