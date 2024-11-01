/* 프로그래머스 - 추억 점수
    1. name의 키와 yearning의 value를 가진 dict 생성
    2. photo 안에 배열들을 순환하여 dict 객체로 점수 카운트
    2-1. dict 객체 안에 없는 키일 경우 0 반환
*/

function solution(name, yearning, photo) {
  const dict = name.reduce((acc, cur, index) => {
    acc[cur] = yearning[index];
    return acc;
  }, {});

  const result = photo.map((item) => {
    return item.reduce((acc, cur) => {
      return acc + (dict[cur] ?? 0);
    }, 0);
  });

  return result;
}
