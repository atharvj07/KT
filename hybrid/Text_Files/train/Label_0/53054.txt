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
    TaskD solver = new TaskD();
    solver.solve(1, in, out);
    out.close();
  }

  static class TaskD {

    public void solve(int testNumber, InputReader in, OutputWriter out) {
      // Random random = new Random(0xdead);
      // for (int it = 0; it < 1000; ++it) {
      //     int n = random.nextInt(10) + 1;
      //     int m = random.nextInt(10) + 1;
      //     int[] p = new int[n * m];
      //     for (int i = 0; i < p.length; ++i) {
      //         p[i] = i;
      //     }
      //     for (int i = 0; i < p.length; ++i) {
      //         int j = random.nextInt(p.length);
      //         int t = p[i];
      //         p[i] = p[j];
      //         p[j] = t;
      //     }
      //     int[][] a = new int[n][m];
      //     for (int i = 0; i < n; ++i)
      //         for (int j = 0; j < m; ++j)
      //             a[i][j] = p[i * m + j];
      //     for (int i = 0; i < n; ++i) {
      //         for (int j = 0; j < m; ++j) {
      //             System.err.print((a[i][j] + 1) + " ");
      //         }
      //         System.err.println();
      //     }
      //     doSolveSimple(a);
      // }

      int n = in.nextInt();
      int m = in.nextInt();
      int[][] a = new int[n][m];
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
          a[i][j] = in.nextInt() - 1;
        }
      }
      doSolve(out, n, m, a);
    }

    public void doSolve(OutputWriter out, int n, int m, int[][] a) {
      int[][] ind = new int[n][n];
      boolean[][] g = new boolean[n][n];
      for (int col = 0; col < m; ++col) {
        for (int i = 0; i < n; ++i) {
          Arrays.fill(g[i], false);
          for (int j = col; j < m; ++j) {
            g[i][a[i][j] / m] = true;
            ind[i][a[i][j] / m] = j;
          }
        }
        int[] matching = new int[n];
        MaxMatching.maxMatching(g, matching);
        for (int i = 0; i < n; ++i) {
          int row = matching[i];
          int pos = ind[row][i];
          {
            int t = a[row][pos];
            a[row][pos] = a[row][col];
            a[row][col] = t;
          }
        }
      }
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
          out.print((a[i][j] + 1) + " ");
        }
        out.printLine();
      }
      while (true) {
        boolean ch = false;
        for (int i = 0; i < n; ++i) {
          for (int j = 0; j < m; ++j) {
            int row = a[i][j] / m;
            if (row != i) {
              int t = a[i][j];
              a[i][j] = a[row][j];
              a[row][j] = t;
              ch = true;
            }
          }
        }
        if (!ch) {
          break;
        }
      }
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
          out.print((a[i][j] + 1) + " ");
        }
        out.printLine();
      }
      for (int i = 0; i < n; ++i) {
        Arrays.sort(a[i]);
        for (int j = 0; j < m; ++j) {
          if (a[i][j] != i * m + j) {
            throw new RuntimeException();
          }
        }
      }
    }

  }

  static class MaxMatching {

    static boolean findPath(int u1, boolean[][] d, int[] matching, boolean[] vis) {
      vis[u1] = true;
      for (int v = 0; v < matching.length; ++v) {
        int u2 = matching[v];
        if (d[u1][v] && (u2 == -1 || !vis[u2] && findPath(u2, d, matching, vis))) {
          matching[v] = u1;
          return true;
        }
      }
      return false;
    }

    public static int maxMatching(boolean[][] d, /* out */ int[] matching) {
      int n1 = d.length;
      int n2 = n1 == 0 ? 0 : d[0].length;
      Arrays.fill(matching, -1);
      int matches = 0;
      for (int u = 0; u < n1; u++) {
        if (findPath(u, d, matching, new boolean[n1])) {
          ++matches;
        }
      }
      return matches;
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

