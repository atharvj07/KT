/**
 * Created by Aminul on 2/16/2021.
 */

import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class G {
    public static void main(String[] args) throws Exception {
        FastReader in = new FastReader(System.in);
        PrintWriter pw = new PrintWriter(System.out);
        int test = in.nextInt();
        for (int t = 1; t <= test; t++) {
            int n = in.nextInt(), m = in.nextInt();
            long[] arr = new long[n];
            long maxSum = 0, totalSum = 0;
            for (int i = 0; i < n; i++) {
                arr[i] = in.nextInt();
                if(i > 0) {
                    arr[i] += arr[i - 1];
                }
                maxSum = max(maxSum, arr[i]);
            }
            totalSum = arr[n - 1];

            SparseTable rmq = new SparseTable(arr);
            for (int i = 0; i < m; i++) {
                int x = in.nextInt();
                if (maxSum >= x) {
                    int idx = binarySearch(0, n - 1, rmq, x);
                    pw.print(idx + " ");
                } else if (totalSum <= 0) {
                    pw.print(-1 + " ");
                } else {
                    long p = binarySearchForTotal(0, (long)2e9, x, totalSum, maxSum);
                    long res = p * n;
                    long rem = x - (p * totalSum);
                    if(rem == 0) {
                        res--;
                    } else {
                        res += binarySearch(0, n - 1, rmq, rem);
                    }
                    pw.print(res + " ");

                }
            }
            pw.println();
        }

        pw.close();
    }


    static long binarySearchForTotal(long l, long r, long target, long totalSum, long maxSum) {
        long res = 0;
        while (l <= r) {
            long mid = (l + r) >> 1;
            long sum = maxSum +  (mid * totalSum);
            if (sum >= target) {
                res = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return res;
    }


    static int binarySearch(int l, int r, SparseTable rmq, long target) {
        int res = -1;
        while (l <= r) {
            int mid = (l + r) >> 1;
            if (rmq.query(0, mid) >= target) {
                res = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return res;
    }

    static class SparseTable {
        int[] logTable;
        long[][] rmq;
        long[] a;

        public SparseTable(long[] a) {
            this.a = a;
            int n = a.length;

            logTable = new int[n + 1];
            for (int i = 2; i <= n; i++)
                logTable[i] = logTable[i >> 1] + 1;

            rmq = new long[logTable[n] + 1][n];

            for (int i = 0; i < n; ++i)
                rmq[0][i] = a[i];

            for (int k = 1; (1 << k) < n; ++k) {
                for (int i = 0; i + (1 << k) <= n; i++) {
                    long x = rmq[k - 1][i];
                    long y = rmq[k - 1][i + (1 << k - 1)];
                    rmq[k][i] = max(x, y); // change here for other type of queries, ie : max, gcd, and, or etc
                }
            }
        }

        public long query(int i, int j) {
            int k = logTable[j - i];
            long x = rmq[k][i];
            long y = rmq[k][j - (1 << k) + 1];
            return max(x, y); // change here for other type of queries, ie : max, gcd, and, or etc
        }
    }

    static void debug(Object... obj) {
        System.err.println(Arrays.deepToString(obj));
    }

    static class FastReader {
        InputStream is;
        private byte[] inbuf = new byte[1024];
        private int lenbuf = 0, ptrbuf = 0;

        public FastReader(InputStream is) {
            this.is = is;
        }

        public int readByte() {
            if (lenbuf == -1) throw new InputMismatchException();
            if (ptrbuf >= lenbuf) {
                ptrbuf = 0;
                try {
                    lenbuf = is.read(inbuf);
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
                if (lenbuf <= 0) return -1;
            }
            return inbuf[ptrbuf++];
        }

        public boolean isSpaceChar(int c) {
            return !(c >= 33 && c <= 126);
        }

        private boolean isEndOfLine(int c) {
            return c == '\n' || c == '\r' || c == -1;
        }

        public int skip() {
            int b;
            while ((b = readByte()) != -1 && isSpaceChar(b)) ;
            return b;
        }

        public String next() {
            int b = skip();
            StringBuilder sb = new StringBuilder();
            while (!(isSpaceChar(b))) {
                sb.appendCodePoint(b);
                b = readByte();
            }
            return sb.toString();
        }


        public String nextLine() {
            int c = skip();
            StringBuilder sb = new StringBuilder();
            while (!isEndOfLine(c)) {
                sb.appendCodePoint(c);
                c = readByte();
            }
            return sb.toString();
        }

        public int nextInt() {
            int num = 0, b;
            boolean minus = false;
            while ((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-')) ;
            if (b == '-') {
                minus = true;
                b = readByte();
            }
            while (true) {
                if (b >= '0' && b <= '9') {
                    num = (num << 3) + (num << 1) + (b - '0');
                } else {
                    return minus ? -num : num;
                }
                b = readByte();
            }
        }

        public long nextLong() {
            long num = 0;
            int b;
            boolean minus = false;
            while ((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-')) ;
            if (b == '-') {
                minus = true;
                b = readByte();
            }

            while (true) {
                if (b >= '0' && b <= '9') {
                    num = (num << 3) + (num << 1) + (b - '0');
                } else {
                    return minus ? -num : num;
                }
                b = readByte();
            }
        }

        public double nextDouble() {
            return Double.parseDouble(next());
        }

        public char[] next(int n) {
            char[] buf = new char[n];
            int b = skip(), p = 0;
            while (p < n && !(isSpaceChar(b))) {
                buf[p++] = (char) b;
                b = readByte();
            }
            return n == p ? buf : Arrays.copyOf(buf, p);
        }

        public char readChar() {
            return (char) skip();
        }
    }
}