import java.util.*;
import java.io.*;

public class CFA {
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

  void helper() {
    int n = nextInt();
    int m = nextInt();
    int[][] mat = new int[n][m];
    for (int i = 0; i < n; i++) {
      mat[i] = nextIntArr(m);
    }
    int[][] res = new Solution().matrixRankTransform(mat);
    for (int[] arr : res) {
      for (int v : arr) {
        out(v + " ");
      }
      outln("");
    }
  }

  class Solution {
    class WeightedUF {
      int[] id;
      int count;
      int[] sz;
      public WeightedUF(int n) {
        count = n;
        id = new int[n];
        for(int i = 0; i < n; i++) {
          id[i] = i;
        }
        sz = new int[n];
        Arrays.fill(sz, 1);
      }

      public boolean isConnected(int p, int q) {
        return find(p) == find(q);
      }
      public int find(int p) {
        while(p != id[p]) {
          p = id[p];
        }
        return p;
      }

      public boolean union(int p, int q) {
        int i = find(p);
        int j = find(q);
        if(i == j) {
          return false;
        }
        if(sz[i] < sz[j]) {
          id[i] = j;
          sz[j] += sz[i];
        }
        else {
          id[j] = i;
          sz[i] += sz[j];
        }
        count--;
        return true;
      }
    }

    class Point implements Comparable<Point> {
      int row;
      int col;
      int val;
      public Point(int row, int col, int val) {
        this.row = row;
        this.col = col;
        this.val = val;
      }

      public String toString() {
        return row + " " + col + " " + val;
      }

      @Override
      public int compareTo(Point o) {
        return Integer.compare(val, o.val);
      }
    }

    List<List<Integer>> graph;
    public int[][] matrixRankTransform(int[][] matrix) {
      int n = matrix.length;
      int m = matrix[0].length;
      graph = new ArrayList<>();
      for (int i = 0; i < n * m; i++) {
        graph.add(new ArrayList<>());
      }
      WeightedUF uf = new WeightedUF(n * m);

      // union
      for (int i = 0; i < n; i++) {
        List<Point> ls = new ArrayList<>();
        for (int j = 0; j < m; j++) {
          ls.add(new Point(i, j, matrix[i][j]));
        }
        Collections.sort(ls);
        for (int j = 0; j < m - 1; j++) {
          int idx1 = findIdx(ls.get(j), m);
          int idx2 = findIdx(ls.get(j + 1), m);
          if (ls.get(j).val == ls.get(j + 1).val) {
            uf.union(idx1, idx2);
          }
        }
      }

      for (int j = 0; j < m; j++) {
        List<Point> ls = new ArrayList<>();
        for (int i = 0; i < n; i++) {
          ls.add(new Point(i, j, matrix[i][j]));
        }
        Collections.sort(ls);
        for (int i = 0; i < n - 1; i++) {
          int idx1 = findIdx(ls.get(i), m);
          int idx2 = findIdx(ls.get(i + 1), m);
          if (ls.get(i).val == ls.get(i + 1).val) {
            uf.union(idx1, idx2);
          }
        }
      }

      // Add edges
      for (int i = 0; i < n; i++) {
        List<Point> ls = new ArrayList<>();
        for (int j = 0; j < m; j++) {
          ls.add(new Point(i, j, matrix[i][j]));
        }
        Collections.sort(ls);
        for (int j = 0; j < m - 1; j++) {
          int idx1 = findIdx(ls.get(j), m);
          int idx2 = findIdx(ls.get(j + 1), m);
          if (ls.get(j).val != ls.get(j + 1).val) {
            int p1 = uf.find(idx1);
            int p2 = uf.find(idx2);
            graph.get(p1).add(p2);
          }
        }
      }

      for (int j = 0; j < m; j++) {
        List<Point> ls = new ArrayList<>();
        for (int i = 0; i < n; i++) {
          ls.add(new Point(i, j, matrix[i][j]));
        }
        Collections.sort(ls);
        for (int i = 0; i < n - 1; i++) {
          int idx1 = findIdx(ls.get(i), m);
          int idx2 = findIdx(ls.get(i + 1), m);
          if (ls.get(i).val != ls.get(i + 1).val) {
            int p1 = uf.find(idx1);
            int p2 = uf.find(idx2);
            graph.get(p1).add(p2);
          }
        }
      }

      int[] degree = new int[n * m];
      for (int i = 0; i < graph.size(); i++) {
        for (int nxt : graph.get(i)) {
          degree[nxt]++;
        }
      }
      Deque<Integer> deck = new LinkedList<>();
      for (int i = 0; i < graph.size(); i++) {
        if (degree[i] == 0) {
          deck.addLast(i);
        }
      }

      List<Integer> order = new ArrayList<>();
      while (!deck.isEmpty()) {
        int cur = deck.removeFirst();
        order.add(cur);
        for (int nxt : graph.get(cur)) {
          degree[nxt]--;
          if (degree[nxt] == 0) {
            deck.addLast(nxt);
          }
        }
      }

      int[] nums = new int[n * m];
      Arrays.fill(nums, 1);
      for (int v : order) {
        for (int nxt : graph.get(v)) {
          nums[nxt] = Math.max(nums[nxt], nums[v] + 1);
        }
      }
      int[][] res = new int[n][m];
      for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
          int par = uf.find(i * m + j);
          res[i][j] = nums[par];
        }
      }
      return res;
    }

    int findIdx(Point p, int colNum) {
      return colNum * p.row + p.col;
    }
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

  int gcd(int a, int b) {
    while(a != 0 && b != 0) {
      int c = b;
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
  public CFA() {
    br = new BufferedReader(new InputStreamReader(System.in));
    out = new PrintWriter(System.out);
    solve();
    out.close();
  }
  public static void main(String[] args) {
    new CFA();
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
