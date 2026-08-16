import java.util.* ;

public class AndPermutations
{
	static int[] andZero(int n)
	{
		if(n%2!=0)
			return null ;
		else
		{
			int[] ans = new int[n+1] ;
			Arrays.fill(ans,-1) ;
			int maxLog = binlog(n) ;
			boolean allDone = false ;
			while(!allDone)
			{
				// System.out.println("maxLog :"+maxLog) ;
				int maxTwo = (1<<maxLog) ;
				while(ans[maxTwo]!=-1)
					maxTwo = maxTwo>>1 ;
				ans[maxTwo] = maxTwo -1 ;
				ans[maxTwo-1] = maxTwo ;
				if(maxTwo==2)
				{
					// System.out.println("maxTwo was equal to 2") ;	
					break ;
				}
				int temp = maxTwo -1 ;
				for(int i=maxTwo+1 ; i<=n;i++)
				{
					
					if(ans[i]!=-1)
					{
						// System.out.println((i)+" --> "+ans[i]) ;
						break ;//has reached a point where things are full.
					}
					ans[i] = --temp ;			
					ans[temp] = i ;
					if(temp==1)
						allDone = true ;
					// if(i==n)
						// System.out.println((i)+" ---> "+ans[i]) ;
				}
				
				maxLog-- ;
			}
			// System.out.println(1+" ---> "+ans[1]) ;
			return ans ;
		}
	}
	static boolean uniques(int[] a)
	{
		int[] b = new int[a.length] ;
		// System.out.println("Length :"+a.length) ;
		for(int i=1;i<a.length;i++)
		{
			// System.out.println("a["+i+"] is :"+a[i]) ;
			if(b[a[i]]==0)
				b[a[i]] = i ;
			else
			{
				System.out.println("Positions "+i+" and "+b[a[i]]+" have the same value :"+a[i]) ;
				return false ;
			}
		}
		return true ;
	}
	public static void main(String args[])
	{
		Scanner in = new Scanner(System.in) ;
		int n = in.nextInt() ;
		int[] ans1 = andZero(n) ;
		// System.out.println(uniques(ans1)) ;
		if(ans1==null)
			System.out.println("NO") ;
		else 
		{
			System.out.println("YES") ;
			for(int i=1;i<ans1.length;i++)
			{
				System.out.print(ans1[i]+" ") ;
			}
			System.out.println() ;
		}
		int[] ans2 = nonZeroAnd(n) ;
		if(ans2==null)
			System.out.println("NO") ;
		else 
		{
			System.out.println("YES") ;
			for(int i=1;i<ans2.length;i++)
			{
				System.out.print(ans2[i]+" ") ;
			}
			System.out.println() ;
		}
	}
	public static int binlog( int bits ) // returns 0 for bits=0
	{
		int log = 0;
		if( ( bits & 0xffff0000 ) != 0 ) { bits >>>= 16; log = 16; }
		if( bits >= 256 ) { bits >>>= 8; log += 8; }
		if( bits >= 16  ) { bits >>>= 4; log += 4; }
		if( bits >= 4   ) { bits >>>= 2; log += 2; }
		return log + ( bits >>> 1 );
	}
	static int[] nonZeroAnd(int n)
	{
		int maxLog = binlog(n) ;
		if((1<<maxLog) == n || n<6)
			return null ;
		else
		{
			int[] ans ;
			if(n==6)
			{
				ans = new int[]{-1,3,6,2,5,1,4} ;
			}
			else 
			{
				ans = new int[n+1] ;
				ans[1] = 7 ;
				ans[2] = 3 ;
				ans[3] = 6 ;
				ans[4] = 5 ;
				ans[5] = 1 ;
				ans[6] = 2 ;
				ans[7] = 4 ;
				if(n>7)
				{
					for(int i=3;i<maxLog;i++)
					{
						int initial = (1<<i) ;
						int max = (initial<<1) ;
						for(int j=initial;j<max-1;j++)
						{
							ans[j] = j+1 ;
						}
						ans[max-1] = initial ;
					}
					int maxTwo = (1<<maxLog) ;
					for(int i=maxTwo;i<n;i++)
					{
						ans[i] = i+1 ;
					}
					ans[n] = maxTwo ;
				}
			}
			return ans ;	
		}
	}
	
}