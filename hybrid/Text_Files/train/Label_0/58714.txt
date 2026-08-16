import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
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
        MyBufferedReader in = new MyBufferedReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskE solver = new TaskE();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskE {
        int MOD = 998244353;

        public void solve(int testNumber, MyBufferedReader in, PrintWriter out) {
            int n = in.getAnInt();
            long[] a = in.getALineOfLong(n);

            long[] pow2 = new long[n];
            long pow = 1;
            for (int i = 0; i < n; i++) {
                pow2[i] = pow;
                pow = (2 * pow) % MOD;
            }

            long sum = 0;
            for (int i = 0; i < n - 1; i++) {
                long ai = a[i];
                long b = (ai * pow2[n - i - 1]) % MOD;
                long c = (ai * (n - i - 1)) % MOD;
                c *= pow2[n - i - 2];
                c %= MOD;
                sum += (b + c) % MOD;
                sum %= MOD;
            }

            sum += a[n - 1];
            sum %= MOD;

            out.println(sum);
        }

    }

    static class MyBufferedReader {
        BufferedReader in;

        public MyBufferedReader(InputStream s) {
            this.in = new BufferedReader(new InputStreamReader(s));
        }

        public MyBufferedReader(BufferedReader in) {
            this.in = in;
        }

        public int getAnInt() {
            int res = -1;
            try {
                res = Integer.parseInt(new StringTokenizer(in.readLine()).nextToken());
            } catch (IOException e) {
                e.printStackTrace();
            }
            return res;
        }

        public long[] getALineOfLong(int numExpected) {
            if (numExpected == 0) {
                return new long[0];
            }

            long[] res = new long[numExpected];
            StringTokenizer st = null;
            try {
                st = new StringTokenizer(in.readLine());
            } catch (IOException e) {
                e.printStackTrace();
            }
            for (int i = 0; i < numExpected; i++)
                res[i] = Long.parseLong(st.nextToken());
            return res;
        }

    }
}

