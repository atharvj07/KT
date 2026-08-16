import java.io.*;

import java.util.StringTokenizer;

/**
 * Created by gamezovladislav on 10.04.2017.
 */
public class TaskB {

    static boolean[] used;

    public static void main(String[] args) throws IOException {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        solve(in, out);
        out.close();
    }

    private static void solve(InputReader in, PrintWriter out) {
        int n = in.nextInt();
        int m = in.nextInt();
        int k = in.nextInt();
        used = new boolean[n+10];
        for (int i = 0; i <= n+2; i++) {
            used[i] = false;
        }
        for (int i = 0; i < m; i++) {
            int x = in.nextInt();
            used[x] = true;
        }
        int pos = 1;
        if (used[1]) {
            out.print(1);
            return;
        }
        for (int i = 0; i < k; i++) {
            int q = in.nextInt();
            int w = in.nextInt();
            if (q == pos) {
                pos = w;
            } else {
                if (w == pos) {
                    pos = q;
                }
            }
            if (used[pos]) {
                out.print(pos);
                return;
            }
        }
        out.print(pos);
    }

    static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }

        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public long nextLong() {
            return Long.parseLong(next());
        }

    }
}
