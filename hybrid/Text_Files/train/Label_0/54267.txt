import java.io.*;
import java.util.*;
import java.math.*;
import static java.lang.Math.*;

public class Main implements Runnable {

    public void solve() throws IOException {
        int n = nextInt(), V = nextInt();
        int[ ] a = new int[n];
        for(int i = 0; i < n; ++i) {
            a[i] = nextInt();
        }
        int[] b = new int[n];
        for(int i = 0; i < n; ++i) {
            b[i] = nextInt();
        }
        double left = 0, right = 1000000;
        while (right - left > 1e-9) {
            double c = (left + right) / 2;
            double q = 0;
            boolean can = true;
            for(int i = 0; i < n;++i) {
                can &= b[i] >= (a[i] * c);
                q += a[i] * c;
            }
            can &= q < V;
            if (!can)
                right = c;
            else if (q > V)
                right = c;
            else
                left = c;
        }
        double ans = 0;
        for(int i = 0; i < n; ++i)
            ans += a[i] * right;
        pw.printf(Locale.US, "%1.8f", ans);
    }

    static final String filename = "A";
    static final boolean fromConsole = true;

    public void run() {
        try {
            if (!fromConsole) {
                in = new BufferedReader(new FileReader(filename + ".in"));
                pw = new PrintWriter(filename + ".out");
            } else {
                in = new BufferedReader(new InputStreamReader(System.in));
                pw = new PrintWriter(System.out);
            }
            st = new StringTokenizer("");
            long st = System.currentTimeMillis();
            solve();
            //pw.printf("\nWorking time: %d ms\n", System.currentTimeMillis() - st);
            pw.close();
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(-1);
        }
    }

    private StringTokenizer st;
    private BufferedReader in;
    private PrintWriter pw;

    boolean hasNext() throws IOException {
        while (!st.hasMoreTokens()) {
            String line = in.readLine();
            if (line == null) {
                return false;
            }
            st = new StringTokenizer(line);
        }
        return st.hasMoreTokens();
    }

    String next() throws IOException {
        return hasNext() ? st.nextToken() : null;
    }

    int nextInt() throws IOException {
        return Integer.parseInt(next());
    }

    BigInteger nextBigInteger() throws IOException {
        return new BigInteger(next());
    }

    long nextLong() throws IOException {
        return Long.parseLong(next());
    }

    double nextDouble() throws IOException {
        return Double.parseDouble(next());
    }

    public static void main(String[] args) {
        new Thread(new Main()).start();
    }
}