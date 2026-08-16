import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class CliqueProblem {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        Interval[] intervals = new Interval[n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            intervals[i] = new Interval(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }

        Arrays.sort(intervals);
        Interval max = intervals[0];
        int size = 1;
        for (int i = 1; i < n; i++) {
            if (intervals[i].x - intervals[i].w >= max.x + max.w) {
                max = intervals[i];
                size++;
            }
        }

        System.out.println(size);
    }

    private static class Interval implements Comparable<Interval> {
        public int x;
        public int w;

        public Interval(int x, int w) {
            this.x = x;
            this.w = w;
        }

        @Override
        public int compareTo(Interval o) {
            return (this.x + this.w) - (o.x + o.w);
        }
    }
}
