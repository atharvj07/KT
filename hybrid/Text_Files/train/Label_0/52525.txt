import java.io.*;
import java.util.*;
 
public class Solution extends PrintWriter {
    
    long M = 998244353L;
    
    int MX = 200000;
    long[] fac = new long[MX+1];
    long[] fac_inv = new long[MX+1];
    long[] inv = new long[MX+1];
 
    long A(int n, int k) {
        return (fac_inv[n - k] * fac[n]) % M;
    }
    
    void build_fac() {
        inv[1] = 1L;
        for(int i = 2; i <= MX; i++) 
            inv[i] = M - (M/i) * inv[(int)(M%i)] % M;
        fac[0] = 1L;
        fac_inv[0] = 1L;
        for(int i = 1; i <= MX; i++) {
            fac[i] = (fac[i-1]*i)%M;
            fac_inv[i] = (fac_inv[i-1]*inv[i])%M;
        }
    }
    
    private void solve() {
        build_fac();
        n = sc.nextInt();
        int m = sc.nextInt();
        Integer[] d = new Integer[n];
        for(int i = 0; i < n; i++) {
            d[i] = sc.nextInt();
        }
        Arrays.sort(d);
        dd = new long[n];
        long sum = 0L;
        for(int i = 0; i < n; i++) {
            sum = (sum + d[i]) % M;
            dd[i] = sum;
        }
        for(int i = 0; i < m; i++) {
            long ans = 0L;
            int a = sc.nextInt();
            int b = sc.nextInt();
            int l = -1;
            int r = n;
            while(l < r-1) {
                int mid = (l+r)/2;
                if(d[mid] < b) l = mid;
                else r = mid;
            }
            int t = (n-r);
            long L = 0L;
            if(t-a+1 >= 0 && r >= 1) {
                L = ((t - a + 1) * fac[t]) % M ;
                L = (L * A(n, r-1)) % M;
                L = (L * dd(0,l)) % M;
            }
            
            long R = 0L;
            if(t-a >= 0 && r >= 0) {
                R = ((t - a) * fac[t-1]) % M ;
                R = (R * A(n, r)) % M;
                R = (R * dd(r,n-1)) % M;
            }
            ans = (L + R) % M;
            println((ans * fac_inv[n]) % M);
        }
    }
    
    int n;
    
    long[] dd;
    
    long dd(int l, int r) {
        return (dd(r) - dd(l-1) + M) % M ;
    }
    
    long dd(int i) {
        if(i < 0) return 0L;
        else if(i >= n) return dd[n-1];
        else return dd[i];
    }
    

//  Solution() throws FileNotFoundException { super(new File("output.txt")); }
//  InputReader sc = new InputReader(new FileInputStream("test_input.txt"));
  Solution() { super(System.out); }
  InputReader sc = new InputReader(System.in);
  static class InputReader {
      InputReader(InputStream in) { this.in = in; } InputStream in;
      
      private byte[] buf = new byte[16384];
      private int    curChar;
      private int    numChars;
      
 
      public int read() {
          if (numChars == -1)
              throw new InputMismatchException();
          if (curChar >= numChars) {
              curChar = 0;
              try {
                  numChars = in.read(buf);
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
 
      private boolean isSpaceChar(int c) {
          return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
      }
 
      private boolean isEndOfLine(int c) {
          return c == '\n' || c == '\r' || c == -1;
      }
  }
 
    public static void main(String[] $) {
        new Thread(null, new Runnable() {
            public void run() {
                long start = System.nanoTime();
                try {Solution solution = new Solution(); solution.solve(); solution.flush();} 
                catch (Exception e) {e.printStackTrace(); System.exit(1);}
                System.err.println((System.nanoTime()-start)/1E9);
            }
        }, "1", 1 << 27).start();
 
    }
    

}