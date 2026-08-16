import java.util.*;

public class Main {
  static int N;
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    N = sc.nextInt();
    int Q = sc.nextInt();
    for(int i = 0; i < Q; i++) { 
      int v = sc.nextInt();
      int w = sc.nextInt();
      System.out.println(dfs(v, w));
    }
  }

  public static int dfs(int s, int t) {
    int s1 = (s - 1) / N;
    int t1 = (t - 1) / N;
    if((s - 1) % N != 0) s1 += 1;
    if((t - 1) % N != 0) t1 += 1;
    if(s == t) return s;
    if(s >= t) {
      if(N == 1) return t;
      return dfs(s1, t);
    } else {
      if(N == 1) return s;
      return dfs(s, t1);
    }
  }
}