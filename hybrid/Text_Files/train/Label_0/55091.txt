
import java.util.*;
import java.io.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;
import static java.lang.Math.*;

public class Main {

	int INF = 1 << 28;
	//long INF = 1L << 62;
	double EPS = 1e-10;

	void run() {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		String id = sc.next();
		int m = sc.nextInt(); HashSet<Integer> vs = new HashSet<Integer>();
		for(int i=0;i<m;i++) vs.add(sc.nextInt());
		long[][] dp = new long[2][10]; dp[0][0] = 1;
		int p=1;
		for(int i=1;i<=n;i++) {
			fill(dp[p], 0);
			for(int j=0;j<10;j++) {
				if(id.charAt(n-i) != '*' )  dp[p][(j+v((id.charAt(n-i)-'0')*(i%2==1? 1: 2)))%10] += dp[1-p][j];
				else for(int k: vs) dp[p][(j+v(k*(i%2==1? 1: 2)))%10] += dp[1-p][j];
			}
//			debug(dp[p]);
			p = 1-p;
		}
		System.out.println(dp[1-p][0]);
	}
	
	int v(int v) {
		return v/10 + v%10;
	}

	void debug(Object... os) {
		System.err.println(Arrays.deepToString(os));
	}

	public static void main(String[] args) {
		new Main().run();
	}
}