import java.util.*;

public class Main{
	public static void main(String[] arg){
      Scanner sc=new Scanner(System.in);
      int n=sc.nextInt(); 
      int x=sc.nextInt();
      int y=sc.nextInt();
      int dp[][]=new int[n+1][n+1];
      dp[x][y]=1;
      for(int i=1;i<n;i++){
          for(int j=i+1;j<=n;j++){
              dp[i][j]=Math.min((j-i),Math.max(Integer.MIN_VALUE,Math.abs(i-x)+Math.abs(y-j)+1));
          }
      }
      int ans[]=new int[n];
      for(int i=1;i<n;i++){
          for(int j=i+1;j<=n;j++){
              ans[dp[i][j]]++;
          }
      }
      
      for(int i=1;i<n;i++){
        System.out.println(ans[i]);
      }
    }
}