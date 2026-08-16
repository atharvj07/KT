import java.util.*;
import java.io.*;

public class D {

	static int [] bits ;
	static long [][][] memo ; // less , k , pos
	
	static long dp(int less , int rem , int pos)
	{
		
		if(rem == 0)
			return 1 ; 
		
		if(pos == bits.length)
			return 0 ; 
		
		if(memo[less][rem][pos] != -1)
			return memo[less][rem][pos] ; 
		
		long take = (less | bits[pos]) == 0 ? 0 : dp(less, rem - 1, pos + 1); 
		long leave = dp(less | bits[pos] , rem, pos + 1) ; 
		
		
		return memo[less][rem][pos] = take + leave ; 
		
	}
	static int len(long num)
	{
		int ans = 0 ; 
		
		while(num > 0)
		{
			num /= 2 ; 
			
			ans ++ ; 
		}
	
		return ans ; 
	
	}
	static long sum(long num , int k)
	{
		long l = num , r = num << 1l ; 
		
		long ans = 0l ; 
		
		int len = len(r);
		
		bits = new int[len];
		
		long temp = r ;
		for(int i = len - 1 ; i >= 0 ; i-- , temp >>= 1)
			bits[i] = (temp & 1) != 0 ? 1 : 0 ; 
		
		memo = new long [2][k+1][len];
		for(int i = 0 ; i < 2 ; i++)
			for(int j = 0 ;  j <= k ; j++)
				Arrays.fill(memo[i][j], -1);
		
		ans += dp(0, k , 0);
		
		len = len(l) ; 
		bits = new int [len];
		
		
		temp = l ;
		for(int i = len - 1 ; i >= 0 ; i-- , temp >>= 1)
			bits[i] = (temp & 1) != 0 ? 1 : 0 ; 
		
		memo = new long [2][k+1][len];
		for(int i = 0 ; i < 2 ; i++)
			for(int j = 0 ;  j <= k ; j++)
				Arrays.fill(memo[i][j], -1);
		
		ans -= dp(0, k , 0);
		
		
		
		return ans ; 
		
	}
	
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner();
		
		long m = sc.nextLong() , ans = -1 ,  start = 1 , end = (long)1e18; 
		int k = sc.nextInt()  ;
		
		
		while(start <= end)
		{
			long mid = (start + end) / 2 ; 
			long cnt = sum(mid , k);
			if(cnt >= m)
			{
				end = mid - 1 ;
				ans = mid ;
			}
			else 
				start = mid + 1;
		}
		
		System.out.println(ans);

	}

	static class Scanner {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		String next() throws Exception {
			while (st == null || !st.hasMoreTokens())
				st = new StringTokenizer(br.readLine());

			return st.nextToken();
		}

		int nextInt() throws Exception {
			return Integer.parseInt(next());
		}

		long nextLong () throws Exception
		{
			return Long.parseLong(next());
		}

	}

}
