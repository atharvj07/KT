import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author kessido
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        GTakeMetro solver = new GTakeMetro();
        solver.solve(1, in, out);
        out.close();
    }

    static class GTakeMetro {
        int n;
        int m;
        int s;
        long t;

        void step() {
            int curJump = (int) ((t--) % n);
            int sign = s < m ? 1 : -1;
            s += sign * curJump;
            s %= n;
            if (s < 0) s += n;
        }

        void doLoop() {
            for (int i = 0; i < n; i++) step();
        }

        public void solve(int testNumber, InputReader in, PrintWriter out) {
            n = in.NextInt();
            m = in.NextInt();
            s = in.NextInt() - 1;
            t = in.NextLong();

            while ((t % n) != 0) step();

            long[] lastSeem = new long[n];
            Arrays.fill(lastSeem, -1);
            while (t != 0) {
                doLoop();
                if (lastSeem[s] != -1) {
                    long interval = lastSeem[s] - t;
                    t %= interval;
                    break;
                } else {
                    lastSeem[s] = t;
                }
            }
            while (t != 0) step();
            out.println(s + 1);
        }

    }

    static class InputReader {
        BufferedReader reader;
        StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }

        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine(), " \t\n\r\f,");
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }

        public int NextInt() {
            return Integer.parseInt(next());
        }

        public long NextLong() {
            return Long.parseLong(next());
        }

    }
}

