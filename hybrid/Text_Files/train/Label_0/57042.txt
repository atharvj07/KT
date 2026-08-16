import java.io.*;
import java.util.*;

class LongWidth {
  final long value;
  final int width;

  LongWidth(long value, int width) {
    this.value = value;
    this.width = width;
  }

  public String toString() {
    return String.format("(%d, %d)", value, width);
  }
}

public class Main {
  private static final ModCalculator mc = new ModCalculator(998_244_353L);
  private static final LongWidth EMPTY = new LongWidth(0, 0);

  private static UpdateRangeGetRangeSegmentTree.Operator<LongWidth> createOperator(int n) {
    final long[] tenPowList = new long[n];
    final long[] allOneList = new long[n];
    tenPowList[0] = 1;
    allOneList[0] = 1;
    for (int i = 1; i < n; i++) {
      tenPowList[i] = mc.mul(tenPowList[i - 1], 10);
      allOneList[i] = mc.add(allOneList[i - 1], tenPowList[i]);
    }

    return new UpdateRangeGetRangeSegmentTree.Operator<LongWidth>() {
      @Override
      public boolean isNoOpLazy(long lazy) {
        return lazy == -1;
      }
  
      @Override
      public long getNoOpLazy() {
        return -1;
      }
  
      @Override
      public long multiplyLazyValue(long lazy, int count) {
        return mc.mul(lazy, allOneList[count - 1]);
      }
  
      @Override
      public long applyOffset(long lazy, int offset) {
        return lazy;
      }
  
      @Override
      public long mergeLazyValue(long oldLazy, long newLazy) {
        return newLazy;
      }
  
      @Override
      public LongWidth apply(LongWidth value, long lazy) {
        return new LongWidth(lazy, value.width);
      }
  
      @Override
      public LongWidth mergeValue(LongWidth smallIndexValue, LongWidth largeIndexValue) {
        long v2 = mc.mul(smallIndexValue.value, tenPowList[largeIndexValue.width]);
        long v3 = mc.add(v2, largeIndexValue.value);
        return new LongWidth(v3, smallIndexValue.width + largeIndexValue.width);
      }
  
      @Override
      public LongWidth getUnitValue() {
        return EMPTY;
      }  
    };
  }

  private static List<Long> solve(int n, int q, int[][] lrds) {
    LongWidth[] initialValues = new LongWidth[n + 1];
    Arrays.fill(initialValues, new LongWidth(1, 1));
    UpdateRangeGetRangeSegmentTree<LongWidth> segmentTree = new UpdateRangeGetRangeSegmentTree<>(createOperator(n), initialValues);
    List<Long> answers = new ArrayList<>();
//    segmentTree.dump();
    for (int[] lrd : lrds) {
      int l = lrd[0];
      int r = lrd[1];
      int d = lrd[2];
      segmentTree.update(l, r + 1, Long.valueOf(d));
//      segmentTree.dump();
      answers.add(segmentTree.getRange(1, n + 1).value);
//      throw new RuntimeException();
    }
    return answers;
  }

  private static void execute(ContestReader reader, ContestWriter out) {
    int n = reader.nextInt();
    int q = reader.nextInt();
    int[][] lrds = reader.nextInt(q, 3);
    out.printList(solve(n, q, lrds));
  }
  
  public static void main(String[] args) {
    ContestReader reader = new ContestReader(System.in);
    ContestWriter out = new ContestWriter(System.out);
    execute(reader, out);
    out.flush();
  }
}

// Verify ABC179 F
// https://atcoder.jp/contests/abc179/tasks/abc179_f

// Verify ABC179 F
// https://atcoder.jp/contests/abc179/tasks/abc179_f

class UpdateRangeGetRangeSegmentTree<ValueType> {
  public interface Operator<ValueType> {
    boolean isNoOpLazy(long lazy);
    long getNoOpLazy();
    long multiplyLazyValue(long lazy, int count);
    long applyOffset(long lazy, int offset);
    long mergeLazyValue(long oldLazy, long newLazy);
    ValueType apply(ValueType value, long lazy);
    ValueType mergeValue(ValueType smallIndexValue, ValueType largeIndexValue);
    ValueType getUnitValue();
  }
  
  private final Operator<ValueType> operator;
  private final int n;
  private final long[] lazies;
  private final ValueType[] values;
  
  public UpdateRangeGetRangeSegmentTree(Operator<ValueType> operator, ValueType[] initialValues) {
    this.operator = operator;
    
    int tempN = 1;
    while (tempN < initialValues.length) {
      tempN *= 2;
    }
    n = tempN;
    lazies = createTArray(2 * n -1);
    Arrays.fill(lazies, operator.getNoOpLazy());
    values = createSArray(2 * n -1);
    for (int i = 0; i < initialValues.length; i++) {
      values[i + n - 1] = initialValues[i];
    }
    for (int i = initialValues.length; i < n; i++) {
      values[i + n - 1] = this.operator.getUnitValue();
    }
    for (int i = n - 2; i >= 0; i--) {
      values[i] = this.operator.mergeValue(values[2 * i + 1], values[2 * i + 2]);
    }
  }

  @SuppressWarnings("unchecked")
  private long[] createTArray(int size) {
    return (new long[size]);    
  }
  
  @SuppressWarnings("unchecked")
  private ValueType[] createSArray(int size) {
    return (ValueType[])(new Object[size]);    
  }

  private void updateLazy(int lazyIndex, long lazy) {
    if (!operator.isNoOpLazy(lazies[lazyIndex])) {
      lazies[lazyIndex] = operator.mergeLazyValue(lazies[lazyIndex], lazy);
    } else {
      lazies[lazyIndex] = lazy;
    }
  }
  
  private void eval(int k, int l, int r) {
    if (operator.isNoOpLazy(lazies[k])) {
      return;
    }
//    System.err.println("eval");
//    System.err.println(values[k]);
//    System.err.println(r - l);
    values[k] = operator.apply(values[k], operator.multiplyLazyValue(lazies[k], r - l));
//    System.err.println(values[k]);
    if (r - l > 1) {
      updateLazy(2 * k + 1, lazies[k]);
      updateLazy(2 * k + 2, operator.applyOffset(lazies[k], (r - l) / 2));
    }
    lazies[k] = operator.getNoOpLazy();
  }
  
  private void update(int a, int b, long lazy, int k, int l, int r) {
    eval(k, l, r);
    if (b <= l || r <= a) {
      return;
    }
    if (a <= l && r <= b) {
      updateLazy(k, lazy);
      eval(k, l, r);
    } else {
      update(a, b, lazy, 2 * k + 1, l, (l + r) / 2);
      update(a, b, operator.applyOffset(lazy, (r - l) / 2), 2 * k + 2, (l + r) / 2, r);
      values[k] = operator.mergeValue(values[2 * k + 1], values[2 * k + 2]);
    }
//    System.err.printf("%d %d %d %d %d\n", a, b, k, l, r);
//    System.err.println(lazy);
//    dump();
  }
  
  public void update(int a, int b, long lazy) {
    update(a, b, lazy, 0, 0, n);
  }
  
  public void update(int a, long lazy) {
    update(a, a + 1, lazy);
  }
  
  private ValueType getRange(int a, int b, int k, int l, int r) {
    if (b <= l || r <= a) {
      return operator.getUnitValue();
    }
    eval(k, l, r);
    if (a <= l && r <= b) {
      return values[k];
    }
    ValueType vl = getRange(a, b, 2 * k + 1, l, (l + r) / 2);
    ValueType vr = getRange(a, b, 2 * k + 2, (l + r) / 2, r);
    return operator.mergeValue(vl, vr);
  }
  
  public ValueType getRange(int a, int b) {
    return getRange(a, b, 0, 0, n);
  }
  
  public ValueType get(int a) {
    return getRange(a, a + 1);
  }
}


class ModCalculator {
  private final long mod;
  private final ModInverseCache modInverseCache;
  private final ModCombinationCache modCombinationCache;
  
  ModCalculator(long mod) {
    this.mod = mod;
    this.modInverseCache = new ModInverseCache();
    this.modCombinationCache = new ModCombinationCache();
  }
  
  public long norm(long v) {
    long nogmalized = v % mod;
    if (nogmalized < 0) {
      nogmalized += mod;
    }
    return nogmalized;
  }
  
  public long add(long a, long b) {
    return norm(a + b);
  }
  
  public long sub(long a, long b) {
    return norm(a - b + mod);
  }
  
  public long mul(long a, long b) {
    return norm(a * b);
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

  // Verify ARC 042 D
  // https://atcoder.jp/contests/arc042/tasks/arc042_d
  // a^x mod p === b
  // return -1 there is no such positive x
  public long log(long a, long b) {
    Map<Long, Long> map = new HashMap<>();
    long powA = 1;
    long rootP = 0;
    while (true) {
      if (powA == b && rootP != 0) {
        return rootP;
      }
      if (map.containsKey(powA)) {
        return -1;
      }
      map.put(powA, rootP);
      powA = mul(powA, a);
      rootP++;
      if (rootP * rootP > mod) {
        break;
      }
    }
    long inversePowA = inverse(powA);
    for (int i = 1; i <= rootP; i++) {
      b = mul(b, inversePowA);
      Long value = map.get(b);
      if (value != null && value + rootP * i > 0) {
        return value + rootP * i;
      }
    }
    return -1;
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

  // Verify ttpc2019 J
  // https://atcoder.jp/contests/ttpc2019/tasks/ttpc2019_j
  class PrimitiveLongList {
    long[] values;
    int size;

    public PrimitiveLongList() {
      values = new long[10];
    }

    private void resize() {
      long[] newValues = new long[values.length * 2];
      System.arraycopy(values, 0, newValues, 0, values.length);
      values = newValues;
    }

    public void add(long value) {
      if (size >= values.length) {
        resize();
      }
      values[size] = value;
      size++;
    }

    private void validateIndex(int index) {
      if (index < 0 || size <= index) {
        throw new IndexOutOfBoundsException(String.format("size: %d, index: %d", size, index));
      }
    }

    public long get(int index) {
      validateIndex(index);
      return values[index];
    }

    public void set(int index, long value) {
      validateIndex(index);
      values[index] = value;
    }

    public int size() {
      return size;
    }
  }

  // Verify AGC 040 C
  // https://atcoder.jp/contests/agc040/tasks/agc040_c
  class ModInverseCache {
    private final PrimitiveLongList inverseCache;

    public ModInverseCache() {
      inverseCache = new PrimitiveLongList();
      inverseCache.add(0L);
      inverseCache.add(1L);
    }

    private void resize(int n) {
      for (int i = inverseCache.size(); i <= n; i++) {
        long k = mod / i;
        int r = (int)(mod % i);
        long inverse = mul(-k, inverseCache.get(r));
        inverseCache.add(inverse);
      }
    }

    long get(int n) {
      resize(n);
      return inverseCache.get(n);
    }
  }
  
  class ModCombinationCache {
    private final PrimitiveLongList factorialCache;
    private final PrimitiveLongList factorialInverseCache;
    
    public ModCombinationCache() {
      factorialCache = new PrimitiveLongList();
      factorialCache.add(1L);
      factorialInverseCache = new PrimitiveLongList();
      factorialInverseCache.add(1L);
    }
    
    private void resize(int n) {
      for (int i = factorialCache.size() - 1; i < n; i++) {
        factorialCache.add(mul(factorialCache.get(i), i + 1));
        factorialInverseCache.add(mul(factorialInverseCache.get(i), modInverseCache.get(i + 1)));
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
