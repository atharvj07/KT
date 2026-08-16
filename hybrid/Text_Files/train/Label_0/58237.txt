import java.io.*;
import java.util.*;

class Solver {
  final int n, k;
  final double[][] xycs;
  ComplexDouble[] cs;

  Solver(int n, int k, double[][] xycs) {
    this.n = n;
    this.k = k;
    this.xycs = xycs;
  }

  private ComplexDouble[] crossTwoCircle(ComplexDouble c1, double r1, ComplexDouble c2, double r2) {
    ComplexDouble v = c2.sub(c1);
    double d = v.abs();
    if (d <= Math.abs(r1 - r2) || r1 + r2 <= d) {
      return new ComplexDouble[0];
    }
    double x = (r1*r1 - r2*r2 + d*d) / (2.0 * d);
    double y = Math.sqrt(r1*r1 - x*x);
    ComplexDouble normV = v.mul(1.0 / v.abs());
    return new ComplexDouble[]{
      c1.add(normV.mul(x)).add(normV.mul(ComplexDouble.I).mul(y)),
      c1.add(normV.mul(x)).sub(normV.mul(ComplexDouble.I).mul(y))
    };
  }

  private int countInside(ComplexDouble c, double t, int excludeIndex1, int excludeIndex2) {
    int count = 0;
    for (int i = 0; i < n; i++) {
      if (i == excludeIndex1 || i == excludeIndex2) {
        continue;
      }
      if (cs[i].sub(c).abs() * xycs[i][2] < t) {
        count++;
      }
    }
    return count;
  }

  private boolean acceptable(double t) {
    for (int i = 0; i < n; i++) {
      if (countInside(cs[i], t, -1, -1) >= k) {
        return true;
      }
    }
    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {
        for (ComplexDouble c : crossTwoCircle(cs[i], t / xycs[i][2], cs[j], t / xycs[j][2])) {
          if (countInside(c, t, i, j) + 2 >= k) {
            return true;
          }
        }
      }
    }
    return false;
  }

  public double solve() {
    cs = new ComplexDouble[n];
    for (int i = 0; i < n; i++) {
      cs[i] = new ComplexDouble(xycs[i][0], xycs[i][1]);
    }

    double tMax = 1e6;
    double tMin = 0;
    for (int i = 0; i < 64; i++) {
      double tMid = (tMax + tMin) / 2;
      if (acceptable(tMid)) {
        tMax = tMid;
      } else {
        tMin = tMid;
      }
    }
    return tMax;
  }
}

class ComplexDouble {
  public final static ComplexDouble I = new ComplexDouble(0, 1);

  final double real, imag;
  
  ComplexDouble(double real, double imag) {
    this.real = real;
    this.imag = imag;
  }
  
  ComplexDouble conv() {
    return new ComplexDouble(this.real, -1 * this.imag);
  }
  
  ComplexDouble add(ComplexDouble cd) {
    return new ComplexDouble(this.real + cd.real, this.imag + cd.imag);
  }
  
  ComplexDouble sub(ComplexDouble cd) {
    return new ComplexDouble(this.real - cd.real, this.imag - cd.imag);
  }
  
  ComplexDouble mul(double d) {
    return new ComplexDouble(this.real * d, this.imag * d);
  }
  
  ComplexDouble mul(ComplexDouble cd) {
    double mulReal = this.real * cd.real - this.imag * cd.imag;
    double mulImag = this.real * cd.imag + this.imag * cd.real;
    return new ComplexDouble(mulReal, mulImag);
  }
  
  ComplexDouble div(ComplexDouble cd) {
    return this.mul(cd.conv()).mul(1.0 / cd.norm());
  }
  
  static ComplexDouble polar(double abs, double theta) {
    return new ComplexDouble(abs * Math.cos(theta), abs * Math.sin(theta));
  }
  
  double norm() {
    return this.real * this.real + this.imag * this.imag;
  }
  
  double abs() {
    return Math.sqrt(norm());
  }
  
  public String toString() {
    return String.format("(%.3f, %.3f)", real, imag);
  }
}

public class Main {
  private static void execute(ContestReader reader, PrintWriter out) {
    int n = reader.nextInt();
    int k = reader.nextInt();
    double[][] xycs = reader.nextDouble(n, 3);
    out.printf("%.20f\n", new Solver(n, k, xycs).solve());
  }
  
  public static void main(String[] args) {
    ContestReader reader = new ContestReader(System.in);
    PrintWriter out = new PrintWriter(System.out);
    execute(reader, out);
    out.flush();
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
