import java.io.*;
import java.util.*;

public class C {
    public static void main(String[] args) {
        new C().run();
    }

    void solve() throws IOException {
        int n = ni(); int l = ni(); int r = ni(); int Ql = ni(); int Qr = ni();
        int w[] = nia(n);
        long lp[] = new long[n];
        long rp[] = new long[n];

        lp[0] = w[0] * l;
        rp[n - 1] = w[n - 1] * r;
        for (int i = 1; i < n; ++i) {
            lp[i] = lp[i - 1] + w[i] * l;
            rp[n - i - 1] = rp[n - i] + w[n - i - 1] * r;
        }

        long allleft = lp[n - 1] + Ql * (n - 1);
        long allright = rp[0] + Qr * (n - 1);
        long min = Math.min(allleft, allright);
        for(int i = 0; i < n - 1; ++i) {
            long pen = 0;
            int lt = i + 1;
            int rt = n - lt;
            if (lt < rt)
                pen = (rt - lt - 1) * Qr;
            else if (rt < lt)
                pen = (lt - rt - 1) * Ql;
            long c = lp[i] + rp[i + 1] + pen;
            if (c < min)
                min = c;
        }

        prln(min);
    }

    public void run() {
        try {
            if (isFileIO) {
                pw = new PrintWriter(new File("output.out"));
                br = new BufferedReader(new FileReader("input.in"));
            } else {
                pw = new PrintWriter(System.out);
                br = new BufferedReader(new InputStreamReader(System.in));
            }
            solve();
            pw.close();
            br.close();
        } catch (IOException e) {
            System.err.println("IO Error");
        }
    }

    private int[] nia(int n) throws IOException {
        int arr[] = new int[n];
        for (int i = 0; i < n; ++i)
            arr[i] = Integer.parseInt(nextToken());
        return arr;
    }

    private int[] niam1(int n) throws IOException {
        int arr[] = new int[n];
        for (int i = 0; i < n; ++i)
            arr[i] = Integer.parseInt(nextToken()) - 1;
        return arr;
    }

    private long[] nla(int n) throws IOException {
        long arr[] = new long[n];
        for (int i = 0; i < n; ++i)
            arr[i] = Long.parseLong(nextToken());
        return arr;
    }

    private void pr(Object o) {
        pw.print(o);
    }

    private void prln(Object o) {
        pw.println(o);
    }

    private void prln() {
        pw.println();
    }

    int ni() throws IOException {
        return Integer.parseInt(nextToken());
    }

    long nl() throws IOException {
        return Long.parseLong(nextToken());
    }

    double nd() throws IOException {
        return Double.parseDouble(nextToken());
    }

    private String nextToken() throws IOException {
        while (tokenizer == null || !tokenizer.hasMoreTokens()) {
            tokenizer = new StringTokenizer(br.readLine());
        }

        return tokenizer.nextToken();
    }

    // private void qsort(int a[]) {
    // Random rand = new Random(271828182l);
    // qsort(a, 0, a.length, rand);
    // }
    //
    // private void qsort(int a[], int l, int r, Random rand) {
    // if (r - l <= 1)
    // return;
    //
    // if (r - l == 2) {
    // if (a[r - 1] < a[l]) {
    // int t = a[r - 1];
    // a[r - 1] = a[l];
    // a[l] = t;
    // }
    //
    // return;
    // }
    //
    // int x = a[rand.nextInt(r - l) + l];
    // int i = l, j = r - 1;
    // while (i < j) {
    // while (a[i] < x)
    // ++i;
    // while (a[j] > x)
    // --j;
    // if (i < j) {
    // int t = a[i];
    // a[i] = a[j];
    // a[j] = t;
    // ++i;
    // --j;
    // }
    // }
    //
    // qsort(a, l, j + 1, rand);
    // qsort(a, i, r, rand);
    // }

    private BufferedReader br;
    private StringTokenizer tokenizer;
    private PrintWriter pw;
    private final boolean isFileIO = false;
}
