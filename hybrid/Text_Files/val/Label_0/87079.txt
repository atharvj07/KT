/*
 *
 * @author Mukesh Singh
 *
 */

import java.io.*;
import java.util.*;
import java.text.DecimalFormat;
@SuppressWarnings("unchecked")



public class Solution {	
	
	void solve() throws Exception {
		long n = in.nextInt();
		if(n <= 2){
			System.out.println("No");
			return;
		}
		long sum = (n*(n+1))/2;
		String res = "";
		for(long i= 2; i <= n; ++i ){
			if((sum - i) %i == 0){
				System.out.println("Yes");
				System.out.print(1+" ");
				System.out.println(i);
				System.out.print((n-1)+" ");
				for(int j = 1; j <= n ; ++j ){
					if(j != i)
						System.out.println(j+" ");
				}
				
				
				return;
			}
		}
		System.out.println("No");
	}
	//@ main function
	public static void main(String[] args) throws Exception {
		new Solution();
	}
	
	InputReader in;
	PrintStream out ;
	DecimalFormat df ;
	Solution() {
		try {
			File defaultInput = new File("file.in");
			if (defaultInput.exists()) 
				in = new InputReader("file.in");
			else 
				in = new InputReader();
			defaultInput = new File("file.out");
			if (defaultInput.exists()) 
				out = new PrintStream(new FileOutputStream("file.out"));
			else
				out = new PrintStream(System.out);
			df = new DecimalFormat("######0.00");
			solve();
			out.close();
		} 
		catch (Exception e) {
			e.printStackTrace();
			System.exit(261);
		}
	}
	
	class InputReader {
		BufferedReader reader;
		StringTokenizer tokenizer;
		
		InputReader() {
			reader = new BufferedReader(new InputStreamReader(System.in));
		}
		
		InputReader(String fileName) throws FileNotFoundException {
			reader = new BufferedReader(new FileReader(new File(fileName)));
		}
		
		String readLine() throws IOException {
			return reader.readLine();
		}
		
		String nextToken() throws IOException {
			while (tokenizer == null || !tokenizer.hasMoreTokens())
				tokenizer = new StringTokenizer(readLine());
			return tokenizer.nextToken();
		}
		
		boolean hasMoreTokens() throws IOException {
			while (tokenizer == null || !tokenizer.hasMoreTokens()) {
				String s = readLine();
				if (s == null)
					return false;
				tokenizer = new StringTokenizer(s);
			}
			return true;
		}
		
		int nextInt() throws NumberFormatException, IOException {
			return Integer.parseInt(nextToken());
		}
		
		long nextLong() throws NumberFormatException, IOException {
			return Long.parseLong(nextToken());
		}
		
		double nextDouble() throws NumberFormatException, IOException {
			return Double.parseDouble(nextToken());
		}
	}
}