import java.awt.geom.Point2D;
import java.io.IOException;
import java.io.InputStream;
import java.util.*;
import java.util.function.BiFunction;
import java.util.function.Function;
import java.util.function.Supplier;

public class Main {
  final static int INF = 1 << 28;
  final static long MOD = 1_000_000_007;
  final static double EPS = 1e-9;
  final static double GOLDEN_RATIO = (1.0 + Math.sqrt(5)) / 2.0;
  Scanner sc = new Scanner(System.in);

  public static void main(String[] args) {
    new Main().run();
  }

  static int[][] ofs = {
      {0, -1},
      {1, 0},
      {0, 1},
      {-1, 0}
  };

  static int min = INF;
  static int count = 0;

  static class State implements Comparable<State> {
    int x, y;
    int dir;

    final static State[][][] LUT;

    private State(int x, int y, int dir) {
      this.x = x;
      this.y = y;
      this.dir = dir;
    }

    static State valueOf(int x, int y, int dir) {
      if (field[y][x] == 'g') {
        min = Math.min(min, count);
      }
      return LUT[x][y][dir];
    }

    static {
      State[][][] table = new State[50][50][4];
      for (int i = 0; i < 50; ++i) {
        for (int j = 0; j < 50; ++j) {
          for (int k = 0; k < 4; ++k) {
            table[i][j][k] = new State(i, j, k);
          }
        }
      }
      LUT = table;
    }

    State next(char c) {
      switch (c) {
        case '^':
          if (is('C')) {
            return this;
          } else {
            return valueOf(x + ofs[dir][0], y + ofs[dir][1], dir);
          }
        case 'v':
          if (is('D')) {
            return this;
          } else {
            return valueOf(x + ofs[(dir + 2) % 4][0], y + ofs[(dir + 2) % 4][1], dir);
          }
        case '<':
          return valueOf(x, y, (dir - 1 + 4) % 4);
        case '>':
          return valueOf(x, y, (dir + 1) % 4);
        default:
          assert false;
          return null;
      }
    }

    boolean is(char c) {
      switch (c) {
        case 'N':
          return dir == 0;
        case 'E':
          return dir == 1;
        case 'S':
          return dir == 2;
        case 'W':
          return dir == 3;
        case 'C':
          return field[y + ofs[dir][1]][x + ofs[dir][0]] == '#';
        case 'D':
          return field[y + ofs[(dir + 2) % 4][1]][x + ofs[(dir + 2) % 4][0]] == '#';
        default:
          return true;
      }
    }

    boolean is(String s) {
      if (s.length() == 1) {
        return is(s.charAt(0));
      } else {
        return !is(s.charAt(1));
      }
    }

    @Override
    public int compareTo(State s) {
      if (x != s.x) {
        return x - s.x;
      }
      if (y != s.y) {
        return y - s.y;
      }
      return dir - s.dir;
    }
  }

  int h, w;
  static char[][] field;
  String s;

//  TreeSet<Ret> done = new TreeSet<>();

  boolean isIf(int index) {
    return s.charAt(index) == '[';
  }

  boolean isWhile(int index) {
    return s.charAt(index) == '{';
  }

  boolean isCmd(int index) {
    switch (s.charAt(index)) {
      case '^':
      case 'v':
      case '<':
      case '>':
        return true;
      default:
        return false;
    }
  }

  String jouken(int index) {
    if (s.charAt(index) == '~') {
      return "" + s.charAt(index) + s.charAt(index + 1);
    } else {
      return "" + s.charAt(index);
    }
  }

  class Ret implements Comparable<Ret> {
    int index;
    State state;

    Ret(int i, State s) {
      index = i;
      state = s;
    }

    @Override
    public int compareTo(Ret d) {
      if (index != d.index) {
        return index - d.index;
      }
      return state.compareTo(d.state);
    }
  }

  Ret bun(int index, State state) {
    if (isIf(index)) {
      ++index;
      String jouken = jouken(index);
      index += jouken.length();
      if (state.is(jouken)) {
        Ret ret = program(index, state);
        if (ret == null) {
          return null;
        }
        state = ret.state;
      }
      int indent = 0;
      for (; ; ) {
        if (s.charAt(index) == '[') {
          ++indent;
        }
        if (s.charAt(index) == ']') {
          if (indent == 0) {
            break;
          }
          --indent;
        }
        ++index;
      }
      ++index;
      return new Ret(index, state);
    } else if (isWhile(index)) {
      ++index;
      String jouken = jouken(index);
      index += jouken.length();
      while (state.is(jouken)) {
        Ret ret = program(index, state);
        if (ret == null) {
          return null;
        }
        state = ret.state;
      }
      int indent = 0;
      for (; ; ) {
        if (s.charAt(index) == '{') {
          ++indent;
        }
        if (s.charAt(index) == '}') {
          if (indent == 0) {
            break;
          }
          --indent;
        }
        ++index;
      }
      ++index;
      return new Ret(index, state);
    } else {
      assert isCmd(index);
      char cmd = s.charAt(index);
      ++index;
      ++count;
      state = state.next(cmd);
      return new Ret(index, state);
    }
  }

  Ret program(int index, State state) {
//    Ret init = new Ret(index, state);
//    if (done.contains(init)) {
//      return null;
//    }
//    done.add(init);
    while (index < s.length()) {
      if (done[index][state.y][state.x][state.dir]) {
        return null;
      }
      done[index][state.y][state.x][state.dir] = true;
      char c = s.charAt(index);
      if (c == ']' || c == '}') {
        return new Ret(index + 1, state);
      }
      Ret ret = bun(index, state);
      if (ret == null) {
        return null;
      }
//      if (done.contains(ret)) {
//        return null;
//      }
//      done.add(ret);
      index = ret.index;
      state = ret.state;
    }
    return new Ret(index, state);
  }

  boolean[][][][] done;

  void run() {
    h = ni();
    w = ni();
    field = new char[h][w];
    State init = null;
    for (int i = 0; i < h; ++i) {
      String str = sc.next();
      for (int j = 0; j < w; ++j) {
        field[i][j] = str.charAt(j);
        if (field[i][j] == 's') {
          init = State.valueOf(j, i, 0);
        }
      }
    }
    s = sc.next();
    done = new boolean[s.length()][h][w][4];
    program(0, init);
    System.out.println(min == INF ? -1 : min);
  }

  int ni() {
    return Integer.parseInt(sc.next());
  }

  void debug(Object... os) {
    System.err.println(Arrays.deepToString(os));
  }
}