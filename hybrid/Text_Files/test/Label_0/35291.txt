/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
public class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		int n;
		long h,k;
		Scanner in = new Scanner(System.in);
		n=in.nextInt();
		h=in.nextLong();
		k=in.nextLong();
		int a[] = new int[n];
		for(int i=0;i<n;i++){
			a[i]=in.nextInt();
		}
		long count=0;
		long sum=0;
		for(int i=0;i<n;){
			while(i<n&&sum+a[i]<=h)
				sum=sum+a[i++];
			count = count+(sum/k);
			sum=sum%k;
			if(i<n&&sum+a[i]>h){
				sum=0;
				count++;
			}
		}
		if(sum>0)count++;
		System.out.println(count);
	}
}