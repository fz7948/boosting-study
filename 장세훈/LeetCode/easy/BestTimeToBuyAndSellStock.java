class BestTimeToBuyAndSellStock {
   
    /*
        121. Best Time to Buy and Sell Stock
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

        2중 for문으로 풀면 타임아웃 발생
        생각을 해보면 for문 하나로 처리 가능
        prices를 순회하할 때 최소값을 찾으며 동시에 수익 최댓값을 찾으면 됨.
     */

    public int maxProfit(int[] prices) {
        int min = prices[0];
        int answer = 0;

        for (int price : prices) {
            if (min > price)
                min = price;
            else if (price - min > answer)
                answer = price - min;
        }

        return answer;
    }
}