/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
public class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
	    Scanner in=new Scanner(System.in);
	    int t;
	    t=in.nextInt();
	    while(t>0)
	    {
	        int n,i;
	        n=in.nextInt();
	        in.nextLine();
	        String s=in.nextLine();
	        if (s.matches("(2020[0-9]*)||([0-9]*2020)||(202[0-9]*0)||(2[0-9]*020)||(20[0-9]*20)"))
	        System.out.println("YES");
	        else
	        System.out.println("NO");
	        t--;
	    }
	}
}
