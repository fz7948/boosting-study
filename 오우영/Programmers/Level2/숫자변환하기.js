function solution(x, y, n) {
  let dpArr = new Array(y + 1).fill(-1);
  dpArr[x] = 0;

  for (let i = x; i <= y; i++) {
    if (dpArr[i] === -1) {
      continue;
    }

    if (i + n <= y) {
      if (dpArr[i + n] === -1) {
        dpArr[i + n] = dpArr[i] + 1;
      } else {
        dpArr[i + n] =
          dpArr[i + n] > dpArr[i] + 1 ? dpArr[i] + 1 : dpArr[i + n];
      }
    }
    if (i * 2 <= y) {
      if (dpArr[i * 2] === -1) {
        dpArr[i * 2] = dpArr[i] + 1;
      } else {
        dpArr[i * 2] =
          dpArr[i * 2] > dpArr[i] + 1 ? dpArr[i] + 1 : dpArr[i * 2];
      }
    }
    if (i * 3 <= y) {
      if (dpArr[i * 3] === -1) {
        dpArr[i * 3] = dpArr[i] + 1;
      } else {
        dpArr[i * 3] =
          dpArr[i * 3] > dpArr[i] + 1 ? dpArr[i] + 1 : dpArr[i * 3];
      }
    }
  }
  return dpArr[y];
}
