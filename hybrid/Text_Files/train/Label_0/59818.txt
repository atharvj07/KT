import java.util.*;
import java.io.*;
public class ChrisandMagicSquare
{
	
	
	/************************ SOLUTION STARTS HERE ***********************/
	
	
	
	private static void solve(FastScanner s1, PrintWriter out){
		
		int n = s1.nextInt();
		if(n == 1){
			out.println(1);
			return;
		}
		int grid[][] = new int[n][];
		for(int i=0;i<n;i++)
			grid[i] = s1.nextIntArray(n);
		
		int xx=-1 , yy=-1;
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				if(grid[i][j] == 0){
					xx = i;
					yy = j;
				}
			}	
		}
		
		long sum = 0;
		for(int i=0;i<n;i++){
			if(i != xx){
				for(int j=0;j<n;j++)
					sum += grid[i][j];
				
				break;
			}
		}
		long d1Check = xx != yy ? 0 : sum , d2Check = (xx + yy != n-1 ) ? 0 : sum;
		for(int i=0;i<n;i++){
			
			if(xx != yy){
				d1Check += grid[i][i];
			}
			if(xx + yy != n - 1){
				d2Check += grid[i][n - i - 1];
			}
			if(i != xx){
				long check = 0;
				for(int j=0;j<n;j++)
					check += grid[i][j];
				if(check != sum){
					out.println(-1);
					return;
				}
			}
			if(i != yy){
				long check = 0;
				for(int j=0;j<n;j++)
					check += grid[j][i];
				if(check != sum){
					out.println(-1);
					return;
				}
			}
		}
		if(d1Check != sum || d2Check != sum){
			out.println(-1);
			return;
		}
		long row = 0, col = 0;
		for(int i=0;i<n;i++){
			row += grid[xx][i];
			col += grid[i][yy];
		}
		long diag1 = 0 , diag2 = 0;
		if(xx == yy){
			for(int i=0;i<n;i++)
				diag1 += grid[i][i];
		}
		if(xx + yy == n - 1){
			for(int i=0;i<n;i++)
				diag2 += grid[i][n - i - 1];
		}
		
		long ans1 = sum - row;
		long ans2 = sum - col;
		long ans3 = diag1 == 0 ? ans1 : sum - diag1;
		long ans4 = diag2 == 0 ? ans1 : sum - diag2;
		if(ans1 == ans2 && ans1 == ans3 && ans1 == ans4)
			out.println(ans1 >= 1 && ans1 <= (long)(1e18) ? ans1 : -1);
		else
			out.println(-1);
	}
	
	
	
	/************************ SOLUTION ENDS HERE ************************/
	
	
	
	
	
	/************************ TEMPLATE STARTS HERE *********************/
	
	public static void main(String []args) throws IOException {
		FastScanner in  = new FastScanner(System.in);
		PrintWriter out = 
				new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)), false); 
		solve(in, out);
		in.close();
		out.close();
	}    
	
	static class FastScanner{
		BufferedReader reader;
		StringTokenizer st;
		FastScanner(InputStream stream){reader=new BufferedReader(new InputStreamReader(stream));st=null;}	
		String next()
		{while(st == null || !st.hasMoreTokens()){try{String line = reader.readLine();if(line == null){return null;}		    
		st = new StringTokenizer(line);}catch (Exception e){throw new RuntimeException();}}return st.nextToken();}
		String nextLine()  {String s=null;try{s=reader.readLine();}catch(IOException e){e.printStackTrace();}return s;}	    	  	
		int    nextInt()   {return Integer.parseInt(next());}
		long   nextLong()  {return Long.parseLong(next());}		
		double nextDouble(){return Double.parseDouble(next());}
		char   nextChar()  {return next().charAt(0);}
		int[]  nextIntArray(int n)         {int[] arr= new int[n];   int i=0;while(i<n){arr[i++]=nextInt();}  return arr;}
		long[] nextLongArray(int n)        {long[]arr= new long[n];  int i=0;while(i<n){arr[i++]=nextLong();} return arr;}	
		int[]  nextIntArrayOneBased(int n) {int[] arr= new int[n+1]; int i=1;while(i<=n){arr[i++]=nextInt();} return arr;}	    	
		long[] nextLongArrayOneBased(int n){long[]arr= new long[n+1];int i=1;while(i<=n){arr[i++]=nextLong();}return arr;}	    	
		void   close(){try{reader.close();}catch(IOException e){e.printStackTrace();}}				
	}
	
	/************************ TEMPLATE ENDS HERE ************************/
}