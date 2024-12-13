/*

프로그래머스 - 푸드파이터대회
https://school.programmers.co.kr/learn/courses/30/lessons/134240

*/

function solution(food) {
  let res = "";
  for (let i = 1; i < food.length; i++) {
    res += String(i).repeat(Math.floor(food[i] / 2));
  }

  return res + "0" + [...res].reverse().join("");
}
