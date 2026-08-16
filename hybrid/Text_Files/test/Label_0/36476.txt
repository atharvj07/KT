
import java.util.*;
import java.lang.*;
import java.io.*;

public class rr
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc=new Scanner(System.in);
		int tt=sc.nextInt();
		while(tt-->0){
		    int x=sc.nextInt();
		    int y=sc.nextInt();
		    int n=sc.nextInt();
		    int t=n%x;
		    if(t==y){
		        System.out.println(n);
		        
		    }
		    else if(y<t){
		        n-=t-y;
		        		        System.out.println(n);
		    }
		    else{
		        n=n-t-x+(y);
		        System.out.println(n);
		    }
		}
	}
}
