// string(s)가 주어지고, longestpalindromic substring 을 return
// A substring is a contiguous non-empty sequence of characters within a string.

// Example 1
// input: s = "babad"
// output: "bad"
// explanation: "aba" is also a valid answer

// Example 2
// input: s = "cbbd"
// ouput: "bb"

// Expand Around Center 중심 확장법!
// 문자열의 모든 위치에서 팰리늗롬이 될 수 있는 최대 길이를 확장하며 확인
// 팰린드롬 : 가운데를 기준으로 좌우 대칭을 이룸
// 팰린드롬의 중심 개수는 총 n + (n - 1)개 => 홀수(n) + 짝수(n-1)
// 각 중심에서 양쪽으로 확장하며 가장 긴 팰린드롬을 찾기

function longestPalindrome(s: string): string {
  if (s.length < 2) return s;

  let start = 0;
  let maxLength = 0;

  const expandAroundCenter = (left: number, right: number) => {
    while (left >= 0 && right < s.length && s[left] === s[right]) {
      left--;
      right++;
    }

    let length = right - left - 1;

    if (length > maxLength) {
      start = left + 1;
      maxLength = length;
    }
  }

  for (let i = 0; i < s.length; i++) {
    expandAroundCenter(i, i); // 홀수 check
    expandAroundCenter(i, i + 1); // 짝수 check
  }

  return s.substring(start, start + maxLength);
}