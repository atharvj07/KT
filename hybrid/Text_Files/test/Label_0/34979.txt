import java.util.* ;


public class PythonIndentation
{
	public static void main(String args[])
	{
		Scanner in = new Scanner(System.in) ;
		int n = in.nextInt() ;
		boolean[] lst = new boolean[n] ;
		for(int i=0;i<n;i++)
		{
			lst[i] = (in.next().equals("s"))?false:true ;
		}
		System.out.println(dp(lst)) ;
	}
	
	static int dp(boolean[] lst)
	{//false in lst means an "s" (simple statement), and true a "f"(for loop)
		int[][] dp = new int[2][lst.length] ;
		dp[0][0] = 1 ;
		for(int i=1;i<lst.length;i++)
		{
			
			for(int j=0;j<lst.length;j++)
			{
				if(lst[i-1])//(i-1)st statement is a for loop 
				{
					if(j==0)
						dp[i%2][j] = 0 ;
					else
						dp[i%2][j] = dp[(i-1)%2][j-1] ;
				}
			
				else//i-1 st statement is a simple statement
				{
					if(j==0)
					{
						int temp = 0 ;
						for(int k=0;k<lst.length;k++)
							temp = (temp+dp[(i-1)%2][k])%1000000007 ;
						dp[i%2][j] = temp ;
					}
					else
						dp[i%2][j] = (dp[i%2][j-1]-dp[(i-1)%2][j-1])%1000000007 ;
				}
			}
		}
		int ans = 0 ;
		for(int i=0;i<lst.length;i++)
		{
			ans = (ans + dp[(lst.length-1)%2][i])%1000000007 ;
		}
		if(ans<0)
			ans = ans + 1000000007 ;
		
		return ans ;
	}
}