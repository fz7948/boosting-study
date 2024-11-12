/* 프로그래머스 - 뒤에 있는 큰 수 찾기 */

function solution(numbers) {
  let answer = new Array(numbers.length).fill(-1);
  let stack = [];
  for (let i = 0; i < numbers.length; i++) {
    while (stack && numbers[stack.at(-1)] < numbers[i]) {
      answer[stack.pop()] = numbers[i];
    }
    stack.push(i);
  }
  return answer;
}
