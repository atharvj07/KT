import java.util.*;
import java.io.*;

public class P250C {

  private static void solve() {
    int n = nextInt();
    int k = nextInt();

    int[] s = new int[k + 1];

    int last = -1;
    int lastToLast = -1;
    for (int i = 0; i < n; i++) {
      int cur = nextInt();

      if (last != -1 && last != cur) {
        s[cur]++;
        if (lastToLast == -1 || cur == lastToLast) {
          s[last]++;
        }
      }
      if (last != -1 && last != cur) {
        lastToLast = last;
      }
      last = cur;
    }

    int max = s[1];
    int maxK = 1;

    for (int i = 1; i <= k; i++) {
      if (max < s[i]) {
        maxK = i;
        max = s[i];
      }
    }

    System.out.println(maxK);
  }

  private static void run() {
    br = new BufferedReader(new InputStreamReader(System.in));
    out = new PrintWriter(System.out);

    solve();

    out.close();
  }

  private static StringTokenizer st;
  private static BufferedReader br;
  private static PrintWriter out;

  private static String next() {
    while (st == null || !st.hasMoreElements()) {
      String s;
      try {
        s = br.readLine();
      } catch (IOException e) {
        return null;
      }
      st = new StringTokenizer(s);
    }
    return st.nextToken();
  }

  private static int nextInt() {
    return Integer.parseInt(next());
  }

  private static long nextLong() {
    return Long.parseLong(next());
  }

  public static void main(String[] args) {
    run();
  }
}