import java.io.PrintWriter;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        try (Scanner in = new Scanner(System.in); PrintWriter out = new PrintWriter(System.out)) {
            int n = in.nextInt();
            TreeSet<Segment> set = new TreeSet<>();
            Segment query = new Segment(0, -1);
            set.add(new Segment(0, 0));
            for (int i = 0; i < n; i++) {
                query.l = in.nextInt();
                Segment res = set.floor(query);
                if (res == null) {
                    out.println("No");
                    continue;
                }
                out.println("Yes");
                if (res.r < query.l) {
                    Segment seg = new Segment(res.r + 1, query.l);
                    res.r--;
                    if (!res.isValid()) set.remove(res);
                    set.add(seg);
                } else {
                    set.remove(res);
                    Segment left = new Segment(res.l, query.l - 1);
                    Segment right = new Segment(query.l + 1, res.r);
                    if (left.isValid()) set.add(left);
                    if (right.isValid()) set.add(right);
                }
            }
        }
    }

    private static class Segment implements Comparable<Segment> {
        int l, r;

        Segment(int l, int r) {
            this.l = l;
            this.r = r;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;

            Segment segment = (Segment) o;

            if (l != segment.l) return false;
            return r == segment.r;
        }

        @Override
        public int hashCode() {
            int result = l;
            result = 31 * result + r;
            return result;
        }

        @Override
        public int compareTo(Segment o) {
            return Integer.compare(l, o.l);
        }

        boolean isValid() {
            return l <= r;
        }
    }
}

