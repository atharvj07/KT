import java.io.*;
import java.util.*;

public class Main {
    FasterScanner sc = new FasterScanner();
    PrintWriter pw = new PrintWriter(System.out);
    static int MOD = 1000000007;

    public static void main(String[] args) {
        Main m = new Main();
        m.solve();
        m.done();
    }

    public void solve() {
        int t = sc.nextInt();
        for (int tt = 0; tt < t; tt++) {
            String s = sc.nextLine();
            char[] C = s.toCharArray();
            if (check(C, 0, C.length - 1)) {
                pw.println(s);
                continue;
            }
            int L = 0;
            int R = C.length - 1;
            while (L < R) { // find where they differ
                if (C[L] != C[R]) break;
                L++;
                R--;
            }
            if (L == 0) { // only prefix or suffix
                int prefixLen = 1;
                int suffixLen = 1;
                for (int i = 1; i < C.length; i++) if (check(C, 0, i)) prefixLen = i+1;
                for (int i = C.length - 2; i >= 0; i--) if (check(C, i, C.length-1)) suffixLen = C.length-i;
                if (prefixLen >= suffixLen) pw.println(s.substring(0, prefixLen));
                else pw.println(s.substring(C.length-suffixLen));
            } else { // concatenation of prefix and suffix
                int prefixLen = 1;
                int suffixLen = 1;
                for (int i = L+1; i <= R; i++) if (check(C, L, i)) prefixLen = i+1-L; // prefix
                for (int i = R-1; i >= L; i--) if (check(C, i, R)) suffixLen = R-i+1; // suffix
                if (prefixLen >= suffixLen) pw.println(s.substring(0, L+prefixLen) + s.substring(R+1));
                else pw.println(s.substring(0, L) + s.substring(R-suffixLen+1));
            }
        }
    }

    public boolean check(char[] C, int L, int R) {
        while (L < R) if (C[L++] != C[R--]) return false;
        return true;
    }

    public void done() {
        pw.flush();
        pw.close();
    }
}

class FasterScanner {
    private byte[] buf = new byte[1024];
    private int curChar;
    private int numChars;

    public int read() {
        if (numChars == -1)
            throw new InputMismatchException();
        if (curChar >= numChars) {
            curChar = 0;
            try {
                numChars = System.in.read(buf);
            } catch (IOException e) {
                throw new InputMismatchException();
            }
            if (numChars <= 0)
                return -1;
        }
        return buf[curChar++];
    }

    public String nextLine() {
        int c = read();
        while (isSpaceChar(c))
            c = read();
        StringBuilder res = new StringBuilder();
        do {
            res.appendCodePoint(c);
            c = read();
        } while (!isEndOfLine(c));
        return res.toString();
    }

    public String nextString() {
        int c = read();
        while (isSpaceChar(c))
            c = read();
        StringBuilder res = new StringBuilder();
        do {
            res.appendCodePoint(c);
            c = read();
        } while (!isSpaceChar(c));
        return res.toString();
    }

    public long nextLong() {
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
        } while (!isSpaceChar(c));
        return res * sgn;
    }

    public int nextInt() {
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
        } while (!isSpaceChar(c));
        return res * sgn;
    }
        
    public int[] nextIntArray(int n) {
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = nextInt();
        }
        return arr;
    }
    
    public long[] nextLongArray(int n) {
        long[] arr = new long[n];
        for (int i = 0; i < n; i++) {
            arr[i] = nextLong();
        }
        return arr;
    }

    private boolean isSpaceChar(int c) {
        return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
    }

    private boolean isEndOfLine(int c) {
        return c == '\n' || c == '\r' || c == -1;
    }
}