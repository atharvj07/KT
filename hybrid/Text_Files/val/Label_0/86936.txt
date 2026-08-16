import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.util.Collections;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author lebegio
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        MyReader in = new MyReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskD solver = new TaskD();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskD {
        public void solve(int testNumber, MyReader in, PrintWriter out) {
            int n = in.nextInt();
            int l = in.nextInt();
            int r = in.nextInt();
            int[] A = new int[n];
            int[] P = new int[n];
            for (int i = 0; i < n; i++) {
                A[i] = in.nextInt();
            }
            ArrayList<Pair> nodes = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                P[i] = in.nextInt();
                nodes.add(new Pair(A[i], P[i], i));
            }

            Collections.sort(nodes, (o1, o2) -> {
                return Long.compare(o2.y, o1.y);//reverse order
            });

            int d = (int) (r - nodes.get(0).x);
            for (Pair p : nodes) {
                int max = (int) Math.min(r, p.x + d);
                p.z = max;
                d = (int) (max - p.x - 1);
                if (max < l) {
                    out.println(-1);
                    return;
                }
            }

            Collections.sort(nodes, (o1, o2) -> {
                return o1.poz - o2.poz;
            });

            for (Pair p : nodes) {
                out.print(p.z + " ");
            }
        }

    }

    static class MyReader {
        private BufferedReader buffReader;
        private StringTokenizer strTokenizer;
        private static final int SIZE = 32768;

        public MyReader(InputStream inputStream) {
            buffReader = new BufferedReader(new InputStreamReader(inputStream), SIZE);
        }

        public String next() {
            if (strTokenizer == null || !strTokenizer.hasMoreTokens()) {
                try {
                    strTokenizer = new StringTokenizer(buffReader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return strTokenizer.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

    }

    static class Pair {
        public int poz = 0;
        public long x = 0;
        public long y = 0;
        public long z = 0;
        public boolean isStart = true;

        public Pair(long xx, long yy) {
            this.x = xx;
            this.y = yy;
        }

        public Pair(long xx, long yy, int poz) {
            this.x = xx;
            this.y = yy;
            this.poz = poz;
        }

        public Pair(long xx, long yy, int poz, boolean isStart) {
            this.x = xx;
            this.y = yy;
            this.poz = poz;
            this.isStart = isStart;
        }

    }
}

