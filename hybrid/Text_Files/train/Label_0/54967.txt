import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.InputMismatchException;
import java.io.IOException;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskE solver = new TaskE();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskE {
        public void solve(int testNumber, InputReader in, PrintWriter out) {
            int n = in.readInt();
            char[] buffer = IOUtils.readCharArray(in, n);
            int[] s = new int[n];
            for (int i = 0; i < n; ++i) {
                s[i] = buffer[i] - 'a';
            }

            // calculate char to to each position min dist
            int[][] char_pos_dist = new int[8][n];
            int[] q = new int[n];
            int[] d = new int[n];
            boolean[] char_visited = new boolean[8];
            for (int ch = 0; ch < 8; ++ch) {
                Arrays.fill(d, 100);
                Arrays.fill(char_visited, false);
                int front = 0;
                int back = 0;
                for (int i = 0; i < n; ++i) {
                    if (s[i] == ch) {
                        q[front++] = i;
                        d[i] = 0;
                    }
                }
                char_visited[ch] = true;
                while (back < front) {
                    int cur = q[back++];
                    if (!char_visited[s[cur]]) {
                        char_visited[s[cur]] = true;
                        for (int i = 0; i < n; ++i) {
                            if (s[i] == s[cur] && d[i] > d[cur] + 1) {
                                q[front++] = i;
                                d[i] = d[cur] + 1;
                            }
                        }
                    }
                    for (int i = -1; i <= 1; i += 2) {
                        if (cur + i < 0 || cur + i >= n) continue;
                        if (d[cur + i] > d[cur] + 1) {
                            q[front++] = cur + i;
                            d[cur + i] = d[cur] + 1;
                        }
                    }
                }
                System.arraycopy(d, 0, char_pos_dist[ch], 0, n);
            }

            // calculate char to char min dist
            int[][] char_char_dist = ArrayUtils.GetIntegerArray(100, 8, 8);
            for (int ch = 0; ch < 8; ++ch) {
                for (int pos = 0; pos < n; ++pos) {
                    char_char_dist[ch][s[pos]] = Math.min(char_char_dist[ch][s[pos]], char_pos_dist[ch][pos]);
                }
            }

            // calculate masks for whether each position gets best possible dist to chars or not.
            int[] mask = new int[n];
            for (int pos = 0; pos < n; pos++) {
                for (int ch = 0; ch < 8; ch++) {
                    if (char_pos_dist[ch][pos] > char_char_dist[ch][s[pos]]) {
                        mask[pos] |= (1 << ch);
                    }
                }
            }

            // calculate the results
            long[] result = new long[100];
            int[][] cnt = new int[8][1 << 8];
            for (int pos = 0; pos < n; ++pos) {
                for (int start_pos = Math.max(0, pos - 7); start_pos < pos; ++start_pos) {
                    int dist = pos - start_pos;
                    for (int ch = 0; ch < 8; ++ch) {
                        dist = Math.min(dist, char_pos_dist[ch][pos] + 1 + char_pos_dist[ch][start_pos]);
                    }
                    result[dist]++;
                }
                if (pos >= 8) {
                    cnt[s[pos - 8]][mask[pos - 8]]++;
                    for (int ch = 0; ch < 8; ch++) {
                        for (int msk = 0; msk < (1 << 8); msk++) {
                            if (cnt[ch][msk] == 0) continue;
                            int dist = 100;
                            for (int ch_m = 0; ch_m < 8; ch_m++) {
                                dist = Math.min(dist, char_pos_dist[ch_m][pos] + 1 + char_char_dist[ch][ch_m] + ((msk >> ch_m) & 1));
                            }
                            result[dist] += cnt[ch][msk];
                        }
                    }
                }
            }
            for (int i = result.length - 1; i >= 0; --i) {
                if (result[i] > 0) {
                    out.println(i + " " + result[i]);
                    break;
                }
            }
        }

    }

    static class IOUtils {
        public static char[] readCharArray(InputReader in, int n) {
            char[] c = new char[n];
            for (int i = 0; i < n; ++i) {
                c[i] = in.readCharacter();
            }
            return c;
        }

    }

    static class InputReader {
        private InputStream stream;
        private byte[] buf = new byte[1024];
        private int curChar;
        private int numChars;

        public InputReader(InputStream stream) {
            this.stream = stream;
        }

        public int read() {
            // InputMismatchException -> UnknownError
            if (numChars == -1)
                throw new UnknownError();
            if (curChar >= numChars) {
                curChar = 0;
                try {
                    numChars = stream.read(buf);
                } catch (IOException e) {
                    throw new UnknownError();
                }
                if (numChars <= 0)
                    return -1;
            }
            return buf[curChar++];
        }

        public int readInt() {
            int c = read();
            while (isSpaceChar(c))
                c = read();
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = read();
            } else if (c == '+') {
                c = read();
            }
            int res = 0;
            do {
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                res *= 10;
                res += c - '0';
                c = read();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        public char readCharacter() {
            int c = read();
            while (isSpaceChar(c)) {
                c = read();
            }
            return (char) c;
        }

        public static boolean isSpaceChar(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

    }

    static class ArrayUtils {
        public static void FillArray(int[][] a, int val) {
            for (int[] b : a) {
                FillArray(b, val);
            }
        }

        public static void FillArray(int[] a, int val) {
            Arrays.fill(a, val);
        }

        public static int[][] GetIntegerArray(int val, int a, int b) {
            int[][] resArray = new int[a][b];
            FillArray(resArray, val);
            return resArray;
        }

    }
}

