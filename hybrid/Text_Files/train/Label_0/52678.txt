import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.OutputStream;
import java.util.Arrays;
import java.util.Collection;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.io.BufferedOutputStream;
import java.util.stream.Stream;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        Kattio in = new Kattio(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskE2 solver = new TaskE2();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskE2 {
        public void solve(int testNumber, Kattio in, PrintWriter out) {
            int n = in.nextInt();
            int m = in.nextInt();

            char[][] arr = new char[n + 1][m + 1];
            int[][][] pre = new int[n + 2][m + 2][2];
            int[][][] clo = new int[n + 2][m + 2][4];

            for (int i = 1; i <= n; ++i) {
                char[] tmp = in.next().toCharArray();
                Arrays.fill(clo[i][0], -1);
                Arrays.fill(clo[i][m + 1], -1);
                for (int j = 1; j <= m; ++j) {
                    arr[i][j] = tmp[j - 1];
                    Arrays.fill(clo[i][j], -1);
                }
            }

            for (int j = 0; j <= m + 1; ++j) {
                Arrays.fill(clo[0][j], -1);
                Arrays.fill(clo[n + 1][j], -1);
            }

            // Mark the index of the furthest * from the left and top
            for (int i = 1; i <= n; ++i) {
                for (int j = 1; j <= m; ++j) {
                    if (arr[i][j] == '*') {

                        clo[i][j][0] = j;
                        clo[i][j][2] = i;

                        if (clo[i][j - 1][0] != -1) {
                            clo[i][j][0] = clo[i][j - 1][0];
                        }

                        if (clo[i - 1][j][2] != -1) {
                            clo[i][j][2] = clo[i - 1][j][2];
                        }
                    }
                }
            }


            // Mark the index of the furthest * from the right and bottom
            for (int i = n; i > 0; --i) {
                for (int j = m; j > 0; --j) {
                    if (arr[i][j] == '*') {
                        clo[i][j][1] = j;
                        clo[i][j][3] = i;

                        if (clo[i][j + 1][1] != -1) {
                            clo[i][j][1] = clo[i][j + 1][1];
                        }

                        if (clo[i + 1][j][3] != -1) {
                            clo[i][j][3] = clo[i + 1][j][3];
                        }
                    }
                }
            }

            ArrayList<Star> ans = new ArrayList<>();
            for (int i = 1; i <= n; ++i) {
                for (int j = 1; j <= m; ++j) {
                    if (arr[i][j] == '*') {
                        int diff1 = Math.min(j - clo[i][j][0], clo[i][j][1] - j);
                        int diff2 = Math.min(i - clo[i][j][2], clo[i][j][3] - i);
                        int diff = Math.min(diff1, diff2);

                        if (diff == 0)
                            continue;

                        pre[i][j - diff][0] += 1;
                        pre[i][j + diff + 1][0] -= 1;

                        pre[i - diff][j][1] += 1;
                        pre[i + diff + 1][j][1] -= 1;

                        ans.add(new Star(i, j, diff));
                    }
                }
            }


            for (int i = 1; i <= n; ++i) {
                for (int j = 1; j <= m; ++j) {
                    pre[i][j][0] += pre[i][j - 1][0];
                    pre[i][j][1] += pre[i - 1][j][1];

                    if (pre[i][j][0] + pre[i][j][1] == 0 && arr[i][j] == '*') {
                        out.println(-1);
                        return;
                    }
                }
            }

            out.println(ans.size());
            ans.stream().forEach(out::println);
        }

        public class Star {
            int x;
            int y;
            int l;

            public Star(int x, int y, int l) {
                this.x = x;
                this.y = y;
                this.l = l;
            }


            public String toString() {
                return x + " " + y + " " + l;
            }

        }

    }

    static class Kattio extends PrintWriter {
        private BufferedReader r;
        private String line;
        private StringTokenizer st;
        private String token;

        public Kattio(InputStream i) {
            super(new BufferedOutputStream(System.out));
            r = new BufferedReader(new InputStreamReader(i));
        }

        public Kattio(InputStream i, OutputStream o) {
            super(new BufferedOutputStream(o));
            r = new BufferedReader(new InputStreamReader(i));
        }

        public int nextInt() {
            return Integer.parseInt(nextToken());
        }

        public String next() {
            return nextToken();
        }

        private String peekToken() {
            if (token == null)
                try {
                    while (st == null || !st.hasMoreTokens()) {
                        line = r.readLine();
                        if (line == null) return null;
                        st = new StringTokenizer(line);
                    }
                    token = st.nextToken();
                } catch (IOException e) {
                }
            return token;
        }

        private String nextToken() {
            String ans = peekToken();
            token = null;
            return ans;
        }

    }
}

