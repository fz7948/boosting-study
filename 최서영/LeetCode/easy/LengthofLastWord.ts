// https://leetcode.com/problems/length-of-last-word/

function lengthOfLastWord(s: string): number {
  return s.trim().split(' ').pop()?.length || 0;
};
