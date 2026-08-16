/**
 * Created at 20:57 on 2019/03/24
 */

import java.io.*;
import java.util.*;
import java.math.BigInteger;

public class Main {

  static FastScanner sc = new FastScanner();

  static int N;
  static int A = 0, G = 1, C = 2, T = 3;

  static long[][][][][] dp;

  public static void main(String[] args) {

    N = sc.nextInt();
    dp = new long[N][5][5][5][5];

    for (int i0=0; i0<N; i0++) {
      for (int i1=0; i1<5; i1++) {
        for (int i2=0; i2<5; i2++) {
          for (int i3=0; i3<5; i3++) {
            for (int i4=0; i4<5; i4++) {
              dp[i0][i1][i2][i3][i4] = -1;
            }
          }
        }
      }
    }

    long sum = 0;
    for (int i=0; i<4; i++) {
      sum += f(0, i, 4, 4, 4);
    }
    sum %= 1e9+7;

    System.out.println(sum);
  }

  static long f(int i, int back0, int back1, int back2, int back3) {

    if (dp[i][back0][back1][back2][back3] != -1) {
      return dp[i][back0][back1][back2][back3];
    }

    if ((back0 == C && back1 == G && back2 == A) ||
            (back0 == G && back1 == C && back2 == A) ||
            (back0 == C && back1 == A && back2 == G) ||
            (back0 == C &&               back2 == G && back3 == A) ||
            (back0 == C && back1 == G &&               back3 == A)) {
      dp[i][back0][back1][back2][back3] = 0;
      return 0;
    }

    if (i == N-1) {
      dp[i][back0][back1][back2][back3] = 1;
      return 1;
    }

    long sum = 0;
    for (int j=0; j<4; j++) {
      sum += f(i+1, j, back0, back1, back2);
    }

    sum = sum % (long)(1e9+7);

    dp[i][back0][back1][back2][back3] = sum;
    return sum;

  }

  static class Debugger {

    static long startTime;
    static boolean on = true;

    //入力受け取り後に呼び出す(入力時間をカウントしないため)
    static void start() {
      startTime = System.currentTimeMillis();
    }

    static void printTime() {
      if (on) System.out.println("(" + (System.currentTimeMillis() - startTime) + "ms)");
    }

    static void toggle() {
      on = !on;
    }

  }

  static class BigInt extends BigInteger {

    BigInteger MOD = new BigInteger("1000000007");
    static BigInt ZERO = new BigInt(0);
    static BigInt ONE = new BigInt(1);
    static BigInt TEN = new BigInt(10);

    public BigInt(long l) {
      super(Long.toString(l));
    }

    public BigInt(BigInteger i) {
      super(i.toByteArray());
    }

    public BigInt pow(int i) {
      return new BigInt(super.pow(i));
    }

    public BigInt[] divideAndRemainder(long l) {
      return divideAndRemainder(new BigInt(l));
    }

    public BigInt[] divideAndRemainder(BigInt i) {
      BigInt[] ret = new BigInt[2];
      BigInteger[] dAndR = super.divideAndRemainder(i);
      ret[0] = new BigInt(dAndR[0]);
      ret[1] = new BigInt(dAndR[1]);
      return ret;
    }

    public BigInt mod(long l) {
      return mod(new BigInt(l));
    }

    public BigInt mod(BigInt i) {
      return new BigInt(super.mod(i));
    }

    public BigInt mod() {
      return new BigInt(super.mod(MOD));
    }

    public BigInt add(long l) {
      return add(new BigInt(l));
    }

    public BigInt add(BigInt i) {
      return new BigInt(super.add(i));
    }

    public BigInt subtract(long l) {
      return subtract(new BigInt(l));
    }

    public BigInt subtract(BigInt i) {
      return new BigInt(super.subtract(i));
    }

    public BigInt multiply(long l) {
      return multiply(new BigInt(l));
    }

    public BigInt multiply(BigInt i) {
      return new BigInt(super.multiply(i));
    }

    public BigInt divide(long l) {
      return divide(new BigInt(l));
    }

    public BigInt divide(BigInt i) {
      return new BigInt(super.divide(i));
    }

    public BigInt abs() {
      return new BigInt(super.abs());
    }

  }

  /*
    add()でインデックスを指定しない場合指定されたソート順に違わない位置に追加する
    (ただしソートされていることが前提となる)
    Comparatorが0を返したとき、それらの順序は保証しない
    (TreeSet, TreeMapと違い削除はしない)
   */
  static class TreeList<E> extends ArrayList<E> {

    Comparator<? super E> comparator;

    TreeList(Comparator<? super E> c) {
      super();
      comparator = c;
    }

    /*
      ソート済みのリストに要素を追加する
     */
    public boolean add(E e) {
      int lowIndex = 0;
      int highIndex = size() - 1;
      int index = 0;

      if (size() == 0) {
        super.add(e);
        return true;
      }

      if (comparator.compare(e, get(0)) < 0) {
        index = 0;
      } else if (comparator.compare(e, get(highIndex)) > 0) {
        index = highIndex + 1;
      } else {
        while (lowIndex <= highIndex) {

          if (highIndex == lowIndex + 1 || highIndex == lowIndex) {
            index = highIndex;
            break;
          }

          int midIndex = (lowIndex + highIndex) / 2;
          ;

          if (comparator.compare(e, get(midIndex)) > 0) {
            lowIndex = midIndex;
          } else {
            highIndex = midIndex;
          }

        }
      }

      super.add(index, e);
      return true;
    }

  }

  static class FastScanner {
    private final InputStream in = System.in;
    private final byte[] buffer = new byte[1024];
    private int ptr = 0;
    private int buflen = 0;

    private boolean hasNextByte() {
      if (ptr < buflen) {
        return true;
      } else {
        ptr = 0;
        try {
          buflen = in.read(buffer);
        } catch (IOException e) {
          e.printStackTrace();
        }
        if (buflen <= 0) {
          return false;
        }
      }
      return true;
    }

    private int readByte() {
      if (hasNextByte()) return buffer[ptr++];
      else return -1;
    }

    private static boolean isPrintableChar(int c) {
      return 33 <= c && c <= 126;
    }

    private void skipUnprintable() {
      while (hasNextByte() && !isPrintableChar(buffer[ptr])) ptr++;
    }

    public boolean hasNext() {
      skipUnprintable();
      return hasNextByte();
    }

    public String next() {
      if (!hasNext()) throw new NoSuchElementException();
      StringBuilder sb = new StringBuilder();
      int b = readByte();
      while (isPrintableChar(b)) {
        sb.appendCodePoint(b);
        b = readByte();
      }
      return sb.toString();
    }

    public long nextLong() {
      if (!hasNext()) throw new NoSuchElementException();
      long n = 0;
      boolean minus = false;
      int b = readByte();
      if (b == '-') {
        minus = true;
        b = readByte();
      }
      if (b < '0' || '9' < b) {
        throw new NumberFormatException();
      }
      while (true) {
        if ('0' <= b && b <= '9') {
          n *= 10;
          n += b - '0';
        } else if (b == -1 || !isPrintableChar(b)) {
          return minus ? -n : n;
        } else {
          throw new NumberFormatException();
        }
        b = readByte();
      }
    }

    public int nextInt() {
      return (int) nextLong();
    }
  }

}
