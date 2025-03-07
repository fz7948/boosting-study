class ClosestPrimeNumbersInRange {

    /*
        https://leetcode.com/problems/closest-prime-numbers-in-range
     */

    public int[] closestPrimes(int left, int right) {
        List<Integer> prime = new ArrayList<>();
        boolean[] isPrime = new boolean[right + 1];
        Arrays.fill(isPrime, true);
        isPrime[0] = isPrime[1] = false;


        for (int i = 2; i < isPrime.length; i++) {
            if (isPrime[i]) {
                prime.add(i);
                for (int j = i + i; j < isPrime.length; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        int gap = Integer.MAX_VALUE;
        int l = -1, r = -1;
        for (int i = 0; i < prime.size() - 1; i++) {
            if (prime.get(i) >= left && prime.get(i + 1) - prime.get(i) < gap) {
                l = prime.get(i);
                r = prime.get(i + 1);
                gap = r - l;
            }
        }

        return new int[]{l, r};
    }
}