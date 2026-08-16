
import java.io.OutputStream;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.File;


/**
 * 
 * @author MEGNAD
 *
 */



public class CowProgram {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        JoltyScanner in = new JoltyScanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        ProblemBCowProgram solver = new ProblemBCowProgram();
        solver.solve(1, in, out);
        out.close();
    }

    static class ProblemBCowProgram {
        int n;
        long[] a;
        boolean[] stack2;
        boolean[] stack3;
        long[] memo2;
        long[] memo3;
        long oo = 987654321987654321L;

        long dfs2(int x) {
            if (memo2[x] != oo) return memo2[x];
            stack2[x] = true;
            long newx = x + a[x];
            long ans;
            if (newx > n || newx <= 0) {
                ans = 0;
            } else if (stack3[(int) newx]) {
                ans = -1;
            } else {
                ans = dfs3((int) newx);
            }
            stack2[x] = false;
            return memo2[x] = ans == -1 ? ans : ans + a[x];
        }

        long dfs3(int x) {
            if (memo3[x] != oo) return memo3[x];
            stack3[x] = true;
            long newx = x - a[x];
            long ans;
            if (newx > n || newx <= 0) {
                ans = 0;
            } else if (stack2[(int) newx]) {
                ans = -1;
            } else {
                ans = dfs2((int) newx);
            }
            stack3[x] = false;
            return memo3[x] = ans == -1 ? ans : ans + a[x];
        }

        public void solve(int testNumber, JoltyScanner in, PrintWriter out) {
            n = in.nextInt();
            a = new long[n + 1];
            for (int i = 2; i <= n; ++i) a[i] = in.nextInt();
            stack2 = new boolean[n + 1];
            stack3 = new boolean[n + 1];
            memo2 = new long[n + 1];
            Arrays.fill(memo2, oo);
            memo3 = new long[n + 1];
            Arrays.fill(memo3, oo);
            for (int a1 = 1; a1 <= n - 1; ++a1) {
                int x = 1, y = 0;
                stack2[x] = true;
                long ans = x + a1 > n || x + a1 <= 0 ? y + a1 : dfs3(x + a1);
                if (ans != -1) ans += a1;
                out.println(ans);
            }
        }

    }

    static class JoltyScanner {
        public int BS = 1 << 16;
        public char NC = (char) 0;
        public byte[] buf = new byte[BS];
        public int bId = 0;
        public int size = 0;
        public char c = NC;
        public double num = 1;
        public BufferedInputStream in;

        public JoltyScanner(InputStream is) {
            in = new BufferedInputStream(is, BS);
        }

        public JoltyScanner(String s) throws FileNotFoundException {
            in = new BufferedInputStream(new FileInputStream(new File(s)), BS);
        }

        public char nextChar() {
            while (bId == size) {
                try {
                    size = in.read(buf);
                } catch (Exception e) {
                    return NC;
                }
                if (size == -1) return NC;
                bId = 0;
            }
            return (char) buf[bId++];
        }

        public int nextInt() {
            return (int) nextLong();
        }

        public long nextLong() {
            num = 1;
            boolean neg = false;
            if (c == NC) c = nextChar();
            for (; (c < '0' || c > '9'); c = nextChar()) {
                if (c == '-') neg = true;
            }
            long res = 0;
            for (; c >= '0' && c <= '9'; c = nextChar()) {
                res = (res << 3) + (res << 1) + c - '0';
                num *= 10;
            }
            return neg ? -res : res;
        }

    }
}
