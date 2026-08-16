import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.io.BufferedWriter;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.util.BitSet;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author Jialin Ouyang (Jialin.Ouyang@gmail.com)
 */
public class Main {
  public static void main(String[] args) {
    InputStream inputStream = System.in;
    OutputStream outputStream = System.out;
    QuickScanner in = new QuickScanner(inputStream);
    QuickWriter out = new QuickWriter(outputStream);
    TaskD solver = new TaskD();
    solver.solve(1, in, out);
    out.close();
  }

  static class TaskD {
    int n;
    int m;
    BitSet[] matrix;
    int[] row;
    int[] column;

    public void solve(int testNumber, QuickScanner in, QuickWriter out) {
      n = in.nextInt();
      m = in.nextInt();
      matrix = new BitSet[n];
      for (int i = 0; i < n; ++i) {
        matrix[i] = new BitSet(n);
      }
      row = new int[m];
      column = new int[m];
      for (int i = 0; i < m; ++i) {
        row[i] = in.nextInt() - 1;
        column[i] = in.nextInt() - 1;
        matrix[row[i]].set(column[i]);
      }
      Matrix01Utils.inverse(n, matrix, matrix);
      for (int i = 0; i < m; ++i) {
        out.println(matrix[column[i]].get(row[i]) ? "NO" : "YES");
      }
    }

  }

  static class QuickScanner {
    private static final int BUFFER_SIZE = 1024;
    private InputStream stream;
    private byte[] buffer;
    private int currentPosition;
    private int numberOfChars;

    public QuickScanner(InputStream stream) {
      this.stream = stream;
      this.buffer = new byte[BUFFER_SIZE];
      this.currentPosition = 0;
      this.numberOfChars = 0;
    }

    public int nextInt() {
      int c = nextNonSpaceChar();
      boolean positive = true;
      if (c == '-') {
        positive = false;
        c = nextChar();
      }
      int res = 0;
      do {
        if (c < '0' || '9' < c) throw new RuntimeException();
        res = res * 10 + c - '0';
        c = nextChar();
      } while (!isSpaceChar(c));
      return positive ? res : -res;
    }

    public int nextNonSpaceChar() {
      int res = nextChar();
      for (; isSpaceChar(res) || res < 0; res = nextChar()) ;
      return res;
    }

    public int nextChar() {
      if (numberOfChars == -1) {
        throw new RuntimeException();
      }
      if (currentPosition >= numberOfChars) {
        currentPosition = 0;
        try {
          numberOfChars = stream.read(buffer);
        } catch (Exception e) {
          throw new RuntimeException(e);
        }
        if (numberOfChars <= 0) {
          return -1;
        }
      }
      return buffer[currentPosition++];
    }

    public boolean isSpaceChar(int c) {
      return c == ' ' || c == '\t' || isEndOfLineChar(c);
    }

    public boolean isEndOfLineChar(int c) {
      return c == '\n' || c == '\r' || c < 0;
    }

  }

  static class Matrix01Utils {
    private static BitSet[] tmp;

    public static void inverse(int n, BitSet[] a, BitSet[] res) {
      if (a == res) {
        initInternal(n);
      }
      BitSet[] tmp = a == res ? Matrix01Utils.tmp : res;
      for (int i = 0; i < n; ++i) {
        tmp[i].clear();
        tmp[i].set(i);
      }
      for (int column = 0; column < n; ++column) {
        if (!a[column].get(column)) {
          int rowIdx = -1;
          for (int row = column + 1; row < n; ++row) {
            if (a[row].get(column)) {
              rowIdx = row;
              break;
            }
          }
          if (rowIdx < 0) throw new IllegalArgumentException("Not invertible.");
          BitSet tmpBS;
          tmpBS = a[column];
          a[column] = a[rowIdx];
          a[rowIdx] = tmpBS;
          tmpBS = tmp[column];
          tmp[column] = tmp[rowIdx];
          tmp[rowIdx] = tmpBS;
        }
        for (int row = column + 1; row < n; ++row)
          if (a[row].get(column)) {
            a[row].xor(a[column]);
            tmp[row].xor(tmp[column]);
          }
      }
      for (int column = n - 1; column >= 0; --column) {
        for (int row = column - 1; row >= 0; --row)
          if (a[row].get(column)) {
            a[row].xor(a[column]);
            tmp[row].xor(tmp[column]);
          }
      }
      if (res != tmp) {
        for (int i = 0; i < n; ++i) {
          res[i] = tmp[i];
        }
      }
    }

    private static void initInternal(int n) {
      if (tmp == null || tmp.length < n || tmp[0].size() < n) {
        int n2 = Integer.highestOneBit(n) << 1;
        tmp = new BitSet[n2];
        for (int i = 0; i < n2; ++i) {
          tmp[i] = new BitSet(n2);
        }
      }
    }

  }

  static class QuickWriter {
    private final PrintWriter writer;

    public QuickWriter(OutputStream outputStream) {
      this.writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(outputStream)));
    }

    public QuickWriter(Writer writer) {
      this.writer = new PrintWriter(writer);
    }

    public void print(Object... objects) {
      for (int i = 0; i < objects.length; ++i) {
        if (i > 0) {
          writer.print(' ');
        }
        writer.print(objects[i]);
      }
    }

    public void println(Object... objects) {
      print(objects);
      writer.print('\n');
    }

    public void close() {
      writer.close();
    }

  }
}

