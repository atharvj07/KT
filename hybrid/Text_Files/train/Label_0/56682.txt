import java.io.*;
import java.util.*;

class Solver {
  int n;
  long[] xs;
  long[] ys;
  String[] ds;
  
  
  long[] xds;
  long[] yds;
  
  public Solver(int n, long[] xs, long[] ys, String[] ds) {
    this.n = n;
    this.xs = xs;
    this.ys = ys;
    this.ds = ds;
  }
  
  public double solve() {
    xds = new long[n];
    yds = new long[n];
    
    for (int i = 0; i < n; i++) {
      switch(ds[i].charAt(0)) {
        case 'R':
          xds[i] = 1;
          yds[i] = 0;
          break;
        case 'L':
          xds[i] = -1;
          yds[i] = 0;
          break;
        case 'U':
          xds[i] = 0;
          yds[i] = 1;
          break;
        case 'D':
          xds[i] = 0;
          yds[i] = -1;
          break;
      }
    }
    
    List<Double> allHitTimes = new ArrayList<>();
    allHitTimes.add(0.0);
    allHitTimes.addAll(findMaxPointDirectionChangeTime(xs, xds));
    allHitTimes.addAll(findMaxPointDirectionChangeTime(ys, yds));
    reverseWorld();
    allHitTimes.addAll(findMaxPointDirectionChangeTime(xs, xds));
    allHitTimes.addAll(findMaxPointDirectionChangeTime(ys, yds));
    reverseWorld();
    
    Collections.sort(allHitTimes);
    double areaMin = solveTimeAt(allHitTimes.get(allHitTimes.size() - 1));
    for (int i = 1; i < allHitTimes.size(); i++) {
      areaMin = Math.min(areaMin, solveTimeRange(allHitTimes.get(i-1), allHitTimes.get(i)));
    }
    return areaMin;
  }
  
  private double solveTimeRange(double timeMin, double timeMax) {
    double timeMid = 0.5 * (timeMin + timeMax);
    
    double xMin = Double.MAX_VALUE;
    double xMax = -1.0 * Double.MAX_VALUE;
    double yMin = Double.MAX_VALUE;
    double yMax = -1.0 * Double.MAX_VALUE;
    int xMinIndex = 0;
    int xMaxIndex = 0;
    int yMinIndex = 0;
    int yMaxIndex = 0;
    
    for (int i = 0; i < n; i++) {
      double x = (double)xs[i] + (double)xds[i] * timeMid;
      double y = (double)ys[i] + (double)yds[i] * timeMid;
      if (xMin > x) {
        xMin = x;
        xMinIndex = i;
      }
      if (xMax < x) {
        xMax = x;
        xMaxIndex = i;
      }
      if (yMin > y) {
        yMin = y;
        yMinIndex = i;
      }
      if (yMax < y) {
        yMax = y;
        yMaxIndex = i;
      }
    }
    
    double w = xs[xMaxIndex] - xs[xMinIndex];
    double wd = xds[xMaxIndex] - xds[xMinIndex];
    double h = ys[yMaxIndex] - ys[yMinIndex];
    double hd = yds[yMaxIndex] - yds[yMinIndex];
    
    // Min (w + wd * t) * (h + hd * t)
    double a = wd * hd;
    double b = wd * h + hd * w;
    double c = w * h;
    return calculateMin(a, b, c, timeMin, timeMax);
  }
  
  private double calculate(double a, double b, double c, double x) {
    return a * x * x + b * x + c;
  }
  
  private double calculateMin(double a, double b, double c, double xMin, double xMax) {
    if (a == 0 && b == 0) {
      return c;
    }
    if (a == 0 && b > 0) {
      return calculate(a, b, c, xMin);
    }
    if (a == 0 && b < 0) {
      return calculate(a, b, c, xMax);
    }
    double answer = calculate(a, b, c, xMin);
    answer = Math.min(answer, calculate(a, b, c, xMax));
    
    double xAxis = -0.5 * b / a;
    if (xMin <= xAxis && xAxis <= xMax) {
      answer = Math.min(answer, calculate(a, b, c, xAxis));
    }
    return answer;
  }
  
  private double solveTimeAt(double time) {
    double xMin = Double.MAX_VALUE;
    double xMax = -1.0 * Double.MAX_VALUE;
    double yMin = Double.MAX_VALUE;
    double yMax = -1.0 * Double.MAX_VALUE;
    
    for (int i = 0; i < n; i++) {
      double x = (double)xs[i] + (double)xds[i] * time;
      double y = (double)ys[i] + (double)yds[i] * time;
      xMin = Math.min(xMin, x);
      xMax = Math.max(xMax, x);
      yMin = Math.min(yMin, y);
      yMax = Math.max(yMax, y);
    }
    return (xMax - xMin) * (yMax - yMin);
  }
  
  private void reverseWorld() {
    for (int i = 0; i < n; i++) {
      xs[i] *= -1;
      ys[i] *= -1;
      xds[i] *= -1;
      yds[i] *= -1;
    }
  }
  
  
  private List<Double> findMaxPointDirectionChangeTime(long[] zs, long[] zds) {
    List<Double> hitTimes = new ArrayList<>();
    
    long maxPointZ = zs[0];
    long maxPointZD = zds[0];
    for (int i = 1; i < n; i++) {
      if (maxPointZ < zs[i]) {
        maxPointZ = zs[i];
        maxPointZD = zds[i];
      }
    }
    if (maxPointZD > 0) {
      return hitTimes;
    }
    
    double firstHitTime = Double.MAX_VALUE;
    long firstHitZ = 0;
    long firstHitZD = 0;
    for (int i = 0; i < n; i++) {
      if (zds[i] == maxPointZD || zds[i] < 0) {
        continue;
      }
      // maxPointZ + t * maxPointZD == zs[i] + t * zds[i]
      // maxPointZ + t * maxPointZD == zs[i] + t * zds[i]
      double t = -1.0 * (maxPointZ - zs[i]) / (maxPointZD - zds[i]);
      if (0.0 <= t && t < firstHitTime) {
        firstHitTime = t;
        firstHitZ = zs[i];
        firstHitZD = zds[i];
      }
    }
    
    if (firstHitTime == Double.MAX_VALUE) {
      return hitTimes;
    }
    hitTimes.add(firstHitTime);
    
    if (firstHitZD > 0) {
      return hitTimes;
    }
    
    double secondHitTime = Double.MAX_VALUE;
    for (int i = 0; i < n; i++) {
      if (zds[i] <= 0) {
        continue;
      }
      
      double t = -1.0 * (firstHitZ - zs[i]) / (firstHitZD - zds[i]);
      if (firstHitTime <= t && t < secondHitTime) {
        secondHitTime = t;
      }
    }
    
    if (secondHitTime == Double.MAX_VALUE) {
      return hitTimes;
    }
    
    hitTimes.add(secondHitTime);
    return hitTimes;
  }
}

public class Main {
  private static void execute(ContestReader reader, PrintWriter out) {
    int n = reader.nextInt();
    long[] xs = new long[n];
    long[] ys = new long[n];
    String[] ds = new String[n];
    for (int i = 0; i < n; i++) {
      xs[i] = reader.nextLong();
      ys[i] = reader.nextLong();
      ds[i] = reader.next();
    }
    out.printf("%.20f\n", new Solver(n, xs, ys, ds).solve());
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
  
  public int[][] nextIntMatrix(int n, int m) {
    int[][] matrix = new int[n][m];
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        matrix[i][j] = nextInt();
      }
    }
    return matrix;
  }
  
  public long[][] nextLongMatrix(int n, int m) {
    long[][] matrix = new long[n][m];
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        matrix[i][j] = nextInt();
      }
    }
    return matrix;
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

