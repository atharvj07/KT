import java.util.ArrayList;
import java.util.Scanner;

public class e {
	static final long MOD = (long)1e9+7;
	static int n;
	static long s;
	static long[] fs;
	static long[] invs;
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		invs = new long[25];
		invs[1] = 1;
		for (int i = 2; i < invs.length; ++i)
			invs[i] = (MOD - (MOD / i) * invs[((int) (MOD % i))] % MOD) % MOD;
		n = in.nextInt();
		s = in.nextLong();
		fs = new long[n];
		for(int i=0;i<n;i++)
			fs[i] = in.nextLong();
		long ans = genList(0, 1, 0);
		if(ans < 0) ans += MOD;
		System.out.println(ans);
	}
	static long genList(int idx, long c, long pow) {
		if(idx == n) {
			pow = s - pow;
			if(pow < 0)
				return 0;
			long choose = 1;
			for(int i=0;i<n-1;i++) {
				choose *= (pow+n-1-i) % MOD;
				choose %= MOD;
				choose *= invs[i+1];
				choose %= MOD;
			}
			return (c * choose) % MOD;
		}
		long ans = 0;
		ans += genList(idx+1, c, pow);
		ans += genList(idx+1, -c, pow+fs[idx]+1);
		return ans % MOD;
	}
}