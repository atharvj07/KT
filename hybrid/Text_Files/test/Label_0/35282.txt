import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.io.InputStream;
import java.io.InputStreamReader;
import static java.lang.Math.abs;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.Arrays;
import java.util.HashSet;

public class Main {
    public static void main(String[] args) throws IOException {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        try (PrintWriter out = new PrintWriter(outputStream)) {
            TaskB solver = new TaskB();
            solver.solve(1, in, out);
        }
    }
}
class TaskB {
    public void solve(int testNumber, InputReader in, PrintWriter out){
        int n = in.nextInt();
        int m = 8 - in.nextInt();
        int a[] = new int[] {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        a[n] -= m;
        out.println(1 + a[n]/7 + (a[n]%7 != 0 ? 1 : 0));
    }
}
class InputReader {
    private final BufferedReader reader;
    private StringTokenizer tokenizer;
    public InputReader(InputStream stream) throws FileNotFoundException {
        reader = new BufferedReader(new InputStreamReader(stream));
        tokenizer = null;
    }

    public String nextLine() {
        try {
            return reader.readLine();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public String next() {
        while (tokenizer == null || !tokenizer.hasMoreTokens()) {
            tokenizer = new StringTokenizer(nextLine());
        }
        return tokenizer.nextToken();
    }

    public int nextInt() {
        return Integer.parseInt(next());
    }
    public long nextLong() {
        return Long.parseLong(next());
    }
    public double nextDouble() {
        return Double.parseDouble(next());
    }
    public BigInteger nextBigInteger() {
        return new BigInteger(next());
    }
    public int[] nextInts(int n) {
        int a[] = new int[n];
        for (int i = 0; i < n; ++i)
            a[i] = nextInt();
        return a;
    }
    int[] getPrimes(int n) {
        int a[] = new int[n];
        Arrays.fill(a, 1);
        a[0] = a[1] = 0;
        for (int i = 2; i * i < n; ++i) {
            if (a[i] == 1) {
                for (int j = i * i; j < n; j += i)
                    a[j] = 0;
            }
        }
        return a;
    }
}