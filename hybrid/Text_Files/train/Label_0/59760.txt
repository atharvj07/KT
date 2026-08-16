import java.util.*;
import java.io.*;
import java.math.*;
 
public class Main {
    static PrintWriter out;
    static Reader in;
    public static void main(String[] args) throws IOException {
        //out = new PrintWriter(new File("out.txt"));
        //PrintWriter out = new PrintWriter(System.out);
        //in = new Reader(new FileInputStream("in.txt"));
        //Reader in = new Reader();
        input_output();
        Main solver = new Main();
        solver.solve();
        out.flush();
        out.close();
 
    }
 
    static long INF = (long)1e15+5;
    static int maxn = (int)1e5+5;
    static int mod=(int)1e9+7 ;
    static int n, m, q, k, t;

    static ArrayList<Integer> adj[];
    static int[] size, c, d, x;
    static long[][] g, f;

    void solve() throws IOException{
        n = in.nextInt();
        int money = in.nextInt();

        adj = new ArrayList[n+1];
        for (int i = 1; i <= n; i++) adj[i] = new ArrayList<Integer>();

        c = new int[n+1];
        d = new int[n+1];
        x = new int[n+1];

        for (int i = 1; i <= n; i++) {
            c[i] = in.nextInt();
            d[i] = in.nextInt();
            if (i != 1) {
                x[i] = in.nextInt();
                adj[x[i]].add(i);
                adj[i].add(x[i]);
            }
        }

        g = new long[n+1][n+1];
        f = new long[n+1][n+1];

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                g[i][j] = INF;
                f[i][j] = INF;
            }
        }
        size = new int[n+1];
        dfs(1, 0);

        int ans = 0;
        for (int i = 1; i <= n; i++) {
            if (f[1][i] <= money)
                ans = i;
        }

        out.println(ans);
    }  

    //<>

    static void dfs(int s, int p) {
        size[s] = 1;
        boolean leaf = true;

        g[s][1] = c[s];
        f[s][1] = c[s]-d[s];
        int sz = 1;

        for (int e: adj[s]) {
            if (e == p) continue;
            leaf = false;
            dfs(e, s);
            for (int i = sz; i >= 0; i--) {
                for (int j = 1; j <= size[e]; j++) {
                    g[s][i+j] = Math.min(g[s][i+j], g[s][i]+g[e][j]);
                }
            }
            for (int i = sz; i > 0; i--) {
                for (int j = 1; j <= size[e]; j++) {
                    f[s][i+j] = Math.min(f[s][i+j], f[s][i]+f[e][j]);
                }
            }
            sz += size[e];
            size[s] += size[e];
        }
        for (int i = 1; i <= sz; i++) f[s][i] = Math.min(f[s][i], g[s][i]);
    }

    static class Reader {
 
        private InputStream mIs;
        private byte[] buf = new byte[1024];
        private int curChar;
        private int numChars;
    
        public Reader() {
            this(System.in);
        }
    
        public Reader(InputStream is) {
            mIs = is;
        }
    
        public int read() {
            if (numChars == -1) {
                throw new InputMismatchException();
    
        }
            if (curChar >= numChars) {
                curChar = 0;
                try {
                    numChars = mIs.read(buf);
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
                if (numChars <= 0) {
                    return -1;
                }
            }
            return buf[curChar++];
        }
    
        public String nextLine() {
            int c = read();
            while (isSpaceChar(c)) {
                c = read();
            }
            StringBuilder res = new StringBuilder();
            do {
                res.appendCodePoint(c);
                c = read();
            } while (!isEndOfLine(c));
            return res.toString();
        }
    
        public String next() {
            int c = read();
            while (isSpaceChar(c)) {
                c = read();
            }
            StringBuilder res = new StringBuilder();
            do {
                res.appendCodePoint(c);
                c = read();
            } while (!isSpaceChar(c));
            return res.toString();
        }
    
        double nextDouble()
        {
            return Double.parseDouble(next());
        }
    
        public long nextLong() {
            int c = read();
            while (isSpaceChar(c)) {
                c = read();
            }
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            long res = 0;
            do {
                if (c < '0' || c > '9') {
                    throw new InputMismatchException();
                }
                res *= 10;
                res += c - '0';
                c = read();
            } while (!isSpaceChar(c));
            return res * sgn;
        }
    
        public int nextInt() {
            int c = read();
            while (isSpaceChar(c)) {
                c = read();
            }
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            int res = 0;
            do {
                if (c < '0' || c > '9') {
                    throw new InputMismatchException();
                }
                res *= 10;
                res += c - '0';
                c = read();
            } while (!isSpaceChar(c));
            return res * sgn;
        }
    
        public boolean isSpaceChar(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }
    
        public boolean isEndOfLine(int c) {
            return c == '\n' || c == '\r' || c == -1;
        }
 
    }
    static void input_output() throws IOException {
        File f = new File("in.txt");
        if(f.exists() && !f.isDirectory()) { 
            in = new Reader(new FileInputStream("in.txt"));
        } else in = new Reader();
        f = new File("out.txt");
        if(f.exists() && !f.isDirectory()) {
            out = new PrintWriter(new File("out.txt"));
        } else out = new PrintWriter(System.out);
    }
}