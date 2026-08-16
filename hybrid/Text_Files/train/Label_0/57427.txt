import java.util.Scanner;
public class Main
{	
	public static void main(String arg[])
	{
		Scanner in =new Scanner(System.in);
		while(in.hasNext())
		{
			int n=in.nextInt();
			if(n==0)
				return;
			int a[]=new int[n];
			double b[]=new double[n];
			for(int i=0;i<n;i++)
			{
				a[i]=in.nextInt();
				double h=in.nextDouble()/100;
				double w=in.nextDouble();
				b[i]=w/(h*h);
			}
			double ans =Integer.MAX_VALUE;
			int index=0;
			for(int i=0;i<n;i++)
			{
				double tmp =Math.abs(22-b[i]);
				if(ans>tmp)
				{
					ans =tmp;
					index=i;
				}
			}
			System.out.println(a[index]);
		}
	}
}