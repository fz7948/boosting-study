class AssignCookies {
    /*
        https://leetcode.com/problems/assign-cookies/
        
        그리디 문제
        배열을 정렬하고 앞 순서부터 쿠키를 할당
     */
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);

        int i = 0, j = 0;

        while (i < g.length && j < s.length) {
            if (s[j] >= g[i]) i++;
            j++;
        }

        return i;
    }
}