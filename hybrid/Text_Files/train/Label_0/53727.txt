import java.io.InputStream;
import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.PrintWriter;
import java.util.List;
import java.util.StringTokenizer;
import java.io.InputStreamReader;
import java.io.IOException;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author AlexFetisov
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskE_CandyGameAgain solver = new TaskE_CandyGameAgain();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskE_CandyGameAgain {
        private long[] a;
        List<Integer> commands;
        int A;
        int B;
        int C;

        public void solve(int testNumber, InputReader in, PrintWriter out) {
            int n = in.nextInt();
            a = new long[n];
            for (int i = 0; i < n; ++i) a[i] = in.nextLong();

            int am0 = 0;
            for (long x : a) if (x == 0) ++am0;
            if (am0 >= n - 1) {
                out.println(-1);
                return;
            }

            A = -1;
            B = -1;
            for (int i = 0; i < n; ++i)
                if (a[i] != 0) {
                    A = i;
                    break;
                }
            for (int i = A + 1; i < n; ++i)
                if (a[i] != 0) {
                    B = i;
                    break;
                }
            C = B + 1;
            commands = new ArrayList<Integer>();

            while (C < n) {
                if (a[C] != 0) {
                    emptyBox();
                }
                ++C;
            }

            out.println(commands.size() / 2);
            for (int i = 0; i < commands.size(); i += 2) {
                out.println((commands.get(i + 1) + 1) + " " + (commands.get(i) + 1));
            }
        }

        private void emptyBox() {
            while (true) {
                if (a[A] == 0 || a[B] == 0 || a[C] == 0) {
                    if (a[A] == 0) {
                        A = B;
                        B = C;
                    } else if (a[B] == 0) {
                        B = C;
                    }
                    break;
                }

                if (IntegerUtils.max(a[A], a[B], a[C]) == Math.min(a[A], Math.min(a[B], a[C]))) {
                    commands.add(A);
                    commands.add(B);
                    a[A] -= a[B];
                    a[B] *= 2;
                    continue;
                }

                int minId = getMinId(A, B, C);
                int maxId = getMaxId(A, B, C);
                int medId = A + B + C - minId - maxId;

                if (a[minId] == a[medId]) {
                    commands.add(medId);
                    commands.add(minId);
                    a[medId] -= a[minId];
                    a[minId] *= 2;
                    continue;
                }

                long x = (a[medId] / a[minId]);

                for (int bit = 0; x != 0; ++bit) {
                    if (BitUtils.checkBit(x, bit)) {
                        commands.add(medId);
                        commands.add(minId);
                        a[medId] -= a[minId];
                        x -= (1L << bit);
                        a[minId] *= 2L;
                    } else {
                        commands.add(maxId);
                        commands.add(minId);
                        a[maxId] -= a[minId];
                        a[minId] *= 2L;
                    }
                }

            }
        }

        private int getMaxId(int A, int B, int C) {
            if (a[A] > a[B] && a[A] > a[C]) {
                return A;
            } else if (a[B] > a[C]) {
                return B;
            } else {
                return C;
            }
        }

        private int getMinId(int A, int B, int C) {
            if (a[A] < a[B] && a[A] < a[C]) {
                return A;
            } else if (a[B] < a[C]) {
                return B;
            } else {
                return C;
            }
        }

    }

    static class IntegerUtils {
        public static long max(long... a) {
            long result = a[0];
            for (int i = 1; i < a.length; ++i) {
                result = Math.max(result, a[i]);
            }
            return result;
        }

    }

    static class InputReader {
        private BufferedReader reader;
        private StringTokenizer stt;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream));
        }

        public String nextLine() {
            try {
                return reader.readLine();
            } catch (IOException e) {
                return null;
            }
        }

        public String nextString() {
            while (stt == null || !stt.hasMoreTokens()) {
                stt = new StringTokenizer(nextLine());
            }
            return stt.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(nextString());
        }

        public long nextLong() {
            return Long.parseLong(nextString());
        }

    }

    static class BitUtils {
        public static boolean checkBit(long mask, int bit) {
            return (mask & (1L << bit)) > 0;
        }

    }
}

