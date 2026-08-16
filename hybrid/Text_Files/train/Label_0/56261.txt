/**
 * <p>
 * Unsolved
 * </p>
 * <p>
 * Created on Jul 30, 2012, 11:28:20 AM
 * </p>
 * @Author Andy Y.F. Huang
 */
public class p214CGame {
  
  private int go(int comp[], boolean graph[][], int start) {
    int len = comp.length;
    boolean done[] = new boolean[len];
    int inDegree[] = new int[len];
    for (int i = 0; i < len; i++)
      for (int j = 0; j < len; j++)
        if (graph[i][j])
          inDegree[j]++;
    int done_cnt = 0, cost = 0;
    while (done_cnt < len) {
      while (true) {
        boolean changed = false;
        for (int i = 0; i < len; i++) {
          if (!done[i] && comp[i] == start && inDegree[i] == 0) {
            changed = true;
            done[i] = true;
            cost++;
            done_cnt++;
            for (int j = 0; j < len; j++)
              if (graph[i][j])
                inDegree[j]--;
          }
        }
        if (!changed)
          break;
      }
      if (done_cnt == len)
        break;
      start = (start + 1) % 3;
      cost++;
    }
    return cost;
  }
  
  private void solve(int test_number) {
    int vertices = in.nextInt();
    int comp[] = new int[vertices];
    for (int i = 0; i < vertices; i++)
      comp[i] = in.nextInt() - 1;
    boolean graph[][] = new boolean[vertices][vertices];
    for (int i = 0; i < vertices; i++) {
      int deg = in.nextInt();
      for (int j = 0; j < deg; j++) 
        graph[in.nextInt() - 1][i] = true;
    }
    int ans = 123456789;
    for (int i = 0; i < 3; i++) 
      ans = Math.min(ans, go(comp, graph, i));
    out.appendln(ans);
  }

  private Input in;
  private Output out;

  void solve() {
    in = new Input("");
    out = new Output("");
    solve(1);
    out.close();
  }

  public static void main(String[] args) {
    p214CGame solver = new p214CGame();
    solver.solve();
  }

  static void pln(Object... obj) {
    pf(obj);
    System.out.println();
  }

  static void pf(Object... obj) {
    for (int i = 0; i < obj.length; i++) {
      if (i != 0)
        System.out.print(' ');
      System.out.print(obj[i]);
    }
  }
}

class Input {
  private java.io.BufferedReader reader;
  private java.util.StringTokenizer tokenizer;

  Input(String filename) {
    if (!filename.isEmpty()) {
      try {
        reader = new java.io.BufferedReader(new java.io.FileReader(filename));
      }
      catch (java.io.FileNotFoundException e) {
        throw new RuntimeException(e);
      }
    }
    else
      reader = new java.io.BufferedReader(new java.io.InputStreamReader(
          System.in));
    tokenizer = new java.util.StringTokenizer("");
  }

  String next() {
    while (!tokenizer.hasMoreTokens()) {
      try {
        tokenizer = new java.util.StringTokenizer(reader.readLine());
      }
      catch (java.io.IOException e) {
        throw new RuntimeException(e);
      }
    }
    return tokenizer.nextToken();
  }

  String nextLine() {
    try {
      return reader.readLine();
    }
    catch (java.io.IOException e) {
      throw new RuntimeException(e);
    }
  }

  long nextLong() {
    return Long.parseLong(next());
  }

  int nextInt() {
    return Integer.parseInt(next());
  }

  double nextDouble() {
    return Double.parseDouble(next());
  }

}

class Output {
  private java.io.PrintWriter buffer;

  Output(String filename) {
    if (!filename.isEmpty())
      try {
        buffer = new java.io.PrintWriter(filename);
      }
      catch (java.io.FileNotFoundException e) {
        throw new RuntimeException();
      }
    else
      buffer = new java.io.PrintWriter(System.out);
  }

  void flush() {
    buffer.flush();
  }

  void close() {
    buffer.close();
  }

  void append(Object... obj) {
    for (int i = 0; i < obj.length; i++) {
      if (i != 0)
        buffer.write(' ');
      buffer.print(obj[i]);
    }
  }

  void appendln(Object... obj) {
    append(obj);
    buffer.write('\n');
  }

}