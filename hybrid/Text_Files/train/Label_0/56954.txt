// Change Of Plans BABY.... Change Of Plans //
import java.io.*;
import java.util.*;
import static java.lang.Math.*;

public class Tree01 {

    static ArrayList<Integer> one[];
    static ArrayList<Integer> zero[];
    static int dsu[];
    static int vis[];
    static ArrayList<Long> sizes = new ArrayList<>();
    static ArrayList<Integer> which_forest =new ArrayList<>();
    static long size = 0;

    static void MainSolution() {
        n = ni();
        one = new ArrayList[n + 1];
        zero = new ArrayList[n + 1];
        dsu = new int[n + 1];
        vis = new int[n + 1];
        for (int i = 0; i < n + 1; i++) {
            one[i] = new ArrayList<>();
            zero[i] = new ArrayList<>();
        }

        for (int i = 1; i < n; i++) {
            int x = ni(), y = ni(), z = ni();
            if (z == 0) {
                zero[x].add(y);
                zero[y].add(x);
            } else {
                one[x].add(y);
                one[y].add(x);
            }
        }
        int c = 1;
        long ans = 0;
        for (int i = 1; i <= n; i++) {
            if (vis[i] != 1 && one[i].size() != 0) {
                dfsone(i, c);
                sizes.add(size);
                ans += ((size) * (size - 1));
                c++;
                size = 0;
            }
        }
        vis = new int[n + 1];
//        for (int i : dsu) p(i);
//        pl(sizes);
//        pl();
        for (int i = 1; i <= n; i++) {
            if (vis[i] != 1 && zero[i].size() != 0) {
                dfszero(i);
                ans += ((size) * (size - 1));
                if(sizes.size()!=0) {
                    for(int x:which_forest)
                    ans += (size - 1) * (sizes.get(x - 1) - 1);
                    which_forest = new ArrayList<>();
                }
                size = 0;
            }
        }

        pl(ans);
    }

    static void dfsone(int node, int c) {
        if (vis[node] == 1) return;
        dsu[node] = c;
        size++;
        vis[node] = 1;
        for (int i : one[node]) {
            dfsone(i, c);
        }
    }

    static void dfszero(int node) {
        if (vis[node] == 1) return;
        if (dsu[node] != 0) which_forest .add(dsu[node]);
        size++;
        vis[node] = 1;
        for (int i : zero[node]) dfszero(i);
    }

    /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //THE DON'T CARE ZONE BEGINS HERE...//
    static int mod9 = 1000000007;
    static int n, m, l, k, t, mod = 998244353;
    static AwesomeInput input = new AwesomeInput(System.in);
    static PrintWriter pw = new PrintWriter(System.out, true);

    static class AwesomeInput {
        private InputStream letsDoIT;
        private byte[] buf = new byte[1024];
        private int curChar;
        private int numChars;
        private SpaceCharFilter filter;

        private AwesomeInput(InputStream ayega) {
            this.letsDoIT = ayega;
        }

        public int read() {
            if (numChars == -1)
                throw new InputMismatchException();
            if (curChar >= numChars) {
                curChar = 0;
                try {
                    numChars = letsDoIT.read(buf);
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
                if (numChars <= 0)
                    return -1;
            }
            return buf[curChar++];
        }

        public int ForInteger() {
            int c = read();
            while (isSpaceChar(c))
                c = read();
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            int res = 0;
            do {
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                res *= 10;
                res += c - '0';
                c = read();
            }
            while (!isSpaceChar(c));
            return res * sgn;
        }

        public long ForLong() {
            int c = read();
            while (isSpaceChar(c))
                c = read();
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            long res = 0;
            do {
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                res *= 10;
                res += c - '0';
                c = read();
            }
            while (!isSpaceChar(c));
            return res * sgn;
        }

        public String ForString() {
            int c = read();
            while (isSpaceChar(c))
                c = read();
            StringBuilder res = new StringBuilder();
            do {
                res.appendCodePoint(c);
                c = read();
            }
            while (!isSpaceChar(c));

            return res.toString();
        }

        public boolean isSpaceChar(int c) {
            if (filter != null)
                return filter.isSpaceChar(c);
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        public interface SpaceCharFilter {
            boolean isSpaceChar(int ch);
        }
    }

    // functions to take input//
    static int ni() {
        return input.ForInteger();
    }

    static String ns() {
        return input.ForString();
    }

    static long nl() {
        return input.ForLong();
    }

    static double nd() throws IOException {
        return Double.parseDouble(new BufferedReader(new InputStreamReader(System.in)).readLine());
    }

    //functions to give output
    static void pl() {
        pw.println();
    }

    static void p(Object o) {
        pw.print(o + " ");
    }

    static void pws(Object o) {
        pw.print(o + "");
    }

    static void pl(Object o) {
        pw.println(o);
    }

    static void flush() {
        pw.flush();
        pw.close();
    }

    public static int[] fastSort(int[] f) {
        int n = f.length;
        int[] to = new int[n];
        {
            int[] b = new int[65537];
            for (int i = 0; i < n; i++) b[1 + (f[i] & 0xffff)]++;
            for (int i = 1; i <= 65536; i++) b[i] += b[i - 1];
            for (int i = 0; i < n; i++) to[b[f[i] & 0xffff]++] = f[i];
            int[] d = f;
            f = to;
            to = d;
        }
        {
            int[] b = new int[65537];
            for (int i = 0; i < n; i++) b[1 + (f[i] >>> 16)]++;
            for (int i = 1; i <= 65536; i++) b[i] += b[i - 1];
            for (int i = 0; i < n; i++) to[b[f[i] >>> 16]++] = f[i];
            int[] d = f;
            f = to;
            to = d;
        }
        return f;
    }

    public static void main(String[] args) {      //threading has been used to increase the stack size.

        new Thread(null, null, "DHAGA", 1 << 25)  //the last parameter is stack size desired.
        {
            public void run() {
                try {
                    double s = System.currentTimeMillis();
                    MainSolution();
                    //pl(("\nExecution Time : " + ((double) System.currentTimeMillis() - s) / 1000) + " s");
                    flush();
                } catch (Exception e) {
                    e.printStackTrace();
                    System.exit(1);
                }
            }
        }.start();
    }
}