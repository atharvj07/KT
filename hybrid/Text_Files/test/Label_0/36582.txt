import java.io.*;
import java.util.StringTokenizer;

/**
 * Created by Julia on 01.04.2017.
 */
public class SolverE {

    public static void main(String[] args) throws IOException {
        new SolverE().run();
    }

    StringTokenizer stok;
    BufferedReader br;
    PrintWriter pw;

    String nextToken() throws IOException {
        while (stok == null || !stok.hasMoreTokens()) {
            stok = new StringTokenizer(br.readLine());
        }
        return stok.nextToken();
    }

    int nextInt() throws IOException {
        return Integer.parseInt(nextToken());
    }

    long nextLong() throws IOException {
        return Long.parseLong(nextToken());
    }

    double nextDouble() throws IOException {
        return Double.parseDouble(nextToken());
    }

    void run() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        pw = new PrintWriter(new OutputStreamWriter(System.out));
//        br = new BufferedReader(new FileReader("input.txt"));
//        pw = new PrintWriter("output.txt");
        solve();
        pw.close();
    }

    private void solve() throws IOException {
        int c = nextInt();
        for (int i=0; i<c; i++) {
            solveTest();
        }
    }

    private void solveTest() throws IOException {
        int n = nextInt();
        int m = nextInt();
        long t = nextLong();
        long[] mas = new long[n];
        for (int i=0; i<n; i++) {
            mas[i] = nextInt();
        }
        int result = 0;
        long resD = 1;
        long min = 0;
        long max = t + 1;
        while (max - min > 1) {
            long mid = (max + min) / 2;

            boolean exceeded = false;
            long curtime = 0;
            long lastblock = 0;
            int curres=0;
            int curtask = 0;
            for (int i=0; i<n; i++) {
                if (mas[i]<=mid) {
                    curtime += mas[i];
                    lastblock += mas[i];
                    if (curtime <= t) {
                        curres++;
                    } else {
                        exceeded = true;
                    }
                    curtask++;
                    if (curtask == m) {
                        curtime += lastblock;
                        lastblock = 0;
                        curtask = 0;
                    }
                }
            }
            if (curres > result) {
                result = curres;
                resD = mid;
            }

            if (exceeded) {
                max = mid;
            } else {
                min = mid;
            }
        }
        pw.println(result + " " + resD);
    }
}
