import java.util.Scanner;
public class Main
{
	public static void main(String arg[])
	{
		Scanner sc = new Scanner(System.in);
		while(sc.hasNext())
		{
			int n=sc.nextInt();
			if(n==0)
				return;
			if(n==1)
			{
				System.out.println("deficient number");
				continue;
			}
			
			int sum=1;			
			for(int i=2;i*i<n;i++)
			{
				if(n%i==0)
				{
					sum+=i+n/i;
					if(i==n/i)
						sum-=i;
				}
				if(sum>n)
				{
					System.out.println("abundant number");
					break;
				}
			}
			if(n==sum)
				System.out.println("perfect number");
			else if(n>sum)
				System.out.println("deficient number");
		}
	}
}