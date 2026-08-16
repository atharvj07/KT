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

  int LIMIT = 500 * 1000;
  SegmentLazy seg;
  void helper() {
    int n = nextInt();
    int k = nextInt();
    int[] arr = nextIntArr(n);
    seg = new SegmentLazy(new int[LIMIT]);
    shuffle(arr);
    Arrays.sort(arr);
    for (int i = 0, j = n - 1; i < j; i++, j--) {
      int tmp = arr[i];
      arr[i] = arr[j];
      arr[j] = tmp;
    }

    seg.update_tree(1, 0, LIMIT - 1, 0, 0, 1);
    int available = 0;
    int res = Integer.MAX_VALUE;
    for (int i = 0; i < n; i++) {
      while (seg.query_tree(1, 0, LIMIT - 1, available, available) == 0) {
        available++;
      }

      if (arr[i] % 2 == 0) {
        seg.update_tree(1, 0, LIMIT - 1, available + 2, available + arr[i] / 2, 1);
        seg.update_tree(1, 0, LIMIT - 1, available + 2, available + arr[i] / 2 + 1, 1);
      } else {
        seg.update_tree(1, 0, LIMIT - 1, available + 2, available + (arr[i] + 1) / 2, 2);
      }
      // [available, available], -1.
      seg.update_tree(1, 0, LIMIT - 1, available, available, -1);
      res = Math.min(res, seg.queryKth(k));
    }

    outln(res == Integer.MAX_VALUE ? -1 : res);
  }

  private class SegmentLazy {
    int arr[];
    long tree[];
    long lazy[];

    public SegmentLazy(int[] elements) {
      arr = Arrays.copyOf(elements, elements.length);
      tree = new long[5 * arr.length];
      lazy = new long[5 * arr.length];
    }

    void build_tree(int node, int nodeStartIndex, int nodeEndIndex) {
      if(nodeStartIndex > nodeEndIndex) return; // Out of range
      if(nodeStartIndex == nodeEndIndex) { // Leaf node
        tree[node] = arr[nodeStartIndex]; // Init value
        return;
      }

      build_tree(node * 2, nodeStartIndex, (nodeStartIndex + nodeEndIndex) / 2); // Init left child
      build_tree(node * 2 + 1, 1 + (nodeStartIndex + nodeEndIndex) / 2, nodeEndIndex); // Init right child
      tree[node] = tree[node * 2] +  tree[node * 2 + 1]; // Init root value
    }

    /**
     * Increment elements within range [queryStartIndex, queryEndIndex] with value
     */
    void update_tree(int node, int nodeStartIndex, int nodeEndIndex, int queryStartIndex, int queryEndIndex, int value) {
      if(nodeStartIndex > nodeEndIndex || nodeStartIndex > queryEndIndex || nodeEndIndex < queryStartIndex) // Current segment is not within range [i, j]
        return;
      if(nodeStartIndex >= queryStartIndex && nodeEndIndex <= queryEndIndex) { // Segment is fully within range
        tree[node] += value * (nodeEndIndex - nodeStartIndex + 1);
        lazy[node] += value;
        return;
      }

      //-------------
      shift(node, nodeStartIndex, nodeEndIndex);
      //-------------
      update_tree(node * 2, nodeStartIndex, (nodeStartIndex + nodeEndIndex) / 2, queryStartIndex, queryEndIndex, value); // Updating left child
      update_tree(node * 2 + 1, 1 + (nodeStartIndex + nodeEndIndex) / 2, nodeEndIndex, queryStartIndex, queryEndIndex, value); // Updating right child

      tree[node] = tree[node * 2] + tree[node * 2 + 1]; // Updating root
    }

    /**
     * Query tree to get max element value within range [queryStartIndex, queryEndIndex]
     */
    long query_tree(int node, int nodeStartIndex, int nodeEndIndex, int queryStartIndex, int queryEndIndex) {
      if(nodeStartIndex > nodeEndIndex || nodeStartIndex > queryEndIndex || nodeEndIndex < queryStartIndex) return 0; // Out of range
      if(nodeStartIndex >= queryStartIndex && nodeEndIndex <= queryEndIndex) // Current segment is totally within range [i, j]
        return tree[node];

      //-------------
      shift(node, nodeStartIndex, nodeEndIndex);
      //-------------
      long q1 = query_tree(node * 2, nodeStartIndex, (nodeStartIndex + nodeEndIndex) / 2, queryStartIndex, queryEndIndex); // Query left child
      long q2 = query_tree(1 + node * 2, 1 + (nodeStartIndex + nodeEndIndex) / 2, nodeEndIndex, queryStartIndex, queryEndIndex); // Query right child

      return q1 + q2;
    }

    int queryKth(int k) {
      int low = 0;
      int high = arr.length;
      while (low < high) {
        int mid = (low + high) / 2;
        if (query_tree(1, 0, arr.length - 1, 0, mid) < k) {
          low = mid + 1;
        } else {
          high = mid;
        }
      }
      return low == arr.length ? Integer.MAX_VALUE : low;
    }

    private void shift(int node, int nodeStartIndex, int nodeEndIndex) {
      if(lazy[node] != 0) { // This node needs to be updated
        if (nodeEndIndex > nodeStartIndex) {
          int mid = (nodeStartIndex + nodeEndIndex) / 2;
          tree[2 * node] += (mid - nodeStartIndex + 1) * lazy[node];
          tree[2 * node + 1] += (nodeEndIndex - mid) * lazy[node];

          lazy[node * 2] += lazy[node]; // Mark child as lazy
          lazy[node * 2 + 1] += lazy[node]; // Mark child as lazy
          lazy[node] = 0; // Reset it
        }
      }
    }
  }

  void shuffle(int[] a) {
    int n = a.length;
    for(int i = 0; i < n; i++) {
      int r = i + (int) (Math.random() * (n - i));
      int tmp = a[i];
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
