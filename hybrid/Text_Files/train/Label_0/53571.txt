
import java.io.*;
import java.util.StringTokenizer;

/**
 * Created by Darren on 14-10-11.
 */
public class D {
    Reader in = new Reader(System.in);
    PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        new D().run();
    }

    int n, m;
    int[] first, second;
    int[] dp;
    int[] prev;

    void run() throws IOException {
        n = in.nextInt();
        first = new int[n+1];
        for (int i = 1; i <= n; i++)
            first[i] = in.nextInt();
        m = in.nextInt();
        second = new int[m+1];
        for (int i = 1; i <= m; i++)
            second[i] = in.nextInt();

        dp = new int[m+1];
        prev = new int[m+1];

        for (int i = 1; i <= n; i++) {
            int len = 0, last = 0;
            for (int j = 1; j <= m; j++) {
                if (second[j] == first[i] && len + 1 > dp[j]) {
                    dp[j] = len + 1;
                    prev[j] = last;
                } else if (second[j] < first[i] && len < dp[j]) {
                    len = dp[j];
                    last = j;
                }
            }
        }

        int max = 0, maxIndex = 0;
        for (int i = 1; i <= m; i++) {
            if (max < dp[i]) {
                max = dp[i];
                maxIndex = i;
            }
        }

        out.println(max);
        if (max > 0) {
            StringBuilder builder = new StringBuilder();
            for (int i = maxIndex; i > 0; i = prev[i])
                builder.insert(0, ' ').insert(0, second[i]);
            out.println(builder.toString());
        }
        out.flush();
    }

    static class Reader {
        BufferedReader reader;
        StringTokenizer tokenizer;

        public Reader(InputStream input) {
            reader = new BufferedReader(new InputStreamReader(input));
            tokenizer = new StringTokenizer("");
        }

        /** get next word */
        String nextToken() throws IOException {
            while ( ! tokenizer.hasMoreTokens() ) {
                //TODO add check for eof if necessary
                tokenizer = new StringTokenizer( reader.readLine() );
            }
            return tokenizer.nextToken();
        }

        String readLine() throws IOException {
            return reader.readLine();
        }

        int nextInt() throws IOException {
            return Integer.parseInt( nextToken() );
        }

        long nextLong() throws IOException {
            return Long.parseLong( nextToken() );
        }

        double nextDouble() throws IOException {
            return Double.parseDouble( nextToken() );
        }
    }
}
