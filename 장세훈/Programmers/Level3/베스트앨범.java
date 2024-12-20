class 베스트앨범 {

    public static void main(String[] args) {
        new 베스트앨범().solution(
                new String[]{"classic", "pop", "classic", "classic", "pop"},
                new int[]{500, 600, 150, 800, 2500}
        );
    }

    public int[] solution(String[] genres, int[] plays) {
        Map<String, Integer> playTotal = new HashMap<>();
        Map<String, PriorityQueue<Genre>> genreMap = new HashMap<>();
        List<Integer> answer = new ArrayList<>();

        for (int i = 0; i < genres.length; i++) {
            playTotal.put(genres[i], playTotal.getOrDefault(genres[i], 0) + plays[i]);
            genreMap.putIfAbsent(genres[i], new PriorityQueue<>((g1, g2) -> {
                if (g1.play == g2.play) return g1.index - g2.index;
                return g2.play - g1.play;
            }));
            genreMap.get(genres[i]).add(new Genre(plays[i], i));
        }

        List<String> sortedGenres = playTotal.keySet().stream().sorted(Comparator.comparingInt(playTotal::get).reversed()).collect(Collectors.toList());

        for (String sortedGenre : sortedGenres) {
            if (!genreMap.get(sortedGenre).isEmpty())
                answer.add(genreMap.get(sortedGenre).poll().index);
            if (!genreMap.get(sortedGenre).isEmpty())
                answer.add(genreMap.get(sortedGenre).poll().index);
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }

    class Genre {
        int play;
        int index;

        public Genre(int play, int index) {
            this.play = play;
            this.index = index;
        }
    }
}