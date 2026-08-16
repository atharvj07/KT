
import java.io.*;
import java.util.*;

public class NewClass {

    static final int INF = Integer.MAX_VALUE;

    static void mergeSort(int[] a, int p, int r) {
        if (p < r) {
            int q = (p + r) / 2;
            mergeSort(a, p, q);
            mergeSort(a, q + 1, r);
            merge(a, p, q, r);
        }
    }

    static void merge(int[] a, int p, int q, int r) {
        int n1 = q - p + 1;
        int n2 = r - q;
        int[] L = new int[n1 + 1], R = new int[n2 + 1];

        for (int i = 0; i < n1; i++) {
            L[i] = a[p + i];
        }
        for (int i = 0; i < n2; i++) {
            R[i] = a[q + 1 + i];
        }
        L[n1] = R[n2] = INF;

        for (int k = p, i = 0, j = 0; k <= r; k++) {
            if (L[i] <= R[j]) {
                a[k] = L[i++];
            } else {
                a[k] = R[j++];
            }
        }
    }

    public static boolean sieve(int n) {
        int a[] = new int[n + 1];
        for (int i = 2; i <= n; i++) {
            a[i] = 1;
        }
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (a[i] == 1) {
                for (int k = 2; i * k <= n; k++) {
                    a[i * k] = 0;
                }
            }
        }
        return a[n] == 1;
    }

    public static long sum(int a) {
        long su = 0;
        while (a > 0) {
            su += a % 10;
            a /= 10;
        }
        return su;
    }

    public static int divi(int b) {
        int n = 0;
        for (int i = 2; i <= Math.sqrt(b); i++) {
            if (b % i == 0) {
                n = i;
                break;
            }
        }
        if (n == 0) {
            return b;
        }
        return n;
    }

    public static boolean prime(int n) {

        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static String reve(int a, int b, String s) {
        String q = "";
        for (int i = b; i >= a; i--) {
            q += s.charAt(i);
        }
        return q;
    }

    public static boolean isvowel(char c) {
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'y') {
            return true;
        } else {
            return false;
        }
    }

    static long gcd(long a, long b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    public static int hole(int n) {
        int y = 0;
        if (n == 1) {
            return 0;
        }
        if (prime(n)) {
            return 1;
        }
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                if (prime(i)) {
                    y++;
                }
                if (prime(n / i) && i != (n / i)) {
                    y++;
                }
            }
        }
        return y;
    }

    public static void main(String[] args) throws IOException {
        InputReader in = new InputReader(System.in);
        OutputWriter or = new OutputWriter(System.out);
      int n = in.nextInt();
      int k=in.nextInt()-1;
     long [] a= new long[n];
     long [] f= new long[n];
        for (int i = 0,p=1; i < n; i++){
            a[i]=in.nextLong();
            
        }
        int i=1;
        while(k-i>=0){
      k-=i; i++;
    }
       or.print(a[k]);
        or.flush();
    }
}
    class InputReader {

        private final InputStream stream;
        private final byte[] buf = new byte[8192];
        private int curChar, snumChars;

        public InputReader(InputStream stream) {
            this.stream = stream;
        }

        public int read() {
            if (snumChars == -1) {
                throw new InputMismatchException();
            }
            if (curChar >= snumChars) {
                curChar = 0;
                try {
                    snumChars = stream.read(buf);
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
                if (snumChars <= 0) {
                    return -1;
                }
            }
            return buf[curChar++];
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
                res *= 10;
                res += c - '0';
                c = read();
            } while (!isSpaceChar(c));
            return res * sgn;
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
                res *= 10;
                res += c - '0';
                c = read();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        public int[] nextIntArray(int n) {
            int a[] = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = nextInt();
            }
            return a;
        }

        public String readString() {
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

        public boolean isSpaceChar(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        private boolean isEndOfLine(int c) {
            return c == '\n' || c == '\r' || c == -1;
        }

    }

    class OutputWriter {

        private final PrintWriter writer;

        public OutputWriter(OutputStream outputStream) {
            writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(outputStream)));
        }

        public OutputWriter(Writer writer) {
            this.writer = new PrintWriter(writer);
        }

        public void print(Object... objects) {
            for (int i = 0; i < objects.length; i++) {
                if (i != 0) {
                    writer.print(' ');
                }
                writer.print(objects[i]);
            }
        }

        public void printLine(Object... objects) {
            print(objects);
            writer.println();
        }

        public void close() {
            writer.close();
        }

        public void flush() {
            writer.flush();
        }

    }
