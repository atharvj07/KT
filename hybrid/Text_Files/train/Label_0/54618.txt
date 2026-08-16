/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;
import java.util.Arrays;
import java.math.BigInteger;
 
/* Name of the class has to be "Main" only if the class is public. */
public class Main
{
     public static void main (String[] args) throws java.lang.Exception
     {
     	Scanner in =new Scanner(System.in);
		int n,j,t=1,i,m,p=0,h;
		String st,s,s1="";
		//substring( //toCharArray();
		//Arrays.sort();
		s=in.next();
		n=s.length();
		char c[]=s.toCharArray();
		for(i=0;i<n;i++)
		{
		     if(c[i]=='a' || c[i]=='i'|| c[i]=='e'|| c[i]=='o'|| c[i]=='u' || c[i]=='1'|| c[i]=='3'|| c[i]=='5'|| c[i]=='7'|| c[i]=='9')
		          p++;
		}
		System.out.println(p);
     }
}