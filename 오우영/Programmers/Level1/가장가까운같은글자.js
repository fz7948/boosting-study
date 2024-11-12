/* 프로그래머스 - 가장 가까운 같은 글자
    1. tmp 임시배열에 중복된 문자가 없다면 -1
    1-1. 중복된 문자를 포함한다면 해당 문자의 앞에서 lastIndexOf로 가장 마지막에 있는 단어
*/

function solution(s) {
  let result = [];
  let tmp = [];

  for (let i = 0; i < s.length; i++) {
    if (!tmp.includes(s[i])) {
      result.push(-1);
      tmp.push(s[i]);
    } else if (tmp.includes(s[i])) {
      result.push(i - tmp.lastIndexOf(s[i]));
      tmp.push(s[i]);
    }
  }
  return result;
}
