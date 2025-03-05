class TrappingRainWater {
 
    /*
        https://leetcode.com/problems/trapping-rain-water/
     */

    public int trap(int[] height) {

        Deque<Integer> stack = new ArrayDeque<>();
        int result = 0;

        for (int h : height) {
            if (stack.isEmpty()) {
                if (h != 0)
                    stack.addLast(h);
            } else {
                if (stack.peekFirst() <= h) {
                    while (!stack.isEmpty()) {
                        result += stack.peekFirst() - stack.pollLast();
                    }
                }

                stack.addLast(h);
            }
        }

        while (!stack.isEmpty()) {
            int base = stack.pollLast();

            while (!stack.isEmpty() && base > stack.peekLast())
                result += base - stack.pollLast();
        }

        return result;
    }
}