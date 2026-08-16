import java.util.*;

public class D {
	static final int MOD = 1000000007;
	static final int MAX = 200000;
	static final long [] FACTORIAL = new long[MAX];
	static final long [] INVERTED = new long[MAX];
	static{
		FACTORIAL[0] = 1;
		for (int i = 1; i < MAX; ++i){
			FACTORIAL[i] = (FACTORIAL[i - 1]*i)%MOD;
		}
		for (int i = 0; i < MAX; ++i){
			INVERTED[i] = pow(FACTORIAL[i], MOD - 2);
		}
	}
	static long c(int n, int m){
		long res = FACTORIAL[n];
		res = (res*INVERTED[m])%MOD;
		res = (res*INVERTED[n - m])%MOD;
		return res;
	}
	static long pow(long n, long m){
		if (m == 0){
			return 1;
		}
		if (m == 1){
			return n;
		}
		long res = pow(n, m >> 1);
		res = (res * res)%MOD;
		if ((m&1) == 1){
			res = (res * n)%MOD;
		}
		return res;
	}
	static long solve(int n, int m, int g){
		long [] count = new long [2];
		if (n == 0){
			count[(m&1)^1] = 1;
		}else if (m == 0){
			if (n == 1){
				count[1] = 1;
			}else{
				count[0] = 1;
			}
		}else{
			for (int i = 0; i < m; ++i){
				count[(i&1)] += c(n - 1 + m - i, n - 1);
				count[(i&1)] %= MOD;
			}
			if (n == 1){
				count[(m&1)^1] += 1;
			}else{
				count[(m&1)] += 1;
			}
		}
		return count[g]%MOD;
	}
	public static void main(String [] args){
		final Scanner s = new Scanner(System.in);
		final int n = s.nextInt();
		final int m = s.nextInt();
		final int g = s.nextInt();
		System.out.println(solve(m, n, g));
		s.close();
	}
}
