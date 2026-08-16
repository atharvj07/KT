
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char[] s = sc.next().toCharArray();
        sc.close();
        int n = s.length;
        long[][] dp = new long[n+1][13];
        int[] mod = {1,10,9,12,3,4};
        int div = 1000000007;
        dp[0][0] = 1;
        int digit ;
        for(int i=0;i<n;i++){
            if(s[n-1-i]=='?'){
                for(int j=0;j<=9;j++){
                    digit = j*mod[i%6]%13;
                    for(int k=0;k<13;k++){
                        dp[i+1][k] += dp[i][(k-digit+13)%13];
                        dp[i+1][k]%=div;
                    }
                }
            }else{
                digit = (s[n-1-i]-'0')*mod[i%6]%13;
                for(int j=0;j<13;j++){
                    dp[i+1][j] += dp[i][(j-digit+13)%13];
                    dp[i+1][j]%=div;
                }
            }
        }
        System.out.println(dp[n][5]);
    }
}