/*package whatever //do not write package name here */

import java.util.*;

public class GFG {
	public static void main (String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int a[]=new int[2001];
		int i,c=0,res=-1;
		for(i=0;i<n;i++)
		{
		    int n1=sc.nextInt();
		    a[i+1]=n1;
		}
		for(i=0;i<n;i++)
		{
		    int current=i+1;
		    while(current!=-1)
		    {
		        current=a[current];
		        c+=1;
		    }
		    res=Math.max(res,c);
		    c=0;
		}
		System.out.println(res);
	}
}