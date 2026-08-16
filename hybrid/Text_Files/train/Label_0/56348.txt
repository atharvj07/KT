
import java.util.*;
public class Main {

	public static void main(String[] args) {
		Scanner in=new Scanner(System.in);
		while(true) {
			int n=in.nextInt();
			if(n==0)break;
			
			int dp[][]=new int[n][n];
			for(int i=0;i<n;i++) {
				String str=in.next();
				for(int j=0;j<n;j++) {
					dp[i][j]=str.charAt(j)=='.'? 1 : 0;
				}
			}
			
			
			int max=0;
			for(int i=0;i<n;i++) {
				for(int j=0;j<n;j++) {
					if(dp[i][j]>0 && isEx(dp,i,j)) {
						dp[i][j]=Math.min(dp[i-1][j], Math.min(dp[i][j-1], dp[i-1][j-1]))+1;
					}
					max=Math.max(max, dp[i][j]);
				}
			}
			System.out.println(max);
		}
	}
	
	static boolean isEx(int A[][],int y,int x) {
		if(y-1>=0 && x-1>=0) {
			if(A[y-1][x]>0 && A[y][x-1]>0 && A[y-1][x-1]>0)return true;
		}
		return false;
	}

}

