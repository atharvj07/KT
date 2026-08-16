import java.util.*;

public class Main {
    static long MOD = 998244353;
    
    public static void main(String[] args) throws Exception {
        // Your code here! 
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int s = sc.nextInt();
        int[] array = new int[n];
        for (int i = 0; i < n; i++) {
            array[i] = sc.nextInt();
        }
        
        // ans: f(T)の全パターンの和
        // f(T): 集合Tの部分集合であって、和がsになるパターン数
        long ans = 0;
        
        // ans: [x^s] (f{1}+f{2}+f{3}+f{1,2}+f{1,3}+f{2,3}+f{1,2,3})
        // ex. f{1,2,3}: f1f2f3 - 1
        // ex. f{1,2}: f1f2 - 1
        
        // ex. n = 3, s = 4, array[] = {2, 2, 4}
        // -> f{3}に1個、f{1,2}に1個、f{1,3}に1個、f{2,3}に1個、f{1,2,3}に2個 -> ans = 6
        // F1: f1 - 1
        // F2: (F1+1)(f2+1) - 1 = f1 + f1f2 + f2
        // F3: (F2+1)(f3+1) - 1 = f1+f1f2+f2 + f1f3+f1f2f3+f2f3 + f3
        // Fn: (Fn-1+1)(fn+1) - 1 = (f1+1)(f2+1)(...)(fn+1)
        // -> ans: [x^s] (Fn) = [x^s] (f1+1)(f2+1)(...)(fn+1)
        
        // dp[i][s]: [x^s] (Fi)
        long[][] dp = new long[n+1][s+1];
        dp[0][0] = 1;
        for (int i = 0; i < n; i++) {
            int offset = array[i];
            
            // Fi = (Fi-1)(fi + 1)
            
            // Fi-1fi (選ぶ)
            for (int j = s; j - offset >= 0; j--) {
                dp[i+1][j] += dp[i][j-offset];
                dp[i+1][j] %= MOD;
            }
            // Fi-1fi (選ばない)
            for (int j = 0; j <= s; j++) {
                dp[i+1][j] += dp[i][j];
                dp[i+1][j] %= MOD;
            }
            // Fi-1
            for (int j = 0; j <= s; j++) {
                dp[i+1][j] += dp[i][j];
                dp[i+1][j] %= MOD;
            }
        }
        // for (int i = 0; i <= n; i++) {
        //     System.out.println(Arrays.toString(dp[i]));
        // }
        
        System.out.println(dp[n][s]);
    }
}