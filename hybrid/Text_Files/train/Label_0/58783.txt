/**
 * author: derrick20
 * created: 1/25/21 12:29 AM
 */
import java.io.*;
import java.util.*;
import static java.lang.Math.*;

public class CompanyAcquisitions {
    public static void main(String[] args) {
        FastScanner sc = new FastScanner();
        PrintWriter out = new PrintWriter(System.out);
        
        int N = sc.nextInt();
        int[] children = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            int par = sc.nextInt();
            if (par != -1) {
                children[par]++;
            }
        }
        long[] twoPow = new long[N + 1];
        twoPow[0] = 1;
        for (int i = 1; i <= N; i++) {
            twoPow[i] = 2 * twoPow[i - 1] % mod;
        }
        long M0 = 0;
        for (int c : children) {
            M0 = (M0 + twoPow[c] - 1) % mod;
        }
        long Mt = twoPow[N - 1] - 1;
        long Et = (Mt - M0 + mod) % mod;
        out.println(Et);
        out.close();
    }

    static long mod = (long) 1e9 + 7;

    static class FastScanner {
        private int BS = 1 << 16;
        private char NC = (char) 0;
        private byte[] buf = new byte[BS];
        private int bId = 0, size = 0;
        private char c = NC;
        private double cnt = 1;
        private BufferedInputStream in;
    
        public FastScanner() {
            in = new BufferedInputStream(System.in, BS);
        }
    
        public FastScanner(String s) {
            try {
                in = new BufferedInputStream(new FileInputStream(new File(s)), BS);
            } catch (Exception e) {
                in = new BufferedInputStream(System.in, BS);
            }
        }
    
        char getChar() {
            while (bId == size) {
                try {
                    size = in.read(buf);
                } catch (Exception e) {
                    return NC;
                }
                if (size == -1) return NC;
                bId = 0;
            }
            return (char) buf[bId++];
        }
    
        int nextInt() {
            return (int) nextLong();
        }
    
        long nextLong() {
            cnt = 1;
            boolean neg = false;
            if (c == NC) c = getChar();
            for (; (c < '0' || c > '9'); c = getChar()) {
                if (c == '-') neg = true;
            }
            long res = 0;
            for (; c >= '0' && c <= '9'; c = getChar()) {
                res = (res << 3) + (res << 1) + c - '0';
                cnt *= 10;
            }
            return neg ? -res : res;
        }
    
        double nextDouble() {
            boolean neg = false;
            if (c == NC) c = getChar();
            for (; (c < '0' || c > '9'); c = getChar()) {
                if (c == '-') neg = true;
            }
            double cur = nextLong();
            if (c != '.') {
                return neg ? -cur : cur;
            } else {
                double frac = nextLong() / cnt;
                return neg ? -cur - frac : cur + frac;
            }
        }
    
        String next() {
            StringBuilder res = new StringBuilder();
            while (c <= 32) c = getChar();
            while (c > 32) {
                res.append(c);
                c = getChar();
            }
            return res.toString();
        }
    
        String nextLine() {
            StringBuilder res = new StringBuilder();
            while (c <= 32) c = getChar();
            while (c != '\n') {
                res.append(c);
                c = getChar();
            }
            return res.toString();
        }
    
        boolean hasNext() {
            if (c > 32) return true;
            while (true) {
                c = getChar();
                if (c == NC) return false;
                else if (c > 32) return true;
            }
        }
    }
    static void ASSERT(boolean assertion, String message) {
        if (!assertion) throw new AssertionError(message);
    }
    static void ASSERT(boolean assertion) {
        if (!assertion) throw new AssertionError();
    }
}