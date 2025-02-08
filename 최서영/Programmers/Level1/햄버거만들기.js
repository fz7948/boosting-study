// https://school.programmers.co.kr/learn/courses/30/lessons/133502

// 나의 풀이
function mySolution(ingredient) {
  let count = 0;
  const INGREDIENT_ORDER = "1231";

  for (let i = 0; i < ingredient.length; i++) {
    if (ingredient.slice(i, i + 4).join('') === INGREDIENT_ORDER) {
      count++;
      ingredient.splice(i, 4);
      i -= 3;
    }
  }

  return count;
}

// stack 이용한 풀이
function stackSolution(ingredient) {
  let stk = [];
  let count = 0;

  for (let i = 0; i < ingredient.length; i++) {
    stk.push(ingredient[i]);

    if (
        stk[stk.length - 1] === 1 &&
        stk[stk.length - 2] === 3 &&
        stk[stk.length - 3] === 2 &&
        stk[stk.length - 4] === 1
    ) {
      count++;
      stk.splice(-4);
    }
  }
  return count;
}
