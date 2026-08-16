import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        Main main = new Main();
        main.solve();
    }
    public void solve() throws Exception {
        FastScan scan = new FastScan(System.in);
        int H = scan.scanInt();
        int W = scan.scanInt();
        int D = scan.scanInt();
        HashMap<Integer, Point> map = new HashMap<>();
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                int A = scan.scanInt();
                map.put(A, new Point(i, j));
            }
        }
        int[] s = new int[H*W+1];
        for (int i = 1; i <= H * W - D; i++) {
            Point p1 = map.get(i);
            Point p2 = map.get(i+D);
            s[i+D] = s[i]
                    + Math.abs(p1.i-p2.i)
                    + Math.abs(p1.j-p2.j);
        }
        int Q = scan.scanInt();
        for (int i = 0; i < Q; i++) {
            int L = scan.scanInt();
            int R = scan.scanInt();
            System.out.println(s[R]-s[L]);
        }
    }
    static class Point {
        int i;
        int j;
        Point(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }
    static class FastScan {
        BufferedReader br;
        StringTokenizer st;
        FastScan(InputStream is) {
            InputStreamReader isr = new InputStreamReader(is);
            this.br = new BufferedReader(isr);
        }
        String next() throws IOException {
            while (this.st == null || !this.st.hasMoreTokens()) {
                this.st = new StringTokenizer(br.readLine().trim());
            }
            return st.nextToken();
        }
        long scanLong() throws IOException {
            return Long.parseLong(this.next());
        }
        int scanInt() throws IOException {
            return Integer.parseInt(this.next());
        }
        double scanDouble() throws IOException {
            return Double.parseDouble(this.next());
        }
        char scanCharacter() throws IOException {
            return this.next().charAt(0);
        }
        String nextLine() throws IOException {
            return br.readLine().trim();
        }
    }
}
