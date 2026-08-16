import java.util.*;
import java.io.*;

public class File {
	public static class FastScanner {
		BufferedReader br;
		StringTokenizer st;
		
		public FastScanner() {
			br = new BufferedReader(new InputStreamReader(System.in));
		}
		
		String next() {
			while (st == null || !st.hasMoreElements()) {
				try {
					st = new StringTokenizer(br.readLine());
				}
				catch (IOException e) {
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
	}
	
	static class FenwickTree {
		int N;
		int[] BIT;
		
		public FenwickTree(int N) {
			this.N = N;
			BIT = new int[N+1];
		}
		
		// val would be 1, as we're adding +1 to counts.
		public void update(int index, int val) {
			for (; index <= N; index += (index & -index)) {
				BIT[index] += val;
			}
		}
		
		public int query(int index) {
			int total = 0;
			
			for (; index > 0; index -= (index & -index)) {
				total += BIT[index];
			}
			
			return total;
		}
	}
	
	public static void main(String[] args) {
		FastScanner sc = new FastScanner();
		PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));
		
		
		int n = sc.nextInt();
		long t = sc.nextLong();
				
		long[] arr = new long[n];
		
		Set<Long> sumSet = new HashSet<>();
		long currSum = 0;
		
		for (int i = 0; i < n; i++) {
			arr[i] = sc.nextLong();
			currSum += arr[i];
			sumSet.add(currSum);
		}
		
		List<Long> sumList = new ArrayList<>(sumSet);		
		Collections.sort(sumList);
				
		FenwickTree BIT = new FenwickTree(sumList.size());
		
		currSum = 0;
		long result = 0L;
		
		for (int i = 0; i < n; i++) {
			currSum += arr[i];
			
			if (currSum < t) {
				result++;
			}
			
			// getting the smallest prefix sum such that currSum - prefixSum < t.			
			int pos = ceilingSearch(sumList, currSum - t);
			
			// There are i prefixSums before the current index.
			// Query how many non valid prefix sums there are using
			// BIT.query(pos - 1)..
				// The result of this is how of the prefixes would be too small such that 
				// currSum - prefixSum >= t.
			// Subtract those invalid prefix sums from the total number of prefixes.
			result += i - BIT.query(pos - 1);
			
			// Update the Fenwick tree with the current sum.
			int index = binarySearch(sumList, currSum);
			BIT.update(index, 1);
		}
		
		
		
		out.println(result);
		
		out.close();
	}
	
	// Return index of leftmost value >= target
	public static int binarySearch(List<Long> sumList, long target) {	
		int result = sumList.size() - 1;
	
		int lo = 0;
		int hi = sumList.size() - 1;
		
		while (lo <= hi) {
			int mid = lo + (hi - lo) / 2;
			
			if (sumList.get(mid) >= target) {
				result = Math.min(result, mid);
				hi = mid - 1;
			}
			else {
				lo = mid + 1;
			}
		}
		
		return result + 1;
	}
	
	// Smallest value strictly greater than target.
	public static int ceilingSearch(List<Long> sumList, long target) {
		int index = sumList.size();
		
		int lo = 0;
		int hi = sumList.size() - 1;
		
		while (lo <= hi) {
			int mid = lo + (hi - lo) / 2;
			
			if (sumList.get(mid) > target) {
				index = Math.min(index, mid);
				hi = mid - 1;
			}
			else {
				lo = mid + 1;
			}
		}
		
		return index + 1;
	}
}





















