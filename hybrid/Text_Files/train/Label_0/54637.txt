import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Solve6 {

    public static void main(String[] args) throws IOException {
        PrintWriter pw = new PrintWriter(System.out);
        new Solve6().solve(pw);
        pw.flush();
        pw.close();
    }

    public void solve(PrintWriter pw) throws IOException {
        FastReader sc = new FastReader();
        HashMap<Integer, Integer> id = new HashMap();
        HashMap<Integer, Integer> pos = new HashMap();
        int n = sc.nextInt(), m = sc.nextInt(), k = sc.nextInt();
        for (int i = 1; i <= n; i++) {
            int x = sc.nextInt();
            id.put(x, i);
            pos.put(i, x);
        }
        long s = 0;
        for (int i = 0; i < m; i++) {
            int b = sc.nextInt();
            int temp = id.get(b);
            s += (temp - 1) / k + 1;
            if (temp > 1) {
                int y = pos.get(temp - 1);
                id.put(b, temp - 1);
                id.put(y, temp);
                pos.put(temp - 1, b);
                pos.put(temp, y);
            }
        }
        pw.println(s);
    }

    static class FastReader {

        StringTokenizer st;
        BufferedReader br;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        public String next() throws IOException {
            if (st == null || !st.hasMoreTokens()) {
                st = new StringTokenizer(br.readLine());
            }
            return st.nextToken();
        }

        public boolean hasNext() throws IOException {
            if (st != null && st.hasMoreTokens()) {
                return true;
            }
            String s = br.readLine();
            if (s == null || s.isEmpty()) {
                return false;
            }
            st = new StringTokenizer(s);
            return true;
        }

        public int nextInt() throws IOException {
            return Integer.parseInt(next());
        }

        public long nextLong() throws IOException {
            return Long.parseLong(next());
        }

        public double nextDouble() throws IOException {
            return Double.parseDouble(next());
        }

        public String nextLine() throws IOException {
            return br.readLine();
        }
    }
}
