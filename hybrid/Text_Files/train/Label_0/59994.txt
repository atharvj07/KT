import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.FileNotFoundException;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        FastScanner in = new FastScanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        BRGBBalls solver = new BRGBBalls();
        solver.solve(1, in, out);
        out.close();
    }

    static class BRGBBalls {
        public void solve(int testNumber, FastScanner in, PrintWriter out) {
            int n = in.nextInt();
            char[] s = in.next().toCharArray();
            int[] count = new int[3];
            long ans = 1;
            long mod = 998244353;
            int open = 0, mid = 0, closed = 0;
            int max = 0, min = 0;
            for (int i = 0; i < s.length; i++) {
                int pos = "RGB".indexOf(s[i]);
                count[pos]++;
                int newMin = Math.min(count[0], Math.min(count[1], count[2]));
                int newMax = Math.max(count[0], Math.max(count[1], count[2]));
                if (newMax > max) {
                    open++;
                } else if (newMin > min) {
                    ans = ans * mid % mod;
                    mid--;
                } else {
                    ans = ans * open % mod;
                    open--;
                    mid++;
                }
                max = newMax;
                min = newMin;
            }
            for (int i = 1; i <= n; i++) {
                ans = ans * i % mod;
            }
            out.println(ans);
        }

    }

    static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        public FastScanner(InputStream in) {
            br = new BufferedReader(new InputStreamReader(in));
        }

        public FastScanner(String fileName) {
            try {
                br = new BufferedReader(new FileReader(fileName));
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public String next() {
            while (st == null || !st.hasMoreElements()) {
                String line = null;
                try {
                    line = br.readLine();
                } catch (IOException e) {
                }
                st = new StringTokenizer(line);
            }
            return st.nextToken();
        }

    }
}

