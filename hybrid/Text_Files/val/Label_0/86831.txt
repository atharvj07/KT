
import java.util.Arrays;

public class Main {

  private static void solve() {
    int n = ni();
    int[] from = new int[n - 1];
    int[] to = new int[n - 1];
    for (int i = 0; i < n - 1; i++) {
      from[i] = ni() - 1;
      to[i] = ni() - 1;
    }
    int[][] g = packU(n, from, to);
    int[] center = centerNoRec(g);

    if (center.length == 2) {
      long[] ret = f2(center[0], center[1], g);
      System.out.println(ret[0] + " " + ret[1]);
    } else {
      long[] ret = f1(center[0], g);
      for (int v : g[center[0]]) {
        long[] now = f2(center[0], v, g);
        if (now[1] < ret[1]) {
          ret = now;
        }
      }
      System.out.println(ret[0] + " " + ret[1]);
    }

  }

  private static long[] f1(int c1, int[][] g) {
    int n = g.length;
    int[] dep1 = new int[n];
    Arrays.fill(dep1, -1);
    dfs(c1, -1, g, 0, dep1);
    int depth = Arrays.stream(dep1).max().getAsInt();
    int[] max = new int[depth + 1];
    for (int i = 0; i < n; i++) {
      int v1 = dep1[i];
      if (v1 >= 0)
        max[v1] = Math.max(max[v1], g[i].length - 1);
    }
    max[0]++;
    max[depth] = 1;
    long ret = 1;
    for (int v : max) {
      ret *= v;
    }
    return new long[] {depth + 1, ret};
  }

  private static long[] f2(int c1, int c2, int[][] g) {
    int n = g.length;
    int[] dep1 = new int[n];
    int[] dep2 = new int[n];
    Arrays.fill(dep1, -1);
    Arrays.fill(dep2, -1);

    dfs(c1, c2, g, 0, dep1);
    dfs(c2, c1, g, 0, dep2);

    int depth =
        Math.max(Arrays.stream(dep1).max().getAsInt(), Arrays.stream(dep2).max().getAsInt());
    int[] max = new int[depth + 1];
    for (int i = 0; i < n; i++) {
      int v1 = dep1[i];
      int v2 = dep2[i];
      if (v1 >= 0)
        max[v1] = Math.max(max[v1], g[i].length - 1);
      if (v2 >= 0)
        max[v2] = Math.max(max[v2], g[i].length - 1);
    }
    max[depth] = 1;
    long ret = 1;
    for (int v : max) {
      ret *= v;
    }
    ret *= 2;
    return new long[] {depth + 1, ret};
  }

  public static int[][] parents(int[][] g, int root) {
    int n = g.length;
    int[] par = new int[n];
    Arrays.fill(par, -1);

    int[] depth = new int[n];
    depth[0] = 0;

    int[] q = new int[n];
    q[0] = root;
    for (int p = 0, r = 1; p < r; p++) {
      int cur = q[p];
      for (int nex : g[cur]) {
        if (par[cur] != nex) {
          q[r++] = nex;
          par[nex] = cur;
          depth[nex] = depth[cur] + 1;
        }
      }
    }
    return new int[][] {par, q, depth};
  }

  private static void dfs(int cur, int pre, int[][] g, int d, int[] dep) {
    dep[cur] = d;
    for (int nex : g[cur]) {
      if (nex == pre) {
        continue;
      }
      dfs(nex, cur, g, d + 1, dep);
    }
  }

  public static int[] centerNoRec(int[][] g) {
    int n = g.length;
    if (n == 1)
      return new int[] {0};
    if (n == 2)
      return new int[] {0, 1};
    int root = -1;
    for (int i = 0; i < n; i++) {
      if (g[i].length >= 2) {
        root = i;
        break;
      }
    }
    int[][] pars = parents(g, root);
    int[] par = pars[0], ord = pars[1];
    int[] up = new int[n];
    int[] up2 = new int[n];
    Arrays.fill(up, -9999999);
    Arrays.fill(up2, -9999999);
    for (int i = n - 1; i >= 0; i--) {
      int cur = ord[i];
      if (g[cur].length == 1) {
        up[cur] = 0;
      } else {
        for (int e : g[cur]) {
          if (par[cur] != e) {
            if (up[e] + 1 > up[cur]) {
              up2[cur] = up[cur];
              up[cur] = up[e] + 1;
            } else if (up[e] + 1 > up2[cur]) {
              up2[cur] = up[e] + 1;
            }
          }
        }
      }
    }
    for (int i = 1; i < n; i++) {
      int cur = ord[i];
      int v = up[par[cur]] == up[cur] + 1 ? up2[par[cur]] + 1 : up[par[cur]] + 1;
      if (v > up[cur]) {
        up2[cur] = up[cur];
        up[cur] = v;
      } else if (v > up2[cur]) {
        up2[cur] = v;
      }
    }

    int min = 9999999;
    for (int i = 0; i < n; i++)
      min = Math.min(min, up[i]);

    int[] cen = new int[2];
    Arrays.fill(cen, -1);
    int p = 0;
    for (int i = 0; i < n; i++) {
      if (up[i] == min) {
        cen[p++] = i;
      }
    }
    return Arrays.copyOf(cen, p);
  }

  static int[][] packU(int n, int[] from, int[] to) {
    int[][] g = new int[n][];
    int[] p = new int[n];
    for (int f : from)
      p[f]++;
    for (int t : to)
      p[t]++;
    for (int i = 0; i < n; i++)
      g[i] = new int[p[i]];
    for (int i = 0; i < from.length; i++) {
      g[from[i]][--p[from[i]]] = to[i];
      g[to[i]][--p[to[i]]] = from[i];
    }
    return g;
  }

  public static void main(String[] args) {
    new Thread(null, new Runnable() {
      @Override
      public void run() {
        long start = System.currentTimeMillis();
        String debug = args.length > 0 ? args[0] : null;
        if (debug != null) {
          try {
            is = java.nio.file.Files.newInputStream(java.nio.file.Paths.get(debug));
          } catch (Exception e) {
            throw new RuntimeException(e);
          }
        }
        reader = new java.io.BufferedReader(new java.io.InputStreamReader(is), 32768);
        solve();
        out.flush();
        tr((System.currentTimeMillis() - start) + "ms");
      }
    }, "", 64000000).start();
  }

  private static java.io.InputStream is = System.in;
  private static java.io.PrintWriter out = new java.io.PrintWriter(System.out);
  private static java.util.StringTokenizer tokenizer = null;
  private static java.io.BufferedReader reader;

  public static String next() {
    while (tokenizer == null || !tokenizer.hasMoreTokens()) {
      try {
        tokenizer = new java.util.StringTokenizer(reader.readLine());
      } catch (Exception e) {
        throw new RuntimeException(e);
      }
    }
    return tokenizer.nextToken();
  }

  private static double nd() {
    return Double.parseDouble(next());
  }

  private static long nl() {
    return Long.parseLong(next());
  }

  private static int[] na(int n) {
    int[] a = new int[n];
    for (int i = 0; i < n; i++)
      a[i] = ni();
    return a;
  }

  private static char[] ns() {
    return next().toCharArray();
  }

  private static long[] nal(int n) {
    long[] a = new long[n];
    for (int i = 0; i < n; i++)
      a[i] = nl();
    return a;
  }

  private static int[][] ntable(int n, int m) {
    int[][] table = new int[n][m];
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        table[i][j] = ni();
      }
    }
    return table;
  }

  private static int[][] nlist(int n, int m) {
    int[][] table = new int[m][n];
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        table[j][i] = ni();
      }
    }
    return table;
  }

  private static int ni() {
    return Integer.parseInt(next());
  }

  private static void tr(Object... o) {
    if (is != System.in)
      System.out.println(java.util.Arrays.deepToString(o));
  }
}

