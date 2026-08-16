import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringJoiner;
import java.util.StringTokenizer;
import java.util.function.IntUnaryOperator;
import java.util.function.LongUnaryOperator;

public class Main {
    static In in = new In();
    static Out out = new Out();
    static final long mod = 1000000007;
    static final long inf = 0x1fffffffffffffffL;
    static final int iinf = 0x3fffffff;
    static final int[] da = {-1, 0, 1, 0, -1, 1, 1, -1, -1};

    void solve() {
        int n = in.nextInt();
        long[] a = in.nextLongArray(n);
        if (n == 2) {
            if ((a[0] + a[1]) % 2 == 0 && a[0] >= a[1]) {
                out.println(a[0] - (a[0] + a[1]) / 2);
            } else {
                out.println(-1);
            }
        } else {
            long a3 = 0;
            for (int i = 2; i < n; i++) {
                a3 ^= a[i];
            }
            long s = a[0] + a[1];
            if (s - a3 >= 0 && (s - a3) % 2 == 0) {
                long m = (s - a3) / 2;
                if ((a3 & m) != 0) {
                    out.println(-1);
                } else {
                    long[][] dp = new long[60][2];
                    for (int i = 50; i >= 0; i--) {
                        if (((m >> i) & 1) == 1) {
                            if (((a[1] >> i) & 1) == 1) {
                                dp[i][0] = dp[i + 1][0] | (1L << i);
                                if (dp[i + 1][1] == -1) {
                                    dp[i][1] = -1;
                                } else {
                                    dp[i][1] = dp[i + 1][1] | (1L << i);
                                }
                            } else {
                                if (dp[i + 1][1] == -1) {
                                    dp[i][0] = dp[i + 1][0] | (1L << i);
                                } else {
                                    dp[i][0] = dp[i + 1][1] | (1L << i);
                                }
                                dp[i][1] = -1;
                            }
                        } else if (((a3 >> i) & 1) == 1) {
                            if (((a[1] >> i) & 1) == 1) {
                                dp[i][0] = dp[i + 1][0];
                                if (dp[i + 1][1] == -1) {
                                    dp[i][1] = -1;
                                } else {
                                    dp[i][1] = dp[i + 1][1] | (1L << i);
                                }
                            } else {
                                if (dp[i + 1][1] != -1) {
                                    dp[i][0] = dp[i + 1][1] | (1L << i);
                                } else {
                                    if (dp[i + 1][0] != 0) {
                                        dp[i][0] = dp[i + 1][0];
                                    }
                                }
                                if (dp[i + 1][0] != 0) {
                                    dp[i][0] = Math.min(dp[i][0], dp[i + 1][0]);
                                }
                                dp[i][1] = dp[i + 1][1];
                            }
                        } else {
                            dp[i][0] = dp[i + 1][0];
                            if (((a[1] >> i) & 1) == 0) {
                                dp[i][1] = dp[i + 1][1];
                            } else {
                                dp[i][1] = -1;
                            }
                        }
                        if ((dp[i][0] >> i) <= (a[1] >> i)) {
                            dp[i][0] = 0;
                        }
                    }
                    if (dp[0][1] != -1 && dp[0][1] != 0) {
                        out.println(0);
                    } else if (a[0] - (dp[0][0] - a[1]) == 0) {
                        out.println(-1);
                    } else {
                        long s1 = (a[0] - (dp[0][0] - a[1]));
                        long s2 = dp[0][0];
                        if ((s1 ^ s2) == a3 && (s1 & s2) == m) {
                            out.println(dp[0][0] - a[1]);
                        } else {
                            out.println(-1);
                        }
                    }
                }
            } else {
                out.println(-1);
            }
        }
    }

    public static void main(String[]$) {
        new Main().solve();
        out.flush();
    }
}

class In {
    private BufferedReader reader = new BufferedReader(new InputStreamReader(System.in), 0x10000);
    private StringTokenizer tokenizer;

    String next() {
        try {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                tokenizer = new StringTokenizer(reader.readLine());
            }
        } catch (IOException ignored) {
        }
        return tokenizer.nextToken();
    }

    int nextInt() {
        return Integer.parseInt(next());
    }

    long nextLong() {
        return Long.parseLong(next());
    }

    char[] nextCharArray() {
        return next().toCharArray();
    }

    char[][] nextCharGrid(int n, int m) {
        char[][] a = new char[n][m];
        for (int i = 0; i < n; i++) {
            a[i] = next().toCharArray();
        }
        return a;
    }

    int[] nextIntArray(int n) {
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = nextInt();
        }
        return a;
    }

    int[] nextIntArray(int n, IntUnaryOperator op) {
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = op.applyAsInt(nextInt());
        }
        return a;
    }

    long[] nextLongArray(int n) {
        long[] a = new long[n];
        for (int i = 0; i < n; i++) {
            a[i] = nextLong();
        }
        return a;
    }

    long[] nextLongArray(int n, LongUnaryOperator op) {
        long[] a = new long[n];
        for (int i = 0; i < n; i++) {
            a[i] = op.applyAsLong(nextLong());
        }
        return a;
    }
    
    List<List<Integer>> nextEdges(int n, int m) {
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            res.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            int u = nextInt() - 1;
            int v = nextInt() - 1;
            res.get(u).add(v);
            res.get(v).add(u);
        }
        return res;
    }
}

class Out {
    private PrintWriter out = new PrintWriter(System.out);
    boolean autoFlush = false;

    void println(Object... a) {
        StringJoiner joiner = new StringJoiner(" ");
        for (Object obj : a) {
            joiner.add(String.valueOf(obj));
        }
        out.println(joiner);
        if (autoFlush) {
            out.flush();
        }
    }

    void println(char[] s) {
        out.println(String.valueOf(s));
        if (autoFlush) {
            out.flush();
        }
    }

    void println(int[] a) {
        StringJoiner joiner = new StringJoiner(" ");
        for (int i : a) {
            joiner.add(Integer.toString(i));
        }
        out.println(joiner);
        if (autoFlush) {
            out.flush();
        }
    }

    void println(long[] a) {
        StringJoiner joiner = new StringJoiner(" ");
        for (long i : a) {
            joiner.add(Long.toString(i));
        }
        out.println(joiner);
        if (autoFlush) {
            out.flush();
        }
    }

    void flush() {
        out.flush();
    }
}
