import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Main {
    private FastScanner in;
    private PrintWriter out;

    private void solve() throws IOException {
        int n = in.nextInt();

        long a[] = new long[n];
        for (int i = 0; i < n; i++)
            a[i] = in.nextLong();

        long ans = 0;
        int l = 0, r = --n;

        while (l < n && a[l + 1] > a[l])
            l++;
        while (r > 1 && a[r - 1] > a[r])
            r--;

        long al = a[l], ar = a[r];

        while (l + 1 < r) {
            if (al < ar)
                ans += (++al) - a[++l];
            else if (al > ar)
                ans += (++ar) - a[--r];
            else if (al + a[r - 1] < ar + a[l + 1])
                ans += (++al) - a[++l];
            else
                ans += (++ar) - a[--r];

            while (l < n && a[l + 1] > al)
                al = a[++l];
            while (r > 1 && a[r - 1] > ar)
                ar = a[--r];
        }

        if (l < r && al == ar)
            ans++;

        out.println(ans);
    }

    class FastScanner {
        StringTokenizer st;
        BufferedReader br;

        FastScanner(InputStream s) {
            br = new BufferedReader(new InputStreamReader(s));
        }

        String next() throws IOException {
            while (st == null || !st.hasMoreTokens())
                st = new StringTokenizer(br.readLine());
            return st.nextToken();
        }

        int nextInt() throws IOException {
            return Integer.parseInt(next());
        }

        long nextLong() throws IOException {
            return Long.parseLong(next());
        }

        double nextDouble() throws IOException {
            return Double.parseDouble(next());
        }

        String nextLine() throws IOException {
            return br.readLine();
        }

        boolean ready() throws IOException {
            return br.ready();
        }

    }

    private void run() throws IOException {
        in = new FastScanner(System.in);
        out = new PrintWriter(System.out);

        solve();

        out.flush();
        out.close();
    }

    public static void main(String[] args) throws IOException {
        new Main().run();
    }
}