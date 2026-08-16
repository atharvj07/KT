import java.io.*;
import java.util.StringTokenizer;

/**
 * 167A
 * θ(n) time
 * θ(n) space
 *
 * @author artyom
 */
public class _167A implements Runnable {
    private BufferedReader in;
    private StringTokenizer tok;

    private Object solve() throws IOException {
        int n = nextInt();
        double a = nextInt(), d = nextInt();
        double[] r = new double[n];
        for (int i = 0; i < n; i++) {
            double t0 = nextInt(), v = nextInt(),
                    s = v * v / (2 * a),
                    t = s <= d ? v / a + (d - s) / v : Math.sqrt(2 * d / a);
            r[i] = t0 + t;
        }
        for (int i = 1; i < n; i++) {
            r[i] = Math.max(r[i], r[i - 1]);
        }
        return join(r);
    }

    //--------------------------------------------------------------
    public static void main(String[] args) {
        new _167A().run();
    }

    @Override
    public void run() {
        try {
            in = new BufferedReader(new InputStreamReader(System.in));
            tok = null;
            System.out.print(solve());
            in.close();
        } catch (IOException e) {
            System.exit(0);
        }
    }

    private String nextToken() throws IOException {
        while (tok == null || !tok.hasMoreTokens()) {
            tok = new StringTokenizer(in.readLine());
        }
        return tok.nextToken();
    }

    private int nextInt() throws IOException {
        return Integer.parseInt(nextToken());
    }

    private static String join(double[] entries) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0, n = entries.length - 1; i <= n; i++) {
            sb.append(entries[i]);
            if (i < n) {
                sb.append('\n');
            }
        }
        return sb.toString();
    }
}