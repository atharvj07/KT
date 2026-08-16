import java.io.IOException;
import java.io.InputStream;
import java.util.*;
import java.math.BigInteger;
 
public class Main implements Runnable {
	
	static int mod = 1000000007;
	
    public static void main(String[] args) {
    	new Thread(null, new Main(), "", 1024 * 1024 * 1024).start();
    }
    
    public void run() {
        FastScanner sc = new FastScanner();
        int n = sc.nextInt();
        long V = sc.nextLong();
        long[] a = sc.nextlongArray(n);
        long[] b = sc.nextlongArray(n);
        long[] c = sc.nextlongArray(n);
        long[] d = sc.nextlongArray(n);
        System.out.println(coinCombination(a,b,c,d,V));

    }
    
	//4つの袋からそれぞれ1枚ずつコインを取り、合計でV円にする組合せの数
	static long coinCombination(long[] a, long[] b, long[] c, long[] d, long V){
		//半分全列挙		
		long[] up = new long[a.length*b.length];
		long[] down = new long[c.length*d.length];
		
		int id = 0;
		for(int i=0;i<a.length;i++){
			for(int j=0;j<b.length;j++){
				up[id] = a[i] + b[j];
				id++;
			}
		}
		id = 0;
		for(int i=0;i<c.length;i++){
			for(int j=0;j<d.length;j++){
				down[id] = c[i] + d[j];
				id++;
			}
		}
		
		Arrays.sort(down);
		
		long ans = 0;
		
		for(long p:up){
			ans += numOfEquals(down,V-p,0,down.length-1);
		}
		
		return ans;
	}
	
	//[from,to]内のkeyの数を二分探索
	static int numOfEquals(long[] a, long key, int from, int to){
		if(from == to){
			if(a[from]==key){
				return 1;
			}
			else{
				return 0;
			}
		}
		int m = (from+to+1)/2;	//オーバーフロー対策なし
		long am = a[m];
		
		if(key<am){
			return numOfEquals(a,key,from,m-1);
		}
		else if(key>am){
			return numOfEquals(a,key,m,to);
		}
		else{	//key = am
			int lb = lowerBound(a,key,from,m);
			int ub = upperBound(a,key,m,to);
			return ub - lb;
		}
	}
	static int lowerBound(long[] a, long key, int from, int to){
		if(from == to){
			if(a[from]<key){
				return from+1;
			}
			else{
				return from;
			}
		}
		int m = (from+to+1)/2;	//オーバーフロー対策なし
		long am = a[m];
		
		if(key<=am){
			return lowerBound(a,key,from,m-1);
		}
		else{
			return lowerBound(a,key,m,to);
		}
	}
	static int upperBound(long[] a, long key, int from, int to){
		if(from == to){
			return from+1;
		}
		int m = (from+to+1)/2;	//オーバーフロー対策なし
		long am = a[m];
		
		if(key<am){
			return upperBound(a,key,from,m-1);
		}
		else{
			return upperBound(a,key,m,to);
		}
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
		} else {
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
	private int readByte() {
		if (hasNextByte())
			return buffer[ptr++];
		else
			return -1;
	}
	private static boolean isPrintableChar(int c) {
		return 33 <= c && c <= 126;
	}
	public boolean hasNext() {
		while (hasNextByte() && !isPrintableChar(buffer[ptr]))
			ptr++;
		return hasNextByte();
	}
	public String next() {
		if (!hasNext())
			throw new NoSuchElementException();
		StringBuilder sb = new StringBuilder();
		int b = readByte();
		while (isPrintableChar(b)) {
			sb.appendCodePoint(b);
			b = readByte();
		}
		return sb.toString();
	}
	public long nextLong() {
		if (!hasNext())
			throw new NoSuchElementException();
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
		while (true) {
			if ('0' <= b && b <= '9') {
				n *= 10;
				n += b - '0';
			} else if (b == -1 || !isPrintableChar(b)) {
				return minus ? -n : n;
			} else {
				throw new NumberFormatException();
			}
			b = readByte();
		}
	}
	public int nextInt() {
		long nl = nextLong();
		if (nl < Integer.MIN_VALUE || nl > Integer.MAX_VALUE)
			throw new NumberFormatException();
		return (int) nl;
	}
	public int[] nextintArray(int n){
		int[] a = new int[n];
		for(int i=0;i<n;i++){
			a[i] = nextInt();
		}
		return a;
	}
	public long[] nextlongArray(int n){
		long[] a = new long[n];
		for(int i=0;i<n;i++){
			a[i] = nextLong();
		}
		return a;
	}
	public Integer[] nextIntegerArray(int n){
		Integer[] a = new Integer[n];
		for(int i=0;i<n;i++){
			a[i] = nextInt();
		}
		return a;
	}
	public double nextDouble() {
		return Double.parseDouble(next());
	}
}
