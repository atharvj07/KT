/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
public class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner in = new Scanner(System.in);
		String s = in.next();
		char c = s.charAt(0);
		int d = Integer.parseInt(s.charAt(1)+"");
		
		
		if(c == 'a' || c == 'h') {
		    if(d == 1 || d == 8) System.out.println(3);
		    else System.out.println(5);
		}else {
		    if(d == 1 || d == 8) System.out.println(5);
		    else System.out.println(8);
		}
		
		
	}
}
