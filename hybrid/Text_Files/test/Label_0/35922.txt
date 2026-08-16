import java.util.Scanner;

public class Solution653B {
	public static void main(String args[]) {
		Scanner sc=new Scanner(System.in);
		int t;
		t=sc.nextInt();
		long out[]=new long[t];
		for(int i=0;i<t;i++)
		{
			long n;
			n=sc.nextLong();
			if(n==1)
			out[i]=0;
			else
			{
				long nm=0;
				while(n%6==0)
				{	nm++;
					n=n/6;
				}
				while(n%3==0)
				{	nm+=2;
					n=n/3;
				}
				if(n==1)
					out[i]=nm;
				else
					out[i]=-1;
			}
		}
		for(int i=0;i<t;i++)
			System.out.println(out[i]);
	}
}
