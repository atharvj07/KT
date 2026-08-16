

import java.util.Collections;
import java.util.Scanner;

public class Super {

	public static void main(String[] args) 
	{
		Scanner jk = new Scanner(System.in);
		int n = jk.nextInt();
		Long m = jk.nextLong();
		Double[] ins = new Double[n];
		for (int i=0; i<n; i++)
		{
			Double a = jk.nextDouble();
			Double b = jk.nextDouble();
			ins[i] = (a/b)*m;
		}
		Double ans = ins[0];
		for (Double i:ins)
		{
			if (ans>i)
			{
				ans = i;
			}
		}
		System.out.println(ans);

	}

}
