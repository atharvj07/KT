import java.util.*;
import java.io.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;
import static java.lang.Math.*;
//rankaleeさんのをこぴぺさせていただきました...

public class Main {

	int INF = 1 << 28;
	//long INF = 1L << 62;
	double EPS = 1e-10;
	long MOD = (int)(1e8)+7;
	
	void run() {
		Scanner sc = new Scanner(System.in);
		int h = sc.nextInt(), w = sc.nextInt();
		int[] pow = new int[w+1];
		pow[0] = 1;
		for(int i=1;i<=w;i++) pow[i] = (int)(pow[i-1]*3%MOD);
		long[][][] dp = new long[2][3][pow[w]];
		dp[0][0][0] = 1;
		String[] map = new String[h];
		for(int i=0;i<h;i++) map[i] = sc.next();
		int p = 1;
		for(int i=0;i<h;i++) for(int j=0;j<w;j++) {
			for(long[] a: dp[p]) fill(a, 0);
			for(int k=0;k<3;k++) for(int u=0;u<pow[w];u++) if(dp[1-p][k][u] != 0){
				
				int tu = u/pow[j]%3;
//				debug(p, k , u, i, j, tu);
				if(map[i].charAt(j) == '.') {
					if(tu * k > 0) continue;
					if(k == 0 || j < w-1) dp[p][k][u] = ( dp[p][k][u] + dp[1-p][k][u] ) % MOD;
					continue;
				}
				int r = map[i].charAt(j) - '0' - tu - k;
				for(int nk=0;nk<3;nk++) {
					int nu = r - nk;
					if(nu < 0 || nu > 2) continue;
					if(nk == 0 || j < w-1 ) {
						dp[p][nk][u + pow[j]*(nu-tu)] = (dp[p][nk][u + pow[j]*(nu-tu)] + dp[1-p][k][u]) % MOD;
					}
				}
			}
//			debug(dp[p]);
			p = 1-p;
		}
		System.out.println(dp[1-p][0][0]);
	}

	void debug(Object... os) {
		System.err.println(Arrays.deepToString(os));
	}

	public static void main(String[] args) {
		new Main().run();
	}
}