/**
 * Created by Baelish on 1/29/2018.
 */

import java.io.*;
import java.util.*;

public class D {
    public static void main(String[] args) throws Exception {
        new Thread(null ,new Runnable(){
            public void run(){try{solveIt();} catch(Exception e){e.printStackTrace();}}
        },"Main",1<<28).start();
    }

    public static void solveIt() throws Exception {
        FastReader in = new FastReader(System.in);
        PrintWriter pw = new PrintWriter(System.out);
        n = in.nextInt(); int m = in.nextInt();
        for(int i = 0; i <= n; i++) Arrays.fill(g[i], -1);
        for(int i = 0; i < m; i++){
            int u = in.nextInt(), v = in.nextInt(), c = in.nextChar()-'a';
            g[u][v] = c;
        }
        for(int a[][][] : dp){
            for(int b[][] : a){
                for(int c[] : b) Arrays.fill(c, -1);
            }
        }

        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= n; j++){
                int res = solve(i, j, 1, 0);
                if(res == 1) pw.print("A");
                else pw.print("B");
                //debug(i, j, res);
            }
            pw.println();
        }

        pw.close();
    }

    static int dp[][][][] = new int[101][101][2][26], g[][] = new int[101][101], n;

    static int solve(int a, int b, int who, int last){
        if(dp[a][b][who][last] != -1) return dp[a][b][who][last];
        int res = 0;

        if(who == 1){
            for(int i = 1; i <= n; i++){
                if(g[a][i] >= last) res = Math.max(res, 1^solve(i, b, who^1, g[a][i]));
            }
        }
        else{
            for(int i = 1; i <= n; i++){
                if(g[b][i] >= last) res = Math.max(res, 1^solve(a, i, who^1, g[b][i]));
            }
        }

        return dp[a][b][who][last] = res;
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
        public char nextChar() {
            return (char)skip();
        }

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