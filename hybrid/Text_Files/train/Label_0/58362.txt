import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.List;
import java.util.StringTokenizer;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
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
        TaskA solver = new TaskA();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskA {
        public void solve(int testNumber, InputReader in, PrintWriter out) {
            int n = in.nextInt();
            int k = in.nextInt();
            int[] a = new int[n];
            for (int i = 0; i < n; ++i) a[i] = in.nextInt();
            List<Integer> res = new ArrayList<>();
            int lastSwitch = -1;
            for (int i = 0; i <= k; ++i) {
                int nextSwitch = -1;
                for (int j = 0; j < n; ++j)
                    if (j != lastSwitch && (nextSwitch < 0 || a[j] < a[nextSwitch])) {
                        nextSwitch = j;
                    }
                for (int j = 0; j < n; ++j)
                    if (j != lastSwitch && j != nextSwitch) {
                        res.add(j);
                        --a[j];
                        if (a[j] < 0) {
                            out.println(-1);
                            return;
                        }
                    }
                res.add(nextSwitch);
                --a[nextSwitch];
                if (a[nextSwitch] < 0) {
                    out.println(-1);
                    return;
                }
                lastSwitch = nextSwitch;
            }
            out.println(res.size());
            for (int i = 0; i < res.size(); ++i) {
                out.print(res.get(i) + 1 + " ");
            }
            out.println();
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

