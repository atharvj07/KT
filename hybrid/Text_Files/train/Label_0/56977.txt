import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
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
        TaskB solver = new TaskB();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskB {
        public void solve(int testNumber, InputReader in, PrintWriter out) {
            long l = in.NextInt();
            long r = in.NextInt();
            long x = in.NextInt();
            long y = in.NextInt();
            ArrayList<Long> dividers = MathExtentions.getAllDividers(y);
            int res = 0;
            for (long a : dividers)
                if (l <= a && a <= r)
                    for (long b : dividers)
                        if (l <= b && b <= r)
                            if (MathExtentions.gcd(a, b) == x && MathExtentions.lcm(a, b) == y)
                                res++;
            out.println(res);

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

    }

    static class MathExtentions {
        public static long gcd(final long a, final long b) {
            if (a == 0)
                return b;
            return gcd(b % a, a);
        }

        public static long lcm(long a, long b) {
            if (a == 0 || b == 0) return 0;
            long gcd = gcd(a, b);
            return (a / gcd) * b;
        }

        public static ArrayList<Long> getAllDividers(long y) {
            //not complete! can use factors
            ArrayList<Long> res = new ArrayList<>();
            long i = 1;
            for (; i * i < y; i++) {
                if (y % i == 0) {
                    res.add(i);
                    res.add(y / i);
                }
            }
            if (i * i == y) res.add(i);
            return res;
        }

    }
}

