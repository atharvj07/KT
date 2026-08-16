import java.util.*;
import java.io.*;
public class E584 {
    public static void main(String[] args) {
        MyScanner sc = new MyScanner();
        PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));
        int t = sc.nextInt();
        while (t > 0) {
            int n = sc.nextInt(); int m = sc.nextInt();
            int [][] a = new int[m][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    a[j][i] = sc.nextInt();
                }
            }
            int [][] dp = new int[m + 1][(1 << n)];
            for (int i = 1; i <= m; i++) {
                for (int j = 0; j < (1 << n); j++) {
                    dp[i][j] = Math.max(dp[i][j], dp[i - 1][j]);
                    int [] b = a[i - 1];
                    for (int start = 0; start < n; start++) {
                        int [] c = new int[n];
                        for (int p = 0; p < n; p++) c[p] = b[(start + p) % n];
                        for (int k = 0; k < (1 << n); k++) {
                            if ((k | j) == j) {
                                int sum = 0;
                                for (int p = 0; p < n; p++) {
                                    if (((k >> p) & 1) == 0 && ((j >> p) & 1) == 1) sum += c[p];
                                }
                                dp[i][j] = Math.max(dp[i][j], dp[i - 1][k] + sum);
                            }
                        }
                    }
                }
            }
            out.println(dp[m][(1 << n) - 1]);
            t--;
        }

        out.close();
    }



    //-----------MyScanner class for faster input----------
    public static class MyScanner {
        BufferedReader br;
        StringTokenizer st;

        public MyScanner() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
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

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }


    }

}