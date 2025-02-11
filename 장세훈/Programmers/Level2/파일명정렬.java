class 파일명정렬 {

    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/17686
     */
    public String[] solution(String[] files) {
        List<Word> words = new ArrayList<>();

        for (String file : files) {
            String head = "";
            String number = "";
            String tail = "";
            boolean isDoneNumber = false;

            for (int i = 0; i < file.length(); i++) {
                if ((i > 0 && Character.isDigit(file.charAt(i - 1)) && !Character.isDigit(file.charAt(i))) || isDoneNumber) {
                    isDoneNumber = true;
                    tail += file.charAt(i);
                } else if (!Character.isDigit(file.charAt(i)))
                    head += file.charAt(i);
                else if (Character.isDigit(file.charAt(i)))
                    number += file.charAt(i);
            }
            words.add(new Word(head, number, tail));
        }

        words.sort((o1, o2) -> {
            if (o1.head.equalsIgnoreCase(o2.head)) return Integer.parseInt(o1.number) - Integer.parseInt(o2.number);
            else return o1.head.compareToIgnoreCase(o2.head);
        });

        return words.stream().map(Word::toString).toArray(String[]::new);
    }

    class Word {
        String head;
        String number;
        String tail = "";

        public Word(String head, String number, String tail) {
            this.head = head;
            this.number = number;
            this.tail = tail;
        }

        @Override
        public String toString() {
            return head + number + tail;
        }
    }
}