import java.util.*;

public class Main {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		int[] h = new int[n+1];
		for (int i = 1; i <=n; i++) {
			h[i] = s.nextInt();
		}
		long[] a = new long[n+1];
		for (int i = 1; i <= n; i++)
			a[i] = s.nextLong();
		long[] dp = new long[n+1];
		long[] bit=new long[n+1];
		for(int i=1;i<=n;i++) {
			dp[i]=query(h[i]-1,bit)+a[i];
			update(h[i],dp[i],bit);
		}
		long best=0;
		for(int i=1;i<=n;i++) {
			best=Math.max(best, dp[i]);
		}
		System.out.println(best);
	}
	public static long query(int x, long[] bit) {
		long res=0;
		while(x>0) {
			res=Math.max(bit[x], res);
			x-=-x&x;
		}
		return res;
	}
	public static void update(int x, long val, long[] bit) {
		while(x<bit.length) {
			bit[x]=Math.max(bit[x],val);
			x+=-x&x;
		}
	}

}
