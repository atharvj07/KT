import java.io.*;
import java.util.*;

public class ProblemC {
    InputReader in; PrintWriter out;
    int n;
    double[] ans = new double[5];
    boolean ok(int[] a, double r) {
        double from = a[0] - 1e-8;
        double to = a[0] + 2 * r + 1e-8;
        ans[0] = from + r;
        int k = 0;
        while (k < n && a[k] <= to)
            k++;
        if (k == n)
            return true;
        from = a[k] - 1e-8;
        to = a[k] + 2 * r + 1e-8;
        ans[1] = from + r;
        while (k < n && a[k] <= to)
            k++;
        if (k == n)
            return true;
        from = a[k] - 1e-8;
        to = a[k] + 2 * r + 1e-8;
        ans[2] = from + r;
        while (k < n && a[k] <= to)
            k++;
        if (k == n)
            return true;        
        return false;
    }
    void solve() {
        n = in.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++)
            a[i] = in.nextInt();
        Arrays.sort(a);
        double lg = 0.0, rg = 1000000000.0, mi = 0;
        while (rg - lg > 1e-10) {
            mi = (lg + rg) / 2;
            if (mi == lg || mi == rg)
                break;
            if (ok(a, mi))
                rg = mi;
            else
                lg = mi;
        }
        ok(a, rg);
        out.printf("%.6f\n", rg);
        for (int i = 0; i < 3; i++) {
            if (ans[i] > 2000000000.0)
                ans[i] = 2000000000.0;
            out.printf("%.6f ", ans[i]);
        }
    }
    
    ProblemC(){
        boolean oj = System.getProperty("ONLINE_JUDGE") != null;
        try {
            if (oj) {
                in = new InputReader(System.in);
                out = new PrintWriter(System.out);
            }
            else {
                Writer w = new FileWriter("output.txt");
                in = new InputReader(new FileReader("input.txt"));
                out = new PrintWriter(w);
            }
        } catch(Exception e) {
            throw new RuntimeException(e);
        }
        solve();
        out.close();
    }
    public static void main(String[] args){
        new ProblemC();
    }
}

class InputReader {
    private BufferedReader reader;
    private StringTokenizer tokenizer;

    public InputReader(InputStream stream) {
        reader = new BufferedReader(new InputStreamReader(stream));
        tokenizer = null;
    }
    
    public InputReader(FileReader fr) {
        reader = new BufferedReader(fr);
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
    public long nextLong() {
        return Long.parseLong(next());
    }
    public double nextDouble() {
        return Double.parseDouble(next());
    }

}