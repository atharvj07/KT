
import java.util.*;
import java.lang.*;
public class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
	    Scanner sc = new Scanner(System.in);
	    int n = sc.nextInt();
	    int a[]=new int[n];
	    int e=0,ec=0,o=0,oc=0;
	    for(int i=0;i<n;i++)
	    {
	    a[i]=sc.nextInt();
	    if(a[i]%2==0)
	    {
	        e=i;
	        ec++;
	    }
	    else{
	    o=i;
	    oc++;
	    }
	    }
	    if(ec==1)
	    System.out.println(e+1);
	    else
	    System.out.println(o+1);
	    
	   
		
	}
}
