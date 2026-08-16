import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;

public class archaeology {
	public static void main(String[] args) {
		FastScanner scan=new FastScanner();
		PrintWriter out=new PrintWriter(System.out);
		char[] a=scan.next().toCharArray();
		int n=a.length;
		boolean[] good=new boolean[n];
		int l=0, r=n-1;
		while(l<=r) {
			if(a[l]==a[r]) {
				good[l]=good[r]=true;
				l++;
				r--;
			}
			else if(l<n-1&&a[l+1]==a[r]) l++;
			else if(r>0&&a[r-1]==a[l]) r--;
			else {
				l++;
				r--;
			}
		}
		for(int i=0;i<n;i++) {
			if(good[i]) out.print(a[i]);
		}
		out.close();
	}
	static class FastScanner {
		BufferedReader br;
		StringTokenizer st;

		public FastScanner() {
			try	{
				br = new BufferedReader(new InputStreamReader(System.in));
				st = new StringTokenizer(br.readLine());
			} catch (Exception e){e.printStackTrace();}
		}

		public String next() {
			if (st.hasMoreTokens())	return st.nextToken();
			try {st = new StringTokenizer(br.readLine());}
			catch (Exception e) {e.printStackTrace();}
			return st.nextToken();
		}

		public int nextInt() {return Integer.parseInt(next());}

		public long nextLong() {return Long.parseLong(next());}

		public double nextDouble() {return Double.parseDouble(next());}

		public String nextLine() {
			String line = "";
			if(st.hasMoreTokens()) line = st.nextToken();
			else try {return br.readLine();}catch(IOException e){e.printStackTrace();}
			while(st.hasMoreTokens()) line += " "+st.nextToken();
			return line;
		}
	}
}
/*
cbcacbcacbca
prints ccccc not long enough
*/