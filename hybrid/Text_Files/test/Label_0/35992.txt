import java.awt.geom.Point2D;
import java.io.IOException;
import java.io.InputStream;
import java.util.*;
import java.util.function.BiFunction;
import java.util.function.Function;
import java.util.function.Supplier;

public class Main {
  final static int INF = 1 << 28;
  final static long LNF = 1L << 60;
  final static long MOD = 1_000_000_007;
  final static double EPS = 1e-9;
  final static double GOLDEN_RATIO = (1.0 + Math.sqrt(5)) / 2.0;
  Scanner sc = new Scanner(System.in);

  public static void main(String[] args) {
    new Main().run();
  }

  class Iku {
    int dist;
    long cost;

    @Override
    public String toString() {
      return "{" + dist + ", " + cost + "}";
    }
  }

  class Node {
    int index;
    List<Iku> adj = new LinkedList<>();
  }

  class Group {
    int n;
    long[] arr;
    boolean loop;
  }

  long kasanari(long[] p1, long[] p2, int s) {
    boolean flag = true;
    long[] d = new long[3];
    for (int i = 0; i < 3; ++i) {
      long min = Math.min(p1[i], p2[i]);
      long max = Math.max(p1[i], p2[i]);
      flag &= max < min + s;
      d[i] = min + s - max;
    }
    if (!flag) {
      return 0;
    }
    long sum = 0;
    for (int i = 0; i < 3; ++i) {
      for (int j = i + 1; j < 3; ++j) {
        sum += (d[i] * d[j]) * 2;
      }
    }
    return sum;
  }

  void run() {
    for (; ; ) {
      int n = ni();
      int k = ni();
      int s = ni();
      if (n == 0) {
        break;
      }
      long[][] p = new long[n][3];
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < 3; ++j) {
          p[i][j] = ni();
        }
      }
      ArrayList<Node> list = new ArrayList<>();
      for (int i = 0; i < n; ++i) {
        Node node = new Node();
        node.index = i;
        list.add(node);
      }
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
          if (i == j) {
            continue;
          }
          long menseki = kasanari(p[i], p[j], s);
          if (menseki == 0) {
            continue;
          }
          Iku iku = new Iku();
          iku.dist = j;
          iku.cost = menseki;
          list.get(i).adj.add(iku);
        }
      }
      ArrayList<Node> sorted = new ArrayList<>(list);
      sorted.sort(Comparator.comparingInt(a -> a.adj.size()));
      ArrayList<Group> groups = new ArrayList<>();
      boolean[] done = new boolean[n];
      for (Node node : sorted) {
        if (done[node.index]) {
          continue;
        }
        done[node.index] = true;
        ArrayList<Long> arr = new ArrayList<>();
        Node now = node;
        for (; ; ) {
          Node next = null;
          for (Iku iku : now.adj) {
            if (!done[iku.dist]) {
              next = list.get(iku.dist);
              arr.add(iku.cost);
              break;
            }
          }
          if (next == null) {
            break;
          }
          done[next.index] = true;
          now = next;
        }
        Group group = new Group();
        group.loop = node.adj.size() == 2;
        if (group.loop) {
          Node next = null;
          for (Iku iku : now.adj) {
            if (iku.dist == node.index) {
              next = list.get(iku.dist);
              arr.add(iku.cost);
              break;
            }
          }
          assert next != null;
        }
        group.n = arr.size();
        group.arr = new long[group.n];
        for (int i = 0; i < group.n; ++i) {
          group.arr[i] = arr.get(i);
        }
        groups.add(group);
      }
      long max = 0;
      boolean ok = false;
      for (Group g : groups) {
        if (g.loop) {
          if (g.n < k) {
            continue;
          }
          ok = true;
          if (g.n == k) {
            for (int i = 0; i < g.n; ++i) {
              long sum = 0;
              for (int j = 0; j < k; ++j) {
                sum += g.arr[(i + j) % g.n];
              }
              max = Math.max(max, sum);
            }
          } else {
            for (int i = 0; i < g.n; ++i) {
              long sum = 0;
              for (int j = 0; j < k - 1; ++j) {
                sum += g.arr[(i + j) % g.n];
              }
              max = Math.max(max, sum);
            }
          }
        } else {
          if (g.n + 1 < k) {
            continue;
          }
          ok = true;
          for (int i = 0; i < g.n - k + 2; ++i) {
            long sum = 0;
            for (int j = 0; j < k - 1; ++j) {
              sum += g.arr[i + j];
            }
            max = Math.max(max, sum);
          }
        }
      }
      System.out.println(ok ? s * s * k * 6 - max : -1);
    }
  }

  int ni() {
    return Integer.parseInt(sc.next());
  }

  void debug(Object... os) {
    System.err.println(Arrays.deepToString(os));
  }
}