import java.util.Scanner;

public class Main {
 
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		String s = input.next();
		long[] dp = new long[2019]; //stores remainder from 0-2018
		int cur = Integer.parseInt(s.substring(s.length()-1,s.length()));
		dp[cur]++;
		dp[0]=1;
		long cnt = 0;
		long pow_10 = 10;
		long div = 2019;
		//(2019 does not share any divisors with 10 (the base), 
		//therefore storing remainder trick works.
		for (int i = s.length()-2; i >= 0; i--) {
			long digit = Long.parseLong(s.substring(i,i+1));
			cur+=digit*pow_10;
			pow_10*=10;
			pow_10%=div;
			cur%=div;
			dp[cur]++;
		}
		for (int i = 0; i < 2019; i++) {
			cnt+=(dp[i])*(dp[i]-1)/2;
		}
		System.out.println(cnt);
	}
}