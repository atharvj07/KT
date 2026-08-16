import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.NoSuchElementException;
import java.util.TreeSet;

public class E2 {

  private ArrayList<Integer>[] tree;

  //branches[i] := iにぶら下がっている枝の数
  private TreeSet<Integer>[] branches;

  private int[] reached;
  private boolean[] used;

  private int solve() {
    int N = tree.length;
    ArrayDeque<Integer> deque = new ArrayDeque<>();
    for (int i = 0; i < N; i++) {
      if (tree[i].size() == 1) {
        deque.add(i);
      }
    }

    while (!deque.isEmpty()) {
      int now = deque.poll();
      used[now] = true;

      if (branches[now].size() >= 3) {
        return -1;
      }

      if (reached[now] == tree[now].size()) {
        int ans = 0;
        for (int branch : branches[now]) {
          ans += branch;
        }

        //半分に折れる限り折る
        while (ans % 2 == 0) {
          ans /= 2;
        }
        return ans;
      }

      if (branches[now].size() == 2) {
        return -1;
      }

      int length = branches[now].isEmpty() ? 1 : branches[now].first() + 1;
      for (int next : tree[now]) {
        if (used[next]) {
          continue;
        }
        reached[next]++;
        branches[next].add(length);
        if (reached[next] + 1 == tree[next].size()) {
          deque.add(next);
        }
      }
    }
    throw new IllegalStateException();
  }

  private void solve(FastScanner in, PrintWriter out) {
    int N = in.nextInt();
    tree = new ArrayList[N];
    branches = new TreeSet[N];
    reached = new int[N];
    used = new boolean[N];
    for (int i = 0; i < N; i++) {
      tree[i] = new ArrayList<>();
      branches[i] = new TreeSet<>();
    }

    for (int i = 0; i < N - 1; i++) {
      int u = in.nextInt() - 1;
      int v = in.nextInt() - 1;
      tree[v].add(u);
      tree[u].add(v);
    }

    out.println(solve());
  }


  public static void main(String[] args) {
    FastScanner in = new FastScanner();
    PrintWriter out = new PrintWriter(System.out);
    new E2().solve(in, out);
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
