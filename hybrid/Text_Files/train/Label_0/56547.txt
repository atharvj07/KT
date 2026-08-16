import java.util.Scanner;

public class Main {

    public static void main(String[] args){
	
	Scanner stdin = new Scanner(System.in);
	int n = stdin.nextInt();
	int m = stdin.nextInt();
	long S[] = new long[n];
	final long mod = 1000000007;

	for (int i = 0 ; i < n ; i++ ){
	    S[i] = stdin.nextInt();
	}

	//System.out.println(S[0]+S[1]);

	long nowmax = 0;
	long X[] = new long[n];

	for (int i = 0 ; i < n ; i++){
	    X[i] = nowmax;
	    nowmax = Math.max(nowmax , S[i]);
	}

	long nowmin = 10000;
	long Y[] = new long[n];

	for (int i = n-1 ; i > -1 ; i-- ){
	    Y[i] = nowmin;
	    nowmin = Math.min(nowmin , S[i]);
	}

	long dp[][] = new long[n][m+1];

	for (int i = 0 ; i < n ; i++ ){

	    if (i == 0){
		dp[i][1] = 2;
		continue;
	    }

	    long s = S[i];
	    long x = X[i];
	    long y = Y[i];

	    if (x < y && x < s){
		for (int p = 0 ; p < m+1 ; p++){
		    if (p + 1 <= m){
			dp[i][p+1] += dp[i-1][p];
			dp[i][p+1] %= mod;
		    }
		    if (i-p+1 <= m && 0 <= i-p+1){
			dp[i][i-p+1] += dp[i-1][p];
			dp[i][i-p+1] %= mod;
		    }	    
		}
	    }else if (x < y && s < x){
		for (int p = 0; p < m+1 ; p++){
		    if (i-p+1 <= m && 0 <= i-p+1){
			dp[i][p] += dp[i-1][p];
			dp[i][p] %= mod;
		    }
		}
	    }else if (x > y && x < s){
		for (int p = 0; p < m+1 ; p++){
		    if (p+1 <= m){
			dp[i][p+1] += dp[i-1][p];
			dp[i][p+1] %= mod;
		    }
		}
	    }else if (s > y){
		System.out.println(0);
		return;
	    }else{
		for (int p = 0 ; p < m+1 ; p++){
		    if (i-p+1 <= m && 0 <= i-p+1){
			dp[i][p] += dp[i-1][p];
			dp[i][p] %= mod;
		    }
		}
	    }
   
	}

	long ans = 0;
	for (int i = 0; i < m+1 ; i++){
	    ans += dp[n-1][i];
	    ans %= mod;
	}

	System.out.println(ans);
	
    }

}

