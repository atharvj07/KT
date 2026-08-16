import java.util.*;
import java.io.*;
import java.math.*;

import javax.xml.crypto.Data;

public class Main {
	static PrintWriter out = new PrintWriter(System.out);
	static FastScanner sc = new FastScanner();
	static Scanner stdIn = new Scanner(System.in);
	public static void main(String[] args) {
		while(true) {
			int n = sc.nextInt();
			if(n == 0) break;
			Data[] list = new Data[n];
			for(int i = 0; i < n; i++) {
				int m = sc.nextInt();
				int l = sc.nextInt();
				list[i] = new Data(i,l);
				for(int j = 0; j < m; j++) {
					int s = sc.nextInt()-6;
					int e = sc.nextInt()-6;
					for(int k = s; k < e; k++) {
						list[i].Date |= 1<<(k);
					}
				}
				
			}
			int[][] dp = new int[n+1][1<<17];
			for(int i = 1; i <= n; i++) {
				for(int j = 0; j < 1 << 17; j++) {
					dp[i][j] = Math.max(dp[i][j], dp[i-1][j]);
					if((j & (list[i-1].Date)) == 0) {
						dp[i][(int) (j | list[i-1].Date)] = Math.max(dp[i-1][(int) (j | list[i-1].Date)], Math.max(dp[i][j]+list[i-1].l,dp[i][(int)(j | list[i-1].Date)]));
					}
					dp[i][j] = Math.max(dp[i][j], dp[i-1][j]);
					
				}
			}

			
			int ans = 0;
			for(int i = 0; i < (1<<16)+1; i++) {
				ans = Math.max(ans, dp[n][i]);
			}
			out.println(ans);
			System.gc();
		}
		out.flush();
	}
	static class Data {
		int id;
		int l;
		Long Date = 00000000000000000L;
		Data(int a, int b) {
			id = a;
			l = b;
		}
	}

}

//-----------------Template------------------//
class FastScanner {
	private final InputStream in = System.in;
	private final byte[] buffer = new byte[1024];
	private int ptr = 0;
	private int buflen = 0;
	private boolean hasNextByte() {
		if (ptr < buflen) {
			return true;
		}else{
			ptr = 0;
			try {
				buflen = in.read(buffer);
			} catch (IOException e) {
				e.printStackTrace();
			}
			if (buflen <= 0) {
				return false;
			}
		}
		return true;
	}
	private int readByte() { if (hasNextByte()) return buffer[ptr++]; else return -1;}
	private static boolean isPrintableChar(int c) { return 33 <= c && c <= 126;}
	private void skipUnprintable() { while(hasNextByte() && !isPrintableChar(buffer[ptr])) ptr++;}
	public boolean hasNext() { skipUnprintable(); return hasNextByte();}
	public String next() {
		if (!hasNext()) throw new NoSuchElementException();
		StringBuilder sb = new StringBuilder();
		int b = readByte();
		while(isPrintableChar(b)) {
			sb.appendCodePoint(b);
			b = readByte();
		}
		return sb.toString();
	}
	public long nextLong() {
		if (!hasNext()) throw new NoSuchElementException();
		long n = 0;
		boolean minus = false;
		int b = readByte();
		if (b == '-') {
			minus = true;
			b = readByte();
		}
		if (b < '0' || '9' < b) {
			throw new NumberFormatException();
		}
		while(true){
			if ('0' <= b && b <= '9') {
				n *= 10;
				n += b - '0';
			}else if(b == -1 || !isPrintableChar(b)){
				return minus ? -n : n;
			}else{
				throw new NumberFormatException();
			}
			b = readByte();
		}
	}
	 
	public int nextInt() {
		 if (!hasNext()) throw new NoSuchElementException();
		 int n = 0;
		 boolean minus = false;
		 int b = readByte();
		 if (b == '-') {
			 minus = true;
			 b = readByte();
		 }
		 if (b < '0' || '9' < b) {
			 throw new NumberFormatException();
		 }
		 while(true){
			 if ('0' <= b && b <= '9') {
				 n *= 10;
				 n += b - '0';
			 }else if(b == -1 || !isPrintableChar(b)){
				 return minus ? -n : n;
			 }else{
				 throw new NumberFormatException();
			 }
			 b = readByte();
		 }
	}
	 
	public double nextDouble() {
		return Double.parseDouble(next());
	}
	 
 
}