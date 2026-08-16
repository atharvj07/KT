import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Solution{

	public static void main(String[] args) throws Exception{

		FastScanner fs = new FastScanner();
		int t = fs.nextInt();
		
		PrintWriter out = new PrintWriter(System.out);

		while(t-->0){
			
			int n = fs.nextInt(), m = fs.nextInt(), a = fs.nextInt(), b = fs.nextInt();
			
			if(n*a != m*b) {
				out.println("No");
				continue;
			}
			
//			int shift = 0;
//			for(shift=1;shift<m;shift++) {
//				if((shift*n)%m==0)
//					break;
//			}
			
			int[][] res = new int[n][m];
			
			for(int i=0,dx=0;i<n;i++,dx+=a) {
				for(int j = 0;j<a;j++)
					res[i][(j+dx)%m] = 1;
			}
			
			out.println("Yes");
			
			for(int i = 0;i<n;i++) {
				for(int j=0;j<m;j++) {
					out.print(res[i][j]);
				}
				out.println("");
			}
			
		}
		out.close();
		
	}



	


	static class FastScanner{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer("");

		public String next(){
			while(!st.hasMoreElements()){
				try{
					st = new StringTokenizer(br.readLine());
				} catch(IOException e){
					e.printStackTrace();
				}
			}
			return st.nextToken();
		}

		public int nextInt(){
			return Integer.parseInt(next());
		}

		public int[] readArray(int n){
			int[] a = new int[n];
			for(int i=0;i<n;i++)
				a[i] = nextInt();
			return a;
		}
	}

}