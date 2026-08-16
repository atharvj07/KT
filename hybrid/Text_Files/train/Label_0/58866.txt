
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;


public class SaveNature {

  static long gcd(long a, long b) { 
        if (a == 0) return b;           
        return gcd(b % a, a); 
  }

  static long lcm(long a, long b) { 
        return (a * b) / gcd(a, b); 
  } 

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    PrintWriter out = new PrintWriter(System.out);
    int q = sc.nextInt();
    while(q--!=0) {
      int n = sc.nextInt();
      Long[] arr = new Long[n];
      for(int i = 0; i < n; i++) {
        arr[i] = sc.nextLong();
      }
      Arrays.sort(arr,Collections.reverseOrder());
      long x = sc.nextLong(),
      a = sc.nextLong(),
      y = sc.nextLong(),
      b = sc.nextLong();
      if(x<y) {
        long tmp = x;
        x = y;
        y = tmp;
        tmp = a;
        a = b;
        b = tmp;
      }
      long k = sc.nextLong();
      boolean ok = false;
      long lcd = lcm(a,b);
      long l = 1, r = n;
      long ans = 0;
      while(l<=r) {
        int ind = 0;
        long mid = (l+r)/2;
        long tot = 0;
        for(long i = 1; i <= mid; i++) {
          if(i%lcd==0) {
            tot += (arr[ind]*(x+y))/100;
            ind++;
          }
        }
        for(long i = 1; i <= mid; i++) {
          if(i%lcd!=0 && i%a==0) {
            tot += (arr[ind]*x)/100;
            ind++;
          }
        }
        for(long i = 1; i <= mid; i++) {
          if(i%lcd!=0 && i%b==0) {
            tot += (arr[ind]*y)/100;
            ind++;
          }
        }
        if(tot>=k) {
          ok = true;
          r = mid-1;
          ans = mid;
        } else {
          l = mid+1;
        }
      }
      if(ok) {
        out.println(ans);
      } else {
        out.println(-1);
      }
    }
    out.close();
  }

}
