/* 프로그래머스 - 귤 고르기 */

function solution(k, tangerine) {
  let answer = 0;
  const tDict = {};

  tangerine.forEach((t) => (tDict[t] = (tDict[t] || 0) + 1));

  const tArr = Object.values(tDict).sort((a, b) => b - a);

  for (const t of tArr) {
    answer++;
    if (k > t) k -= t;
    else break;
  }

  return answer;
}
