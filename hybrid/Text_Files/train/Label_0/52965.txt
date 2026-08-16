import java.util.*;
import java.io.*;

public class CFF {
  BufferedReader br;
  PrintWriter out;
  StringTokenizer st;
  boolean eof;
  private static final long MOD = 1000L * 1000L * 1000L + 7;
  private static final int[] dx = {0, -1, 0, 1};
  private static final int[] dy = {1, 0, -1, 0};
  private static final String yes = "Yes";
  private static final String no = "No";

  void solve() {
//    int T = nextInt();
    int T = 1;
    for (int i = 0; i < T; i++) {
        helper();
    }
  }

  List<Point> res;
  class Point implements Comparable<Point> {
    int left;
    int right;
    int layer;
    public Point(int left, int right, int layer) {
      this.left = left;
      this.right = right;
      this.layer = layer;
    }

    @Override
    public int compareTo(Point o) {
      return Integer.compare(layer, o.layer);
    }
  }

  void helper() {
    int n = nextInt();
    if (n == 1) {
      outln(0);
      return;
    }
    res = new ArrayList<>();
    int pow2 = 1;
    while (pow2 < n) {
      pow2 = pow2 * 2;
    }
    pow2 = pow2 / 2;
    List<Point> l1 = new ArrayList<>();
    // Add first 2^n
    rec(1, pow2, 0, l1);
    Collections.sort(l1);
    Collections.reverse(l1);
    res.addAll(l1);
    // Add last 2^n
    List<Point> l2 = new ArrayList<>();
    rec(n + 1 - pow2, n, 0, l2);
    Collections.sort(l2);
    Collections.reverse(l2);
    res.addAll(l2);

    outln(res.size());
    for (int i = 0; i < res.size(); i++) {
      outln(res.get(i).left + " " + res.get(i).right);
    }
  }

  void rec(int start, int end, int layer, List<Point> ls) {
    if (start >= end) {
      return;
    }

    int mid = (start + end) / 2;
    // [start, mid] [mid + 1, end]
    for (int i = start, j = end; i < j; i++, j--) {
      ls.add(new Point(i, j, layer));
    }

    rec(start, mid, layer + 1, ls);
    rec(mid + 1, end, layer + 1, ls);
  }

  void shuffle(long[] a) {
    int n = a.length;
    for(int i = 0; i < n; i++) {
        int r = i + (int) (Math.random() * (n - i));
        long tmp = a[i];
        a[i] = a[r];
        a[r] = tmp;
    }
  }
  long gcd(long a, long b) {
    while(a != 0 && b != 0) {
        long c = b;
        b = a % b;
        a = c;
    }
    return a + b;
  }
  private void outln(Object o) {
      out.println(o);
  }
  private void out(Object o) {
      out.print(o);
  }
  private void formatPrint(double val) {
      outln(String.format("%.9f%n", val));
  }
  public CFF() {
    br = new BufferedReader(new InputStreamReader(System.in));
    out = new PrintWriter(System.out);
    solve();
    out.close();
  }
  public static void main(String[] args) {
      new CFF();
  }

  public long[] nextLongArr(int n) {
    long[] res = new long[n];
    for(int i = 0; i < n; i++)
        res[i] = nextLong();
    return res;
  }
  public int[] nextIntArr(int n) {
    int[] res = new int[n];
    for(int i = 0; i < n; i++)
        res[i] = nextInt();
    return res;
  }
  public String nextToken() {
    while (st == null || !st.hasMoreTokens()) {
        try {
            st = new StringTokenizer(br.readLine());
        } catch (Exception e) {
            eof = true;
            return null;
        }
    }
    return st.nextToken();
  }
  public String nextString() {
    try {
        return br.readLine();
    } catch (IOException e) {
        eof = true;
        return null;
    }
  }
  public int nextInt() {
      return Integer.parseInt(nextToken());
  }
  public long nextLong() {
      return Long.parseLong(nextToken());
  }
  public double nextDouble() {
      return Double.parseDouble(nextToken());
  }
}
