import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class C {
	private static BufferedReader in;
	private static StringTokenizer st;
	private static PrintWriter out;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		in = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer("");
		out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
		int n = nextInt();
		int a[] = new int [n+1];
		for (int i = 1; i <=n; i++) {
			a[i] = nextInt();
		}
		int ans = 0;
		if(n % 2 == 0 || n==1){
			System.out.println(-1);
			return;
		}
		for (int i = 1; i <=n; i++) {
			for (int j = (n-1)/2; j >=1; j--) {
				int max = Math.max(a[2*j], a[2*j + 1]);
				ans += max;
				a[j]-= max;
				if(a[j]<0) a[j] = 0;
				a[2*j]-= max;
				a[2*j + 1] -= max;
			}
		}
		ans+=a[1];
		System.out.println(ans);
	}
	

	static String next() throws IOException{
		while(!st.hasMoreTokens()){
			st = new StringTokenizer(in.readLine());
		}
		return st.nextToken();
	}
	static int nextInt() throws NumberFormatException, IOException{
		return Integer.parseInt(next());
	}
	static long nextLong() throws NumberFormatException, IOException{
		return Long.parseLong(next());
	}
	
	static double nextDouble() throws NumberFormatException, IOException{
		return Double.parseDouble(next());
	}

}
