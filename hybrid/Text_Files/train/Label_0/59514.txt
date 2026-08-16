import java.io.*;
import java.util.*;
public class B {
    public static void main(String args[])throws IOException{
        FastReader sc = new FastReader();
        PrintWriter out = new PrintWriter(System.out);
        int t = sc.nextInt();
        while(t-- > 0){
			int n = sc.nextInt();
			int arr[][] = new int[n][2];
			for(int i = 0; i < n; i++) {
				arr[i][0] = sc.nextInt();
				arr[i][1] = i+1;
			}
			Arrays.sort(arr, Comparator.comparingLong(o -> o[0]));
			long count = 0;
			for(int i = 0; i < n; i++) {
				for(int j = i+1; j < n; j++) {
					long p = arr[i][0]*(long)arr[j][0];
					if(p > 2*n - 1) {
						break;
					}
					if(p == arr[i][1] + arr[j][1]) {
						count++;
					}
				}
			}
			out.println(count);
		}
        out.flush();
    }
    static class FastReader {
		BufferedReader br;
		StringTokenizer st;

		public FastReader()
		{
			br = new BufferedReader(
				new InputStreamReader(System.in));
		}

		String next()
		{
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

		int nextInt() { return Integer.parseInt(next()); }

		long nextLong() { return Long.parseLong(next()); }

		double nextDouble()
		{
			return Double.parseDouble(next());
		}

		String nextLine()
		{
			String str = "";
			try {
				str = br.readLine();
			}
			catch (IOException e) {
				e.printStackTrace();
			}
			return str;
		}
	}

	static void swap(long[] arr, int i, int j)
	{
		long temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}
	
	/* This function takes last element as pivot, places
	the pivot element at its correct position in sorted
	array, and places all smaller (smaller than pivot)
	to left of pivot and all greater elements to right
	of pivot */
	static int partition(long[] arr, int low, int high)
	{
		
		// pivot
		long pivot = arr[high];
		
		// Index of smaller element and
		// indicates the right position
		// of pivot found so far
		int i = (low - 1);
	
		for(int j = low; j <= high - 1; j++)
		{
			
			// If current element is smaller
			// than the pivot
			if (arr[j] < pivot)
			{
				
				// Increment index of
				// smaller element
				i++;
				swap(arr, i, j);
			}
		}
		swap(arr, i + 1, high);
		return (i + 1);
	}
	
	/* The main function that implements QuickSort
			arr[] --> Array to be sorted,
			low --> Starting index,
			high --> Ending index
	*/
	static void quickSort(long[] arr, int low, int high)
	{
		if (low < high)
		{
			
			// pi is partitioning index, arr[p]
			// is now at right place
			int pi = partition(arr, low, high);
	
			// Separately sort elements before
			// partition and after partition
			quickSort(arr, low, pi - 1);
			quickSort(arr, pi + 1, high);
		}
	}
}