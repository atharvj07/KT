import java.io.*;
import java.util.*;

class SubSolver {
//  private static final int MAX_SIZE = 50;

  final int k, length;
  final List<Integer> bs;
//  long[][] combinationCache;
  long[] cache;

  SubSolver(int k, int length, List<Integer> bs) {
    this.k = k;
    this.length = length;
    this.bs = bs;
//    System.err.printf("k: %d, length: %d, bs: %s\n", k, length, bs);
  }

  private void buildCombinationCache() {
    long[][] combinationCache = new long[bs.size() + 1][bs.size() + 1];
    combinationCache[1][0] = 1;
    combinationCache[1][1] = 1;
    for (int i = 2; i <= bs.size(); i++) {
      combinationCache[i][0] = 1;
      for (int j = 1; j < i; j++) {
        combinationCache[i][j] = combinationCache[i - 1][j - 1] + combinationCache[i - 1][j];
      }
      combinationCache[i][i] = 1;
    }
    cache = new long[bs.size()];
    cache[0] = 1;
    for (int i = 1; i < bs.size(); i++) {
      for (int j = 0; j <= Math.min(i, k - 1); j++) {
        cache[i] += combinationCache[i][j];
      }
    }
  }

  private static int getBitFromBitmask(int bitset, int bitIndex) {
    return (bitset >> bitIndex) & 1;
  }

  private int getBit(int elementIndex, int bitIndex) {
    return getBitFromBitmask(bs.get(elementIndex), bitIndex);
  }

  private long solve(int baseIndex) {
    List<Long> masks = new ArrayList<>();
    for (int i = 0; i < length; i++) {
      int bit = getBit(baseIndex, i);
      long mask = 0;
      for (int j = baseIndex + 1; j < bs.size(); j++) {
        if (getBit(j, i) != bit) {
          mask |= (1L << (j - baseIndex - 1));
        }
      }
      masks.add(mask);
//      System.err.println(mask);
      if (mask == 0) {
        return 0;
      }
    }
//    System.err.println();

    long excluded = 0;
    for (int bitset = 1; bitset < (1 << length); bitset++) {
//      System.err.println(bitset);
//      long mask = (1L << length) - 1;
      long mask = 0;
      for (int bitIndex = 0; bitIndex < length; bitIndex++) {
        if (getBitFromBitmask(bitset, bitIndex) == 1) {
          mask |= masks.get(bitIndex);
        }
      }
      if (Integer.bitCount(bitset) % 2 == 0) {
//        System.err.printf("%d: bitset, mask: %d, value: %d\n", bitset, mask, -1 * cache[bs.size() - baseIndex - 1 - Long.bitCount(mask)]);
        excluded -= cache[bs.size() - baseIndex - 1 - Long.bitCount(mask)];
      } else {
//        System.err.printf("%d: bitset, mask: %d, value: %d\n", bitset, mask, cache[bs.size() - baseIndex - 1 - Long.bitCount(mask)]);
        excluded += cache[bs.size() - baseIndex - 1 - Long.bitCount(mask)];
      }
    }
    /*
    int mask = bs.get(baseIndex);
    long[][] dptable = new long[k + 1][1 << length];
    dptable[1][0] = 1;
    for (int i = baseIndex + 1; i < bs.size(); i++) {
      for (int a = k - 1; a >= 1; a--) {
        for (int b = 0; b < (1 << length); b++) {
          int xorMask = mask ^ bs.get(i);
          dptable[a + 1][b | xorMask] += dptable[a][b];
        }
      }
    }
    long answer = 0;
    for (int a = 2; a <= k; a++) {
      answer += dptable[a][(1 << length) - 1];
    }
    return answer;
    */
//    System.err.printf("solve: %d %d\n", baseIndex, excluded);
    return cache[bs.size() - baseIndex - 1] - excluded;
  }

  public long solve() {
    buildCombinationCache();

    long answer = 0;
    for (int baseIndex = 0; baseIndex < bs.size(); baseIndex++) {
      answer += solve(baseIndex);
    }
    return answer;
  }
}

class Solver {
  private static final int MAX_L = 18;

  final int n, k, s, t;
  final int[] as;

  Solver(int n, int k, int s, int t, int[] as) {
    this.n = n;
    this.k = k;
    this.s = s;
    this.t = t;
    this.as = as;
  }

  // and: 1, or: 1, all: 1
  // and: 0, or: 0, all: 0
  // and: 1, or: 0, invalid
  // and: 0, or: 1, both 1, 0
  public long solve() {
    List<List<Integer>> aBitMatrix = new ArrayList<>();
    for (int i = 0; i < n; i++) {
      aBitMatrix.add(new ArrayList<>());
      for (int j = 0; j < MAX_L; j++) {
        aBitMatrix.get(i).add((as[i] >> j) & 1);
      }
    }

    for (int j = MAX_L - 1; j >= 0; j--) {
      int sBit = (s >> j) & 1;
      int tBit = (t >> j) & 1;
      if (sBit == 1 && tBit == 0) {
        return 0;
      } else if (sBit == tBit) {
        for (Iterator<List<Integer>> it = aBitMatrix.iterator(); it.hasNext(); ) {
          List<Integer> list = it.next();
          if (list.get(j) == sBit) {
            list.remove(j);
          } else {
            it.remove();
          }
        }
      }
    }

    if (aBitMatrix.isEmpty()) {
      return 0;
    }

    int length = aBitMatrix.get(0).size();
    List<Integer> bs = new ArrayList<>();
    for (var bits: aBitMatrix) {
      int b = 0;
      for (int i = 0; i < length; i++) {
        b |= bits.get(i) << i;
      }
      bs.add(b);
    }

    return new SubSolver(k, length, bs).solve();
  }
}

public class Main {
  private static void execute(ContestReader reader, ContestWriter out) {
    int n = reader.nextInt();
    int k = reader.nextInt();
    int s = reader.nextInt();
    int t = reader.nextInt();
    int[] as = reader.nextInt(n);
    out.println(new Solver(n, k, s, t, as).solve());
  }
  
  public static void main(String[] args) {
    ContestReader reader = new ContestReader(System.in);
    ContestWriter out = new ContestWriter(System.out);
    execute(reader, out);
    out.flush();
  }
}

class ContestWriter extends PrintWriter {
  ContestWriter(PrintStream printStream) {
    super(printStream);
  }

  public void printList(List<? extends Object> list) {
    for (Object object : list) {
      println(object);
    }
  }

  public void printListOneLine(List<? extends Object> list) {
    List<String> stringList = new ArrayList<>();
    for (Object object : list) {
      stringList.add(object.toString());
    }
    println(String.join(" ", stringList));
  }
}

class ContestReader {
  private static final int BUFFER_SIZE = 1024;
  
  private final InputStream stream;
  private final byte[] buffer;
  private int pointer;
  private int bufferLength;
  
  ContestReader(InputStream stream) {
    this.stream = stream;
    this.buffer = new byte[BUFFER_SIZE];
    this.pointer = 0;
    this.bufferLength = 0;
  }
  
  private boolean hasNextByte() {
    if (pointer < bufferLength) {
      return true;
    }
    
    pointer = 0;
    try {
      bufferLength = stream.read(buffer);
    } catch (IOException e) {
      throw new RuntimeException(e);
    }
    return bufferLength > 0;
  }
  
  private int readByte() {
    if (hasNextByte()) {
      return buffer[pointer++];
    } else {
      return -1;
    }
  }
  
  private static boolean isPrintableChar(int c) {
    return 33 <= c && c <= 126;
  }
  
  public boolean hasNext() {
    while (hasNextByte() && !isPrintableChar(buffer[pointer])) {
      pointer++;
    }
    return hasNextByte();
  }
  
  public String next() {
    if (!hasNext()) {
      throw new NoSuchElementException();
    }
    StringBuilder sb = new StringBuilder();
    while(true) {
      int b = readByte();
      if (!isPrintableChar(b)) {
        break;
      }
      sb.appendCodePoint(b);
    }
    return sb.toString();
  }
  
  public String nextLine() {
    if (!hasNext()) {
      throw new NoSuchElementException();
    }
    StringBuilder sb = new StringBuilder();
    while(true) {
      int b = readByte();
      if (!isPrintableChar(b) && b != 0x20) {
        break;
      }
      sb.appendCodePoint(b);
    }
    return sb.toString();
  }
  
  public char nextChar() {
    return next().charAt(0);
  }
  
  public int nextInt() {
    if (!hasNext()) {
      throw new NoSuchElementException();
    }
    
    int n = 0;
    boolean minus = false;
    
    {
      int b = readByte();
      if (b == '-') {
        minus = true;
      } else if ('0' <= b && b <= '9') {
        n = b - '0';
      } else {
        throw new NumberFormatException();
      }
    }
    
    while(true){
      int b = readByte();
      if ('0' <= b && b <= '9') {
        n *= 10;
        n += b - '0';
      } else if (b == -1 || !isPrintableChar(b)) {
        return minus ? -n : n;
      } else {
        throw new NumberFormatException();
      }
    }
  }
  
  public long nextLong() {
    if (!hasNext()) {
      throw new NoSuchElementException();
    }
    
    long n = 0;
    boolean minus = false;
    
    {
      int b = readByte();
      if (b == '-') {
        minus = true;
      } else if ('0' <= b && b <= '9') {
        n = b - '0';
      } else {
        throw new NumberFormatException();
      }
    }
    
    while(true){
      int b = readByte();
      if ('0' <= b && b <= '9') {
        n *= 10;
        n += b - '0';
      } else if (b == -1 || !isPrintableChar(b)) {
        return minus ? -n : n;
      } else {
        throw new NumberFormatException();
      }
    }
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
  
  public String[] nextLine(int n) {
    String[] array = new String[n];
    for (int i = 0; i < n; i++) {
      array[i] = nextLine();
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
  
  public String[][] next(int n, int m) {
    String[][] matrix = new String[n][m];
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        matrix[i][j] = next();
      }
    }
    return matrix;
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

class MyAssert {
  public static void myAssert(boolean flag, String message) {
    if (!flag) {
      throw new RuntimeException(message);
    }
  }
 
  public static void myAssert(boolean flag) {
    myAssert(flag, "");
  }
}
