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
 *
 * @author Washoum
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        inputClass in = new inputClass(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        CXorSum4 solver = new CXorSum4();
        solver.solve(1, in, out);
        out.close();
    }

    static class CXorSum4 {
        public void solve(int testNumber, inputClass sc, PrintWriter out) {
            int n = sc.nextInt();
            int[][] tab = new int[n][60];
            for (int i = 0; i < n; i++) {
                long x = sc.nextLong();
                String s = Long.toBinaryString(x);
                for (int j = 0; j < s.length(); j++) {
                    tab[i][59 - s.length() + 1 + j] = s.charAt(j) - '0';
                }
            }
            int[][] sum1 = new int[n][60];
            for (int i = 0; i < 60; i++) {
                sum1[n - 1][i] = tab[n - 1][i];
            }
            for (int i = n - 2; i >= 0; i--) {
                for (int j = 0; j < 60; j++) {
                    sum1[i][j] = sum1[i + 1][j] + tab[i][j];
                }
            }
            int[][] sum0 = new int[n][60];
            for (int i = 0; i < 60; i++) {
                sum0[n - 1][i] = 1 - tab[n - 1][i];
            }
            for (int i = n - 2; i >= 0; i--) {
                for (int j = 0; j < 60; j++) {
                    sum0[i][j] = sum0[i + 1][j] + 1 - tab[i][j];
                }
            }
            int mod = (int) 1e9 + 7;
            long[] pow = new long[60];
            pow[0] = 1;
            for (int i = 1; i < 60; i++) {
                pow[i] = (pow[i - 1] * 2) % mod;

            }
            long ans = 0;
            for (int i = 0; i < n - 1; i++) {
                for (int j = 0; j < 60; j++) {
                    if (tab[i][j] == 1) {
                        ans += (sum0[i + 1][j] * pow[59 - j]) % mod;
                        ans %= mod;
                    } else {
                        ans += (sum1[i + 1][j] * pow[59 - j]);
                        ans %= mod;
                    }
                }
            }
            out.println(ans);
        }

    }

    static class inputClass {
        BufferedReader br;
        StringTokenizer st;

        public inputClass(InputStream in) {

            br = new BufferedReader(new InputStreamReader(in));
        }

        public String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
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

    }
}

