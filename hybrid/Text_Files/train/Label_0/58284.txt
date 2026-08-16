import java.util.Scanner;

public class Main {
	
	public static void main(String[] args)
	{
		Scanner s=new Scanner(System.in);
		
		long m=998244353;
		
		int n=s.nextInt();
		int k=s.nextInt();
		
		pair[] arr=new pair[n];
		
		for(int i=0;i<k;i++)
		{
			int l=s.nextInt();
			int r=s.nextInt();
			
			pair p=new pair(l,r);
			arr[i]=p;	
		}
		
		long[] dp=new long[n];
		
		for(int i=n-2;i>=0;i--)
		{
			for(int j=0;j<k;j++)
			{
				int min=i+arr[j].l;
				int max=i+arr[j].r;
				
				if(min>n-1)
				{
					
				}
				else if(max>=n-1)
				{
					dp[i]=(dp[i]%m+1%m)%m;
					
					max=n-2;
					
					if(max>=min)
					{
						dp[i]=(dp[i]%m+(dp[min]%m-dp[max+1]%m+m)%m)%m;
					}
					
				}
				else
				{
					dp[i]=(dp[i]%m+(dp[min]%m-dp[max+1]%m+m)%m)%m;
				}
				
			}
			
			dp[i]=(dp[i]%m+dp[i+1]%m)%m;
			
		}
		
		System.out.println((dp[0]%m-dp[1]%m+m)%m);
		
	}
	
}

class pair
{
	int l;
	int r;
	
	public pair(int l,int r)
	{
		this.l=l;
		this.r=r;
	}
}