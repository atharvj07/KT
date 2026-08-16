
import java.io.BufferedReader;
import java.io.Closeable;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

import static java.util.Comparator.comparingLong;

public class Main implements Closeable {

  private InputReader in = new InputReader(System.in);
  private PrintWriter out = new PrintWriter(System.out);

  private class Participant {
    private long height, power;

    private Participant(long height, long power) {
      this.height = height;
      this.power = power;
    }
  }

  public void solve() {
    int n = in.ni();
    Participant[] participants = new Participant[n];
    for (int i = 0; i < n; i++) {
      participants[i] = new Participant(in.nl(), in.nl());
    }
    Arrays.sort(participants, comparingLong(x -> x.height + x.power));
    long[][] dp = new long[2][n + 1];
    for (int i = 0; i < 2; i++) {
      for (int j = 0; j <= n; j++) {
        dp[i][j] = Long.MAX_VALUE;
      }
    }
    dp[0][0] = 0;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (dp[0][j] <= participants[i].height) {
          dp[1][j + 1] = Math.min(dp[1][j + 1], dp[0][j] + participants[i].power);
        }
        dp[1][j] = Math.min(dp[1][j], dp[0][j]);
      }
      dp[1][n] = Math.min(dp[0][n], dp[1][n]);

      long[] tmp = dp[0];
      Arrays.fill(tmp, Long.MAX_VALUE);
      dp[0] = dp[1];
      dp[1] = tmp;
    }
    for (int i = n; i >= 0; i--) {
      if (dp[0][i] != Long.MAX_VALUE) {
        out.println(i);
        return;
      }
    }
  }

  @Override
  public void close() throws IOException {
    in.close();
    out.close();
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

    public int ni() {
      return Integer.parseInt(next());
    }

    public long nl() {
      return Long.parseLong(next());
    }

    public void close() throws IOException {
      reader.close();
    }
  }

  public static void main(String[] args) throws IOException {
    try (Main instance = new Main()) {
      instance.solve();
    }
  }
}
