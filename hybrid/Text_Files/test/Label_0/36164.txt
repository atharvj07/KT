import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.math.BigInteger;
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
        CBearAndPoker solver = new CBearAndPoker();
        solver.solve(1, in, out);
        out.close();
    }

    static class CBearAndPoker {
        public void solve(int testNumber, InputReader in, PrintWriter out) {
            int n = in.nextInt();
            int[] arr = new int[n];
            arr[0] = in.nextInt();
            arr[1] = in.nextInt();
            int gcd = gcd(arr[0], arr[1]);
            for (int i = 2; i < n; i++) {
                arr[i] = in.nextInt();
                gcd = gcd(arr[i], gcd);
            }

            for (int i = 0; i < n; i++) {
                arr[i] /= gcd;
            }

            boolean res = true;
            for (int i = 0; i < n; i++) {
                if (!valid(arr[i])) {
                    res = false;
                    break;
                }
            }
            if (res)
                out.println("Yes");
            else
                out.println("No");
        }

        int gcd(int a, int b) {
            return BigInteger.valueOf(a).gcd(BigInteger.valueOf(b)).intValue();
        }

        boolean valid(int num) {
            while (num != 1 && num % 2 == 0) {
                num /= 2;
            }

            while (num != 1 && num % 3 == 0) {
                num /= 3;
            }
            return num == 1;
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

