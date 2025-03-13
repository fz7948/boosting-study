class CountAndSay {
    /*
        https://leetcode.com/problems/count-and-say/
     */

    public String countAndSay(int n) {
        String say = "";

        for (int i = 1; i <= n; i++) {
            if (i == 1) {
                say = "1";
            } else {
                String base = say.charAt(0) + "";
                int count = 1;
                StringBuilder newSay = new StringBuilder();
                for (int j = 1; j < say.length(); j++) {
                    if (base.equals(say.charAt(j) + ""))
                        count++;
                    else {
                        newSay.append(count).append(base);
                        count = 1;
                        base = say.charAt(j) + "";
                    }
                }
                newSay.append(count).append(base);
                say = newSay.toString();
            }

        }

        return say;
    }
}