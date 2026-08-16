import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;
import java.util.NoSuchElementException;
import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		int a=scan.nextInt();
		int b=scan.nextInt();
		long x=scan.nextLong();
		int max=(int)x;
		for(int i=1;i<a;i++) {
			int y=scan.nextInt();
			max=max(y,max);
			x=gcd(x,y);
		}
		while(max>=0) {
			if(max==b) {
				System.out.println("POSSIBLE");
				return;
			}
			max-=x;
		}
		System.out.println("IMPOSSIBLE");
	}
	static FastScanner scan=new FastScanner();
	static Scanner scanner=new Scanner(System.in);
	static long mod=1000000007;
	static double eps=0.0000000001;
	static int big=Integer.MAX_VALUE;
	static long gcd (long a, long b) {return b>0?gcd(b,a%b):a;}
	static long lcm (long a, long b) {return a*b/gcd(a,b);}
	static int max(int a,int b) {return a>b?a:b;}
	static int min(int a,int b) {return a<b?a:b;}
	static long lmax(long a,long b) {return Math.max(a, b);}
	static long lmin(long a,long b) {return Math.min(a, b);}
	static long factorial(int i) {return i==1?1:i*factorial(i-1);}
	static int lower_bound(int a[],int key) {
		int right=a.length;
		int left=0;
		while(right-left>0) {
			int mid=(right+left)/2;
			if(a[mid]<key) {
				left=mid;
			}
			else {
				right=mid;
			}
		}
		return left;
	}
	static int upper_bound(int a[],int key) {
		int right=a.length;
		int left=0;
		while(right-left>0) {
			int mid=(right+left)/2;
			if(a[mid]<=key) {
				left=mid;
			}
			else {
				right=mid;
			}
		}
		return left;
	}
	static boolean isPrime (long n) {
		if (n==2) return true;
		if (n<2 || n%2==0) return false;
		double d = Math.sqrt(n);
		for (int i=3; i<=d; i+=2)if(n%i==0){return false;}
		return true;
	}
	static int upper_division(int a,int b) {
		if(a%b==0) {
			return a/b;
		}
		else {
			return a/b+1;
		}
	}
	static long lupper_division(long a,long b) {
		if(a%b==0) {
			return a/b;
		}
		else {
			return a/b+1;
		}
	}
	static int[] setArray(int a) {
		int b[]=new int[a];
		for(int i=0;i<a;i++) {
			b[i]=scan.nextInt();
		}
		return b;
	}
	static long[] lsetArray(int a) {
		long b[]=new long[a];
		for(int i=0;i<a;i++) {
			b[i]=scan.nextLong();
		}
		return b;
	}
	static String reverce(String str) {
		String strr="";
		for(int i=str.length()-1;i>=0;i--) {
			strr+=str.charAt(i);
		}
		return strr;
	}
	public static void printArray(int[] que) {
		for(int i=0;i<que.length-1;i++) {
			System.out.print(que[i]+" ");
		}
		System.out.println(que[que.length-1]);
	}
	public static int[][] doublesort(int[][]a) {
		Arrays.sort(a,(x,y)->Integer.compare(x[0],y[0]));
		return a;
	}
	static long modpow(long x,long n,long mo) {
		long sum=1;
		while(n>0) {
			if((n&1)==1) {
				sum=sum*x%mo;
			}
			x=x*x%mo;
			n>>=1;
		}
		return sum;
	}
	public static char[] revch(char ch[]) {
		char ret[]=new char[ch.length];
		for(int i=ch.length-1,j=0;i>=0;i--,j++) {
			ret[j]=ch[i];
		}
		return ret;
	}
	public static int[] revint(int ch[]) {
		int ret[]=new int[ch.length];
		for(int i=ch.length-1,j=0;i>=0;i--,j++) {
			ret[j]=ch[i];
		}
		return ret;
	}
	public static void warshall_floyd(int v[][],int n) {
		for(int k=0;k<n;k++)
			for(int i=0;i<n;i++)
				for(int j=0;j<n;j++)
					v[i][j]=min(v[i][j],v[i][k]+v[k][j]);
	}
	public static long modinv(long a,long m) {
		long b=m,u=1,v=0;
		while(b!=0) {
			long t=a/b;
			a-=t*b;
			long x=a;
			a=b;
			b=x;
			
			u-=t*v;
			x=u;
			u=v;
			v=x;
		}
		u%=m;
		if(u<0)u+=m;
		return u;
	}
}
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
	public boolean hasNext() { while(hasNextByte() && !isPrintableChar(buffer[ptr])) ptr++; return hasNextByte();}
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
		long nl = nextLong();
		if (nl < Integer.MIN_VALUE || nl > Integer.MAX_VALUE) throw new NumberFormatException();
		return (int) nl;
	}
	public double nextDouble() { return Double.parseDouble(next());}
	public char nextchar() {
		try { return (char)System.in.read(); } catch(Exception e) {
			throw new RuntimeException(e);
		}
	}
}