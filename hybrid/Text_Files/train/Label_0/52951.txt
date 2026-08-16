import java.io.*;
import java.lang.reflect.Array;
import java.math.BigInteger;
import java.util.*;
import java.util.concurrent.atomic.AtomicIntegerArray;

public class Solution {

    public static void main(String[] args) throws Exception {
        MyReader reader = new MyReader(System.in);
//        MyReader reader = new MyReader(new FileInputStream("input.txt"));
        MyWriter writer = new MyWriter(System.out);
        new Solution().run(reader, writer);
        writer.close();
    }

    private void run(MyReader reader, MyWriter writer) throws Exception {
        char[] c = reader.nextCharArray();
        int n = c.length;
        int[] x = new int[n];
        for (int i = 0; i < n; i++) {
            x[i] = c[i] - '0';
        }
        long mod = 1_000_000_007;
        long[] p = new long[n + 1];
        long[] s = new long[n + 1];
        p[0] = 1;
        for (int i = 1; i <= n; i++) {
            p[i] = p[i - 1] * 10 % mod;
        }
        s[n] = 1;
        for (int i = n - 1; i >= 0; i--) {
            s[i] = (p[n - i - 1] * x[i] + s[i + 1]) % mod;
        }
        long[][][] d = new long[n + 1][n + 1][2];
        long ans = 0;
        for (int i = 1; i < 10; i++) {
            for (long[][] q : d) {
                for (long[] w : q) {
                    Arrays.fill(w, 0);
                }
            }
            for (int j = 0; j <= n; j++) {
                d[j][0][0] = s[j];
                d[j][0][1] = p[n - j];
            }
            for (int j = n - 1; j >= 0; j--) {
                for (int k = 1; k <= n; k++) {
                    for (int l = 1; l >= 0; l--) {
                        int lim = l == 1 ? 10 : x[j] + 1;
                        for (int m = 0; m < lim; m++) {
                            d[j][k][l] += d[j + 1][k - (m >= i ? 1 : 0)][l == 1 || m < x[j] ? 1 : 0];
                            d[j][k][l] %= mod;
                        }
                    }
                    if (j == 0) {
                        ans = (ans + p[k - 1] * d[0][k][0]) % mod;
                    }
                }
            }
        }
        System.out.println(ans);
    }

    static class MyReader {

        final BufferedInputStream in;
        final int bufSize = 1 << 16;
        final byte buf[] = new byte[bufSize];
        int i = bufSize;
        int k = bufSize;
        boolean end = false;
        final StringBuilder str = new StringBuilder();

        MyReader(InputStream in) {
            this.in = new BufferedInputStream(in, bufSize);
        }

        int nextInt() throws IOException {
            return (int) nextLong();
        }

        int[] nextIntArray(int n) throws IOException {
            int[] m = new int[n];
            for (int i = 0; i < n; i++) {
                m[i] = nextInt();
            }
            return m;
        }

        int[][] nextIntMatrix(int n, int m) throws IOException {
            int[][] a = new int[n][0];
            for (int j = 0; j < n; j++) {
                a[j] = nextIntArray(m);
            }
            return a;
        }

        long nextLong() throws IOException {
            int c;
            long x = 0;
            boolean sign = true;
            while ((c = nextChar()) <= 32) ;
            if (c == '-') {
                sign = false;
                c = nextChar();
            }
            if (c == '+') {
                c = nextChar();
            }
            while (c >= '0') {
                x = x * 10 + (c - '0');
                c = nextChar();
            }
            return sign ? x : -x;
        }

        long[] nextLongArray(int n) throws IOException {
            long[] m = new long[n];
            for (int i = 0; i < n; i++) {
                m[i] = nextLong();
            }
            return m;
        }

        int nextChar() throws IOException {
            if (i == k) {
                k = in.read(buf, 0, bufSize);
                i = 0;
            }
            return i >= k ? -1 : buf[i++];
        }

        String nextString() throws IOException {
            if (end) {
                return null;
            }
            str.setLength(0);
            int c;
            while ((c = nextChar()) <= 32 && c != -1) ;
            if (c == -1) {
                end = true;
                return null;
            }
            while (c > 32) {
                str.append((char) c);
                c = nextChar();
            }
            return str.toString();
        }

        String nextLine() throws IOException {
            if (end) {
                return null;
            }
            str.setLength(0);
            int c = nextChar();
            while (c != '\n' && c != '\r' && c != -1) {
                str.append((char) c);
                c = nextChar();
            }
            if (c == -1) {
                end = true;
                if (str.length() == 0) {
                    return null;
                }
            }
            if (c == '\r') {
                nextChar();
            }
            return str.toString();
        }

        char[] nextCharArray() throws IOException {
            return nextString().toCharArray();
        }

        char[][] nextCharMatrix(int n) throws IOException {
            char[][] a = new char[n][0];
            for (int i = 0; i < n; i++) {
                a[i] = nextCharArray();
            }
            return a;
        }
    }

    static class MyWriter {

        final BufferedOutputStream out;
        final int bufSize = 1 << 16;
        final byte buf[] = new byte[bufSize];
        int i = 0;
        final byte c[] = new byte[30];
        static final String newLine = System.getProperty("line.separator");

        MyWriter(OutputStream out) {
            this.out = new BufferedOutputStream(out, bufSize);
        }

        void print(long x) throws IOException {
            int j = 0;
            if (i + 30 >= bufSize) {
                flush();
            }
            if (x < 0) {
                buf[i++] = (byte) ('-');
                x = -x;
            }
            while (j == 0 || x != 0) {
                c[j++] = (byte) (x % 10 + '0');
                x /= 10;
            }
            while (j-- > 0)
                buf[i++] = c[j];
        }

        void print(int[] m) throws IOException {
            for (int a : m) {
                print(a);
                print(' ');
            }
        }

        void print(long[] m) throws IOException {
            for (long a : m) {
                print(a);
                print(' ');
            }
        }

        void print(String s) throws IOException {
            for (int i = 0; i < s.length(); i++) {
                print(s.charAt(i));
            }
        }

        void print(char x) throws IOException {
            if (i == bufSize) {
                flush();
            }
            buf[i++] = (byte) x;
        }

        void print(char[] m) throws IOException {
            for (char c : m) {
                print(c);
            }
        }

        void println(String s) throws IOException {
            print(s);
            println();
        }

        void println() throws IOException {
            print(newLine);
        }

        void flush() throws IOException {
            out.write(buf, 0, i);
            out.flush();
            i = 0;
        }

        void close() throws IOException {
            flush();
            out.close();
        }
    }
}