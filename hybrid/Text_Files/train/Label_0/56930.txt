import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class App {
	public static PrintWriter out;
	static int s = Integer.MIN_VALUE;
	public static void main(String[] args) {
		MyScanner sc = new MyScanner();
		out = new PrintWriter(new BufferedOutputStream(System.out));
		
		
		
		/* My brute force way of doing it.
		int n = sc.nextInt();
		int[] a = new int[n];
		for(int i = 0;i<n;i++) {
			a[i] = sc.nextInt();
		}
		for(int r = 1; r < n; r++) {
			for(int l = 0;l < r; l++) {
				s = Math.max(s, f(a,l,r));
			}
		}
		out.println(s);
		*/
		
		/*
		 * Alright, the function works like this:
		 * You have an array. l, r are the start and end indices within which you perform your calculation.
		 * The calculate takes the first value (a[i]) and finds the absolute difference with the next value (a[i+1]). 
		 * From this absolute difference, it subtracts the next absolute difference ( a[i+1],a[i+2]), then adds the next, then subtracts, then adds, ad mortem.
		 * 
		 * Now you begin to understand why it's useful to have an array of differences. You simply add the elements in this array!
		 * 
		 * The non brute force idea, is to generate all possibilities as fast as possible, using divide and conquer.
		 * It first sets out the two cases, which arise from the fact that the position of the bounds affect the numerical values of the arrays of the differences.
		 *
		 * E.g. if the array is [1,4,2,3,1], then the two possible arrays of differences are:
		 * 1. [3,-2,1,-2] or 2. [-3,2,-1,2] 
		 * For bound(0,2), this falls into case 1; 3 + -2
		 * For bound(1,2), this falls into case 2; 2
		 * For bound(3,4), this falls into case 2; 2.
		 * For bound(i,whatever), if differenceArray[i] == positive, then that is the case it falls into.
		 * 
		 * 
		 * 
		 * 
		 */
		
		int n = sc.nextInt();
		long[] arr1 = new long[n-1];
		long[] arr2 = new long[n-1];
		long[] a = new long[n];
		for(int i = 0; i< n ; i++) {
			a[i] = sc.nextInt();
			if(i!=0) {
				long vv = Math.abs(a[i-1] - a[i]);
				if(i%2 == 1) {
					arr1[i-1] = vv;
					arr2[i-1] = -vv;
				}else {
					arr1[i-1] = -vv;
					arr2[i-1] = vv;
				}
			}
		}
		out.println(Math.max(find_max(arr1,0,n-2),find_max(arr2,0,n-2)));
		
		//Tests
		//long[] x = new long[] {-4,0};
		//out.println(cross(x,0,1,1));
		//out.println(find_max(new long[] {-500,1,500,1,-500},0,4));
		
		
		out.close();

	}
	/*
	 * Here's how find_max works. The basic idea is to compare:
	 * 
	 *  the greatest possible positive sum returned from the left array,
	 *  with the greatest possible positive sum returned from the right array,
	 *  with the sum of the combined arrays.
	 *  
	 * The bounds will simply fall into place. 
	 * 			If the sum returned from the left array is the greatest greatest value, then the bounds will be within the left array.
	 * 			Likewise for the right array.
	 * 			If the sum of the combined arrays (not the sum of the greatest possible positive sums) is the greatest value, then the bounds will be the full array.
	 * 
	 * Here's a simple breakdown:
	 * For the array [1,4,2,3,1], the two arrays of differences are:
	 * 		arr1 = [3,-2,1,-2] or arr2 = [-3,2,-1,2] 
	 * 
	 * arr1 = [3,-2,1,-2]:
	 * [3,-2]        			and      [1,-2]
	 * [3] and [2]						[1] and [-2]
	 * Compare above three			Compare above three
	 * ^ returns 3					^ returns 1
	 * 
	 * 			Compare 3,1 and sum of [3,-2,1,-2]
	 *          ^ returns 3;
	 * Therefore for arr1, the max is 3, and this corresponds to the bounds(0,1);
	 * 
	 * 
	 */
	private static long find_max(long[] arr, int low, int high) {
		
		// Some recursion
		if(high == low) {
			return arr[low];
		}
		int mid = (low+high)/2;
		
		long lm = find_max(arr,low,mid); // huh divide and conquer
		long rm = find_max(arr,mid+1,high);
		long com = cross(arr,low,mid,high); // Finding the greatest possible positive sum for this array.
		com = Math.max(com, lm); // Comparison betwen the three values.
		com = Math.max(com, rm);
		
		return com;
	}
	// This function is a helper function that finds the greatest possible positive sum of the array.
	private static long cross(long[] arr, int low, int mid, int high) {
		long leftsum = Long.MIN_VALUE;
		long leftsum1 = Long.MIN_VALUE;
		long sum = 0;
		for(int i = mid;i>=low;i--) {
			sum = sum + arr[i];
			if(sum>leftsum1) {
				leftsum1 = sum;
			}
		}
		long rightsum = Long.MIN_VALUE;
		long rightsum1 = Long.MIN_VALUE;
		sum = 0;
		for(int i = mid + 1;i<=high;i++) {
			sum = sum + arr[i];
			if(sum>rightsum1) {
				rightsum1 = sum;
			}
		}
		if(rightsum1<=0) {
			rightsum1 = 0;
		}
		return Math.max(0, leftsum1+rightsum1);
	}
	private static int f(int[] a,int l, int r) {
		int sum = 0;
		for(int i = l; i < r ; i++) {
			
			sum = (int) (sum + Math.abs(a[i]-a[i+1]) * Math.pow(-1, i-l));
			
		};
		return sum;
	}

}

class MyScanner{
	BufferedReader br;
	StringTokenizer st;
	
	public MyScanner() {
		br = new BufferedReader(new InputStreamReader(System.in));
		
	}
	String next() {
		while (st == null || !st.hasMoreElements()) {
			try {
				st = new StringTokenizer(br.readLine());
			}catch (IOException e) {
				e.printStackTrace();
			}
		}
		return st.nextToken();
	}
	
	int nextInt() {
		return Integer.parseInt(next());
	}
	long nextLong() {
		return Long.parseLong(next());
	}
	double nextDouble() {
		return Double.parseDouble(next());
	}
	String nextLine() {
		String str = "";
		try {
			str = br.readLine();
		}catch(IOException e) {
			e.printStackTrace();
		}
		return str;
	}
}
