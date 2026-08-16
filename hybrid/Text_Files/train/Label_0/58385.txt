import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class Solve7 {

    public static void main(String[] args) throws IOException {
        PrintWriter pw = new PrintWriter(System.out);
        new Solve7().solve(pw);
        pw.flush();
        pw.close();
    }

    public void solve(PrintWriter pw) throws IOException {
        FastReader sc = new FastReader();
        int n = sc.nextInt();
        int[] a = new int[n];
        int[][] freq = new int[11][10];
        int[] num = new int[11];
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            a[i] = x;
            int c = 0;
            int len = 0;
            while (x != 0) {
                ++freq[c++][x % 10];
                x /= 10;
                ++len;
            }
            ++num[len];
        }
        final int MOD = 998244353;
        long ans = 0;
        for (int i = 0; i < n; i++) {
            int x = a[i];
            int c = 0;
            int digits = 0;
            for (int k = 0; k < 10; k++) {
                int count = 0;
                for (int j = 0; j < 10; j++) {
                    ans += (j * powerWithMod(10, c, MOD)) * freq[digits][j];
                    count += freq[digits][j];
                    ans %= MOD;
                }
                ++digits;
                if (count == 0) {
                    break;
                }
                ++c;
                if (x != 0) {
                    ans += 1l * (x % 10) * powerWithMod(10, c, MOD) * count;
                    ans %= MOD;
                    ++c;
                    x /= 10;
                    ans += 1l * x * powerWithMod(10, c, MOD) * num[digits];
                    ans %= MOD;
                }
            }
        }
        pw.println(ans);
    }

    public long powerWithMod(long a, long n, long mod) {
        if (n == 0) {
            return 1;
        }
        if (n == 1) {
            return a % mod;
        }
        long y = powerWithMod(a, n / 2, mod);
        if ((n & 1) == 1) {
            return (((y * y) % mod) * a) % mod;
        } else {
            return (y * y) % mod;
        }
    }

    static class FastReader {

        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        public FastReader(String s) {
            try {
                br = new BufferedReader(new FileReader(s));
            } catch (FileNotFoundException e) {
            }
        }

        public String next() {
            if (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (Exception e) {
                }
            }
            return st.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public long nextLong() {
            return Long.parseLong(next());
        }

        public double nextDouble() {
            return Double.parseDouble(next());
        }

        public String nextLine() {
            try {
                return br.readLine();
            } catch (Exception e) {
            }
            return null;
        }

        public boolean hasNext() throws IOException {
            if (st != null && st.hasMoreTokens()) {
                return true;
            }
            String s = br.readLine();
            if (s == null || s.isEmpty()) {
                return false;
            }
            st = new StringTokenizer(s);
            return true;
        }
    }
}
