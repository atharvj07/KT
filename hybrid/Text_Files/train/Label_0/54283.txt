import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.InputMismatchException;
import java.io.IOException;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author Pradyumn
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        FastReader in = new FastReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskD solver = new TaskD();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskD {
        public void solve(int testNumber, FastReader in, PrintWriter out) {
            int n = in.nextInt();
            TaskD.SegmentTree segmentTree = new TaskD.SegmentTree(n);
            int m = in.nextInt();
            int[] a = in.nextIntArray(m);
            int[] ans = new int[n];
            int last = 0;
            for (int q = 0; q < n; ++q) {
                int type = in.nextInt();
                if (type >= 0) {
                    ans[last] = type;
                    segmentTree.add(last);
                    ++last;
                } else {
                    for (int step = 0; step < m; ++step) {
                        int cur = a[step] - (step + 1);
                        if (cur >= segmentTree.getSum(0, n - 1))
                            break;
                        segmentTree.delete(cur);
                    }
                }
            }

            if (segmentTree.getSum(0, n - 1) == 0) {
                out.println("Poor stack!");
            } else {
                for (int i = 0; i < last; ++i) {
                    if (segmentTree.getSum(i, i) > 0)
                        out.print(ans[i]);
                }
                out.println();
            }
        }

        static class SegmentTree {
            int[] seg;
            int N;
            int size;

            public SegmentTree(int n) {
                N = n;
                size = N << 2;
                seg = new int[size];
            }

            public void delete(int ind) {
                delete(0, N - 1, 0, ind);
            }

            public void add(int ind) {
                add(0, N - 1, 0, ind);
            }

            public int getSum(int l, int r) {
                return getSum(0, N - 1, 0, l, r);
            }

            public void delete(int s, int e, int c, int ind) {
                --seg[c];
                if (s == e)
                    return;
                int m = (s + e) >>> 1;
                int sumLeft = seg[2 * c + 1];
                if (sumLeft > ind)
                    delete(s, m, 2 * c + 1, ind);
                else
                    delete(m + 1, e, 2 * c + 2, ind - sumLeft);
            }

            public void add(int s, int e, int c, int ind) {
                ++seg[c];
                if (s == e)
                    return;
                int m = (s + e) >>> 1;
                if (ind <= m)
                    add(s, m, 2 * c + 1, ind);
                else
                    add(m + 1, e, 2 * c + 2, ind);
            }

            public int getSum(int s, int e, int c, int l, int r) {
                if (l > r || s > e || s > r || l > e)
                    return 0;
                if (s == e) {
                    return seg[c];
                }
                if (s >= l && e <= r)
                    return seg[c];
                int m = (s + e) >>> 1;
                return getSum(s, m, 2 * c + 1, l, r) + getSum(m + 1, e, 2 * c + 2, l, r);
            }

        }

    }

    static class FastReader {
        private InputStream stream;
        private byte[] buf = new byte[8192];
        private int curChar;
        private int pnumChars;

        public FastReader(InputStream stream) {
            this.stream = stream;
        }

        private int pread() {
            if (pnumChars == -1) {
                throw new InputMismatchException();
            }
            if (curChar >= pnumChars) {
                curChar = 0;
                try {
                    pnumChars = stream.read(buf);
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
                if (pnumChars <= 0) {
                    return -1;
                }
            }
            return buf[curChar++];
        }

        public int nextInt() {
            int c = pread();
            while (isSpaceChar(c))
                c = pread();
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = pread();
            }
            int res = 0;
            do {
                if (c == ',') {
                    c = pread();
                }
                if (c < '0' || c > '9') {
                    throw new InputMismatchException();
                }
                res *= 10;
                res += c - '0';
                c = pread();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        public int[] nextIntArray(int n) {
            int[] array = new int[n];
            for (int i = 0; i < n; i++) {
                array[i] = nextInt();
            }
            return array;
        }

        private boolean isSpaceChar(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

    }
}

