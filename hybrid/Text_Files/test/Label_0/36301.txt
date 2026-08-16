import java.io.*;
import java.util.*;

class Edge {
  final int id, dst;
  
  Edge(int id, int dst) {
    this.id = id;
    this.dst = dst;
  }
}

class Solver {
  final int n, m;
  final int[][] abs;
  
  List<List<Edge>> graph;
  boolean[] visitedNode;
  boolean[] visitedEdge;
  List<Integer> edgeStack;
  List<String> output;
  
  Solver(int n, int m, int[][] abs) {
    this.n = n;
    this.m = m;
    this.abs = abs;
  }
  
  private void assignDirection(int edgeId1, int edgeId2) {
    int[] indexes = new int[]{
      abs[edgeId1][0],
      abs[edgeId1][1],
      abs[edgeId2][0],
      abs[edgeId2][1]
    };
    int srcIndex = 0;
    for (int i = 0; i < 4; i++) {
      for (int j = i+1; j < 4; j++) {
        if (indexes[i] == indexes[j]) {
          srcIndex = indexes[i];
        }
      }
    }
    if (srcIndex == 0) {
      throw new RuntimeException();
    }
    for (int index : indexes) {
      if (index == srcIndex) {
        continue;
      }
      output.add(String.format("%d %d", srcIndex, index));
    }
  }
  
  private void mightAssignDirection() {
    if (edgeStack.size() < 4) {
      return;
    }
    int edgeId1 = edgeStack.get(edgeStack.size() - 1);
    int edgeId2 = edgeStack.get(edgeStack.size() - 2);
    int edgeId3 = edgeStack.get(edgeStack.size() - 3);
    int edgeId4 = edgeStack.get(edgeStack.size() - 4);
    if ((edgeId1 == edgeId2 && edgeId3 == edgeId4)
        || (edgeId1 == edgeId4 && edgeId2 == edgeId3)) {
      edgeStack.remove(edgeStack.size() - 1);
      edgeStack.remove(edgeStack.size() - 1);
      edgeStack.remove(edgeStack.size() - 1);
      edgeStack.remove(edgeStack.size() - 1);
      assignDirection(edgeId1, edgeId3);
    }
  }
  
  private void edgeDfs(int index) {
    if (visitedNode[index]) {
      return;
    }
    visitedNode[index] = true;
    for (Edge edge : graph.get(index)) {
      if (visitedEdge[edge.id]) {
        continue;
      }
      visitedEdge[edge.id] = true;
      
      edgeStack.add(edge.id);
      edgeDfs(edge.dst);
      edgeStack.add(edge.id);
      
      mightAssignDirection();
    }
  }
  
  public List<String> solve() {
    if (m % 2 == 1) {
      return Arrays.asList("-1");
    }
    
    graph = new ArrayList<>();
    visitedNode = new boolean[n + 1];
    visitedEdge = new boolean[m];
    edgeStack = new ArrayList<>();
    output = new ArrayList<>();
    for (int i = 0; i <= n; i++) {
      graph.add(new ArrayList<>());
    }
    for (int i = 0; i < m; i++) {
      int a = abs[i][0];
      int b = abs[i][1];
      graph.get(a).add(new Edge(i, b));
      graph.get(b).add(new Edge(i, a));
    }
    edgeDfs(1);
    return output;
  }
}

public class Main {
  private static void execute(ContestReader reader, PrintWriter out) {
    int n = reader.nextInt();
    int m = reader.nextInt();
    int[][] abs = reader.nextInt(m, 2);
    for (String line : new Solver(n, m, abs).solve()) {
      out.println(line);
    }
  }
  
  public static void main(String[] args) {
    ContestReader reader = new ContestReader(System.in);
    PrintWriter out = new PrintWriter(System.out);
    execute(reader, out);
    out.flush();
  }
}

class ContestReader {
  private BufferedReader reader;
  private StringTokenizer tokenizer;
  
  ContestReader(InputStream in) {
    reader = new BufferedReader(new InputStreamReader(in));
  }
  
  public String next() {
    while (tokenizer == null || !tokenizer.hasMoreTokens()) {
      try {
        tokenizer = new java.util.StringTokenizer(reader.readLine());
      } catch (Exception e) {
        throw new RuntimeException(e);
      }
    }
    return tokenizer.nextToken();
  }
  
  public int nextInt() {
    return Integer.parseInt(next());
  }
  
  public long nextLong() {
    return Long.parseLong(next());
  }
  
  public double nextDouble() {
    return Double.parseDouble(next());
  }
  
  public String[] next(int n) {
    String[] array = new String[n];
    for (int i = 0; i < n; i++) {
      array[i] = next();
    }
    return array;
  }
  
  public int[] nextInt(int n) {
    int[] array = new int[n];
    for (int i = 0; i < n; i++) {
      array[i] = nextInt();
    }
    return array;
  }
  
  public long[] nextLong(int n) {
    long[] array = new long[n];
    for (int i = 0; i < n; i++) {
      array[i] = nextLong();
    }
    return array;
  }
  
  public double[] nextDouble(int n) {
    double[] array = new double[n];
    for (int i = 0; i < n; i++) {
      array[i] = nextDouble();
    }
    return array;
  }
  
  public char[] nextCharArray() {
    return next().toCharArray();
  }
  
  public int[][] nextInt(int n, int m) {
    int[][] matrix = new int[n][m];
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        matrix[i][j] = nextInt();
      }
    }
    return matrix;
  }
  
  public long[][] nextLong(int n, int m) {
    long[][] matrix = new long[n][m];
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        matrix[i][j] = nextLong();
      }
    }
    return matrix;
  }
  
  public double[][] nextDouble(int n, int m) {
    double[][] matrix = new double[n][m];
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        matrix[i][j] = nextDouble();
      }
    }
    return matrix;
  }
  
  public char[][] nextCharArray(int n) {
    char[][] matrix = new char[n][];
    for (int i = 0; i < n; i++) {
      matrix[i] = next().toCharArray();
    }
    return matrix;
  }
}
