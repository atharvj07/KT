import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main implements Runnable {

    private int n;
    private int nn;
    private boolean[][] gr;
    private long[][] D;


    // ////////////////////////////////////////////////////////////////////
    // Solution

    private void solve() throws Throwable {
        n = nextInt();
        nn = 1 << n;
        gr = new boolean[n][n];
        int m = nextInt();
        for (int i = 0; i < m; i++) {
            int a = nextInt() - 1, b = nextInt() - 1;
            gr[a][b] = gr[b][a] = true;
        }
        D = new long[n][nn];
        for (int i = 0; i < n; i++) {
            Arrays.fill(D[i], -1);
        }
        long count = 0;
        for (int i = 0; i < n; i++) {
            count += getD(i, i, 1, 1 << i);
        }
        pw.println(count / 2);
    }


    private long getD(int first, int last, int cnt, int mask) {
        if (D[last][mask] != -1) return D[last][mask];
        long ans = 0;
        if (cnt >= 3 && gr[first][last])
            ans++;
        for (int i = first + 1; i < n; i++) {
            if (gr[last][i] && (mask & (1 << i)) == 0) {
                ans += getD(first, i, cnt + 1, mask | (1 << i));
            }
        }
        D[last][mask] = ans;
        return ans;
    }


    // ////////////////////////////////////////////////////////////////////
    // Utility functions

    PrintWriter pw;
    BufferedReader in;
    StringTokenizer st;

    void initStreams() throws FileNotFoundException {
        //System.setIn(new FileInputStream("2"));
        in = new BufferedReader(new InputStreamReader(System.in));
        pw = new PrintWriter(System.out);
    }

    String nextString() throws IOException {
        while (st == null || !st.hasMoreTokens()) {
            st = new StringTokenizer(in.readLine());
        }
        return st.nextToken();
    }

    int nextInt() throws NumberFormatException, IOException {
        return Integer.parseInt(nextString());
    }

    long nextLong() throws NumberFormatException, IOException {
        return Long.parseLong(nextString());
    }

    double nextDouble() throws NumberFormatException, IOException {
        return Double.parseDouble(nextString());
    }

    static Throwable sError;

    public static void main(String[] args) throws Throwable {
        Thread t = new Thread(new Main());
        t.start();
        t.join();
        if (sError != null) {
            throw sError;
        }
    }

    public void run() {
        try {
            initStreams();
            solve();
        } catch (Throwable e) {
            sError = e;
        } finally {
            if (pw != null)
                pw.close();
        }
    }
}
