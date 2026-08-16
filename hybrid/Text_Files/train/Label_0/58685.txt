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
      int N = in.nextInt();
      long T = in.nextInt();
      long[] A = in.nextLongArray(N);
      RMQ rmq = new RMQ(N);
      TreeMap<Long, ArrayList<Integer>> cnt = new TreeMap<>();
      for (int i = 0; i < N; i++) {
        rmq.update(i, A[i]);
        ArrayList<Integer> list = cnt.get(A[i]);
        if (list == null) {
          cnt.put(A[i], list = new ArrayList<>());
        }
        list.add(i);
      }

      long max = 0;
      for (int i = 0; i < N - 1; i++) {
        long sell = rmq.query(i + 1, N);
        long x = Math.max(0, sell - A[i]);
        max = Math.max(max, x);
      }

      int ans = 0;
      for (long key : cnt.keySet()) {
        long up = key + max;
        ArrayList<Integer> children = cnt.get(key);
        ArrayList<Integer> parents = cnt.get(up);
        if (parents == null) continue;

        int c = 0;
        int p = parents.size() - 1;
        while (c < children.size() && p >= 0) {
          int childNum = ~Collections.binarySearch(children, parents.get(p));
          childNum = childNum - c;

          int parentNum = ~Collections.binarySearch(parents, children.get(c));
          parentNum = Math.max(p + 1 - parentNum, 0);
          if (childNum == 0) break;
          if (childNum > parentNum) {
            p--;
          } else {
            c++;
          }
          ans++;
        }
      }

      out.println(ans);
    }

    class RMQ {
      private int N;
      private long[] seg;

      RMQ(int M) {
        N = Integer.highestOneBit(M) * 2;
        seg = new long[N * 2];
        Arrays.fill(seg, 0);
      }

      void update(int k, long value) {
        seg[k += N - 1] = value;
        while (k > 0) {
          k = (k - 1) / 2;
          seg[k] = Math.max(seg[k * 2 + 1], seg[k * 2 + 2]);
        }
      }

      //[a, b)
      long query(int a, int b) {
        return query(a, b, 0, 0, N);
      }

      long query(int a, int b, int k, int l, int r) {
        if (r <= a || b <= l) return 0;
        if (a <= l && r <= b) return seg[k];
        long x = query(a, b, k * 2 + 1, l, (l + r) / 2);
        long y = query(a, b, k * 2 + 2, (l + r) / 2, r);
        return Math.max(x, y);
      }
    }
  }

  /**
   * ここから下はテンプレートです。
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