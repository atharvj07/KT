import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.io.BufferedWriter;
import java.util.InputMismatchException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.util.Collections;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author Rustam Musin (t.me/musin_acm)
 */
public class Main {
  public static void main(String[] args) {
    InputStream inputStream = System.in;
    OutputStream outputStream = System.out;
    InputReader in = new InputReader(inputStream);
    OutputWriter out = new OutputWriter(outputStream);
    ETestiDlyaZadachiD solver = new ETestiDlyaZadachiD();
    solver.solve(1, in, out);
    out.close();
  }

  static class ETestiDlyaZadachiD {
    int n;
    List<Integer>[] g;

    public void solve(int testNumber, InputReader in, OutputWriter out) {
      n = in.readInt();
      g = new List[n];
      for (int i = 0; i < n; i++) {
        g[i] = new ArrayList<>();
      }
      for (int i = 0; i < n - 1; i++) {
        int x = in.readInt() - 1;
        int y = in.readInt() - 1;
        g[x].add(y);
        g[y].add(x);
      }
      if (false) {
        n = (int) 1e5;
        g = new List[n];
        for (int i = 0; i < n; i++) {
          g[i] = new ArrayList<>();
          if (i + 1 < n) g[i].add(i + 1);
        }
      }
//    Node answer = dfs(0, -1);
      ETestiDlyaZadachiD.Node answer = bfs();
      int offset = answer.start;
      ETestiDlyaZadachiD.Segment[] toPrint = new ETestiDlyaZadachiD.Segment[n];
      for (int i = 0; i < n; i++) {
        ETestiDlyaZadachiD.Segment cur = answer.segments.get(i);
        toPrint[cur.index] = cur;
      }
      for (int i = 0; i < n; i++) out.printLine(toPrint[i].from - offset + 1, toPrint[i].to - offset + 1);
    }

    ETestiDlyaZadachiD.Node bfs() {
      int[] parent = new int[n];
      Arrays.fill(parent, -1);
      int[] q = new int[n];
      int qs = 0;
      q[qs++] = 0;
      boolean[] used = new boolean[n];
      used[0] = true;
      for (int qi = 0; qi < qs; qi++) {
        int v = q[qi];
        for (int to : g[v])
          if (!used[to]) {
            parent[to] = v;
            q[qs++] = to;
            used[to] = true;
          }
      }
      ETestiDlyaZadachiD.Node[] res = new ETestiDlyaZadachiD.Node[n];
      for (int it = n - 1; it >= 0; it--) {
        int v = q[it];
        List<ETestiDlyaZadachiD.Node> children = new ArrayList<>();
        for (int to : g[v]) if (to != parent[v]) children.add(res[to]);
        if (children.isEmpty()) {
          List<ETestiDlyaZadachiD.Segment> cur = new ArrayList<>();
          cur.add(new ETestiDlyaZadachiD.Segment(v, 0, 1));
          res[v] = new ETestiDlyaZadachiD.Node(0, cur);
          continue;
        }

        int maxSize = 0;
        for (var c : children) maxSize = Math.max(maxSize, c.size());
        for (int i = 0; i < children.size(); i++) {
          if (children.get(i).size() == maxSize) {
            Collections.swap(children, 0, i);
            break;
          }
        }
        ETestiDlyaZadachiD.Node firstGroup = children.get(0);
        ETestiDlyaZadachiD.Segment firstPartParent = firstGroup.getLast();
        ETestiDlyaZadachiD.Segment curSegment = new ETestiDlyaZadachiD.Segment(v, firstPartParent.to++, -1);
        int nextEnd = curSegment.from + 2;
        for (int i = 1; i < children.size(); i++)
          firstGroup.add(children.get(i), nextEnd++);
        curSegment.to = nextEnd;
        firstGroup.segments.add(curSegment);
        res[v] = firstGroup;
      }
      return res[0];
    }

    static class Node {
      int start;
      List<ETestiDlyaZadachiD.Segment> segments;

      Node(int start, List<ETestiDlyaZadachiD.Segment> segments) {
        this.start = start;
        this.segments = segments;
      }

      int size() {
        return segments.size();
      }

      void add(ETestiDlyaZadachiD.Node other, int putLastAt) {
        int addOffset = -2 * other.size() + 1 + start - other.start;
        List<ETestiDlyaZadachiD.Segment> oSeg = other.segments;
        for (int i = 0; i < oSeg.size(); i++) {
          ETestiDlyaZadachiD.Segment cur = oSeg.get(i);
          cur.from += addOffset;
          cur.to += addOffset;
          segments.add(cur);
          if (i + 1 == oSeg.size()) cur.to = putLastAt;
        }
        start -= oSeg.size() * 2 - 1;
      }

      ETestiDlyaZadachiD.Segment getLast() {
        return segments.get(segments.size() - 1);
      }

    }

    static class Segment {
      int index;
      int from;
      int to;

      public Segment(int index, int from, int to) {
        this.index = index;
        this.from = from;
        this.to = to;
      }

      public String toString() {
        return "Segment{" +
            "index=" + index +
            ", from=" + from +
            ", to=" + to +
            '}';
      }

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
    private byte[] buf = new byte[1024];
    private int curChar;
    private int numChars;
    private InputReader.SpaceCharFilter filter;

    public InputReader(InputStream stream) {
      this.stream = stream;
    }

    public int read() {
      if (numChars == -1) {
        throw new InputMismatchException();
      }
      if (curChar >= numChars) {
        curChar = 0;
        try {
          numChars = stream.read(buf);
        } catch (IOException e) {
          throw new InputMismatchException();
        }
        if (numChars <= 0) {
          return -1;
        }
      }
      return buf[curChar++];
    }

    public int readInt() {
      int c = read();
      while (isSpaceChar(c)) {
        c = read();
      }
      int sgn = 1;
      if (c == '-') {
        sgn = -1;
        c = read();
      }
      int res = 0;
      do {
        if (c < '0' || c > '9') {
          throw new InputMismatchException();
        }
        res *= 10;
        res += c - '0';
        c = read();
      } while (!isSpaceChar(c));
      return res * sgn;
    }

    public boolean isSpaceChar(int c) {
      if (filter != null) {
        return filter.isSpaceChar(c);
      }
      return isWhitespace(c);
    }

    public static boolean isWhitespace(int c) {
      return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
    }

    public interface SpaceCharFilter {
      public boolean isSpaceChar(int ch);

    }

  }
}

