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
 * @author HossamDoma
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskD solver = new TaskD();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskD {
        public void solve(int testNumber, InputReader in, PrintWriter out) {

            int h = in.nextInt();
            int w = in.nextInt();

            int n = in.nextInt();
            int[] a = new int[n];

            for (int i = 0; i < n; ++i) {
                a[i] = in.nextInt();
            }

            int[][] ans = new int[h][w];

            int i = 0;
            int j = 0;

            boolean[][] vis = new boolean[h][w];

            int cur = 0;
            int tot = 0;
            int tt = h * w;

            int[] dx = {0, 1, 0, -1};
            int[] dy = {1, 0, -1, 0};

            for (int idx = 0; tot < tt; idx = (idx + 1) % 4, i += dx[idx], j += dy[idx]) {

                while (i >= 0 && j >= 0 && i < h && j < w && !vis[i][j]) {
                    vis[i][j] = true;
                    ans[i][j] = cur + 1;
                    a[cur]--;
                    tot++;
                    if (a[cur] == 0) cur++;
                    i += dx[idx];
                    j += dy[idx];
                }

                //roll_back
                i -= dx[idx];
                j -= dy[idx];

            }


            for (int ii = 0; ii < h; ++ii)
                for (int jj = 0; jj < w; ++jj)
                    out.print(ans[ii][jj] + (jj == w - 1 ? "\n" : " "));

        }

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

    }
}

