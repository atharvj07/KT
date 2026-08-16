import java.util.*;
import java.math.*;
public class Sample
{
	static long m = (long)Math.pow(10,9)+7;
	static long f(long x)
	{
		if(x==0)
			return 1;
		if(x<3)
			return x;
		long a = 2;
		for(long i=3; i<=x; i++)
		{
			a*=i;
			a%=m;
		}
		return a;
	}
	static long p(long x)
	{
		long a = 1;
		for(int i=1; i<x; i++)
		{
			a*=2;
			a%=m;
		}
		return a;
	}
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		long n = in.nextLong();
		long ans = f(n)-p(n);
		ans = ans<0 ? ans+m : ans;
		System.out.println(ans);
	}
}