import java.util.*;
import java.io.*;

class Main {

    Scanner in;
    InputStream is;
    PrintWriter out;
    String INPUT = "";
//----------------------------------------------------------------------------------------------------//
   int INF = Integer.MAX_VALUE;
    int m = (int) (1e9) + 7;
    long power(long x, long y) { //log(y)
        if (y == 0) {
            return 1;
        }
        long p = power(x, y / 2) % m;
        p = (p * p) % m;
        return ((y % 2 == 0) ? p : (x * p) % m);
    }
    void solve1() {
        int t = 1;
        //t = ni();
        while (t-- > 0) {
            int n=ni();
            long ans=(power(10, n)-(2L*power(9, n)-power(8, n))+m)%m;
            out.println(ans);
        }
    }
    void solve() {
        int t = 1;
        //t = ni();
        while (t-- > 0) {
            int n=ni();
            long dp[]=new long[n+1];
            dp[0]=1;
            for (int i = 1; i <=n; i++) {
                for (int j = 3; j <=n; j++) {
                    if(i-j>=0){
                        dp[i]=(dp[i-j]+dp[i])%m;
                    }
                }
            }
            out.println(dp[n]);
        }
    }
//----------------------------------------------------------------------------------------------------//

    void run() throws Exception {
        //File fileIN = new File("C:\\Users\\Sarthak\\Desktop\\input.txt");is = new FileInputStream(fileIN);
        //File fileOUT = new File("C:\\Users\\Sarthak\\Desktop\\output.txt");out = new PrintWriter(fileOUT);;
        is = System.in;
        out = new PrintWriter(System.out);

        //long s = System.currentTimeMillis();
        solve();
        out.flush();
        //tr(System.currentTimeMillis() - s + "ms");
    }

    public static void main(String[] args) throws Exception {
        new Main().run();
    }

    private byte[] inbuf = new byte[1024];
    public int lenbuf = 0, ptrbuf = 0;

    private int readByte() {
        if (lenbuf == -1) {
            throw new InputMismatchException();
        }
        if (ptrbuf >= lenbuf) {
            ptrbuf = 0;
            try {
                lenbuf = is.read(inbuf);
            } catch (IOException e) {
                throw new InputMismatchException();
            }
            if (lenbuf <= 0) {
                return -1;
            }
        }
        return inbuf[ptrbuf++];
    }

    private boolean isSpaceChar(int c) {
        return !(c >= 33 && c <= 126);
    }

    private int skip() {
        int b;
        while ((b = readByte()) != -1 && isSpaceChar(b));
        return b;
    }

    private double nd() {
        return Double.parseDouble(ns());
    }

    private char nc() {
        return (char) skip();
    }

    private String ns() {
        int b = skip();
        StringBuilder sb = new StringBuilder();
        while (!(isSpaceChar(b))) {  // when nextLine(take whole line as input wid space), (!isSpaceChar(b) || b == ' ') 
            //if(b!=' ') to remove spaces in Str when taking spaces in Str
            sb.appendCodePoint(b);
            b = readByte();
        }
        return sb.toString();
    }

    private char[] ns(int n) {
        char[] buf = new char[n];
        int b = skip(), p = 0;
        while (p < n && !(isSpaceChar(b))) {
            buf[p++] = (char) b;
            b = readByte();
        }
        return n == p ? buf : Arrays.copyOf(buf, p);
    }

    private char[][] nm(int n, int m) {
        char[][] map = new char[n][];
        for (int i = 0; i < n; i++) {
            map[i] = ns(m);
        }
        return map;
    }

    private int[] na(int n) {
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = ni();
        }
        return a;
    }

    private int ni() {
        int num = 0, b;
        boolean minus = false;
        while ((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-'));
        if (b == '-') {
            minus = true;
            b = readByte();
        }

        while (true) {
            if (b >= '0' && b <= '9') {
                num = num * 10 + (b - '0');
            } else {
                return minus ? -num : num;
            }
            b = readByte();
        }
    }

    private long nl() {
        long num = 0;
        int b;
        boolean minus = false;
        while ((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-'));
        if (b == '-') {
            minus = true;
            b = readByte();
        }

        while (true) {
            if (b >= '0' && b <= '9') {
                num = num * 10 + (b - '0');
            } else {
                return minus ? -num : num;
            }
            b = readByte();
        }
    }
}
