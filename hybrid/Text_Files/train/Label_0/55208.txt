import java.io.*;
import java.util.*;
 
public class Main extends PrintWriter {
    
    
    private void solve()  {
        n = sc.nextInt();
        int m = sc.nextInt();
        a = new long[n];
        for(int i = 0; i < n; i++) a[i] = sc.nextLong();
        sum = new long[4*n];
        max = new long[4*n];
        min = new long[4*n];
        build(1,n,1);
        lazy_set = new long[4*n];
        old = new boolean[4*n];
        for(int i = 0; i < m; i++) {
            int qt = sc.nextInt();
            if(qt == 1) {
                int l = sc.nextInt();
                int r = sc.nextInt();
                println(query_range(1, n, 1, l, r));
            } else if(qt == 2) {
                int l = sc.nextInt();
                int r = sc.nextInt();
                long x = sc.nextLong();
                mod_range(1, n, 1, l, r, x);
            } else {
                int k = sc.nextInt();
                long x = sc.nextLong();
                set_point(1, n, 1, k, x);
            }
        }
    }
    
    void build(int il, int ir, int i) {
        if(il == ir) {
            sum[i] = a[il-1];
            max[i] = a[il-1];
            min[i] = a[il-1];
        } else {
            int imid = (il+ir)/2;
            build(il, imid, 2*i);
            build(imid+1, ir, 2*i+1);
            sum[i] = sum[2*i] + sum[2*i+1];
            max[i] = Math.max(max[2*i], max[2*i+1]);
            min[i] = Math.min(min[2*i], min[2*i+1]);
        }
    }
 
    int n;
    long[] a;
    long[] sum;
    long[] max;
    long[] min;
    
    long[] lazy_set;
    boolean[] old;
    
    long query_range(int il, int ir, int i, int ql, int qr) {
        lazy_propagate(il, ir, i);
        if(ir < ql || il > qr) return 0L;
 
        
        if(ql <= il && ir <= qr) {
            return sum[i];
        }
        
        int imid = (il+ir)/2;
        long a_l = query_range(il, imid, 2*i, ql, qr);
        long a_r = query_range(imid+1, ir, 2*i+1, ql, qr);
        return a_l + a_r;
    }
    
    void mod_range(int il, int ir, int i, int ql, int qr, long x) {
        lazy_propagate(il, ir, i);
        if(ir < ql || il > qr || max[i] < x) return;
        
        if(ql <= il && ir <= qr && max[i] == min[i]) {
            long res = max[i] % x; 
            max[i] = res;
            min[i] = res;
            sum[i] = res * (ir-il+1);
            push(i, res);
            lazy_propagate(il, ir, i);
            return;
        }
        
        int imid = (il+ir)/2;
        mod_range(il, imid, 2*i, ql, qr, x);
        mod_range(imid+1, ir, 2*i+1, ql, qr, x);
        sum[i] = sum[2*i] + sum[2*i+1];
        max[i] = Math.max(max[2*i], max[2*i+1]);
        min[i] = Math.min(min[2*i], min[2*i+1]);
    }
    
    void set_point(int il, int ir, int i, int q, long x) {
        lazy_propagate(il, ir, i);
        if(ir < q || il > q) return;
        
        if(q <= il && ir <= q) {
            sum[i] = x;
            max[i] = x;
            min[i] = x;
            return;
        }
        
        int imid = (il+ir)/2;
        set_point(il, imid, 2*i, q, x);
        set_point(imid+1, ir, 2*i+1, q, x);
        sum[i] = sum[2*i] + sum[2*i+1];
        max[i] = Math.max(max[2*i], max[2*i+1]);
        min[i] = Math.min(min[2*i], min[2*i+1]);
    }
    
    void push(int i, long res) {
        lazy_set[i] = res;
        old[i] = true;
    }
    
    void lazy_propagate(int il, int ir, int i) {
        if(old[i]) {
            max[i] = lazy_set[i];
            min[i] = lazy_set[i];
            sum[i] = lazy_set[i] * (ir-il+1);
            if(il != ir) {
                push(2*i, lazy_set[i]);
                push(2*i+1, lazy_set[i]);
            }
            lazy_reset(i);
        }
    }
    
    void lazy_reset(int i) {
        lazy_set[i] = 0L;
        old[i] = false;
    }
   
//  Main() throws FileNotFoundException { super(new File("output.txt")); }
//  InputReader sc = new InputReader(new FileInputStream("test_input.txt"));
    
  Main() { super(System.out); }
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
                try {Main solution = new Main(); solution.solve(); solution.close();} 
                catch (Exception e) {e.printStackTrace(); System.exit(1);}
                System.err.println((System.nanoTime()-start)/1E9);
            }
        }, "1", 1 << 27).start();
 
    }
    
}