import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class WinterIsComing {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[] tire = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            if (Integer.parseInt(st.nextToken()) < 0) {
                tire[i] = 1;
                k--;
            }
        }
        if (k < 0) {
            System.out.println(-1);
            return;
        }

        int start = -1;
        int end = -1;
        ArrayList<Interval> intervals = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (start == -1) {
                if (tire[i] == 1) {
                    start = i;
                    end = i;
                }
            } else {
                if (tire[i] == 1) {
                    end++;
                } else {
                    intervals.add(new Interval(start, end));
                    start = -1;
                    end = -1;
                }
            }

            if (i == n - 1 && end > -1) {
                intervals.add(new Interval(start, end));
            }
        }

        int numIntervals = intervals.size();
        PriorityQueue<Pair> priorityQueue = new PriorityQueue<>(Math.max(numIntervals, 1), new Comparator<Pair>() {
            @Override
            public int compare(Pair o1, Pair o2) {
                return o1.diff - o2.diff;
            }
        });
        for (int i = 1; i < numIntervals; i++) {
            priorityQueue.add(new Pair(intervals.get(i).start - intervals.get(i - 1).end - 1, i - 1, i));
        }
        while (true) {
            if (priorityQueue.isEmpty()) {
                break;
            }
            Pair pair = priorityQueue.poll();
            if (pair.diff > k) {
                break;
            }
            int i = pair.index1;
            int j = pair.index2;
            for (start = intervals.get(i).end + 1, end = intervals.get(j).start; start < end; start++) {
                tire[start] = 1;
            }
            intervals.get(i).end = intervals.get(j).end;
            intervals.get(j).start = intervals.get(i).start;
            k -= pair.diff;
        }
        if (numIntervals > 0 && n - intervals.get(numIntervals - 1).end - 1 <= k) {
            for (start = intervals.get(numIntervals - 1).end, end = n; start < end; start++) {
                tire[start] = 1;
            }
        }

        int previous = 0;
        int times = 0;
        for (int i = 0; i < n; i++) {
            if (previous != tire[i]) {
                previous = tire[i];
                times++;
            }
        }

        System.out.println(times);
    }

    private static class Interval {
        private int start;
        private int end;

        private Interval(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }

    private static class Pair {
        private int diff;
        private int index1;
        private int index2;

        private Pair(int diff, int index1, int index2) {
            this.diff = diff;
            this.index1 = index1;
            this.index2 = index2;
        }
    }
}