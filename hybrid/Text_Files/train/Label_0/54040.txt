import java.io.*;
import java.util.*;
public class Rnd189B {
    BufferedReader br;
    PrintWriter out;
    StringTokenizer st;
    boolean eof;
    void solve() throws IOException {
        int w = nextInt();
        int h = nextInt();
        long res = 0;
        for(int i = 1; i < h; i++)
            for(int j = 1; j < w; j++) {
                int y = Math.min(h - i, i);
                int x = Math.min(w - j, j);
                res = res + x * y;
            }
        out.print(res);
    }
    public Rnd189B() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        out = new PrintWriter(System.out);
        solve();
        out.close();
    }
    public static void main(String[] args) throws IOException {
        new Rnd189B();
    }
    public String nextToken() {
        while (st == null || !st.hasMoreTokens()) {
            try {
                st = new StringTokenizer(br.readLine());
            } catch (Exception e) {
                eof = true;
                return null;
            }
        }
        return st.nextToken();
    }
    public String nextString() {
        try {
            return br.readLine();
        } catch (IOException e) {
            eof = true;
            return null;
        }
    }
    public int nextInt() throws IOException {
        return Integer.parseInt(nextToken());
    }
    public long nextLong() throws IOException {
        return Long.parseLong(nextToken());
    }
    public double nextDouble() throws IOException {
        return Double.parseDouble(nextToken());
    }
}