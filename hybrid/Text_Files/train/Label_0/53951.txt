/**
 * Created by Baelish on 2/15/2018.
 */

import java.io.*;
import java.util.*;

public class B {
    public static void main(String[] args) throws Exception {
        FastReader in = new FastReader(System.in);
        PrintWriter pw = new PrintWriter(System.out);

        g = new int[(int)1e6+50]; Arrays.fill(g, -1);
        f = new int[(int)1e6+50];

        for(int i = 1; i <= (int)1e6+10; i++){
            f[i] = digMul(i);
        }

        int dp[][] = new int[10][(int)1e6+50];

        for(int i = 1; i <= (int)1e6+10; i++){
            g[i] = g(i);
            if(g[i] >= 1 && g[i] <= 9) dp[g[i]][i] = 1;
        }

        for(int i = 1; i <= 9; i++){
            for(int j = 1; j <= (int)1e6+5; j++){
                dp[i][j] += dp[i][j-1];
            }
        }


        int q = in.nextInt();
        for(int i = 0; i < q; i++){
            int l = in.nextInt(), r = in.nextInt(), k = in.nextInt();
            pw.println(dp[k][r] - dp[k][l-1]);
        }




        pw.close();
    }

    static int g[];
    static int g(int n){
        if(n < 10) return n;
        if(g[n] != -1) return g[n];
        return g[n] = g(f[n]);
    }

    static int f[];
    static int digMul(int x){
        int m = 1;
        while (x > 0){
            int d = x % 10;
            if(d != 0) m *= d;
            x /= 10;
        }
        return m;
    }


    static void debug(Object... obj) {
        System.err.println(Arrays.deepToString(obj));
    }

    static class FastReader {
        InputStream is;
        private byte[] inbuf = new byte[1024];
        private int lenbuf = 0, ptrbuf = 0;
        static final int ints[] = new int[128];

        public FastReader(InputStream is) {
            for (int i = '0'; i <= '9'; i++) ints[i] = i - '0';
            this.is = is;
        }

        public int readByte() {
            if (lenbuf == -1) throw new InputMismatchException();
            if (ptrbuf >= lenbuf) {
                ptrbuf = 0;
                try {
                    lenbuf = is.read(inbuf);
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
                if (lenbuf <= 0) return -1;
            }
            return inbuf[ptrbuf++];
        }

        public boolean isSpaceChar(int c) {
            return !(c >= 33 && c <= 126);
        }

        public int skip() {
            int b;
            while ((b = readByte()) != -1 && isSpaceChar(b)) ;
            return b;
        }

        public String next() {
            int b = skip();
            StringBuilder sb = new StringBuilder();
            while (!(isSpaceChar(b))) { // when nextLine, (isSpaceChar(b) && b != ' ')
                sb.appendCodePoint(b);
                b = readByte();
            }
            return sb.toString();
        }

        public int nextInt() {
            int num = 0, b;
            boolean minus = false;
            while ((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-')) ;
            if (b == '-') {
                minus = true;
                b = readByte();
            }

            while (true) {
                if (b >= '0' && b <= '9') {
                    num = (num << 3) + (num << 1) + ints[b];
                } else {
                    return minus ? -num : num;
                }
                b = readByte();
            }
        }

        public long nextLong() {
            long num = 0;
            int b;
            boolean minus = false;
            while ((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-')) ;
            if (b == '-') {
                minus = true;
                b = readByte();
            }

            while (true) {
                if (b >= '0' && b <= '9') {
                    num = (num << 3) + (num << 1) + ints[b];
                } else {
                    return minus ? -num : num;
                }
                b = readByte();
            }
        }

        public double nextDouble() {
            return Double.parseDouble(next());
        }
       /* public char nextChar() {
            return (char)skip();
        }*/

        public char[] next(int n) {
            char[] buf = new char[n];
            int b = skip(), p = 0;
            while (p < n && !(isSpaceChar(b))) {
                buf[p++] = (char) b;
                b = readByte();
            }
            return n == p ? buf : Arrays.copyOf(buf, p);
        }

        /*private char buff[] = new char[1005];
        public char[] nextCharArray(){
            int b = skip(), p = 0;
            while(!(isSpaceChar(b))){
                buff[p++] = (char)b;
                b = readByte();
            }
            return Arrays.copyOf(buff, p);
        }*/
    }
}