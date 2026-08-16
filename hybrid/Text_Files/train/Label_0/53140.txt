import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.io.BufferedWriter;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.util.InputMismatchException;
import java.io.IOException;
import java.io.InputStream;

/**
 * Built using CHelper plug-in Actual solution is at the top
 *
 * @author ilyakor
 */
public class Main {

  public static void main(String[] args) {
    InputStream inputStream = System.in;
    OutputStream outputStream = System.out;
    InputReader in = new InputReader(inputStream);
    OutputWriter out = new OutputWriter(outputStream);
    TaskC solver = new TaskC();
    solver.solve(1, in, out);
    out.close();
  }

  static class TaskC {

    static final int mod = 998244353;

    public void solve(int testNumber, InputReader in, OutputWriter out) {
      // {
      //     int n = 9;
      //     for (int i = 0; i < (1 << n); ++i) {
      //         int val = calc(i, n);
      //         if (val != 2 * n) {
      //             System.err.println(Integer.toString(i, 2) + " " + val);
      //             System.err.flush();
      //         }
      //     }
      // }
      //
      // int N = 12;
      // for (int i = 0; i < (1 << N); ++i) {
      //     String s = Integer.toString(i, 2);
      //     while (s.length() < N) s = "0" + s;
      //     int x = solve(N, s);
      //     int y = stupid(i, N);
      //     if (x != y) {
      //         solve(N, s);
      //         throw new RuntimeException();
      //     }
      // }

      int n = in.nextInt();
      String x = in.nextToken();
      int res = solve(n, x);
      out.printLine(res);

      // for (int n = 1; n <= 7; ++n) {
      //     for (int x = 0; x < (1 << n); ++x) {
      //         System.err.print(stupid(x, n) / 2 + " ");
      //         System.err.flush();
      //     }
      //     System.err.println();
      //     System.err.flush();
      // }
    }

    int solve(int n, String x) {
      char[] s = x.toCharArray();
      long res = 0;
      for (int i = 0; i < s.length; ++i) {
        res = (res * 2L + (long) (s[i] - '0')) % mod;
      }
      ++res;
      res *= 2L * n;
      res %= mod;
      int[] cnt = new int[n + 1];
      for (int i = 1; i <= n; ++i) {
        if (n % i != 0) {
          continue;
        }
        if ((n / i) % 2 == 0) {
          continue;
        }
        long val = 0;
        for (int j = 0; j < i; ++j) {
          val = (val * 2L + (long) (s[j] - '0')) % mod;
        }
        boolean ok = true;
        for (int j = 0; j < n; ++j) {
          int c = s[j % i] - '0';
          int pos = j / i;
          if (pos % 2 == 1) {
            c = 1 - c;
          }
          if (c == 1 && s[j] == '0') {
            ok = false;
            break;
          }
          if (c == 0 && s[j] == '1') {
            break;
          }
        }
        if (ok) {
          ++val;
        }
        val = (val % mod + mod) % mod;

        for (int j = 1; j * j <= i; ++j) {
          if (i % j == 0) {
            if ((i / j) % 2 == 1) {
              val -= cnt[j];
            }
            if (j != i / j && j % 2 == 1) {
              val -= cnt[i / j];
            }
          }
        }
        val = (val % mod + mod) % mod;

        cnt[i] = (int) val;

        res += (2L * i - 2L * n) * val;
        res %= mod;
        res += mod;
        res %= mod;
      }
      return (int) res;
    }

  }

  static class InputReader {

    private InputStream stream;
    private byte[] buffer = new byte[10000];
    private int cur;
    private int count;

    public InputReader(InputStream stream) {
      this.stream = stream;
    }

    public static boolean isSpace(int c) {
      return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
    }

    public int read() {
      if (count == -1) {
        throw new InputMismatchException();
      }
      try {
        if (cur >= count) {
          cur = 0;
          count = stream.read(buffer);
          if (count <= 0) {
            return -1;
          }
        }
      } catch (IOException e) {
        throw new InputMismatchException();
      }
      return buffer[cur++];
    }

    public int readSkipSpace() {
      int c;
      do {
        c = read();
      } while (isSpace(c));
      return c;
    }

    public String nextToken() {
      int c = readSkipSpace();
      StringBuilder sb = new StringBuilder();
      while (!isSpace(c)) {
        sb.append((char) c);
        c = read();
      }
      return sb.toString();
    }

    public int nextInt() {
      int sgn = 1;
      int c = readSkipSpace();
      if (c == '-') {
        sgn = -1;
        c = read();
      }
      int res = 0;
      do {
        if (c < '0' || c > '9') {
          throw new InputMismatchException();
        }
        res = res * 10 + c - '0';
        c = read();
      } while (!isSpace(c));
      res *= sgn;
      return res;
    }

  }

  static class OutputWriter {

    private final PrintWriter writer;

    public OutputWriter(OutputStream outputStream) {
      writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(outputStream)));
    }

    public OutputWriter(Writer writer) {
      this.writer = new PrintWriter(writer);
    }

    public void print(Object... objects) {
      for (int i = 0; i < objects.length; i++) {
        if (i != 0) {
          writer.print(' ');
        }
        writer.print(objects[i]);
      }
    }

    public void printLine(Object... objects) {
      print(objects);
      writer.println();
    }

    public void close() {
      writer.close();
    }

  }
}

