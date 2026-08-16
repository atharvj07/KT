import java.util.*;
import java.io.*;

public class P1291B {

  private static void solve() {
    int tests = nextInt();

    while (tests-- != 0) {
      int n = nextInt();
      int[] a = new int[n];

      for (int i = 0; i < n; i++) {
        a[i] = nextInt();
      }

      int first = 0;
      for (int i = 0; i < n; i++) {
        if (a[i] >= i) {
          first = i;
        } else {
          break;
        }
      }

      int last = 0;
      for (int i = n - 1; i >= 0; i--) {
        if (a[i] >= n - 1 - i) {
          last = i;
        } else {
          break;
        }
      }

      out.println(last <= first ? "Yes" : "No");
    }
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