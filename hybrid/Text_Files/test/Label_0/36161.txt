import java.io.*;
import java.util.*;

import org.omg.CORBA.PUBLIC_MEMBER;


public class Main 
{
	public static int cnt1,cnt2,x,y;
	static StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
	public static void main(String[] args)throws IOException
	{
		while (in.nextToken() != StreamTokenizer.TT_EOF) 
		{
			cnt1=(int)in.nval;
			cnt2=nextInt();
			x=nextInt();
			y=nextInt();
			long l=1;
			long r=(long) 1e18;
			long a=(l+r)/2;
			while(true)
			{
				if(l==r)
				{
					System.out.println(l);
					break;
				}
				else if(r-l==1)
				{
					if(f(r))
						System.out.println(r);
					else 
					{
						System.out.println(l);
					}
					break;
				}
				else 
				{
					if(f(a))
					{
						r=a;
						a=(l+r)/2;
					}
					else 
					{
						l=a;
						a=(l+r)/2;
					}
				}
			}
		}
	}

	static boolean f(long v)
	{
		long f1=v/x;
		long f2=v/y;
		long both=v/(x*y);
		long f11=f1-both;
		long f22=f2-both;
		long other=v-f11-f22-both;
		long g1,g2;
		if(f22>cnt1)
		{
			g1=0;
		}
		else
		{
			g1=cnt1-f22;
		}
		if(f11>cnt2)
		{
			g2=0;
		}
		else
		{
			g2=cnt2-f11;
		}
		return (g1+g2<=other);
	}
	static int nextInt() throws IOException {
		in.nextToken();
		return (int) in.nval;
	}

	static String nextLine() throws IOException 
	{
		in.nextToken();
		return in.sval; 
	} 

}

					 					    			  	