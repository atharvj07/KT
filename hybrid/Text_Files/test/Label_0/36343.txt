import java.util.*;

public class Main{
    void solve(){
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] a = new int[n];
        int[] b = new int[n];
        int[] c = new int[n];
        for(int i = 0; i < n; i++){
            a[i] = scan.nextInt();
            b[i] = scan.nextInt();
            c[i] = scan.nextInt();
        }
        int[][] dp = new int[n + 1][3];
        for(int i = 0; i < n; i++){
            dp[i + 1][0] = Math.max(dp[i][1] + b[i], dp[i][2] + c[i]);
            dp[i + 1][1] = Math.max(dp[i][0] + a[i], dp[i][2] + c[i]);
            dp[i + 1][2] = Math.max(dp[i][0] + a[i], dp[i][1] + b[i]);
        }
        System.out.println(Math.max(dp[n][0], Math.max(dp[n][1], dp[n][2])));
    }
    
    public static void main(String[] args){
        new Main().solve();
    }
}
