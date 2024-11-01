/* 프로그래머스 - 달리기 경주
    1. 선수 이름 key와 순서 value를 가진 객체 생성
    2. 기존 배열에서 앞 선수와 추월한 선수의 순서를 변경
    3. 객체 인덱스 순서도 변경

*/

function solution(players, callings) {
  const dict = players.reduce((acc, cur, idx) => {
    acc[cur] = idx;
    return acc;
  }, {});

  callings.forEach((player) => {
    const currentPlayerIndex = dict[player];
    const nextPlayer = players[currentPlayerIndex - 1];

    players[currentPlayerIndex - 1] = player;
    players[currentPlayerIndex] = nextPlayer;

    dict[player] -= 1;
    dict[nextPlayer] += 1;
  });

  return players;
}
