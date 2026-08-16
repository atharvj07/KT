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
            int n = in.nextInt();
            int l = in.nextInt();
            int[] t = new int[n];
            for (int i = 0; i < n; ++i) t[i] = in.nextInt();
            double koef = 0.5 * Math.PI / l;
            double rx = 0;
            double ry = 0;
            for (int i = 0; i < n; ++i) {
                double sum = 0;
                double sofar = 0;
                for (int j = 1, k = i + 1; j < n; ++j, ++k) {
                    if (k >= n) k = 0;
                    int delta = t[i] - t[k];
                    if (delta < 0) delta += l;
                    double f = Math.tan(koef * delta);
                    sum += f * sofar;
                    delta = t[k] - t[i];
                    if (delta < 0) delta += l;
                    f = Math.tan(koef * delta);
                    sofar += f;
                }
                sum = (n - 1) * (n - 2) / 2 - sum;
                sum = 0.5 * sum;
                rx += Math.cos(koef * t[i] * 4.0) * sum;
                ry += Math.sin(koef * t[i] * 4.0) * sum;
            }
            rx /= n * (n - 1) * (double) (n - 2) / 6;
            ry /= n * (n - 1) * (double) (n - 2) / 6;
            out.println(rx + " " + ry);
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

