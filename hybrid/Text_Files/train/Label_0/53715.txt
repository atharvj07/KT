import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.InputMismatchException;
import java.io.IOException;
import java.util.Collections;
import java.util.ArrayList;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author cunbidun
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        DEqueue solver = new DEqueue();
        solver.solve(1, in, out);
        out.close();
    }

    static class DEqueue {
        private static final int INF = (int) 2e9 + 7;
        private InputReader in;
        private PrintWriter out;

        public void solve(int testNumber, InputReader in, PrintWriter out) {
            this.in = in;
            this.out = out;
            int n = in.nextInt();
            int k = in.nextInt();
            int[] a = in.nextIntArray(n, 1);
            int ans = 0;
            for (int l = 0; l <= n; l++) {
                for (int r = 0; r <= n; r++) {
                    if (l + r <= MaxMin.Min(n, k)) {
                        int cur = 0;
                        ArrayList<Integer> L = new ArrayList<>();
                        L.add(-INF);
                        ArrayList<Integer> R = new ArrayList<>();
                        R.add(-INF);
                        for (int i = 1; i <= l; i++)
                            L.add(a[i]);
                        for (int i = n; i >= n - r + 1; i--)
                            R.add(a[i]);
                        int[] curL = new int[L.size()];
                        int[] curR = new int[R.size()];


                        Collections.sort(L);
                        Collections.sort(R);
//                    System.out.println(l + " " + r);

//                    for (int i : L) System.out.print(i + " ");
//                    System.out.println();
//                    for (int i : R) System.out.print(i + " ");
//                    System.out.println();

                        for (int i = 1; i <= l; i++) {
                            curL[i] = curL[i - 1] + L.get(i);
                        }
                        for (int i = 1; i <= r; i++) {
                            curR[i] = curR[i - 1] + R.get(i);
                        }

                        int num = l + r;
                        for (int i = 0; i <= l; i++) {
                            for (int j = 0; j <= r; j++) {
                                if (i + j + num <= k) {
                                    cur = MaxMin.Max(cur, curL[l] + curR[r] - (curL[i] + curR[j]));
                                }
                            }
                        }
                        ans = MaxMin.Max(ans, cur);
                    }
                }
            }
            out.println(ans);
        }

    }

    static class InputReader extends InputStream {
        private InputStream stream;
        private byte[] buf = new byte[1024];
        private int curChar;
        private int numChars;

        public InputReader(InputStream stream) {
            this.stream = stream;
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

        public int nextInt() {
            int c = read();
            while (isSpaceChar(c))
                c = read();
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

        public int[] nextIntArray(int length, int stIndex) {
            int[] arr = new int[length + stIndex];
            for (int i = stIndex; i < stIndex + length; i++)
                arr[i] = nextInt();
            return arr;
        }

        private static boolean isSpaceChar(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

    }

    static class MaxMin {
        public static <T extends Comparable<T>> T Max(T x, T y) {
            T max = x;
            if (y.compareTo(max) > 0) max = y;
            return max;
        }

        public static <T extends Comparable<T>> T Min(T x, T y) {
            T min = x;
            if (y.compareTo(min) < 0) min = y;
            return min;
        }

    }
}

