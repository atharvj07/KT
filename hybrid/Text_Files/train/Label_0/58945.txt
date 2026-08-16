import java.io.*;
import java.util.*;

class Solver {
  final int n;
  final long m;
  final int[][] xys;
  
  List<List<Integer>> graph;
  List<Map<Integer, Integer>> graphChildIndexMap;
  
  ModCalculator mc;
  List<List<Long>> countMatrix;
  List<List<Long>> countMulFromHeadMatrix;
//  List<Map<Integer, Long>> countMulFromHeadMapList;
  List<Map<Integer, Long>> countMulFromTailMapList;
  
  Solver(int n, long m, int[][] xys) {
    this.n = n;
    this.m = m;
    this.xys = xys;
  }
  
  private long calculateCountMulFromHead(int index, int childIndexPosition) {
    if (childIndexPosition < 0) {
      return 1L;
    }
    long cacheMulValue = countMulFromHeadMatrix.get(index).get(childIndexPosition);
    if (cacheMulValue >= 0) {
      return cacheMulValue;
    }
    long cacheValue = countMatrix.get(index).get(childIndexPosition);
    if (cacheValue < 0) {
      int childIndex = graph.get(index).get(childIndexPosition);
      cacheValue = mc.add(calculateCount(childIndex, index), 1);
      countMatrix.get(index).set(childIndexPosition, cacheValue);
    }
    long countMulValue = mc.mul(cacheValue, calculateCountMulFromHead(index, childIndexPosition - 1));
    countMulFromHeadMatrix.get(index).set(childIndexPosition, countMulValue);
    return countMulValue;
  }
  
  private long calculateCountMulFromTail(int index, int childIndexPosition) {
    if (childIndexPosition >= graph.get(index).size()) {
      return 1L;
    }
    Long cacheMulValue = countMulFromTailMapList.get(index).get(childIndexPosition);
    if (cacheMulValue != null) {
      return cacheMulValue;
    }
    long cacheValue = countMatrix.get(index).get(childIndexPosition);
    if (cacheValue < 0) {
      int childIndex = graph.get(index).get(childIndexPosition);
      cacheValue = mc.add(calculateCount(childIndex, index), 1);
      countMatrix.get(index).set(childIndexPosition, cacheValue);
    }
    Long countMulValue = mc.mul(cacheValue, calculateCountMulFromTail(index, childIndexPosition + 1));
    countMulFromTailMapList.get(index).put(childIndexPosition, countMulValue);
    return countMulValue;
  }
  
  private long calculateCount(int index, int parentIndex) {
    int parentIndexPosition = graphChildIndexMap.get(index).get(parentIndex);
    long v1 = calculateCountMulFromHead(index, parentIndexPosition - 1);
    long v2 = calculateCountMulFromTail(index, parentIndexPosition + 1);
    return mc.mul(v1, v2);
  }
  
  private long solve(int index) {
    return calculateCountMulFromHead(index, graph.get(index).size() - 1);
  }
  
  public List<Long> solve() {
    graph = new ArrayList<>();
    graphChildIndexMap = new ArrayList<>();
    countMulFromTailMapList = new ArrayList<>();
    for (int i = 0; i <= n; i++) {
      graph.add(new ArrayList<>());
      graphChildIndexMap.add(new HashMap<>());
      countMulFromTailMapList.add(new HashMap<>());
    }
    for (int[] xy : xys) {
      int x = xy[0];
      int y = xy[1];
      graphChildIndexMap.get(x).put(y, graph.get(x).size());
      graph.get(x).add(y);
      graphChildIndexMap.get(y).put(x, graph.get(y).size());
      graph.get(y).add(x);
    }
    
    countMatrix = new ArrayList<>();
    countMulFromHeadMatrix = new ArrayList<>();
    for (int i = 0; i <= n; i++) {
      countMatrix.add(new ArrayList<>());
      countMulFromHeadMatrix.add(new ArrayList<>());
      for (int j = 0; j < graph.get(i).size(); j++) {
        countMatrix.get(i).add(-1L);
        countMulFromHeadMatrix.get(i).add(-1L);
      }
    }
//    for (int i = 0; 
    
    mc = new ModCalculator(m);
    
    List<Long> answers = new ArrayList<>();
    for (int i = 1; i <= n; i++) {
      answers.add(solve(i));
    }
    return answers;
  }
}

public class Main {
  private static void execute(ContestReader reader, PrintWriter out) {
    int n = reader.nextInt();
    long m = reader.nextLong();
    int[][] xys = reader.nextInt(n - 1, 2);
    for (long answer : new Solver(n, m, xys).solve()) {
      out.println(answer);
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
  
  public char nextChar() {
    return next().charAt(0);
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
  
  public char[] nextChar(int n) {
    char[] array = new char[n];
    for (int i = 0; i < n; i++) {
      array[i] = nextChar();
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
  
  public char[][] nextChar(int n, int m) {
    char[][] matrix = new char[n][m];
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        matrix[i][j] = nextChar();
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

class ModCalculator {
  private final long mod;
  private final ModCombinationCache modCombinationCache;
  
  ModCalculator(long mod) {
    this.mod = mod;
    this.modCombinationCache = new ModCombinationCache();
  }
  
  public long add(long a, long b) {
    return (a + b) % mod;
  }
  
  public long sub(long a, long b) {
    return (a - b + mod) % mod;
  }
  
  public long mul(long a, long b) {
    a %= mod;
    b %= mod;
    return (a * b) % mod;
  }
  
  public long pow(long a, long b) {
    if (b == 0) {
      return 1;
    }
    long v = pow(mul(a, a), b / 2);
    if (b % 2 == 1) {
      return mul(v, a);
    } else {
      return v;
    }
  }
  
  public long inverse(long a) {
    return pow(a, mod - 2);
  }
  
  public long div(long a, long b) {
    return mul(a, inverse(b));
  }
  
  public long getF(int n) {
    return modCombinationCache.getF(n);
  }
  
  public long getP(int n, int r) {
    return modCombinationCache.getP(n, r);
  }
  
  public long getC(int n, int k) {
    return modCombinationCache.getC(n, k);
  }
  
  class ModCombinationCache {
    private final List<Long> factorialCache;
    private final List<Long> factorialInverseCache;
    
    public ModCombinationCache() {
      factorialCache = new ArrayList<>();
      factorialCache.add(1L);
      factorialInverseCache = new ArrayList<>();
      factorialInverseCache.add(1L);
    }
    
    private void resize(int n) {
      for (int i = factorialCache.size() - 1; i < n; i++) {
        long v = mul(factorialCache.get(i), i + 1);
        factorialCache.add(v);
        factorialInverseCache.add(inverse(v));
      }
    }
    
    long getF(int n) {
      resize(n);
      return factorialCache.get(n);
    }
    
    long getP(int n, int r) {
      resize(n);
      return mul(factorialCache.get(n), factorialInverseCache.get(n - r));
    }
    
    long getC(int n, int k) {
      resize(n);
      return mul(factorialCache.get(n), mul(factorialInverseCache.get(k), factorialInverseCache.get(n-k)));
    }
  }
}
