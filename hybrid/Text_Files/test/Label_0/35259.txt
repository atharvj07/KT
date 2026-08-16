import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author Mohammed Basioni
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        Scanner in = new Scanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        CTanyaAndColoredCandies solver = new CTanyaAndColoredCandies();
        solver.solve(1, in, out);
        out.close();
    }

    static class CTanyaAndColoredCandies {
        static int n;
        static int s;
        static int k;
        static int[] candies;
        static char[] colors;
        static int[][] memo = new int[51][20001];

        static int dp(int previous, int sum) {
            if (sum >= k)
                return 0;

            if (memo[previous][sum] != -1)
                return memo[previous][sum];
            int take = 10000;
            for (int i = 0; i < n; i++)
                if (colors[i] != colors[previous] && candies[i] > candies[previous])
                    take = Math.min(take, Math.abs(previous - i) + dp(i, sum + candies[i]));


            return memo[previous][sum] = take;
        }

        public void solve(int testNumber, Scanner sc, PrintWriter pw) {
            n = sc.nextInt();
            s = sc.nextInt();
            k = sc.nextInt();
            candies = new int[n];
            colors = new char[n];
            for (int i = 0; i < n; i++)
                candies[i] = sc.nextInt();
            String string = sc.nextLine();
            for (int i = 0; i < n; i++)
                colors[i] = string.charAt(i);
            for (int[] arr : memo)
                Arrays.fill(arr, -1);
            int min = dp(s - 1, candies[s - 1]);
            for (int i = 0; i < n; i++)
                min = Math.min(min, Math.abs(i - (s - 1)) + dp(i, candies[i]));
            pw.println(min >= 10000 ? -1 : min);
        }

    }

    static class Scanner {
        StringTokenizer st;
        BufferedReader br;

        public Scanner(FileReader r) {
            br = new BufferedReader(r);
        }

        public Scanner(InputStream s) {
            br = new BufferedReader(new InputStreamReader(s));
        }

        public String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return st.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public String nextLine() {
            try {
                return br.readLine();
            } catch (Exception e) {
                throw new RuntimeException(e);
            }
        }

    }
}

