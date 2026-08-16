import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Set;
import java.util.StringTokenizer;
import java.util.TreeMap;
import java.util.TreeSet;

public class Main {
	
	public static void CountingSort(int[] A, int[] B, final int n, final int k){
		int[] C = new int[k];
		for(int i = 0; i < k; i++){
			C[i] = 0;
		}
		
		for(int i = 0; i < n; i++){
			C[A[i]]++;
		}
		
		for(int i = 1; i < k; i++){
			C[i] += C[i - 1];
		}
		
		for(int i = n - 1; i >= 0; i--){
			B[C[A[i]] - 1] = A[i];
			C[A[i]]--;
		}
	}
	
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		
		final int n = sc.nextInt();
		int[] array = new int[n];
		int max = Integer.MIN_VALUE;
		for(int i = 0; i < n; i++){
			array[i] = sc.nextInt();
			max = Math.max(max, array[i]);
		}
		
		int[] output = new int[n];
		CountingSort(array, output, n, max + 1);
	
		StringBuilder sb = new StringBuilder();
		for(int i = 0; i < n; i++){
			sb.append(i == 0 ? "" : " ");
			sb.append(output[i]);
		}
		System.out.println(sb.toString());
	}
	
	public static class Scanner {
	    private BufferedReader br;
	    private StringTokenizer tok;

	    public Scanner(InputStream is) throws IOException {
	        br = new BufferedReader(new InputStreamReader(is));
	    }

	    private void getLine() throws IOException {
	        while (!hasNext()) { tok = new StringTokenizer(br.readLine()); }
	    }

	    private boolean hasNext() {
	        return tok != null && tok.hasMoreTokens();
	    }

	    public String next() throws IOException {
	        getLine(); return tok.nextToken();
	    }

	    public int nextInt() throws IOException {
	        return Integer.parseInt(next());
	    }
	    
	    public long nextLong() throws IOException {
	    	return Long.parseLong(next());
	    }
	    
	    public void close() throws IOException {
	        br.close();
	    }
	}

}