import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.io.IOException;
import java.util.InputMismatchException;
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
        TaskG solver = new TaskG();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskG {
        public void solve(int testNumber, InputReader in, PrintWriter out) {
            int l = in.nextInt();
            String s = in.nextString();
            String t = in.nextString();

            if (s.compareTo(t) > 0) {
                String tmp = s;
                s = t;
                t = tmp;
            }

            if (t.startsWith(s) && (s + t).compareTo(t + s) > 0) {
                if (check(out, l, t, s)) return;
                if (check(out, l, s, t)) return;
            } else {
                if (check(out, l, s, t)) return;
            }

            throw new RuntimeException();
        }

        private boolean check(PrintWriter out, int l, String s, String t) {
            int sLen = s.length();
            int tLen = t.length();
            for (int i = 0; i * tLen <= l; i++) {
                if ((l - i * tLen) % sLen == 0) {
                    StringBuilder sb = new StringBuilder();
                    for (int j = 0; j < (l - i * tLen) / sLen; j++) {
                        sb.append(s);
                    }
                    for (int j = 0; j < i; j++) {
                        sb.append(t);
                    }
                    out.println(sb.toString());
                    return true;
                }
            }
            return false;
        }

    }

    static class InputReader {
        BufferedReader in;
        StringTokenizer tok;

        public String nextString() {
            while (!tok.hasMoreTokens()) {
                try {
                    tok = new StringTokenizer(in.readLine(), " ");
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
            }
            return tok.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(nextString());
        }

        public InputReader(InputStream inputStream) {
            in = new BufferedReader(new InputStreamReader(inputStream));
            tok = new StringTokenizer("");
        }

    }
}

