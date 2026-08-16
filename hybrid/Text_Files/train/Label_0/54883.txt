import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.PriorityQueue;
import java.util.StringTokenizer;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author Abhilash
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskD solver = new TaskD();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskD {
        static int n;
        static int m;
        static int r;
        static int k;

        public void solve(int testNumber, InputReader in, PrintWriter out) {
            n = in.nextInt();
            m = in.nextInt();
            r = in.nextInt();
            k = in.nextInt();
            PriorityQueue<TaskD.Cell> pq = new PriorityQueue<>((a, b) -> {
                if (b.val > a.val)
                    return 1;
                else if (a.val > b.val)
                    return -1;
                else
                    return 0;
            });
            for (int i = 1; i <= n; i++) {
                int mid = (m + 1) / 2;
                TaskD.Cell cell1 = new TaskD.Cell(i, mid - 1, 0);
                TaskD.Cell cell2 = new TaskD.Cell(i, mid, 1);
                pq.add(cell1);
                pq.add(cell2);
            }
            long total = 0;
            for (int i = 0; i < k; i++) {
                TaskD.Cell top = pq.poll();
                total += top.val;
                if (top.d == 0 && top.y > 1) {
                    TaskD.Cell newCell = new TaskD.Cell(top.x, top.y - 1, 0);
                    pq.add(newCell);
                } else if (top.d == 1 && top.y < m) {
                    TaskD.Cell newCell = new TaskD.Cell(top.x, top.y + 1, 1);
                    pq.add(newCell);
                }
            }
            double ans = (double) total / ((n - r + 1) * 1l * (m - r + 1));
            out.println(ans);
        }

        static class Cell {
            int x;
            int y;
            int d;
            long val;

            Cell(int x, int y, int d) {
                this.x = x;
                this.y = y;
                this.d = d;
                val = (Math.min(n + 1, x + r) - Math.max(x, r)) * 1l * (Math.min(m + 1, y + r) - Math.max(y, r));
            }

        }

    }

    static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }

        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

    }
}

