import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskB solver = new TaskB();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskB {
        public void solve(int testNumber, InputReader in, PrintWriter out) {
            int n = in.nextInt();
            Node[] s = new Node[n];
            for (int i = 0; i < n; ++i) {
                s[i] = new Node(in.nextInt(), in.nextInt());
            }
            Arrays.sort(s);
            int maxr = 0, ans = 0;
            for (int i = 0; i < n; ++i) {
                if (s[i].l > maxr) {
                    maxr = s[i].r;
                    ++ans;
                }
            }
            out.println(ans);
        }

        class Node implements Comparable<Node> {
            int l;
            int r;

            public Node(int l, int r) {
                this.l = l;
                this.r = r;
            }


            public int compareTo(Node o) {
                if (l == o.l && r == o.r) return 0;
                return r < o.r || r == o.r && l > o.l ? -1 : 1;
            }

        }

    }

    static class InputReader {
        BufferedReader reader;
        StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream));
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
