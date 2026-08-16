import java.util.*;
import java.io.*;

public class F {
    final static long M = 998244353;

    public static void main(String[] args) throws IOException {
        FastScanner input = new FastScanner(System.in);
        PrintWriter output = new PrintWriter(System.out);

        String brackets = input.next();
        int n = brackets.length();

        long[][] c = new long[n + 1][n + 1];
        c[0][0] = 1;
        for (int i = 1; i <= n; i++) {
            c[i][0] = 1;
            for (int j = 1; j <= n; j++)
                c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % M;
        }

        long count = 0;
        char[] chars = brackets.toCharArray();
        for (int i = 0; i < n; i++) {
            int leftBracket = 0, rightBracket = 0, leftMark = 0, rightMark = 0;
            for (int j = 0; j <= i; j++) {
                if (chars[j] == '(')
                    leftBracket++;
                else if (chars[j] == '?')
                    leftMark++;
            }
            for (int j = i + 1; j < n; j++) {
                if (chars[j] == ')')
                    rightBracket++;
                else if (chars[j] == '?')
                    rightMark++;
            }
            int from = Math.max(leftBracket, rightBracket);
            int to = Math.min(i + 1, n - i - 1);

            for (int j = from; j <= to; j++) {
                if (j - leftBracket <= leftMark && j - rightBracket <= rightMark) {
                    count = (count
                            + (((long) j * c[leftMark][j - leftBracket]) % M * c[rightMark][j - rightBracket]) % M) % M;
                }
            }
        }

        output.println(count);
        output.close();
    }

    static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        FastScanner(InputStream s) {
            br = new BufferedReader(new InputStreamReader(s));
        }

        FastScanner(FileReader s) {
            br = new BufferedReader(s);
        }

        String next() throws IOException {
            while (st == null || !st.hasMoreTokens())
                st = new StringTokenizer(br.readLine());
            return st.nextToken();
        }

        String nextLine() throws IOException {
            return br.readLine();
        }

        double nextDouble() throws IOException {
            return Double.parseDouble(next());
        }

        int nextInt() throws IOException {
            return Integer.parseInt(next());
        }

        long nextLong() throws IOException {
            return Long.parseLong(next());
        }
    }
}