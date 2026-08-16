import java.io.*;
import java.util.*;

class Node implements Comparable<Node> {
  final int l, r;
  Node(int l, int r) {
    this.l = l;
    this.r = r;
  }
  
  public int compareTo(Node node) {
    return -1 * this.r + node.r;
  }
}

class Solver {
  final int n, m;
  final int[][] lrs;
  
  Solver(int n, int m, int[][] lrs) {
    this.n = n;
    this.m = m;
    this.lrs = lrs;
  }
  
  public int solve() {
    PriorityQueue<Node> rLargeFirstQueue = new PriorityQueue<>();
    for (int[] lr : lrs) {
      rLargeFirstQueue.add(new Node(lr[0], lr[1]));
    }
    
    PriorityQueue<Integer> lLargeFirstQueue = new PriorityQueue<>(new Comparator<Integer>(){
      public int compare(Integer i1, Integer i2) {
        return -1 * i1.compareTo(i2);
      }
    });
    PriorityQueue<Integer> lSmallFirstQueue = new PriorityQueue<>();
    
    for (int r = m + 1; !rLargeFirstQueue.isEmpty(); r--) {
      while (!rLargeFirstQueue.isEmpty() && rLargeFirstQueue.peek().r == r) {
        lLargeFirstQueue.add(rLargeFirstQueue.poll().l);
      }
      while (lLargeFirstQueue.size() > m + 1 - r) {
        lSmallFirstQueue.add(lLargeFirstQueue.poll());
      }
    }
    
    int answer = 0;
    int availableChair = 0;
    while (!lSmallFirstQueue.isEmpty() && availableChair < m - lLargeFirstQueue.size()) {
      if (lSmallFirstQueue.poll() == availableChair) {
        answer++;
      } else {
        availableChair++;
      }
    }
    return answer + lSmallFirstQueue.size();
  }
}

public class Main {
  private static void execute(ContestReader reader, PrintWriter out) {
    int n = reader.nextInt();
    int m = reader.nextInt();
    int[][] lrs = reader.nextInt(n, 2);
    out.println(new Solver(n, m, lrs).solve());
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
