import java.io.BufferedReader;
import java.io.Closeable;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;

public class Main {
	
	public static void main(String[] args) {
		final Scanner sc = new Scanner(System.in);
		
		final int N = sc.nextInt();
		int[] array = new int[N];
		{
			char[] input = sc.next().toCharArray();
			for(int i = 0; i < N; i++){
				array[i] = Character.getNumericValue(input[i]);
			}
		}
		final int D = sc.nextInt();
		
		int[] output = new int[N];
		System.arraycopy(array, 0, output, 0, N);
		{
			int count = D;
			for(int i = 0; i < N; i++){
				if(count > 0 && array[i] == 0){
					count--;
					output[i] = 1;
				}
			}
			
			for(int i = N - 1; i >= 0; i--){
				if(count > 0 && array[i] == 1){
					count--;
					output[i] = 0;
				}
			}
		}
		
		for(int i = 0; i < N; i++){
			System.out.print(output[i]);
		}
		System.out.println();
		
		
	}

	public static class Scanner implements Closeable {
		private BufferedReader br;
		private StringTokenizer tok;

		public Scanner(InputStream is) {
			br = new BufferedReader(new InputStreamReader(is));
		}

		private void getLine() {
			try {
				while (!hasNext()) {
					tok = new StringTokenizer(br.readLine());
				}
			} catch (IOException e) { /* ignore */
			}
		}

		private boolean hasNext() {
			return tok != null && tok.hasMoreTokens();
		}

		public String next() {
			getLine();
			return tok.nextToken();
		}

		public int nextInt() {
			return Integer.parseInt(next());
		}

		public long nextLong() {
			return Long.parseLong(next());
		}

		public double nextDouble() {
			return Double.parseDouble(next());
		}

		public void close() {
			try {
				br.close();
			} catch (IOException e) { /* ignore */
			}
		}
	}
}