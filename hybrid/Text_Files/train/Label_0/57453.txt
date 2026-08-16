import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.io.BufferedWriter;
import java.util.InputMismatchException;
import java.io.IOException;
import java.util.Stack;
import java.util.ArrayList;
import java.util.Vector;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author Mufaddal Naya
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        OutputWriter out = new OutputWriter(outputStream);
        FPathPassI solver = new FPathPassI();
        solver.solve(1, in, out);
        out.close();
    }

    static class FPathPassI {
        ArrayList<Integer>[] adj;
        int[] a;
        Stack<Integer>[] f;
        int[] tin;
        int[] s;
        long[] res;
        int cur = 0;
        int[] cnt;

        public void solve(int testNumber, InputReader c, OutputWriter w) {
            int n = c.readInt();
            a = c.readIntArray(n, -1);
            adj = c.readGraph(n, n - 1);
            f = new Stack[n];
            for (int i = 0; i < n; i++) {
                f[i] = new Stack<>();
            }
            tin = new int[n];
            s = new int[n];
            res = new long[n];
            cnt = new int[n];
            Arrays.fill(res, (n * (long) (n - 1)) / 2);

            dfs_(0, -1);


            for (int i = 0; i < n; i++) {
                long tot = n;
                while (!f[i].isEmpty()) {
                    tot -= s[f[i].pop()];
                }
                res[i] -= tot * (tot - 1) / 2;
                w.printLine(res[i] + cnt[i]);
            }

            // BruteForce

        /*
        for(int i=0;i<n;i++) {
            boolean vis[] = new boolean[n];
            long tot = 0;
            int cnt = 0;
            for(int j=0;j<n;j++) if(a[j] == i) {
                cnt++;
                for(int xx:adj[j]) {
                    if(!vis[xx]) {
                        long d = brute_(xx, j, i, vis);
                        tot += d*(d-1)/2;
                    }
                }
            }
            if(cnt!=0)
                w.printLine(n*(long)(n-1)/2 - tot + cnt);
            else w.printLine(0);
        }
    }

    private long brute_(int x, int p, int col, boolean[] vis) {
        if(a[x] == col || vis[x]) return 0;
        vis[x] = true;
        int tot = 0;
        for(int xx:adj[x]) {
            if(xx!=p) {
                tot += brute_(xx,x,col, vis);
            }
        }
        return 1+tot;
    }
     */
        }

        private void dfs_(int x, int p) {
            s[x] = 1;
            cnt[a[x]]++;
            tin[x] = cur++;
            for (int xx : adj[x]) {
                if (xx != p) {
                    dfs_(xx, x);
                    long rr = s[xx];
                    while (!f[a[x]].isEmpty() && tin[f[a[x]].peek()] > tin[x]) {
                        rr -= s[f[a[x]].pop()];
                    }
                    s[x] += s[xx];
                    res[a[x]] -= rr * (rr - 1) / 2;
                }
            }
            f[a[x]].add(x);
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

        public int[] readIntArray(int size, int x) {
            int[] array = new int[size];
            for (int i = 0; i < size; i++) {
                array[i] = readInt() + x;
            }
            return array;
        }

        public int read() {
            if (numChars == -1) {
                throw new InputMismatchException();
            }
            if (curChar >= numChars) {
                curChar = 0;
                try {
                    numChars = stream.read(buf);
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
                if (numChars <= 0) {
                    return -1;
                }
            }
            return buf[curChar++];
        }

        public int readInt() {
            int c = read();
            while (isSpaceChar(c)) {
                c = read();
            }
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            int res = 0;
            do {
                if (c < '0' || c > '9') {
                    throw new InputMismatchException();
                }
                res *= 10;
                res += c - '0';
                c = read();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        public ArrayList<Integer>[] readGraph(int n, int m) {
            ArrayList<Integer>[] adj = new ArrayList[n];
            for (int i = 0; i < n; i++) {
                adj[i] = new ArrayList<>();
            }
            for (int i = 0; i < m; i++) {
                int u = readInt() - 1, v = readInt() - 1;
                adj[u].add(v);
                adj[v].add(u);
            }
            return adj;
        }

        public boolean isSpaceChar(int c) {
            if (filter != null) {
                return filter.isSpaceChar(c);
            }
            return isWhitespace(c);
        }

        public static boolean isWhitespace(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        public interface SpaceCharFilter {
            public boolean isSpaceChar(int ch);

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

        public void close() {
            writer.close();
        }

        public void printLine(long i) {
            writer.println(i);
        }

    }
}

