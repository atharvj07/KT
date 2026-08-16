public class Main{
  public void run(java.io.InputStream in, java.io.PrintStream out){
    java.util.Scanner sc = new java.util.Scanner(in);
    int n, i, tmp;
    int[] p, l;
    long res1, res2;
    n = sc.nextInt();
    p = new int[n]; l = new int[n];
    for(i = 0;i < n;i++)p[i] = sc.nextInt();
    for(i = 0;i < n;i++)l[i] = sc.nextInt();
    res1 = solve(n, p, l);
    for(i = 0;i < n / 2;i++){
      tmp = p[i]; p[i] = p[n - 1 - i]; p[n - 1 - i] = tmp;
      tmp = l[i]; l[i] = l[n - 1 - i]; l[n - 1 - i] = tmp;
    }
    res2 = solve(n, p, l);
    if(res1 > res2 && res2 != -1)res1 = res2;
    out.println(res1);
    sc.close();
  }
  private static long solve(int n, int[] p, int[] l){
    long res;
    long[] s = new long[n];
    int i;
    s[0] = p[0];
    for(i = 1;i < n;i++)s[i] = p[i] + s[i - 1];
    res = count(s, 0, n);
    for(i = 0;i < n - 1;i++)s[n - 1 - i] -= s[n - 2 - i];
    for(i = 0;i < n;i++)if(s[i] < (long)l[i])return -1;
    return res;
  }
  private static long count(long[] c, int l, int r){
    int m;
    if(l + 1 >= r){
      if(l < r)return 0;
      return 1;
    }else{
      m = (l + r) / 2;
      return (count(c, l, m) + count(c, m, r) + merge(c, l, m, r));
    }
  }
  private static long merge(long[] c, int l, int m, int r){
    int nl, nr;
    int i, j, k;
    long infi = Long.MAX_VALUE;
    long[] cl, cr;
    long count;
    nl = m - l; nr = r - m;
    cl = new long[nl + 1]; cr = new long[nr + 1];
    for(i = 0;i < nl;i++)cl[i] = c[l + i];
    for(i = 0;i < nr;i++)cr[i] = c[m + i];
    cl[nl] = infi; cr[nr] = infi;
    i = 0; j = 0; count = 0;
    for(k = l;k < r;k++){
      if(cl[i] < cr[j])c[k] = cl[i++];
      else{
        c[k] = cr[j++]; count += (nl - i);
      }
    }
    return count;
  }
  public static void main(String[] args){
    (new Main()).run(System.in, System.out);
  }
}