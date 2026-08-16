import java.io.*;
import java.util.*;

class Main {
  static class FastScanner {
    private final InputStream in = System.in;
    private final byte[] buffer = new byte[1024];
    private int ptr = 0;
    private int buflen = 0;
    private boolean hasNextByte() {
      if (ptr < buflen) {
        return true;
      }else{
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
    private int readByte() { if (hasNextByte()) return buffer[ptr++]; else return -1;}
    private static boolean isPrintableChar(int c) { return 33 <= c && c <= 126;}
    public boolean hasNext() { while(hasNextByte() && !isPrintableChar(buffer[ptr])) ptr++; return hasNextByte();}
    public String next() {
      if (!hasNext()) throw new NoSuchElementException();
      StringBuilder sb = new StringBuilder();
      int b = readByte();
      while(isPrintableChar(b)) {
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
      while(true){
        if ('0' <= b && b <= '9') {
          n *= 10;
          n += b - '0';
        }else if(b == -1 || !isPrintableChar(b)){
          return minus ? -n : n;
        }else{
          throw new NumberFormatException();
        }
        b = readByte();
      }
    }
    public int nextInt() {
      long nl = nextLong();
      if (nl < Integer.MIN_VALUE || nl > Integer.MAX_VALUE) throw new NumberFormatException();
      return (int) nl;
    }
    public double nextDouble() { return Double.parseDouble(next());}
  }

  /**
   * PrimeTools class provides functions dealing with primes, calculating primes
   * upto N in advance.
   *
   * Note that when you only deal with factors, N <- sqrt(N) would be enough.
   */
  static class PrimeTools {
    List<Long> primes = new ArrayList<>(1000);

    private void eratosthenesPrimes(int N) {
      long[] tmp = new long[N+1];
      Arrays.fill(tmp, 1);
      tmp[0] = 0;
      tmp[1] = 0;
      tmp[2] = 1;

      if (N<=1) return;
      primes.add(2L);
      if (N<=2) return;

      for(int i=3; i<=N; i+=2) {
        if (tmp[i] == 0) continue;
        primes.add((long)i);
        if (N<i*i) continue;
        for (int k=i+i; k<=N; k+=i) {
          tmp[k]=0;
        }
      }
    }

    public PrimeTools() {
      this(10000000);
    }

    public PrimeTools(int N) {
      eratosthenesPrimes(N);
    }

    public boolean isPrime(long n) {
      return Collections.binarySearch(primes, n) >= 0;
    }

    // A return set
    // * does not include 1
    // * includes n
    //
    // 2 -> {2}
    // 6 -> {2, 3}
    // 16 -> {2}  // uniqueなもののみ
    //
    // 約数を知りたい場合は、divisors()
    public Set<Long> uniqueFactors(long n) {
      Set<Long> ret = new TreeSet<>();
      if (n==1) return ret;

      for (long p : primes) {
        if (n==1) break;
        if (p*p>n) break;

        if (n % p == 0) {
          ret.add(p);
          while (n % p == 0) {
            n /= p;
          }
        }
      }
      if (n>1) ret.add(n);
      return ret;
    }

    public Map<Long, Long> factorExponents(long n) {
      Map<Long, Long> ret = new TreeMap<>();
      if (n==1) return ret;

      for (long p : uniqueFactors(n)) {
        if (n % p == 0) {
          ret.put(p, 0L);
          while (n % p == 0) {
            n /= p;
            ret.put(p, ret.get(p)+1);
          }
        }
      }
      if (ret.isEmpty()) ret.put(n, 1L);
      return ret;
    }

    /*
     * Rutuns a vector of sorted products of b^0, b^1, ... , b^n"
     */
    static private List<Long> makeProducts(long base, long n) {
      List<Long> ret = new ArrayList<>((int)(n+1));
      ret.add(1L);
      for (long i=1; i<=n; i++) {
        ret.add(ret.get(ret.size()-1)*base);
      }
      return ret;
    }

    /*
     * Returns a sorted sequence of divisors of n.
     * For example, 12 => (1 2 3 4 6 12)"
     */
    public List<Long> divisors(long n) {
      List<Long> ret = new ArrayList<>();
      ret.add(1L);
      for (Map.Entry<Long, Long> kv : factorExponents(n).entrySet()) {
        List<Long> products = makeProducts(kv.getKey(), kv.getValue());
        List<Long> tmp = new ArrayList<>(ret.size()*products.size());
        for (long x : ret) {
          for (long y : products) {
            tmp.add(x*y);
          }
        }
        ret = tmp;
      }
      Collections.sort(ret);
      return ret;
    }

  };

  public static void main(String[] args) {
    FastScanner sc = new FastScanner();
    // * word: next()
    // * integer: nextInt(), nextLong()
    // * string: nextLine()
    long N = sc.nextLong();
    PrimeTools primes = new PrimeTools();

    long ret = 0;
    for (long x : primes.divisors(N)) {
      System.err.println("HOGE " + x);
      x -= 1;
      if (x < 1) continue;

      long q = N/x;
      long r = N%x;
      if (q==r) ret += x;
    }

    System.out.println(ret);
  }
}

/* vim: set expandtab ts=2 sw=2 sts=2 : */
