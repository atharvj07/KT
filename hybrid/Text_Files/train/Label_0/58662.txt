import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Bits {
    static long L, R;
    static int[][][] dp = new int[66][2][2];
    static int[][][] path = new int[66][2][2];

    static int go(int index, int low1, int high1) {
        if (index == -1) {
            return 0;
        }
        if (dp[index][low1][high1] != -1)
            return dp[index][low1][high1];
        int bit1 = (L & (1L << index)) == 0 ? 0 : 1;
        int bit2 = (R & (1L << index)) == 0 ? 0 : 1;
        int res = -1 << 28;
        for (int i = 0; i < 2; i++) {
            int nl1 = low1, nh1 = high1;
            boolean can = true;
            if (low1 == 0) {
                if (i == bit1) {
                    nl1 = 0;
                } else if (i < bit1) {
                    can = false;
                } else if (i > bit1) {
                    nl1 = 1;
                }
            }
            if (high1 == 0) {
                if (i == bit2) {
                    nh1 = 0;
                } else if (i < bit2) {
                    nh1 = 1;
                } else if (i > bit2) {
                    can = false;
                }
            }

            if (can) {
                int way = (i == 1 ? 1 : 0) + go(index - 1, nl1, nh1);
                if (way > res) {
                    res = way;
                    path[index][low1][high1] = i;
                }
            }
        }
        return dp[index][low1][high1] = res;
    }

    public static void main(String[] args) {
        InputReader r = new InputReader(System.in);
        PrintWriter out = new PrintWriter(System.out);
        int t = r.nextInt();
        while (t-- > 0) {
            L = r.nextLong();
            R = r.nextLong();
            for (int[][] x : dp)
                for (int[] y : x)
                    Arrays.fill(y, -1);
            go(63, 0, 0);
            int index = 63, low1 = 0, high1 = 0;
            long x = 0;
            while (index >= 0) {
                int bit1 = (L & (1L << index)) == 0 ? 0 : 1;
                int bit2 = (R & (1L << index)) == 0 ? 0 : 1;
                int i = path[index][low1][high1];
                int nl1 = low1, nh1 = high1;
                if (low1 == 0) {
                    if (i == bit1) {
                        nl1 = 0;
                    } else if (i > bit1) {
                        nl1 = 1;
                    }
                }
                if (high1 == 0) {
                    if (i == bit2) {
                        nh1 = 0;
                    } else if (i < bit2) {
                        nh1 = 1;
                    }
                }
                if (i == 1)
                    x |= 1L << index;
                index--;
                low1 = nl1;
                high1 = nh1;
            }
            out.println(x);
        }
        out.close();
    }

    static class InputReader {
        private BufferedReader reader;
        private StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream));
            tokenizer = null;
        }

        public InputReader(FileReader stream) {
            reader = new BufferedReader(stream);
            tokenizer = null;
        }

        public String nextLine() {
            try {
                return reader.readLine();
            } catch (IOException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
                return null;
            }
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
