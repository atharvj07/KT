import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class Main {
    private FastScanner in;
    private PrintWriter out;

    final int mod = 998244353;

    int add(int x, int y) {
        x += y;
        if (x >= mod) {
            x -= mod;
        }
        return x;
    }

    int mul(int x, int y) {
        return (int) (x * 1L * y % mod);
    }

    int[] fact;
    int[] factInv;


    int solve(int leftCnt, int rightCnt, int middle) {
        if (middle == 0) {
            if (leftCnt == 0 && rightCnt == 0) {
                return 1;
            }
            return 0;
        }
        return c(leftCnt + rightCnt + middle - 1, middle - 1);
    }

    int countOnes(String s) {
        int res = 0;
        for (char c : s.toCharArray()) {
            if (c == '1') {
                res++;
            }
        }
        return res;
    }

    int solveOneWay(String A, String B, String C, String D) {
        boolean atleastOne = false;
        int res = 0;
        int cntC = countOnes(C), cntD = countOnes(D);

        int[] dp = new int[A.length() + 1];
        int curA = 0, curB = 0;
        for (int i = A.length() - 1; i >= 0; i--) {
            if (A.charAt(i) == '0' && B.charAt(i) == '0') {
                dp[i] = dp[i + 1];
                continue;
            }
            atleastOne = true;
            dp[i] = dp[i + 1];
            int mul = 1;
            if (A.charAt(i) == '1' && B.charAt(i) == '1') {
                mul = 2;
            }
            dp[i] = add(dp[i], solve(curA, curB, cntD));
            dp[i] = mul(dp[i], mul);
            curA += (A.charAt(i) == '1' ? 1 : 0);
            curB += (B.charAt(i) == '1' ? 1 : 0);
        }

        curA = 0;
        curB  = 0;
        for (int i = 0; i < A.length(); i++) {
            if (A.charAt(i) == '1' || B.charAt(i) == '1') {
                int f = solve(curA, curB, cntC);
                res = add(res, mul(dp[i], f));


                if (A.charAt(i) == '1') {
                    curA++;
                }
                if (B.charAt(i) == '1') {
                    curB++;
                }
            }
        }
        return atleastOne ? res : -1;
    }

    int solve(String A, String B, String C, String D) {
        int r1 = solveOneWay(A, B, C, D);
        int r2 = solveOneWay(C, D, A, B);
        if (r1 == -1 && r2 == -1) {
            return 1;
        }
        return add(Math.max(r1, 0), Math.max(r2, 0));
    }

    final int MAX = (int) 3e5 + 10;

    int[] fact(int n) {
        int[] res = new int[n];
        res[0] = 1;
        for (int i = 1; i < n; i++) {
            res[i] = mul(res[i - 1], i);
        }
        return res;
    }

    int[] factInv(int[] fact) {
        int n = fact.length;
        int[] res = new int[n];
        res[n - 1] = BigInteger.valueOf(fact[n - 1]).modInverse(BigInteger.valueOf(mod)).intValue();
        for (int i = n - 2; i >= 0; i--) {
            res[i] = mul(res[i + 1], i + 1);
        }
        return res;
    }

    int c(int n, int k) {
        if (k < 0 || k > n) {
            return 0;
        }
        return mul(fact[n], mul(factInv[k], factInv[n - k]));
    }

    private void solve() {
        fact = fact(MAX);
        factInv = factInv(fact);
        int n = in.nextInt();
        int m = in.nextInt();
        String A = in.next();  // len n
        String B = in.next();
        String C = in.next();
        String D = in.next();
        out.println(solve(A, B, C, D));
    }

    private void run() {
        try {
            in = new FastScanner(new File("CodeFestival_QualA_E.in"));
            out = new PrintWriter(new File("CodeFestival_QualA_E.out"));

            solve();

            out.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    private void runIO() {
        in = new FastScanner(System.in);
        out = new PrintWriter(System.out);

        solve();

        out.close();
    }

    private class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        FastScanner(File f) {
            try {
                br = new BufferedReader(new FileReader(f));
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
        }

        FastScanner(InputStream f) {
            br = new BufferedReader(new InputStreamReader(f));
        }

        String next() {
            while (st == null || !st.hasMoreTokens()) {
                String s = null;
                try {
                    s = br.readLine();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                if (s == null)
                    return null;
                st = new StringTokenizer(s);
            }
            return st.nextToken();
        }

        boolean hasMoreTokens() {
            while (st == null || !st.hasMoreTokens()) {
                String s = null;
                try {
                    s = br.readLine();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                if (s == null)
                    return false;
                st = new StringTokenizer(s);
            }
            return true;
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

    public static void main(String[] args) {
        new Main().runIO();
    }
}