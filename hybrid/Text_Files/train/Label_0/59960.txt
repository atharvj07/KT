import java.util.Scanner;
import java.math.BigInteger;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.*;
import java.util.List;
import java.lang.Math;
import java.util.HashMap;
public class javasample {
	static boolean isPrime(int n) 
    { 
        // Corner cases 
        if (n <= 1) return false; 
        if (n <= 3) return true; 
      
        // This is checked so that we can skip  
        // middle five numbers in below loop 
        if (n % 2 == 0 || n % 3 == 0) return false; 
      
        for (int i = 5; i * i <= n; i = i + 6) 
            if (n % i == 0 || n % (i + 2) == 0) 
            return false; 
      
        return true; 
    } 
	public static int useBs(int[] arr, int targetValue) {	
		int a =  Arrays.binarySearch(arr, targetValue);
		if(a >=0 && a<arr.length)
			return a;
		else
			return -1;
	}
	public static void printArray(int []a) {
		for(int i=0;i<a.length;i++) {
			System.out.println(a[i]+" ");
		}
		System.out.println();
	}
	static boolean isPalindrome(String s) {
		int l=s.length();
		for(int i=0;i<l/2;i++)
		{
			if(s.charAt(i)!=s.charAt(l-i-1))
				return false;
		}
		return true;
	}
	static String revString(String str)
	{
		return new StringBuffer(str).reverse().toString();
	}
	static String sortString(String s) {
		char a[]=s.toCharArray();
		Arrays.sort(a);
		return new String(a);
	}
	static int sumList(List<Integer>a) {
		return a.stream().mapToInt(Integer::intValue).sum();
	}
	static int sumArray(int []a) {
		int sum=0;
		for(int i=0;i<a.length;i++) {
			sum+=a[i];
		}
		return sum;
	}
    public static void main(String[]args) throws java.lang.Exception{
    	Scanner sc=new Scanner(System.in);
    	int t=sc.nextInt();
    	while(t-->0) {
//    		int n=sc.nextInt();
//    		if(n==1||n==6) {
//    			System.out.println("FastestFinger");
//    		}else {
//    			if(n%2!=0||n==2) {
//    				System.out.println("Ashishgup");
//    			}else {
//    				if(Math.log(n)/Math.log(2)-(int)(Math.log(n)/Math.log(2))==0) {
//    					System.out.println("FastestFinger");
//    				}else {
//    					int k=0;
//    					while(n>1) {
//    						n/=2;
//    						k+=1;
//    					}
//    					  if(k==1) {
//    						  if(isPrime(n/2))
//    							  System.out.println("FastestFinger");
//    						  else
//    							  System.out.println("Ashishgup");
//    							  
//    					  }
//    					  else
//    						  System.out.println("Ashishgup");
//    			}
//    			}
//    		}
    		int n=sc.nextInt();
    		int a[]=new int[2*n];
    		List<Integer>e=new ArrayList<Integer>();
    		List<Integer>o=new ArrayList<Integer>();
    		for(int i=0;i<2*n;i++) {
    			a[i]=sc.nextInt();
    			if(a[i]%2==0)e.add(i+1);
    			else o.add(i+1);
    		}
    		if(e.size()%2!=0)e.remove(e.size()-1);
    		e.sort(null);
    		if(o.size()%2!=0)o.remove(o.size()-1);
    		o.sort(null);
    		e.addAll(o);
    		for(int i=0;i<2*(n-1);i+=2) {
    			System.out.println(e.get(i)+" "+e.get(i+1));
    		}
    	}
    }
}
