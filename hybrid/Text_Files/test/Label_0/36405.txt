import java.io.*;
import java.util.*;

public class ConsecutiveSubsequence {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader inp = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        Solver solver = new Solver();
        solver.solve(inp, out);
        out.close();
    }

    static class Solver {
        private void solve(InputReader inp, PrintWriter out) {
            HashMap<Integer, Integer> dp = new HashMap<>();
            int n = inp.nextInt(), max = 0, num = 0;
            int[] x = new int[n];
            for (int i = 0; i < n; i++) {
                x[i] = inp.nextInt();
                dp.put(x[i], dp.getOrDefault(x[i] - 1, 0) + 1);
            }
            for (Integer key: dp.keySet()) {
                if (dp.get(key) > max) {
                    max = dp.get(key);
                    num = key;
                }
            }
            out.println(max);
            int a = num, b = num - max + 1;
            for (int i = 0; i < n && b <= a; i++) {
                if (x[i] == b) {
                    out.print((i + 1) + " ");
                    b++;
                }
            }
        }
    }

    static class InputReader {
        BufferedReader reader;
        StringTokenizer tokenizer;

        InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }

        String next() {
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
