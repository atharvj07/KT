import java.util.*;
import java.lang.*;
import java.math.*;
import java.text.*;
import java.io.*;
		public final class Solution {
		static PrintWriter out = new PrintWriter(System.out); 
		static void flush() {
	 	out.flush();
	 	}
		static class FastReader {
	    BufferedReader br;
	    StringTokenizer st;
	
	    public FastReader() {
	    br = new BufferedReader(new
	    InputStreamReader(System.in));
	    }
	    static boolean isPalindrome(String str1, String str2) {
	    String str3 = str1+str2;
	    int i = 0, j = str3.length()-1;
	    while(i < j) {
	    char a = str3.charAt(i), b = str3.charAt(j);
	    if(a != b) return false;
	    i++;j--;
	    }
	    return true;
	    }
	    static boolean isPalindrome(String str) {
	    int i = 0, j = str.length()-1;
	    while(i < j) {
	    char a = str.charAt(i), b = str.charAt(j);
	    if(a != b) return false;
	    i++;j--;
	    }
	    return true;
	    }
	    String next() {
	    while (st == null || !st.hasMoreElements()) {
	    try{st = new StringTokenizer(br.readLine());}
	    catch (IOException  e) {e.printStackTrace();}
	    }
	    return st.nextToken();
	    }
	    int nextInt(){ return Integer.parseInt(next()); }
	    long nextLong() { return Long.parseLong(next());}
	    static int fact(int n) {
	    if(n == 1) return 1;
	    return n * fact(n-1);
	   	}
	    public int[] readIntArray(int n) {
	    int[] arr = new int[n];
		for(int i=0; i<n; ++i)
		arr[i]=nextInt();
		return arr;
		}
	    public int[][] readIntArray(int m, int n){
		int[][] arr = new int[m][n];
		for(int i = 0;i<m;i++) 
		for(int j = 0;j<n;j++) 
		arr[i][j] = nextInt();
		return arr;
	    }
	    public String[] readStringArray(int n) {
		String[] arr = new String[n];
		for(int i=0; i<n; ++i)
		arr[i]= nextLine();
		return arr;
	    }
		static int gcd(int a, int b) { 
		if (b == 0) return a; 
		return gcd(b, a % b);  
		}
	    double nextDouble() {return Double.parseDouble(next());}
	    String nextLine() {
	    String str = "";
	    try{str = br.readLine();}
	    catch (IOException e) {e.printStackTrace();}
	    return str;}
	    }
		
		static int solve(int[] l, int[] r, int n) {
			int x = Integer.MAX_VALUE, y = Integer.MIN_VALUE, min = Integer.MAX_VALUE, max = -1;
//			if(n == 1) {
//				return 0;
//			}
			for(int i = 1;i<n;i++) {
				min = Math.min(min, r[i-1]);
				max = Math.max(max, l[i-1]);
				if(l[i] > min) {
					x = Math.min(x, min);
					y = Math.max(y, l[i]);
				}
				else if(r[i] < max) {
					x = Math.min(x, r[i]);
					y = Math.max(y, max);
				}
			}
			if(x == Integer.MAX_VALUE && y == Integer.MIN_VALUE){
				return 0;
			}
			return (Math.abs(y-x));
		}
		public static void main(String args[]) throws Exception {
	    FastReader sc = new FastReader();
	    long start = System.currentTimeMillis();
	    int t = sc.nextInt();
	    
	    while(t--  > 0 ) {
	    	int n = sc.nextInt();
	    	int[] l = new int[n];
	    	int[] r = new int[n];
	    for(int i =0;i<n;i++) {
	    		l[i]= sc.nextInt();
	    		r[i] = sc.nextInt();
	    }
	    out.println(solve(l,r,n));
	    }
	        	flush();
	    long end = System.currentTimeMillis();
	    NumberFormat formatter = new DecimalFormat("#0.00000");
	    //System.out.print("Execution time is " + formatter.format((end - start) / 1000d) + " seconds");
	    }
	}
		
		
		