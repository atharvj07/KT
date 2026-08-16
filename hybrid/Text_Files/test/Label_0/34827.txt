import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.text.DecimalFormat;
import java.util.HashMap;
import java.io.IOException;
import java.io.InputStreamReader;
import java.text.NumberFormat;
import java.util.HashSet;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author Me
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        PowerTransmission solver = new PowerTransmission();
        solver.solve(1, in, out);
        out.close();
    }

    static class PowerTransmission {
        HashMap<Integer, HashMap<Integer, HashSet<String>>> riseToRunToYIntercept = new HashMap<>();
        DecimalFormat df = new DecimalFormat(".00000000");

        public void solve(int testNumber, InputReader in, PrintWriter out) {
            int N = in.nextInt();
            Point[] p = new Point[N];
            for (int i = 0; i < N; i++) {
                p[i] = new Point(in.nextInt(), in.nextInt());
            }
            for (int i = 0; i < N; i++) {
                for (int j = i + 1; j < N; j++) {
                    int rise = p[j].y - p[i].y;
                    int run = p[j].x - p[i].x;
                    if (run == 0) {
                        run = 1;
                        rise = (int) (1e9);
                        riseToRunToYIntercept.putIfAbsent(rise, new HashMap<>());
                        riseToRunToYIntercept.get(rise).putIfAbsent(run, new HashSet<>());
                        riseToRunToYIntercept.get(rise).get(run).add(df.format(p[j].x));
                    } else {
                        int gcd = gcd(rise, run);
                        rise /= gcd;
                        run /= gcd;
                        riseToRunToYIntercept.putIfAbsent(rise, new HashMap<>());
                        riseToRunToYIntercept.get(rise).putIfAbsent(run, new HashSet<>());
                        double yintercept = -rise / (double) (run) * p[j].x + p[j].y;
                        riseToRunToYIntercept.get(rise).get(run).add(df.format(yintercept));

                        if (rise == (int) (1e9)) {
                            yintercept = p[j].x;
                        }
                    }
                }
            }
            long res = 0;
            long finalAdd = 0;
            for (HashMap<Integer, HashSet<String>> vals : riseToRunToYIntercept.values()) {
                for (HashSet<String> val : vals.values()) {
                    res -= choose2(val.size());
                    finalAdd += val.size();
                }
            }
            res += choose2(finalAdd);
            out.println(res);
        }

        int gcd(int a, int b) {
            if (a == 0) {
                return b;
            }
            return gcd(b % a, a);
        }

        long choose2(long n) {
            if (n <= 1) {
                return 0;
            }
            return (n * (n - 1)) / 2;
        }

        class Point {
            int x;
            int y;

            Point(int x, int y) {
                this.x = x;
                this.y = y;
            }

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

