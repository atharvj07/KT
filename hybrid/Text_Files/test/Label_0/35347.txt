import java.util.*;
import java.io.*;

class Main {
  final static int mod = 1000000000 + 7;
  static long [] sum;
  static void addValue(int node, long value) {
    while(node > 0) {
      value = (value * node) % mod;
      sum[node] = (sum[node] + value) % mod;
      node >>= 1;
    }
  }
  static long getSum(int node, long value) {
    long ans = 0;
    while(node > 1) {
      value = (value * node) % mod;
      long product = (value * (node >> 1)) % mod;
      ans = (ans + product * sum[node ^ 1]) % mod;
      node >>= 1;
    }
    return ans;
  }
  static long pathProduct(int cur, int root) {
    long product = 1;
    while(true) {
      product = (product * cur) % mod;
      if(cur == root) break;
      cur >>= 1;
    }
    return product;
  }
  public static void main(String [] args) {
    Reader in = new Reader();
    int h = in.nextInt();
    int n = (1 << (h - 1));
    int [] a = new int [n];
    sum = new long [1 << h];
    for(int i = 0; i < n; i++) {
      a[i] = in.nextInt() - 1;
    }
    long ans = 0;
    for(int i = 1; i < n; i++) {
      int [] left = getIndex(2 * i, h);
      int [] right = getIndex(2 * i + 1, h);
      for(int j : left) {
        addValue(a[j - n] + n, pathProduct(j, 2 * i));  
      }
      for(int j : right) {
        ans = (ans + getSum(a[j - n] + n, pathProduct(j, i))) % mod; 
      }
      for(int j : left) {
        addValue(a[j - n] + n, (mod - pathProduct(j, 2 * i)) % mod);
      }
    }
    System.out.println(ans);
  }
  static int msb(int value) {
    for(int i = 31; i >= 0; i--) {
      if(((value >> i) & 1) == 1) {
        return i;
      }
    }
    return 0;
  }
  static int [] getIndex(int node, int h) {
    int remaining = h - msb(node) - 1;
    int [] a = new int [1 << remaining];
    for(int i = 0; i < (1 << remaining); i++) {
      a[i] = node * (1 << remaining) + i;
    }
    return a;
  }
}

class Reader {
  BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
  StringTokenizer s = new StringTokenizer("");
  Reader () {}
  String nextLine() {
    try {
      return in.readLine();
    } catch (Exception e) {
      e.printStackTrace();
      return "Error";
    }
  }
  String next() {
    while(!s.hasMoreTokens()) {
      s = new StringTokenizer(nextLine());
    }
    return s.nextToken();
  }
  int nextInt() {
    return Integer.parseInt(next());
  }
}

