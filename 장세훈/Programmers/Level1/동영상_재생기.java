package 장세훈.Programmers.Level1;

import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

/*
    https://school.programmers.co.kr/learn/courses/30/lessons/340213
    단순 구현 문제
    LocalTime을 안썼으면 더 복잡했을 듯..
    아 다른 사람 풀이보니 각 시간을 초로 변환해서 계산한다. 그럼 다소 편하게 구현 가능할 듯.
 */
class 동영상_재생기 {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        Video video = new Video(video_len, pos, op_start, op_end);

        for (String command : commands) {
            if (command.equals("next"))
                video.next();
            else video.prev();
        }

        return video.pos.format(DateTimeFormatter.ofPattern("mm:ss"));
    }

    class Video {
        LocalTime pos;
        LocalTime opStart;
        LocalTime opEnd;
        LocalTime videoLen;

        public Video(String videoLen, String pos, String start, String end) {
            String[] splitPos = pos.split(":");
            String[] splitVideoLen = videoLen.split(":");
            String[] splitStart = start.split(":");
            String[] splitEnd = end.split(":");

            this.videoLen = LocalTime.of(0, Integer.parseInt(splitVideoLen[0]), Integer.parseInt(splitVideoLen[1]));
            this.opStart = LocalTime.of(0, Integer.parseInt(splitStart[0]), Integer.parseInt(splitStart[1]));
            this.opEnd = LocalTime.of(0, Integer.parseInt(splitEnd[0]), Integer.parseInt(splitEnd[1]));
            this.pos = LocalTime.of(0, Integer.parseInt(splitPos[0]), Integer.parseInt(splitPos[1]));
            skipOp();

        }

        private void skipOp() {
            if ((opStart.isBefore(pos) || opStart.equals(pos)) &&
                    (opEnd.isAfter(pos) || opEnd.equals(pos)))
                pos = opEnd;
        }

        void next() {
            pos = pos.plusSeconds(10);
            if (pos.isAfter(videoLen))
                pos = videoLen;
            skipOp();
        }

        void prev() {
            if (pos.isBefore(LocalTime.of(0, 0, 10)))
                pos = LocalTime.of(0, 0);
            else
                pos = pos.minusSeconds(10);
            skipOp();
        }
    }
}

