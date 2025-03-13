class ProductOfNumbers {
    /*
        https://leetcode.com/problems/product-of-the-last-k-numbers/
        
     */
    List<Integer> list;

    public ProductOfNumbers() {
        list = new ArrayList<>();
        list.add(1);
    }

    public void add(int num) {
        if(num == 0) {
            list.clear();
            list.add(1);
        }else {
            list.add(num * list.getLast());
        }
    }

    public int getProduct(int k) {
        if (k >= list.size()) {
            return 0;
        }
        return list.getLast() / list.get(list.size() - 1 - k);
    }
}