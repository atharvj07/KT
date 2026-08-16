import java.util.*;
public class Main {
	static int H, W;
	static int a[][];
	static int dp[][];
	static long ans;
	static int mod = (int)1e9+7;
	static int DH[] = {0,1}, DW[]= {1,0};
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		H = sc.nextInt(); W = sc.nextInt();
		a = new int[H][W];
		for(int i=0;i<H;i++) {
			String s = sc.next();
			for(int j=0;j<W;j++) {
				if(s.charAt(j)=='#') a[i][j] = -1;
			}
		}
		sc.close();
		
		//number of routes from point
		dp = new int[H][W];
		for(int i=0;i<H;i++) {
			for(int j=0;j<W;j++) {
				dp[i][j]=-1;
			}
		}
		dp[H-1][W-1]=1;
		ans = rec(0, 0);
		
		System.out.println(ans);
		
	}
	static int rec(int h, int w) {
		if(dp[h][w]!=-1) return dp[h][w];
		//if(h==H-1 && w == W-1)return 1;
		long ret = 0;
		for(int i=0;i<2;i++) {
			int nh = h + DH[i], nw= w + DW[i];
			if(0<=nh&&nh<H&&0<=nw&&nw<W) {
				if(a[nh][nw]==-1)continue;
				ret += rec(nh, nw); 
				ret %= mod;
			}
		}
		return dp[h][w] = (int)ret;
	}
}
