
import java.io.*;
import java.util.*;

public class E {

    public static long[][] modPow(long[][] x, long pow, int mod) {
        if (pow == 0)
            return new long[][] { { 1, 0 }, { 0, 1 } };
        long[][] temp = modPow(x, pow >> 1, mod);
        temp = modMul(temp, temp, mod);
        if ((pow & 1l) == 1)
            temp = modMul(temp, x, mod);
        return temp;
    }

    public static long[][] modMul(long[][] x, long[][] y, int mod) {
        int n = x.length;
        long[][] z = new long[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                for (int k = 0; k < n; k++)
                    z[i][j] = (z[i][j] + x[i][k] * y[k][j]) % mod;
        return z;
    }

    public static void main(String[] args) {
        InputReader in = new InputReader(System.in);
        int n = in.readInt();
        long x = in.readLong();
        long y = in.readLong();
        int p = in.readInt();
        int[] A = new int[n];
        long currentSum = 0;
        for (int i = 0; i < n; i++) {
            A[i] = in.readInt();
            currentSum = (currentSum + A[i]) % p;
        }
        long currentX = (A[0] + A[n - 1]) % p;
        if (n == 1) {
            System.out.println(currentSum);
            return;
        }
        currentSum -= currentX;
        long[][] m1 = modPow(new long[][] { { 3, 1 }, { 0, 1 } }, x, p);
        long nextSum = ((m1[0][0] * currentSum) % p + (m1[0][1] * currentX) % p)
                % p;
        long[][] m2 = modPow(new long[][] { { 1, 1 }, { 1, 0 } }, x, p);
        long nextX = ((m2[0][0] * A[n - 1]) % p + (m2[0][1] * A[n - 2]) % p)
                % p;
        nextSum += A[n - 1] - nextX;
        nextX += A[0];
        long[][] m3 = modPow(new long[][] { { 3, 1 }, { 0, 1 } }, y, p);
        long ans = ((m3[0][0] * nextSum) % p + (m3[0][1] * nextX) % p) % p;
        System.out.println((ans + nextX) % p);
    }
}

class InputReader {

    private InputStream stream;
    private byte[] buf = new byte[1000];
    private int curChar, numChars;

    public InputReader(InputStream stream) {
        this.stream = stream;
    }

    private int read() {
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

    public int readInt() {
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

    public long readLong() {
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

    public String readString() {
        int c = read();
        while (isSpaceChar(c))
            c = read();
        StringBuffer res = new StringBuffer();
        do {
            res.appendCodePoint(c);
            c = read();
        } while (!isSpaceChar(c));
        return res.toString();
    }

    private boolean isSpaceChar(int c) {
        return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
    }

    private String readLine0() {
        StringBuffer buf = new StringBuffer();
        int c = read();
        while (c != '\n' && c != -1) {
            buf.appendCodePoint(c);
            c = read();
        }
        return buf.toString();
    }

    public String readLine() {
        String s = readLine0();
        while (s.trim().length() == 0)
            s = readLine0();
        return s;
    }

    public String readLine(boolean ignoreEmptyLines) {
        if (ignoreEmptyLines)
            return readLine();
        else
            return readLine0();
    }

    public char readCharacter() {
        int c = read();
        while (isSpaceChar(c))
            c = read();
        return (char) c;
    }

    public double readDouble() {
        int c = read();
        while (isSpaceChar(c))
            c = read();
        int sgn = 1;
        if (c == '-') {
            sgn = -1;
            c = read();
        }
        double res = 0;
        while (!isSpaceChar(c) && c != '.') {
            if (c == 'e' || c == 'E')
                return res * Math.pow(10, readInt());
            if (c < '0' || c > '9')
                throw new InputMismatchException();
            res *= 10;
            res += c - '0';
            c = read();
        }
        if (c == '.') {
            c = read();
            double m = 1;
            while (!isSpaceChar(c)) {
                if (c == 'e' || c == 'E')
                    return res * Math.pow(10, readInt());
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                m /= 10;
                res += (c - '0') * m;
                c = read();
            }
        }
        return res * sgn;
    }
}