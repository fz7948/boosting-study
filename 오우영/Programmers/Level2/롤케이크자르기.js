function solution(topping) {
  let answer = 0;
  let littleMap = new Map();
  let bigMap = new Map();

  for (var i = 0; i < topping.length; i++) {
    if (bigMap.has(topping[i])) {
      bigMap.set(topping[i], bigMap.get(topping[i]) + 1);
    } else {
      bigMap.set(topping[i], 1);
    }
  }

  for (var i = 0; i < topping.length; i++) {
    if (bigMap.get(topping[i]) === 1) {
      bigMap.delete(topping[i]);
    } else {
      bigMap.set(topping[i], bigMap.get(topping[i]) - 1);
    }
    if (littleMap.has(topping[i])) {
      littleMap.set(topping[i], littleMap.get(topping[i]) + 1);
    } else {
      littleMap.set(topping[i], 1);
    }

    if (bigMap.size === littleMap.size) {
      answer++;
    }
  }
  return answer;
}
