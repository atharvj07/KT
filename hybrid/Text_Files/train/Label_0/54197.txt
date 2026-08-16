/**
 * Created at 19:48 on 2019-06-22
 */

import java.io.*;
import java.util.*;

public class Main {

  static FastScanner sc = new FastScanner();

  static int[] dx = {0, 1, 0, -1};
  static int[] dy = {-1, 0, 1, 0};

  static long MOD = (long) (1e9 + 7);

  public static void main(String[] args) {

    int N = sc.nextInt();
    int M = sc.nextInt();

    UnionFindTree tree = new UnionFindTree(N);

    for (int i=0; i<M; i++) {
      tree.union(sc.nextInt()-1, sc.nextInt()-1);
      sc.nextInt();
    }

    int[] a = new int[N];
    int count = 0;
    for (int i=0; i<N; i++) {
      int root = tree.find(i);
      if (a[root] == 0) {
        count++;
        a[root]++;
      }
    }

    System.out.println(count);

  }

  public static class UnionFindTree {
    int[] parent; //インデックスにとノードを対応させ、そのルートノードのインデックスを格納
    int[] rank; //parentと同様に、木の高さを格納
    public UnionFindTree(int size) {
      this.parent = new int[size];
      this.rank = new int[size];
      for (int i = 0; i < size; i++) {
        makeSet(i);
      }
    }
    public void makeSet(int i) {
      parent[i] = i;
      rank[i] = 0; //集合の高さ
    }
    public void union(int x, int y) {
      int xRoot = find(x);
      int yRoot = find(y);
//xが属する木の方が大きい場合
      if (rank[xRoot] > rank[yRoot]) {
        parent[yRoot] = xRoot; //yの親をxに更新
      } else if(rank[xRoot] < rank[yRoot]) {
        parent[xRoot] = yRoot;
      } else if (xRoot != yRoot){
        parent[yRoot] = xRoot;
        rank[xRoot]++; //同じ高さの木がルートの子として着くから大きさ++;
      }
    }
    //引数の属する木のルートのidを返す
    public int find(int i) {
      if (i != parent[i]) {
        parent[i] = find(parent[i]);
      }
      return parent[i];
    }
    //同じ木に属しているか
    public boolean same(int x, int y) {
      return find(x) == find(y);
    }
  }

  public static class Mathf {

    public static int max(int[] a) {
      int M = a[0];
      for (int i = 1; i < a.length; i++) {
        M = Math.max(M, a[i]);
      }
      return M;
    }

    public static int min(int[] a) {
      int m = a[0];
      for (int i = 1; i < a.length; i++) {
        m = Math.min(m, a[i]);
      }
      return m;
    }

    public static long max(long[] a) {
      long M = a[0];
      for (int i = 1; i < a.length; i++) {
        M = Math.max(M, a[i]);
      }
      return M;
    }

    public static long min(long[] a) {
      long m = a[0];
      for (int i = 1; i < a.length; i++) {
        m = Math.min(m, a[i]);
      }
      return m;
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

    public int[] nextIntArray(int N) {
      int[] array = new int[N];
      for (int i = 0; i < N; i++) {
        array[i] = sc.nextInt();
      }
      return array;
    }

    public long[] nextLongArray(int N) {
      long[] array = new long[N];
      for (int i = 0; i < N; i++) {
        array[i] = sc.nextLong();
      }
      return array;
    }
  }

}
