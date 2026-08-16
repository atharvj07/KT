// package codeforces.cr340.div2;

import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Comparator;
import java.util.InputMismatchException;

/**
 * Created by hama_du on 2016/02/16.
 */
public class Main {
    public static void main(String[] args) {
        InputReader in = new InputReader(System.in);
        PrintWriter out = new PrintWriter(System.out);

        int n = in.nextInt();
        int m = in.nextInt();
        int k = in.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n ; i++) {
            a[i] = in.nextInt();
        }
        int[][] lr = new int[m][2];
        for (int i = 0; i < m ; i++) {
            lr[i][0] = in.nextInt()-1;
            lr[i][1] = in.nextInt();
        }

        long[] mo = new long[m]; // sqrtSort(lr, 100000);
        for (int i = 0; i < m ; i++) {
            mo[i] |= ((long)lr[i][0]/320L)<<50;
            mo[i] |= (((lr[i][0]/320L)&1) == 0 ? (long)lr[i][1] : (long)(1<<25)-1-lr[i][1])<<25;
            mo[i] |= i;
        }

        // (long)q[i][0]/S<<50|(long)((q[i][0]/S&1)==0?q[i][1]:(1<<25)-1-q[i][1])<<25|i;
        Arrays.sort(mo);

        int[] imos = new int[n+1];
        for (int i = 0; i < n ; i++) {
            imos[i+1] = imos[i] ^ a[i];
        }

        long[] ans = new long[m];
        int L = 0;
        int R = 0;
        long[] table = new long[4000000];
        table[0] = 1;
        long val = 0;
        for (int qi = 0 ; qi < m ; qi++) {
            int i = (int)(mo[qi] & ((1<<25) - 1));
            int toL = lr[i][0];
            int toR = lr[i][1];
            while (toR > R) {
                val += table[k ^ imos[R+1]];
                table[imos[R+1]]++;
                R++;
            }
            while (toL < L) {
                val += table[k ^ imos[L-1]];
                table[imos[L-1]]++;
                L--;
            }
            while (toR < R) {
                R--;
                table[imos[R+1]]--;
                val -= table[k ^ imos[R+1]];
            }
            while (toL > L) {
                L++;
                table[imos[L-1]]--;
                val -= table[k ^ imos[L-1]];
            }
            ans[i] = val;
        }

        for (int i = 0 ; i < m ; i++) {
            out.println(ans[i]);
        }
        out.flush();
    }

    public static long[] sqrtSort(int[][] q, int n)
    {
        int m = q.length;
        long[] pack = new long[m];
        int S = (int)Math.sqrt(n);
        for(int i = 0;i < m;i++){
            pack[i] = (long)q[i][0]/S<<50|(long)((q[i][0]/S&1)==0?q[i][1]:(1<<25)-1-q[i][1])<<25|i;
        }
        Arrays.sort(pack);
        return pack;
    }


    static class InputReader {
        private InputStream stream;
        private byte[] buf = new byte[1024];
        private int curChar;
        private int numChars;

        public InputReader(InputStream stream) {
            this.stream = stream;
        }

        private int next() {
            if (numChars == -1)
                throw new InputMismatchException();
            if (curChar >= numChars) {
                curChar = 0;
                try {
                    numChars = stream.read(buf);
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
                if (numChars <= 0)
                    return -1;
            }
            return buf[curChar++];
        }

        public char nextChar() {
            int c = next();
            while (isSpaceChar(c))
                c = next();
            if ('a' <= c && c <= 'z') {
                return (char) c;
            }
            if ('A' <= c && c <= 'Z') {
                return (char) c;
            }
            throw new InputMismatchException();
        }

        public String nextToken() {
            int c = next();
            while (isSpaceChar(c))
                c = next();
            StringBuilder res = new StringBuilder();
            do {
                res.append((char) c);
                c = next();
            } while (!isSpaceChar(c));
            return res.toString();
        }

        public int nextInt() {
            int c = next();
            while (isSpaceChar(c))
                c = next();
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = next();
            }
            int res = 0;
            do {
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                res *= 10;
                res += c-'0';
                c = next();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        public long nextLong() {
            int c = next();
            while (isSpaceChar(c))
                c = next();
            long sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = next();
            }
            long res = 0;
            do {
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                res *= 10;
                res += c-'0';
                c = next();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        public boolean isSpaceChar(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        public interface SpaceCharFilter {
            public boolean isSpaceChar(int ch);
        }
    }

    static void debug(Object... o) {
        System.err.println(Arrays.deepToString(o));
    }
}
