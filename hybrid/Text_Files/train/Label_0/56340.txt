import java.util.*;
import java.lang.*;
import java.io.*;

public class Problem
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		while(t-->0){
		    int n=sc.nextInt();
		    int k=sc.nextInt();
		    int a=2;
		        while(a<=n){
		            if(n%a==0){
		                n=n+a;
		                break;
		            }
		            a++;
		        }
		        n=n+(k-1)*2;
		    System.out.println(n);
		}
	}
}