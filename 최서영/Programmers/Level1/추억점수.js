// https://school.programmers.co.kr/learn/courses/30/lessons/176963

// 나의 풀이
function mySolution(name, yearning, photo) {
  let answer = [];

  for (let i = 0; i < photo.length; i++) {
    let score = 0;

    for (let j = 0; j < photo[i].length; j++) {
      let index = name.indexOf(photo[i][j]);
      score += index > -1 ? yearning[index] : 0;
    }

    answer.push(score);
  }

  return answer;
}

// 깔끔 풀이
function cleanSolution(name, yearning, photo) {
  return photo.map((v)=> v.reduce((a, c)=> a += yearning[name.indexOf(c)] ?? 0, 0))
}
