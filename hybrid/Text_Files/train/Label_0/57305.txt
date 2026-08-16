import java.io.*;
import java.util.*;

class Solver {
  private static final long M = 1_000_000_007L;
  
  private final long l, r;
  private long[][][][] dptable;
  
  Solver(long l, long r) {
    this.l = l;
    this.r = r;
  }
  
  private int getIndexFromBoolean(boolean b) {
    return b ? 1 : 0;
  }
  
  private long getBit(long v, int bitPosition) {
    return (v >> bitPosition) & 1L;
  }
  
  private long solve(int bitPosition, boolean xAlreadyHigherThanL, boolean yAlreadyLowerThanR, boolean mostSignificantBitAlreadyFlipped) {
    if (bitPosition < 0) {
      return 1;
    }
    long cacheValue = dptable[bitPosition][getIndexFromBoolean(xAlreadyHigherThanL)][getIndexFromBoolean(yAlreadyLowerThanR)][getIndexFromBoolean(mostSignificantBitAlreadyFlipped)];
    if (cacheValue >= 0) {
      return cacheValue;
    }
    long output = 0L;
    // x: 0, y: 0
    if (xAlreadyHigherThanL || getBit(l, bitPosition) == 0L) {
      output += solve(
          bitPosition - 1,
          xAlreadyHigherThanL,
          yAlreadyLowerThanR || getBit(r, bitPosition) == 1L,
          mostSignificantBitAlreadyFlipped);
    }
    // x: 1, y: 1
    if (yAlreadyLowerThanR || getBit(r, bitPosition) == 1L) {
      output += solve(
          bitPosition - 1,
          xAlreadyHigherThanL || getBit(l, bitPosition) == 0L,
          yAlreadyLowerThanR,
          true);
    }
    // x: 0, y: 1
    if ((xAlreadyHigherThanL || getBit(l, bitPosition) == 0L) 
        && (yAlreadyLowerThanR || getBit(r, bitPosition) == 1L)
        && mostSignificantBitAlreadyFlipped) {
      output += solve(
          bitPosition - 1,
          xAlreadyHigherThanL,
          yAlreadyLowerThanR,
          true);
    }
    output %= M;
    dptable[bitPosition][getIndexFromBoolean(xAlreadyHigherThanL)][getIndexFromBoolean(yAlreadyLowerThanR)][getIndexFromBoolean(mostSignificantBitAlreadyFlipped)] = output;
    return output;
  }
  
  public long solve() {
    dptable = new long[60][2][2][2];
    for (long[][][] d1 : dptable) {
      for (long[][] d2 : d1) {
        for (long[] d3 : d2) {
          Arrays.fill(d3, -1);
        }
      }
    }
    return solve(59, false, false, false);
  }
}

public class Main {
  private static void execute(ContestReader reader, PrintWriter out) {
    long l = reader.nextLong();
    long r = reader.nextLong();
    out.println(new Solver(l, r).solve());
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
  
  public int[] nextIntArray(int n) {
    int[] array = new int[n];
    for (int i = 0; i < n; i++) {
      array[i] = nextInt();
    }
    return array;
  }
  
  public long[] nextLongArray(int n) {
    long[] array = new long[n];
    for (int i = 0; i < n; i++) {
      array[i] = nextLong();
    }
    return array;
  }
}

class Algorithm {
  private static void swap(Object[] list, int a, int b) {
    Object tmp = list[a];
    list[a] = list[b];
    list[b] = tmp;
  }
  
  public static <T extends Comparable<? super T>> boolean nextPermutation(T[] ts) {
    int rightMostAscendingOrderIndex = ts.length - 2;
    while (rightMostAscendingOrderIndex >= 0 &&
        ts[rightMostAscendingOrderIndex].compareTo(ts[rightMostAscendingOrderIndex + 1]) >= 0) {
      rightMostAscendingOrderIndex--;
    }
    if (rightMostAscendingOrderIndex < 0) {
      return false;
    }
    
    int rightMostGreatorIndex = ts.length - 1;
    while (ts[rightMostAscendingOrderIndex].compareTo(ts[rightMostGreatorIndex]) >= 0) {
      rightMostGreatorIndex--;
    }
    
    swap(ts, rightMostAscendingOrderIndex, rightMostGreatorIndex);
    for (int i = 0; i < (ts.length - rightMostAscendingOrderIndex - 1) / 2; i++) {
      swap(ts, rightMostAscendingOrderIndex + 1 + i, ts.length - 1 - i);
    }
    return true;
  }
  
  public static void shuffle(int[] array) {
    Random random = new Random();
    int n = array.length;
    for (int i = 0; i < n; i++) {
      int randomIndex = i + random.nextInt(n - i);
      
      int temp = array[i];
      array[i] = array[randomIndex];
      array[randomIndex] = temp;
    }
  }
  
  public static void shuffle(long[] array) {
    Random random = new Random();
    int n = array.length;
    for (int i = 0; i < n; i++) {
      int randomIndex = i + random.nextInt(n - i);
      
      long temp = array[i];
      array[i] = array[randomIndex];
      array[randomIndex] = temp;
    }
  }
  
  public static void sort(int[] array) {
    shuffle(array);
    Arrays.sort(array);
  }
  
  public static void sort(long[] array) {
    shuffle(array);
    Arrays.sort(array);
  }
}

