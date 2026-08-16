import java.util.Scanner;

/**
 * https://abc050.contest.atcoder.jp/tasks/arc066_a
 */
public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int N = Integer.parseInt(sc.next());
		int[] dp = new int[N];
		for(int i=0; i<N; i++) dp[Integer.parseInt(sc.next())]++;
		sc.close();
		
		boolean f = true;
		for(int i=N-1; i>=0; i-=2){
			if((i>0&&dp[i]!=2)||(i==0&&dp[i]!=1)){
				f = false;
				break;
			}
		}
		
		long ans = f ? getPower(2, N/2) : 0;
		System.out.println(ans);

	}
	
	static final int MOD = 1000000007;
	
	static long getPower(long n, long m) {
		if(m==0){
			return 1;
		}else if(m%2==0){
			return getPower(getMod(n*n), m/2);
		}else{
			return getMod(n*getPower(n,m-1));
		}
	}
	
	static long getMod(long a){
		return a>=0 ? a%MOD : MOD + a%MOD;
	}

}
