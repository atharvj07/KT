import java.io.BufferedInputStream;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;
/*

1
100
10000000000


 */
public class a {
	static String f0 = "What are you doing at the end of the world? Are you busy? Will you save us?";
	static String f1a = "What are you doing while sending \"";
	static String f1b = "\"? Are you busy? Will you send \"";
	static String f1c = "\"?";
	static int maxn = 54;
	
	public static void main(String[] args) {
		JoltyScanner in = new JoltyScanner(System.in);
		PrintWriter out = new PrintWriter(System.out);
		long[] cnts = new long[maxn];
		cnts[0] = f0.length();
		for(int i=1;i<cnts.length;i++) {
			cnts[i] = cnts[i-1] * 2 + f1a.length() + f1b.length() + f1c.length();
		}
		int q = in.nextInt();
		for(int i=0;i<q;i++) {
			int n = in.nextInt();
			long k = in.nextLong()-1;
			
			// Query is off the end
			if(n < maxn && k >= cnts[n]) {
				out.print('.');
				continue;
			}
			
			// Query is on the left recursion of binary tree
			long tmp = k / f1a.length();
			if(tmp < n-1) {
				out.print(f1a.charAt((int)(k % f1a.length())));
				continue;
			}
			
			// Query is in the bottom left corner of tree, so we can skip down some of the left recursion
			if(n >= maxn) {
				k -= f1a.length() * (long)(n-(maxn-1));
				n = maxn-1;
			}
			
			// Query is somewhere in the tree that we have left (which now has log height)
			while(true) {
				if(n == 0) {
					out.print(f0.charAt((int)k));
					break;
				}
				if(k < f1a.length()) {
					out.print(f1a.charAt((int)k));
					break;
				}
				k -= f1a.length();
				if(k < cnts[n-1]) {
					n--;
					continue;
				}
				k -= cnts[n-1];

				if(k < f1b.length()) {
					out.print(f1b.charAt((int)k));
					break;
				}
				k -= f1b.length();
				
				if(k < cnts[n-1]) {
					n--;
					continue;
				}
				k -= cnts[n-1];
				
				out.print(f1c.charAt((int)k));
				break;
			}
		}
		out.println();
		out.close();
	}
	static class JoltyScanner 
	{
		public static final int BUFFER_SIZE = 1 << 16;
		public static final char NULL_CHAR = (char) -1;
		byte[] buffer = new byte[BUFFER_SIZE];
		int bufferIdx = 0, size = 0;
		char c = NULL_CHAR;
		BufferedInputStream in;
		public JoltyScanner(InputStream in) 
		{
			this.in = new BufferedInputStream(in, BUFFER_SIZE);
			c = nextChar();
		}
		public int nextInt() 
		{
			for (; (c < '0' || c > '9'); c = nextChar());
			int res = 0;
			for (; c >= '0' && c <= '9'; c = nextChar()) 
			{
				res = (res << 3) + (res << 1) + c - '0';
			}
			return res;
		}
		public long nextLong() 
		{
			for (; (c < '0' || c > '9'); c = nextChar());
			long res = 0;
			for (; c >= '0' && c <= '9'; c = nextChar()) 
			{
				res = (res << 3) + (res << 1) + c - '0';
			}
			return res;
		}
		public char nextChar() 
		{
			while (bufferIdx == size) 
			{
				try 
				{
					size = in.read(buffer);
				} 
				catch (Exception e) 
				{
					return NULL_CHAR;
				}
				bufferIdx = 0;
			}
			return (char) buffer[bufferIdx++];
		}
	}
}