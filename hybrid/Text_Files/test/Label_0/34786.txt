import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.io.FilterInputStream;
import java.io.BufferedInputStream;
import java.util.ArrayList;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author Jenish
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        ScanReader in = new ScanReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        GMinimumPossibleLCM solver = new GMinimumPossibleLCM();
        solver.solve(1, in, out);
        out.close();
    }

    static class GMinimumPossibleLCM {
        public void solve(int testNumber, ScanReader in, PrintWriter out) {
            int n = in.scanInt();
            int arrayList1[][] = new int[2][10000000 + 5];

            Arrays.fill(arrayList1[0], -1);
            Arrays.fill(arrayList1[1], -1);
            int max = -1;
            for (int i = 0; i < n; i++) {
                int x = in.scanInt();
                if (arrayList1[0][x] == -1) arrayList1[0][x] = (i + 1);
                else arrayList1[1][x] = (i + 1);
                max = Math.max(max, x);
            }


            long ans = Long.MAX_VALUE;
            int iii = -1;
            int jjj = -1;

            for (int i = 1; i <= max + 1; i++) {
                ArrayList<pair> aa = new ArrayList<>();
                for (int j = i; j <= max + 1; j += i) {
                    if (arrayList1[0][j] != -1 && arrayList1[1][j] != -1) {
                        aa.add(new pair(j, arrayList1[0][j]));
                        aa.add(new pair(j, arrayList1[1][j]));
                    } else if (arrayList1[0][j] != -1) {
                        aa.add(new pair(j, arrayList1[0][j]));
                    }

                    if (aa.size() >= 2) {
                        break;
                    }
                }
                if (aa.size() >= 2 && ((aa.get(0).val * aa.get(1).val) / i) < ans) {
                    ans = (aa.get(0).val * aa.get(1).val) / i;
                    iii = aa.get(0).index;
                    jjj = aa.get(1).index;
                }
            }


            if (iii > jjj) {
                int temp = jjj;
                jjj = iii;
                iii = temp;
            }
            out.println(iii + " " + jjj);
        }

        class pair {
            long val;
            int index;

            public pair(long val, int index) {
                this.val = val;
                this.index = index;
            }

        }

    }

    static class ScanReader {
        private byte[] buf = new byte[4 * 1024];
        private int INDEX;
        private BufferedInputStream in;
        private int TOTAL;

        public ScanReader(InputStream inputStream) {
            in = new BufferedInputStream(inputStream);
        }

        private int scan() {
            if (INDEX >= TOTAL) {
                INDEX = 0;
                try {
                    TOTAL = in.read(buf);
                } catch (Exception e) {
                    e.printStackTrace();
                }
                if (TOTAL <= 0) return -1;
            }
            return buf[INDEX++];
        }

        public int scanInt() {
            int I = 0;
            int n = scan();
            while (isWhiteSpace(n)) n = scan();
            int neg = 1;
            if (n == '-') {
                neg = -1;
                n = scan();
            }
            while (!isWhiteSpace(n)) {
                if (n >= '0' && n <= '9') {
                    I *= 10;
                    I += n - '0';
                    n = scan();
                }
            }
            return neg * I;
        }

        private boolean isWhiteSpace(int n) {
            if (n == ' ' || n == '\n' || n == '\r' || n == '\t' || n == -1) return true;
            else return false;
        }

    }
}

