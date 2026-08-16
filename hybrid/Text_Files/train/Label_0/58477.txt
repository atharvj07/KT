import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
//import java.util.Arrays;
import java.util.StringTokenizer;
//import java.util.Collections;
//import java.util.LinkedList;
//import java.util.ArrayList;



public class Solution {
	
	public static boolean binarySearch(long arr[], long n){
        int start=0;
        int end=arr.length;
        while(true) {
        	int mid=(start+end)/2;
        	if(arr[mid]==n) return true;
        	else if(start>end) return false;
        	else if(arr[mid]>n) end=mid-1;
        	else if(arr[mid]<n) start=mid+1;
        }
    }
	
	public static void solve(long n) {
		long arr[]=new long [10000];
		for(int i=0;i<10000;i++) {
			arr[i]=(long)Math.pow(i+1, 3);
		}
		for(int i=0;i<10000;i++) {
			if(binarySearch(arr,n-arr[i])) {
				System.out.println("YES");
				return;
			}
		}
		System.out.println("NO");
	}
	
	public static void main(String[] args){
		FastScanner fs = new FastScanner();
		int tt=fs.nextInt();
		while(tt-->0) {
			long n=fs.nextLong();
//			int arr[]=fs.readArray(n);
			solve(n);
		}

	}
	


	static class FastScanner {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer("");
		String next() {
			while (!st.hasMoreTokens())
				try {
					st=new StringTokenizer(br.readLine());
				} catch (IOException e) {
					e.printStackTrace();
				}
			return st.nextToken();
		}
		
		int nextInt() {
			return Integer.parseInt(next());
		}
		
		int[] readArray(int n) {
			int[] a=new int[n];
			for (int i=0; i<n; i++) a[i]=nextInt();
			return a;
		}
		
		int[][] readArray(int n,int m) {
			int[][] a=new int[n][m];
			for (int i=0; i<n; i++) for(int j=0; j<m; j++) a[i][j]=nextInt();
			return a;
		}
		long nextLong() {
			return Long.parseLong(next());
		}
		double nextDouble() {
			return Double.parseDouble(next());
		}
	}

	
}