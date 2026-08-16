import java.lang.reflect.Array;
import java.util.*;
import java.io.*;

/*

*/

public class Main{
    static long MOD=998244353;
    public static int check(int a,int b){
        if(a==0){
            if(b==0){
                return 0;
            }else {
                return 1;
            }
        }else if(a==1){
            if(b==2){
                return 2;
            }else {
                return 0;
            }
        }else if(a==2) {
            if(b==1){
                return 2;
            }else {
                return 0;
            }
        }else {
            if(b==3){
                return 0;
            }else {
                return 1;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw=new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        StringTokenizer st=new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        long[][][] dp=new long[1001][2003][4];
        dp[1][1][0]=1;//ww
        dp[1][2][1]=1;//wb
        dp[1][2][2]=1;//bw
        dp[1][1][3]=1;//bb
        for(int i=2;i<=n;i++){
            for(int j=1;j<=(2*n);j++){
                for(int a=0;a<4;a++){
                    for(int b=0;b<4;b++){
                        int components=j+check(a,b);
                        dp[i][components][b]=(dp[i][components][b]+dp[i-1][j][a])%MOD;
                    }
                }
            }
        }
        long ans=0;
        for(int j=0;j<4;j++){
            ans=(ans+dp[n][k][j])%MOD;
        }

        pw.println(ans);



        pw.close();
    }
}