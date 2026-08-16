import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution1437C {
  public static void main(String[] args) {
    InputReader in = new InputReader(System.in);
    PrintWriter out = new PrintWriter(System.out);
    Solver1437C solver = new Solver1437C();
    int n = in.nextInt();
    for (int i = 0; i < n; i++) {
      solver.solve(i, in, out);
    }
    out.close();
  }

  static class Solver1437C {
    public void solve(int testNumber, InputReader in, PrintWriter out) {
      int n = in.nextInt();
      int[] t = new int[n];
      int[][] cache = new int[n][2*n+10];

      for (int i = 0; i < n; i++) {
        t[i] = in.nextInt();
        Arrays.fill(cache[i], -1);
      }

      Arrays.sort(t);
      minCost(0, 1, t, cache);
      out.println(cache[0][1]);
    }

    public int minCost(int s, int mintime, int[] t, int[][] cache) {
      if (s == t.length) {
        return 0;
      }

      if (cache[s][mintime] >= 0) {
        return cache[s][mintime];
      }

      int e = s;
      while (e < t.length && t[e] == t[s]) {
        e++;
      }

      int res = Integer.MAX_VALUE;

      for (int i = mintime; i <= Math.max(t[s], mintime); i++) {
        int incr = 0;
        for (int j = s; j < e; j++) {
          incr += Math.abs(t[j] - (i + j - s));
        }
        res = Math.min(res, incr + minCost(
            e, i + e - s, t, cache
        ));
      }

      cache[s][mintime] = res;

      return res;
    }
  }

  static class InputReader {
    public BufferedReader reader;
    public StringTokenizer tokenizer;

    public InputReader(InputStream stream) {
      reader = new BufferedReader(new InputStreamReader(stream), 32768);
      tokenizer = null;
    }

    public String next() {
      while (tokenizer == null || !tokenizer.hasMoreTokens()) {
        try {
          tokenizer = new StringTokenizer(reader.readLine());
        } catch (IOException e) {
          throw new RuntimeException(e);
        }
      }
      return tokenizer.nextToken();
    }

    public int nextInt() {
      return Integer.parseInt(next());
    }
  }
}