import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.text.DecimalFormat;
import java.lang.Math;
import java.util.Iterator; 
import java.util.TreeSet;
import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.math.BigDecimal;
import java.util.*;
public class C1343{
	public static PrintWriter out = new PrintWriter (new BufferedOutputStream(System.out));
	static long mod = (long)(1e9+7);
	static FastReader sc = new FastReader();
	static boolean[] sieve = new boolean[10000001];
	static int pInf = Integer.MAX_VALUE;
	static int nInf = Integer.MIN_VALUE;
	public static void main(String[] args) {
		int t = sc.nextInt();
		//Arrays.fill(sieve, true);
        //soe();
		while(t-->0){
		    int n = sc.nextInt();
		    int r = sc.nextInt();
		    int p = sc.nextInt();
		    int s = sc.nextInt();
		    char[] c = sc.next().toCharArray();
		    char[] ans = new char[n];
		    StringBuffer sb = new StringBuffer("");
		    int count = 0;
		    for(int i = 0; i < n; i++){
		        if(c[i]=='R'){
		            if(p>0){
		                ans[i]='P';
		                count++;
		                p--;
		            }
		            else{
		                ans[i]='X';
		            }
		        }
		        else if(c[i]=='P'){
		            if(s>0){
		                ans[i]='S';
		                count++;
		                s--;
		            }
		            else{
		                ans[i]='X';
		            }
		        }
		        else if(c[i]=='S'){
		            if(r>0){
		                ans[i]='R';
		                count++;
		                r--;
		            }
		            else{
		                ans[i]='X';
		            }
		        }
		    }
		    int g = n%2==0?n/2:(n/2+1);
		    if(count>= g){
		        out.println("YES");
		    }
		    else{
		        out.println("NO");
		    }
		    for(int i = 0; i <n; i++){
		        if(ans[i]=='X'){
		            if(p>0){
		                ans[i] = 'P';
		                p--;
		            }
		            else if(r>0){
		                ans[i] = 'R';
		                r--;
		            }
		            else if(s>0){
		                ans[i] = 'S';
		                s--;
		            }
		        }
		    }
		    if(count>=g){
		        out.println(new String(ans));
		    }
		}
		out.close();
	}
	//static void soe() {
	//	sieve[0]=sieve[1]=false;
	//	for(int i=2;i<=10000000;i++) {
	//		if(sieve[i]) {
	//			if(i*1l*i<=10000000) {
	//				for(int j = i*i;j<=10000000;j+=i) {
	//					sieve[j] = false;
	//				}
	//			}
	//		}
	//	}
	//}
	public static int ffloor(int[] b, long ele){
	    int s = 0;
	    int e = b.length-1;
	    while(s<=e){
	        int m = s+(e-s)/2;
	        if(b[m] == ele){
	            return b[m];
	        }
	        else if(b[m]>ele){
	            e = m-1;
	        }
	        else{
	            s = m+1;
	        }
	    }
	    return b[e];
	}
	public static int cceil(int[] a, long ele){
	    int s = 0;
	    int e = a.length-1;
	    while(s<=e){
	        int m = s+(e-s)/2;
	        if(a[m] == ele){
	            return a[m];
	        }
	        else if(a[m]>ele){
	            e = m-1;
	        }
	        else{
	            s = m+1;
	        }
	    }
	    return a[s];
	}
	public static int floor(ArrayList<Pair> A , long ele){
	    int s = 0;
	    int e = A.size()-1;
	    while(s<=e){
	        int m = s+(e-s)/2;
	        if(A.get(m).x == ele){
	            return A.get(m).x;
	        }
	        else if(A.get(m).x>ele){
	            e = m-1;
	        }
	        else{
	            s = m+1;
	        }
	    }
	    return A.get(e).x;
	}
	public static int ceil(Pair[] a, long ele){
	    int s = 0;
	    int e = a.length-1;
	    while(s<=e){
	        int m = s+(e-s)/2;
	        if(a[m].x == ele){
	            a[m].y = 1;
	            return a[m].x;
	        }
	        else if(a[m].x>ele){
	            e = m-1;
	        }
	        else{
	            s = m+1;
	        }
	    }
	    a[s].y = 1;
	    return a[s].x;
	}
	////////////////////////////////////////////////////////////////////////////////
	static void merge(long arr[], int l, int m, int r)
    {
        // Find sizes of two subarrays to be merged
        int n1 = m - l + 1;
        int n2 = r - m;
 
        /* Create temp arrays */
        long L[] = new long [n1];
        long R[] = new long [n2];
 
        /*Copy data to temp arrays*/
        for (int i=0; i<n1; ++i)
            L[i] = arr[l + i];
        for (int j=0; j<n2; ++j)
            R[j] = arr[m + 1+ j];
 
 
        /* Merge the temp arrays */
 
        // Initial indexes of first and second subarrays
        int i = 0, j = 0;
 
        // Initial index of merged subarry array
        int k = l;
        while (i < n1 && j < n2)
        {
            if (L[i] <= R[j])
            {
                arr[k] = L[i];
                i++;
            }
            else
            {
                arr[k] = R[j];
                j++;
            }
            k++;
        }
 
        /* Copy remaining elements of L[] if any */
        while (i < n1)
        {
            arr[k] = L[i];
            i++;
            k++;
        }
 
        /* Copy remaining elements of R[] if any */
        while (j < n2)
        {
            arr[k] = R[j];
            j++;
            k++;
        }
    }
 
    // Main function that sorts arr[l..r] using
    // merge()
    static void sort(long arr[], int l, int r)
    {
        if (l < r)
        {
            // Find the middle point
            int m = (l+r)/2;
 
            // Sort first and second halves
            sort(arr, l, m);
            sort(arr , m+1, r);
 
            // Merge the sorted halves
            merge(arr, l, m, r);
        }
    }
	static class Pair implements Comparable<Pair>{
		int x;
		int y;
		public Pair(int x, int y) {
			this.x = x;
			this.y = y;
		}
		@Override
		public int compareTo(Pair o) {
			// TODO Auto-generated method stub
			if(this.x==o.x){
			    return (this.y-o.y);
			}
			return (this.x-o.x);
		}
	}
	public static boolean isPrime(int n){
	    if(n < 2){
	        return false;
	    }
	    if(n%2==0){
	        return n==2;
	    }
	    if(n%3==0){
	        return n==3;
	    }
	    int i = 5;
	    int h = (int)Math.floor(Math.sqrt(n)+1);
	    while(i <= h){
	        if(n%i==0){
	            return false;
	        }
	        if(n%(i+2)==0){
	            return false;
	        }
	        i += 6;
	    }
	    return true;
	}
	public static long gcd(long a, long b){
	    return b==0? a:gcd(b, a%b);
	}
	public static long bSearch(int n,ArrayList<Long> A){
	    int s = 0;
	    int e = A.size()-1;
	    while(s<=e){
	        int m = s+(e-s)/2;
	        if(A.get(m)==(long)n){
	            return A.get(m);
	        }
	        else if(A.get(m)>(long)n){
	            e = m-1;
	        }
	        else{
	            s = m+1;
	        }
	    }
	    return A.get(s);
	}
	static long modulo = (long)1e9+7;
	public static long modinv(long x){
	    return modpow(x, modulo-2);
	}
	public static long modpow(long a, long b){
	    if(b==0){
	        return 1;
	    }
	    long x = modpow(a, b/2);
	    x = (x*x)%modulo;
	    if(b%2==1){
	        return (x*a)%modulo;
	    }
	    return x;
	}
	public static class FastReader {
		BufferedReader br;
		StringTokenizer st;
		//it reads the data about the specified point and divide the data about it ,it is quite fast
		//than using direct 

		public FastReader() {
			br = new BufferedReader(new InputStreamReader(System.in));
		}

		String next() {
			while (st == null || !st.hasMoreTokens()) {
				try {
					st = new StringTokenizer(br.readLine());
				} catch (Exception r) {
					r.printStackTrace();
				}
			}
			return st.nextToken();
		}

		int nextInt() {
			return Integer.parseInt(next());//converts string to integer
		}

		double nextDouble() {
			return Double.parseDouble(next());
		}

		long nextLong() {
			return Long.parseLong(next());
		}

		String nextLine() {
			String str = "";
			try {
				str = br.readLine();
			} catch (Exception r) {
				r.printStackTrace();
			}
			return str;
		}
	}
}