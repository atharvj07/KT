import java.util.*;

public class Main {
  public static void main(String[] args) {
    long MOD = (long)Math.pow(10, 9) + 7;
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] a = new int[n];
    for(int i = 0; i < n; i++) {
      a[i] = sc.nextInt();
    }
    int[] b = new int[n + 1];
    b[0] = 0;
    for(int i = 0; i < n; i++) {
      b[i + 1] = b[i] ^ a[i];
    }
    long ans = 0;
    if(b[n] != 0) {
      int p = b[n];
      long[] dp1 = new long[n + 1];
      long[] dp2 = new long[n + 1];
      dp1[0] = 1;
      dp2[0] = 0;
      for(int i = 1; i < n + 1; i++) {
        if(b[i] == 0) {
          dp1[i] = (dp1[i - 1] + dp2[i - 1]) % MOD;
        } else {
          dp1[i] = dp1[i - 1];
        }
        if(b[i] == p) {
          dp2[i] = (dp2[i - 1] + dp1[i - 1]) % MOD;
        } else {
          dp2[i] = dp2[i - 1];
        }
      }
      ans = (dp2[n] - dp2[n - 1] + MOD) % MOD;
    } else {
      long kosuu = 0;
      long[] q = new long[n + 1];
      q[0] = 1;
      for(int i = 1; i < n + 1; i++) {
        if(b[i] == 0) {
          q[i] = q[i - 1] + 1;
        } else {
          q[i] = q[i - 1];
        }
      }
      kosuu = q[n - 1] - q[0];
      long t = 1;
      for(long i = 0; i < kosuu; i++) {
        t = (t * 2) % MOD;
      }
      ans = t;
      HashMap<Integer, ArrayList<Integer>> map = new HashMap<Integer, ArrayList<Integer>>();
      for(int i = 1; i < n; i++) {
        if(b[i] != 0) {
          if(map.containsKey(b[i])) {
            ArrayList<Integer> list = map.get(b[i]);
            list.add(i);
            map.put(b[i], list);
          } else {
            ArrayList<Integer> list = new ArrayList<Integer>();
            list.add(i);
            map.put(b[i], list);
          }
        }
      }
      for(int p : map.keySet()) {
        ArrayList<Integer> list = map.get(p);
        int x = list.size();
        long[] dp1 = new long[x];
        long[] dp2 = new long[x];
        dp1[0] = 1;
        dp2[0] = 1;
        for(int i = 1; i < x; i++) {
          int k = list.get(i);
          int s = list.get(i - 1);
          long w = q[k] - q[s];
          long m = (dp1[i - 1] * w) % MOD;
          dp1[i] = (dp1[i - 1] + m + dp2[i - 1]) % MOD;
          dp2[i] = (m + dp2[i - 1]) % MOD;
        }
        ans = (ans + dp1[x - 1]) % MOD;
      }
    }
    System.out.println(ans);
  }
}