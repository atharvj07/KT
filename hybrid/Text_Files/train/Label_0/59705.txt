import java.io.*;
import java.math.BigInteger;
import java.util.*;
import java.util.stream.IntStream;

public class Solution {


    static MyScanner sc;
    private static PrintWriter out;

    public static void main(String[] s) throws Exception {
        StringBuilder stringBuilder = new StringBuilder();
//
//        stringBuilder.append("3\n" +
//                "3 2 1\n" +
//                "1 2 3\n" +
//                "1 1\n" +
//                "1 2");

        if (stringBuilder.length() == 0) {
            sc = new MyScanner(System.in);
        } else {
            sc = new MyScanner(new BufferedReader(new StringReader(stringBuilder.toString())));
        }

        out = new PrintWriter(new OutputStreamWriter(System.out));
        long t = System.currentTimeMillis();
        solve();
        out.flush();

    }


    private static void solve() {
        int n = sc.nextInt();
        long[] s = sc.nl(n);
        long[] d = sc.nl(n);
        int[][] tr = new int[n - 1][2];

        for (int l = 0; l < n - 1; l++) {
            tr[l][0] = sc.nextInt() - 1;
            tr[l][1] = sc.nextInt();
        }
        BigInteger min = BigInteger.valueOf(Long.MIN_VALUE);

        for (int r = n - 1; r > 0; r--) {
            long diff = s[r] - d[r];
            if (diff > 0) {
                s[tr[r - 1][0]] += diff;
            } else {
                BigInteger l2 = BigInteger.valueOf(tr[r - 1][1]);
                l2 = l2.multiply(BigInteger.valueOf(diff));
                l2 = l2.add(BigInteger.valueOf(s[tr[r - 1][0]]));
                if (min.compareTo(l2) > 0) {
                    out.println("NO");
                    return;
                }
                s[tr[r - 1][0]] = l2.longValue();

            }
        }
        if (s[0] >= d[0]) {
            out.println("YES");
        } else {
            out.println("NO");
        }


    }


    private static void solveT() {
        int t = sc.nextInt();
        while (t-- > 0) {
            solve();
        }
    }

    private static long gcd(long l, long l1) {
        if (l > l1) return gcd(l1, l);
        if (l == 0) return l1;
        return gcd(l1 % l, l);
    }

    private static long pow(long a, long b, long m) {
        if (b == 0) return 1;
        if (b == 1) return a;
        long pp = pow(a, b / 2, m);
        pp *= pp;
        pp %= m;
        return (pp * (b % 2 == 0 ? 1 : a)) % m;
    }


    static class MyScanner {
        BufferedReader br;
        StringTokenizer st;

        MyScanner(BufferedReader br) {
            this.br = br;
        }

        public MyScanner(InputStream in) {
            this(new BufferedReader(new InputStreamReader(in)));
        }

        void findToken() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
        }

        String next() {
            findToken();
            return st.nextToken();
        }

        int[] na(int n) {
            int[] k = new int[n];
            for (int i = 0; i < n; i++) {
                k[i] = sc.nextInt();
            }
            return k;
        }

        long[] nl(int n) {
            long[] k = new long[n];
            for (int i = 0; i < n; i++) {
                k[i] = sc.nextLong();
            }
            return k;
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }
    }


}