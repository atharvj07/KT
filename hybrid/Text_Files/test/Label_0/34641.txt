public class Main{
  static long mod = 1000000007;
  public void run(java.io.InputStream in, java.io.PrintStream out){
    java.util.Scanner sc = new java.util.Scanner(in);
/*answer*/
    long m, n;

    m = sc.nextInt();
    n = sc.nextInt();
    System.out.println(power(m, n));

    sc.close();
  }
  public static void main(String[] args){
    (new Main()).run(System.in, System.out);
  }

  private static long power(long m, long n){
    long q, r;

    if(n == 1)return m;
    else{
      q = n / 2;
      r = n % 2;
      if(r == 0)return (power(((m * m) % mod), q)) % mod;
      else return ((power(((m * m) % mod), q)) * m) % mod;
    }

  }
}