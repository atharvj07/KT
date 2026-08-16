//package mar18;

import java.io.*;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentSkipListMap;

public class HR27 {
	InputStream is;
	PrintWriter out;
	String INPUT = "";
	//boolean codechef=true;
	boolean codechef=true;
	static int mod=1000000007;

	void solve()
	{		
		int n=ni(),k1=ni(),k2=ni();
		int[] a=na(n);
		int[] b=na(n);
		int[] mod=new int[n];
		for(int i=0;i<n;i++)
		{
			mod[i]=Math.abs(a[i]-b[i]);
		}
		Arrays.sort(mod);
		int cnt=k1+k2,cnt2=0;
		for(int i=0;i<cnt;i++)
		{
			int ind=-1,max=-1;
			for(int j=0;j<n;j++)
			{
				if(mod[j]>max)
				{
					max=mod[j];
					ind=j;
				}
			}
			if(ind>=0)
			{
				mod[ind]--;
				mod[ind]=Math.abs(mod[ind]);
			}
		}
		
		long sum=0;
		for(int i=0;i<n;i++)
		{
			sum+=Math.pow(mod[i], 2);
		}
		out.println(sum);
	}

	static class Pair
	{
		long a,b;
		public Pair(long a,long b)
		{
			this.a=a;
			this.b=b;
		}
	}
	
	static long lcm(int a,int b)
	{
		long val=a;
		val*=b;
		return (val/gcd(a,b));
	}
	
	static int gcd(int a,int b)
	{
		if(a==0)return b;
		return gcd(b%a,a);
	}
	
	static int pow(int a, int b, int p)
	{
		long ans = 1, base = a;
		while (b!=0)
		{
			if ((b & 1)!=0)
			{
				ans *= base;
				ans%= p;
			}
			base *= base;
			base%= p;
			b >>= 1;
		}
		return (int)ans;
	}

	static int inv(int x, int p)
	{
		return pow(x, p - 2, p);
	}

	
	void run() throws Exception
	{
		if(codechef)oj=true;
		is = oj ? System.in : new ByteArrayInputStream(INPUT.getBytes());
		out = new PrintWriter(System.out);
		
		long s = System.currentTimeMillis();
		solve();
		out.flush();
		tr(System.currentTimeMillis()-s+"ms");
	}
	
	public static void main(String[] args) throws Exception {new HR27().run();}
	
	private byte[] inbuf = new byte[1024];
	public int lenbuf = 0, ptrbuf = 0;
	
	private int readByte()
	{
		if(lenbuf == -1)throw new InputMismatchException();
		if(ptrbuf >= lenbuf){
			ptrbuf = 0;
			try { lenbuf = is.read(inbuf); } catch (IOException e) { throw new InputMismatchException(); }
			if(lenbuf <= 0)return -1;
		}
		return inbuf[ptrbuf++];
	}
	
	private boolean isSpaceChar(int c) { return !(c >= 33 && c <= 126); }
	private int skip() { int b; while((b = readByte()) != -1 && isSpaceChar(b)); return b; }
	
	private double nd() { return Double.parseDouble(ns()); }
	private char nc() { return (char)skip(); }
	
	private String ns()
	{
		int b = skip();
		StringBuilder sb = new StringBuilder();
		while(!(isSpaceChar(b))){ // when nextLine, (isSpaceChar(b) && b != ' ')
			sb.appendCodePoint(b);
			b = readByte();
		}
		return sb.toString();
	}
	
	private char[] ns(int n)
	{
		char[] buf = new char[n];
		int b = skip(), p = 0;
		while(p < n && !(isSpaceChar(b))){
			buf[p++] = (char)b;
			b = readByte();
		}
		return n == p ? buf : Arrays.copyOf(buf, p);
	}
	
	private char[][] nm(int n, int m)
	{
		char[][] map = new char[n][];
		for(int i = 0;i < n;i++)map[i] = ns(m);
		return map;
	}
	
	private int[] na(int n)
	{
		int[] a = new int[n];
		for(int i = 0;i < n;i++)a[i] = ni();
		return a;
	}
	
	private int ni()
	{
		int num = 0, b;
		boolean minus = false;
		while((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-'));
		if(b == '-'){
			minus = true;
			b = readByte();
		}
		
		while(true){
			if(b >= '0' && b <= '9'){
				num = num * 10 + (b - '0');
			}else{
				return minus ? -num : num;
			}
			b = readByte();
		}
	}
	
	private long nl()
	{
		long num = 0;
		int b;
		boolean minus = false;
		while((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-'));
		if(b == '-'){
			minus = true;
			b = readByte();
		}
		
		while(true){
			if(b >= '0' && b <= '9'){
				num = num * 10 + (b - '0');
			}else{
				return minus ? -num : num;
			}
			b = readByte();
		}
	}
	
	private boolean oj = System.getProperty("ONLINE_JUDGE") != null;
	private void tr(Object... o) { if(!oj)System.out.println(Arrays.deepToString(o)); }
}