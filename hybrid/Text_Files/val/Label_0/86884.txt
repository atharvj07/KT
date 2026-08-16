import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.io.BufferedWriter;
import java.util.Set;
import java.util.InputMismatchException;
import java.io.IOException;
import java.util.TreeSet;
import java.util.ArrayList;
import java.util.HashSet;
import java.io.Writer;
import java.io.OutputStreamWriter;
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
        OutputWriter out = new OutputWriter(outputStream);
        CABlandYard solver = new CABlandYard();
        solver.solve(1, in, out);
        out.close();
    }

    static class CABlandYard {
        public void solve(int testNumber, InputReader in, OutputWriter out) {
            int n = in.nextInt(), m = in.nextInt();
            ArrayList<Set<Integer>> graph = new ArrayList<>();
            for (int i = 0; i < n; i++) graph.add(new HashSet<Integer>());
            String s = in.next();
            int[][] num = new int[n][2];
            for (int i = 0; i < m; i++) {
                int a = in.nextInt() - 1, b = in.nextInt() - 1;
                if (graph.get(a).contains(b)) continue;
                graph.get(a).add(b);
                num[a][s.charAt(b) - 'A']++;
                if (a != b) {
                    num[b][s.charAt(a) - 'A']++;
                    graph.get(b).add(a);
                }
            }
            TreeSet<Integer> q = new TreeSet<Integer>();
            for (int i = 0; i < n; i++) {
                int val = (num[i][0] > 0 ? 1 : 0) * 2 + (num[i][1] > 0 ? 1 : 0);
                q.add((val << 20) + i);
            }
            boolean[] done = new boolean[n];
            while (!q.isEmpty()) {
                int cur = q.first();
                q.remove(cur);
                int val = cur >>> 20;
                int node = cur & ((1 << 20) - 1);
                done[node] = true;
                if (val == 3) {
                    out.println("Yes");
                    break;
                }
                if (q.isEmpty()) {
                    out.println("No");
                    break;
                }
                int type = s.charAt(node) - 'A';
                for (Integer i : graph.get(node)) {
                    if (done[i]) continue;
                    int valueOld = (num[i][0] > 0 ? 1 : 0) * 2 + (num[i][1] > 0 ? 1 : 0);
                    q.remove((valueOld << 20) + i);
                    num[i][type]--;
                    int valueNew = (num[i][0] > 0 ? 1 : 0) * 2 + (num[i][1] > 0 ? 1 : 0);
                    q.add((valueNew << 20) + i);
                    graph.get(i).remove(node);
                }
            }
        }

    }

    static class InputReader {
        private InputStream stream;
        private byte[] buf = new byte[1024];
        private int curChar;
        private int numChars;
        private InputReader.SpaceCharFilter filter;

        public InputReader(InputStream stream) {
            this.stream = stream;
        }

        public int read() {
            if (numChars == -1) throw new InputMismatchException();
            if (curChar >= numChars) {
                curChar = 0;
                try {
                    numChars = stream.read(buf);
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
                if (numChars <= 0) return -1;
            }
            return buf[curChar++];
        }

        public int nextInt() {
            int c = read();
            while (isSpaceChar(c)) c = read();
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            int res = 0;
            do {
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                res *= 10;
                res += c - '0';
                c = read();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        public String next() {
            int c;
            while (isSpaceChar(c = this.read())) {
                ;
            }

            StringBuilder result = new StringBuilder();
            result.appendCodePoint(c);

            while (!isSpaceChar(c = this.read())) {
                result.appendCodePoint(c);
            }

            return result.toString();
        }

        public boolean isSpaceChar(int c) {
            if (filter != null)
                return filter.isSpaceChar(c);
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        public interface SpaceCharFilter {
            boolean isSpaceChar(int ch);

        }

    }

    static class OutputWriter {
        private final PrintWriter writer;

        public OutputWriter(OutputStream outputStream) {
            writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(outputStream)));
        }

        public OutputWriter(Writer writer) {
            this.writer = new PrintWriter(writer);
        }

        public void println(Object... objects) {
            for (int i = 0; i < objects.length; i++) {
                if (i != 0) {
                    writer.print(' ');
                }
                writer.print(objects[i]);
            }
            writer.print('\n');
        }

        public void close() {
            writer.close();
        }

    }
}

