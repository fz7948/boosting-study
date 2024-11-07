/* 프로그래머스 - 크기가 작은 부분문자열
    1. p의 자릿수 체크
    2. 자릿수만큼 t 나열후 p와 대소 구분
    3. 카운트 반환
*/

function solution(t, p) {
  const numberP = Number(p);
  let count = 0;

  for (let i = 0; i < t.length - p.length + 1; i++) {
    const slicedT = t.slice(i, i + p.length);
    const numberT = Number(slicedT);

    if (numberT <= numberP) {
      count += 1;
    }
  }

  return count;
}
