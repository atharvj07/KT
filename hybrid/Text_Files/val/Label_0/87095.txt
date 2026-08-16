import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Comparator;
import java.util.NoSuchElementException;

public class Main {

  int N;
  int[] R;
  int[][] spc;

  private boolean ok(int x, int pos) {
    spc[0][pos] += x;

    int[][] points = new int[N][2];
    for (int team = 0; team < 3; team++) {

      int[][] tmp = new int[N][2];
      for (int i = 0; i < N; i++) {
        tmp[i][0] = spc[i][team];
        tmp[i][1] = i;
      }

      Arrays.sort(tmp, new Comparator<int[]>() {
        @Override
        public int compare(int[] o1, int[] o2) {
          return o2[0] - o1[0];
        }
      });

      int rank = 0;
      for (int i = 0; i < N; i++) {
        if (i > 0 && tmp[i][0] != tmp[i - 1][0]) {
          rank = i;
        }
        int unit = tmp[i][1];
        points[unit][0] += R[rank];
        points[unit][1] = unit;
      }
    }

    Arrays.sort(points, new Comparator<int[]>() {
      @Override
      public int compare(int[] o1, int[] o2) {
        if (o1[0] == o2[0]) {
          return o1[1] - o2[1];
        }
        return o2[0] - o1[0];
      }
    });

    spc[0][pos] -= x;
    for (int i = 0; i < N; i++) {
      if (points[i][1] == 0) {
        return i < 8;
      }
    }
    throw new IllegalArgumentException();
  }

  private void solve(FastScanner in, PrintWriter out) {
    N = in.nextInt();
    R = in.nextIntArray(N);
    spc = new int[N][3];
    for (int i = 0; i < N; i++) {
      spc[i][0] = in.nextInt();
      spc[i][1] = in.nextInt();
      spc[i][2] = in.nextInt();
    }

    int min = 10000;
    for (int pos = 0; pos < 3; pos++) {
      for (int i = 0; i < 200; i++) {
        if (ok(i, pos)) {
          min = Math.min(min, i);
          break;
        }
      }
    }
    if (min == 10000) {
      out.println("Saiko");
      return;
    }

    out.println(min);
  }

  public static void main(String[] args) {
    PrintWriter out = new PrintWriter(System.out);
    new Main().solve(new FastScanner(), out);
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
      if (hasNextByte()) {
        return buffer[ptr++];
      } else {
        return -1;
      }
    }

    private static boolean isPrintableChar(int c) {
      return 33 <= c && c <= 126;
    }

    private void skipUnprintable() {
      while (hasNextByte() && !isPrintableChar(buffer[ptr])) {
        ptr++;
      }
    }

    boolean hasNext() {
      skipUnprintable();
      return hasNextByte();
    }

    public String next() {
      if (!hasNext()) {
        throw new NoSuchElementException();
      }
      StringBuilder sb = new StringBuilder();
      int b = readByte();
      while (isPrintableChar(b)) {
        sb.appendCodePoint(b);
        b = readByte();
      }
      return sb.toString();
    }

    long nextLong() {
      if (!hasNext()) {
        throw new NoSuchElementException();
      }
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
      for (int i = 0; i < n; i++) {
        array[i] = nextInt();
      }
      return array;
    }

    public long[] nextLongArray(int n) {
      long[] array = new long[n];
      for (int i = 0; i < n; i++) {
        array[i] = nextLong();
      }
      return array;
    }

    public String[] nextStringArray(int n) {
      String[] array = new String[n];
      for (int i = 0; i < n; i++) {
        array[i] = next();
      }
      return array;
    }

    public char[][] nextCharMap(int n) {
      char[][] array = new char[n][];
      for (int i = 0; i < n; i++) {
        array[i] = next().toCharArray();
      }
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