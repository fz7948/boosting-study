
// string (s) 가 주어지고, 반복되지 않는 longest substring 을 찾는 문제
// example
// input: s = 'abcabcbb'
// output: 3
// explanation: 'abc'의 길이 = 3


// Sliding window 방식
function lengthOfLongestSubstring(s: string) : number {
  let charSet = new Set<string>();
  let left = 0;
  let maxLength = 0;

  for (let right = 0; right < s.length; right++) {
    while (charSet.has(s[right])) {
      charSet.delete(s[left]);
      left++;
    }
    charSet.add(s[right]);
    maxLength = Math.max(maxLength, right - left + 1);
  }

  return maxLength;
}