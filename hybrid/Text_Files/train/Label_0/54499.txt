import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.Arrays;
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
    static final int maxn = 1001 * 1000;

    public void solve(int testNumber, InputReader in, OutputWriter out) {
      int[] a = new int[maxn];
      int n = in.nextInt();
      for (int i = 0; i < n; ++i) {
        a[in.nextInt()] += 1;
      }
      int[] b = new int[maxn];
      int[] c = new int[maxn];
      for (int i = 0; i < maxn; ++i) {
        if (a[i] == 0) {
          b[i] = 0;
          c[i] = 0;
          continue;
        }
        long val = a[i];
        val *= i;
        val %= mod;
        b[i] = (int) val;
        val *= i;
        val %= mod;
        c[i] = (int) val;
      }

      int[] mu = new int[maxn];
      Arrays.fill(mu, 1);
      for (int i = 2; i * i < maxn; ++i) {
        if (mu[i] == 1) {
          for (int j = i; j < maxn; j += i) {
            mu[j] *= -i;
          }
          for (int j = i * i; j < maxn; j += i * i) {
            mu[j] *= 0;
          }
        }
      }
      for (int i = 2; i < maxn; ++i) {
        if (mu[i] == i) {
          mu[i] = 1;
        } else if (mu[i] == -i) {
          mu[i] = -1;
        } else if (mu[i] < 0) {
          mu[i] = 1;
        } else if (mu[i] > 0) {
          mu[i] = -1;
        }
      }

      long res = 0;
      for (int g = 1; g < maxn; ++g) {
        long cur = 0;
        for (int i = 1; g * i < maxn; ++i) {
          if (mu[i] != 0) {
            int x = i * g;
            int sum = 0, sum2 = 0;
            for (int j = x; j < maxn; j += x) {
              if (b[j] > 0) {
                sum = (sum + b[j]) % mod;
                sum2 = (sum2 + c[j]) % mod;
              }
            }
            if (sum == 0 && sum2 == 0) {
              continue;
            }
            long inc = (sum * (long) sum - sum2 + mod) % mod;
            cur += mu[i] * inc + mod;
            cur %= mod;
          }
        }
        cur *= IntegerUtils.pow(g, mod - 2, mod);
        cur %= mod;
        res += cur;
        res %= mod;
      }
      res *= IntegerUtils.pow(2, mod - 2, mod);
      res %= mod;
      out.printLine(res);
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

  static class IntegerUtils {

    public static int pow(long x, long y, int mod) {
      x %= mod;
      long res = 1;
      while (y > 0) {
        if (y % 2 == 1) {
          --y;
          res = (res * x) % mod;
        } else {
          y /= 2;
          x = (x * x) % mod;
        }
      }
      return (int) (res % mod);
    }

  }
}

