import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.PriorityQueue;
import java.util.InputMismatchException;
import java.io.IOException;
import java.util.Collections;
import java.util.ArrayList;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author caoash
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        FastScanner in = new FastScanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        CLaboratoryWork solver = new CLaboratoryWork();
        solver.solve(1, in, out);
        out.close();
    }

    static class CLaboratoryWork {
        public void solve(int testNumber, FastScanner br, PrintWriter pw) {
            int n = br.nextInt();
            int[] a = br.nextSortedIntArray(n);
            int max = a[n - 1];
            int min = a[0];
            if (min + 1 == max) {
                pw.println(a.length);
                for (int i = 0; i < n; i++) {
                    pw.print(a[i] + " ");
                }
                pw.close();
            } else if (max == min) {
                pw.println(a.length);
                for (int i = 0; i < n; i++) {
                    pw.print(a[i] + " ");
                }
                pw.close();
            } else {
                ArrayList<Integer> ans = new ArrayList<>();
                int maxCnt = 0;
                int minCnt = 0;
                int midCnt = 0;
                for (int i = 0; i < n; i++) {
                    if (a[i] == max) {
                        maxCnt++;
                    } else if (a[i] == min) {
                        minCnt++;
                    } else {
                        midCnt++;
                    }
                }
                int om = maxCnt;
                int omm = minCnt;
                for (int i = 0; i < midCnt; i++) {
                    ans.add(min + 1);
                }
//            pw.println(maxCnt + " " + minCnt + " " + min + " " + max + " " + midCnt);
                for (int i = 0; i < Math.min(om, omm); i++) {
                    ans.add(min + 1);
                    ans.add(min + 1);
                    --maxCnt;
                    --minCnt;
                }
//            pw.println(maxCnt + " " + minCnt + " " + min + " " + max + " " + midCnt);
                while (maxCnt > 0) {
                    --maxCnt;
                    ans.add(max);
                }
                while (minCnt > 0) {
                    --minCnt;
                    ans.add(min);
                }
                int same = 0;
                int c1 = 0;
                int c2 = 0;
                int c3 = 0;
                Collections.sort(ans);
                for (int i = 0; i < ans.size(); i++) {
                    if (ans.get(i) == min) {
                        c1++;
                    } else if (ans.get(i) == max) {
                        c2++;
                    } else {
                        c3++;
                    }
                }
                int midCntt = midCnt;
                same = Math.min(c1, omm) + Math.min(c2, om) + Math.min(c3, midCntt);
                ArrayList<Integer> ans2 = new ArrayList<>();
                int nmc = midCnt;
                for (int i = 0; i < nmc / 2; i++) {
                    ans2.add(min);
                    ans2.add(max);
                    --midCnt;
                    --midCnt;
                }
                for (int i = 0; i < midCnt; i++) {
                    ans2.add(min + 1);
                }
//            System.out.println(ans2.size());
                for (int i = 0; i < omm; i++) {
                    ans2.add(min);
                }
                for (int i = 0; i < om; i++) {
                    ans2.add(max);
                }
//            System.out.println(ans2.size());
                int same2 = 0;
                Collections.sort(ans2);
                c1 = 0;
                c2 = 0;
                c3 = 0;
                for (int i = 0; i < ans.size(); i++) {
                    if (ans2.get(i) == min) {
                        c1++;
                    } else if (ans2.get(i) == max) {
                        c2++;
                    } else {
                        c3++;
                    }
                }
                same2 = Math.min(c1, omm) + Math.min(c2, om) + Math.min(c3, midCntt);
                if (same <= same2) {
                    pw.println(same);
                    for (int val : ans) {
                        pw.print(val + " ");
                    }
                    pw.close();
                } else {
                    pw.println(same2);
                    for (int val : ans2) {
                        pw.print(val + " ");
                    }
                    pw.close();
                }
            }
        }

    }

    static class FastScanner {
        private InputStream stream;
        private byte[] buf = new byte[1024];
        private int curChar;
        private int numChars;
        private FastScanner.SpaceCharFilter filter;

        public FastScanner(InputStream stream) {
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

        public boolean isSpaceChar(int c) {
            if (filter != null) {
                return filter.isSpaceChar(c);
            }
            return isWhitespace(c);
        }

        public static boolean isWhitespace(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        public int[] nextIntArray(int n) {
            int[] array = new int[n];
            for (int i = 0; i < n; ++i) array[i] = nextInt();
            return array;
        }

        public int[] nextSortedIntArray(int n) {
            int array[] = nextIntArray(n);
            PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
            for (int i = 0; i < n; i++) {
                pq.add(array[i]);
            }
            int[] out = new int[n];
            for (int i = 0; i < n; i++) {
                out[i] = pq.poll();
            }
            return out;
        }

        public interface SpaceCharFilter {
            public boolean isSpaceChar(int ch);

        }

    }
}

