import java.util.*;
import java.io.*;

/*
   AtCoder contest
   coder : yoichidon
 */
public class Main {

    public  static long[] reverse(long[] array){
        int N = array.length;
        long[] ans = new long[N];
        for(int n=0; n<N; n++) ans[n]=array[N-n-1];
        return ans;
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String S = sc.next();
        int N = S.length();

        int[] redMax = new int[N];
        int[] blueMax = new int[N];
        for(int n=0; n<N; n++){
            int b = S.charAt(n)-'0';
            redMax[n] = (n==0) ? 2-b : 2-b+redMax[n-1];
            blueMax[n] = (n==0) ? b : b+blueMax[n-1];
        }

        
        long[][] dp = new long[redMax[N-1]+1][blueMax[N-1]+1];

        for(int r=0; r<=redMax[N-1]; r++) for(int b=0; b<=blueMax[N-1]; b++){
            int turn = r+b;
            if(r==0  && b==0) dp[r][b]=1;
            else if(turn<=N && (redMax[turn-1]<r || blueMax[turn-1]<b)) dp[r][b]=0;
            else if(r==0) dp[r][b]=dp[r][b-1];
            else if(b==0) dp[r][b]=dp[r-1][b];
            else dp[r][b] = (dp[r][b-1]+dp[r-1][b])%998244353;

        }

        System.out.println(dp[redMax[N-1]][blueMax[N-1]]);



    }
}
