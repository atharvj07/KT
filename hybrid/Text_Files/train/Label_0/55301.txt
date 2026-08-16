import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.*;

/*
                   _ooOoo_
                  o8888888o
                  88" . "88
                  (| -_- |)
                  O\  =  /O
               ____/`---'\____
             .'  \\|     |//  `.
            /  \\|||  :  |||//  \
           /  _||||| -:- |||||-  \
           |   | \\\  -  /// |   |
           | \_|  ''\---/''  |   |
           \  .-\__  `-`  ___/-. /
         ___`. .'  /--.--\  `. . __
      ."" '<  `.___\_<|>_/___.'  >'"".
     | | :  `- \`.;`\ _ /`;.`/ - ` : | |
     \  \ `-.   \_ __\ /__ _/   .-` /  /
======`-.____`-.___\_____/___.-`____.-'======
                   `=---='
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            pass System Test!
*/

public class Main {
  private static class Task {

    void solve(FastScanner in, PrintWriter out) throws Exception {
      String S = in.next();
      SuffixArray sa = new SuffixArray(S);
      SuffixArray reverseSA = new SuffixArray(new StringBuilder(S).reverse().toString());

      int N = S.length();
      RMQ rmq = new RMQ(N + 1);
      RMQ reverseRMQ = new RMQ(N);
      for (int i = 0; i <= N; i++) {
        rmq.update(i, sa.sa[i]);
        reverseRMQ.update(i, reverseSA.sa[i]);
      }

      int Q = in.nextInt();
      for (int q = 0; q < Q; q++) {
        String x = in.next();
        String y = new StringBuilder(in.next()).reverse().toString();

        int low = sa.lowerBound(x);
        if (low == -1) {
          out.println(0);
          continue;
        }
        int up = sa.upperBound(x);

        int reverseLow = reverseSA.lowerBound(y);
        if (reverseLow == -1) {
          out.println(0);
          continue;
        }
        int reverseUp = reverseSA.upperBound(y);

        long s = rmq.query(low, up);
        long t = N - reverseRMQ.query(reverseLow, reverseUp);
        if (s + x.length() <= t && s <= t - y.length()) {
          out.println(t - s);
        } else {
          out.println(0);
        }

      }
    }

    class RMQ {
      private long INF = (long) 1e18;
      private int N;
      private long[] seg;

      RMQ(long[] array) {
        N = Integer.highestOneBit(array.length) * 2;
        seg = new long[N * 2];
        Arrays.fill(seg, INF);
        for (int i = 0; i < array.length; i++) update(i, array[i]);
      }

      RMQ(int M) {
        N = Integer.highestOneBit(M) * 2;
        seg = new long[N * 2];
        Arrays.fill(seg, INF);
      }

      void update(int k, long value) {
        seg[k += N - 1] = value;
        while (k > 0) {
          k = (k - 1) / 2;
          seg[k] = Math.min(seg[k * 2 + 1], seg[k * 2 + 2]);
        }
      }

      //[a, b)
      long query(int a, int b) {
        return query(a, b, 0, 0, N);
      }

      long query(int a, int b, int k, int l, int r) {
        if (r <= a || b <= l) return INF;
        if (a <= l && r <= b) return seg[k];
        long x = query(a, b, k * 2 + 1, l, (l + r) / 2);
        long y = query(a, b, k * 2 + 2, (l + r) / 2, r);
        return Math.min(x, y);
      }
    }

    class SuffixArray {
      String S;
      int N, K;
      Integer[] sa;
      int[] rank;
      public SuffixArray(String S) {
        this.S = S;
        build();
      }

      private void build() {
        N = S.length();
        rank = new int[N + 1];
        sa = new Integer[N + 1];
        for (int i = 0; i <= N; i++) {
          sa[i] = i;
          rank[i] = i < N ? S.charAt(i) : -1;
        }

        int[] tmp = new int[N + 1];
        for (int _k = 1; _k <= N; _k *= 2) {
          final int k = _k;
          Arrays.sort(sa, new Comparator<Integer>() {
            @Override
            public int compare(Integer i, Integer j) {
              return compareNode(i, j, k);
            }
          });
          tmp[sa[0]] = 0;
          for (int i = 1; i <= N; i++) {
            tmp[sa[i]] = tmp[sa[i - 1]] + ((compareNode(sa[i - 1], sa[i], k) < 0) ? 1 : 0);
          }
          for (int i = 0; i <= N; i++) {
            rank[i] = tmp[i];
          }
        }
      }

      private int compareNode(int i, int j, int k) {
        if (rank[i] != rank[j]) {
          return rank[i] - rank[j];
        } else {
          int ri = i + k <= N ? rank[i + k] : -1;
          int rj = j + k <= N ? rank[j + k] : -1;
          return ri - rj;
        }
      }

      public int lowerBound(String t) {
        int a = -1, b = S.length();
        while (b - a > 1) {
          int c = (a + b) / 2;
          String sub = S.substring(sa[c], Math.min(t.length() + sa[c], S.length()));
          if (sub.compareTo(t) < 0)
            a = c;
          else
            b = c;
        }
        String sub = S.substring(sa[b], Math.min(t.length() + sa[b], S.length()));
        return sub.compareTo(t) == 0 ? b : -1;
      }

      public int upperBound(String t) {
        int a = -1, b = S.length() + 1;
        while (b - a > 1) {
          int c = (a + b) / 2;
          String sub = S.substring(sa[c], Math.min(t.length() + sa[c], S.length()));
          if (sub.compareTo(t) <= 0)
            a = c;
          else
            b = c;
        }
        return b;
      }
    }
  }

  /**
   * ?????????????????????????????¬????????§??????
   */
  public static void main(String[] args) throws Exception {
    OutputStream outputStream = System.out;
    FastScanner in = new FastScanner();
    PrintWriter out = new PrintWriter(outputStream);
    Task solver = new Task();
    solver.solve(in, out);
    out.close();
  }
  private static class FastScanner {
    private final InputStream in = System.in;
    private final byte[] buffer = new byte[1024];
    private int ptr = 0;
    private int bufferLength = 0;

    private boolean hasNextByte() {
      if (ptr < bufferLength) {
        return true;
      } else {
        ptr = 0;
        try {
          bufferLength = in.read(buffer);
        } catch (IOException e) {
          e.printStackTrace();
        }
        if (bufferLength <= 0) {
          return false;
        }
      }
      return true;
    }

    private int readByte() {
      if (hasNextByte()) return buffer[ptr++];
      else return -1;
    }

    private static boolean isPrintableChar(int c) {
      return 33 <= c && c <= 126;
    }

    private void skipUnprintable() {
      while (hasNextByte() && !isPrintableChar(buffer[ptr])) ptr++;
    }

    boolean hasNext() {
      skipUnprintable();
      return hasNextByte();
    }

    public String next() {
      if (!hasNext()) throw new NoSuchElementException();
      StringBuilder sb = new StringBuilder();
      int b = readByte();
      while (isPrintableChar(b)) {
        sb.appendCodePoint(b);
        b = readByte();
      }
      return sb.toString();
    }

    long nextLong() {
      if (!hasNext()) throw new NoSuchElementException();
      long n = 0;
      boolean minus = false;
      int b = readByte();
      if (b == '-') {
        minus = true;
        b = readByte();
      }
      if (b < '0' || '9' < b) {
        throw new NumberFormatException();
      }
      while (true) {
        if ('0' <= b && b <= '9') {
          n *= 10;
          n += b - '0';
        } else if (b == -1 || !isPrintableChar(b)) {
          return minus ? -n : n;
        } else {
          throw new NumberFormatException();
        }
        b = readByte();
      }
    }

    double nextDouble() {
      return Double.parseDouble(next());
    }

    double[] nextDoubleArray(int n) {
      double[] array = new double[n];
      for (int i = 0; i < n; i++) {
        array[i] = nextDouble();
      }
      return array;
    }

    double[][] nextDoubleMap(int n, int m) {
      double[][] map = new double[n][];
      for (int i = 0; i < n; i++) {
        map[i] = nextDoubleArray(m);
      }
      return map;
    }

    public int nextInt() {
      return (int) nextLong();
    }

    public int[] nextIntArray(int n) {
      int[] array = new int[n];
      for (int i = 0; i < n; i++) array[i] = nextInt();
      return array;
    }

    public long[] nextLongArray(int n) {
      long[] array = new long[n];
      for (int i = 0; i < n; i++) array[i] = nextLong();
      return array;
    }

    public String[] nextStringArray(int n) {
      String[] array = new String[n];
      for (int i = 0; i < n; i++) array[i] = next();
      return array;
    }

    public char[][] nextCharMap(int n) {
      char[][] array = new char[n][];
      for (int i = 0; i < n; i++) array[i] = next().toCharArray();
      return array;
    }

    public int[][] nextIntMap(int n, int m) {
      int[][] map = new int[n][];
      for (int i = 0; i < n; i++) {
        map[i] = nextIntArray(m);
      }
      return map;
    }
  }
}