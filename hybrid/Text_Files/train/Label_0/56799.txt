/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
public class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
		BufferedReader bf=new BufferedReader(new InputStreamReader(System.in));
		int t=Integer.parseInt(bf.readLine());
		while(t-->0)
		{
		    String s[]=bf.readLine().split(" ");
		    int c=Integer.parseInt(s[0]);
		    int m=Integer.parseInt(s[1]);
		    int x=Integer.parseInt(s[2]);
		    
		    int z=Math.min(x,Math.min(c,m));
		    int count=z;
		     c=c-z;
		     m=m-z;
		     x=x-z;
		     if(c==0 || m==0)
		     {
		         System.out.println(count);
		     }
		     else
		     {
		         int min=Math.min(c,m);
		         int max=Math.max(c,m);
		    //     System.out.println("min "+min+" "+max);
		         if(2*1L*min<=max)
		         {
		             System.out.println(count+0L+min);
		         }
		         else
		         {
		             long k=(min+0L+max)/3;
		             System.out.println(count+0L+k);
		         }
		     }
		    
		    
		    
		}
	}
}
