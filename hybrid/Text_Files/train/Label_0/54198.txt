import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

/**
 * @author Pavel Mavrin
 */
public class Main {

    private static final int MM = 21000;

    private void solve() throws IOException {
        int n = nextInt();
        int[] p = new int[n];
        for (int i = 0; i < n; i++) {
            p[nextInt() - 1] = i;
        }
        for (int i = 0; i < n; i++) {
            out.print(i * MM + 1 + " ");
        }
        out.println();
        for (int i = 0; i < n; i++) {
            out.print((n - 1 - i) * MM + 1 + p[i] + " ");
        }
        out.println();
    }

    private BufferedReader br;
    private PrintWriter out;
    private StringTokenizer st;

    String next() throws IOException {
        while (st == null || !st.hasMoreTokens()) {
            st = new StringTokenizer(br.readLine());
        }
        return st.nextToken();
    }

    int nextInt() throws IOException {
        return Integer.parseInt(next());
    }

    long nextLong() throws IOException {
        return Long.parseLong(next());
    }

    public static void main(String[] args) throws IOException {
        new Main().run();
    }

    private void run() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        out = new PrintWriter(System.out);
        solve();
        out.close();
    }

}
