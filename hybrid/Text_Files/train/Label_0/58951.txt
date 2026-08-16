import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.*;
import java.math.BigInteger;
 
public class Main implements Runnable {
	
	static int mod = 1000000007;
	
    public static void main(String[] args) {
    	new Thread(null, new Main(), "", 1024 * 1024 * 1024).start();
    }
    
    public void run() {
        PrintWriter out = new PrintWriter(System.out);
        FastScanner sc = new FastScanner();
        
        int q = sc.nextInt();
        
        Eratosthenes et = new Eratosthenes(100000);
        
        int[] isOK = new int[100001];
        Arrays.fill(isOK, 1);
        isOK[0] = 0;
        isOK[1] = 0;
        
        for(int i:et.primeNum){
        	isOK[i] = 0;
        	
        	long i2 = (long)i*i;
        	if(i2>100000){
        		continue;
        	}
        	isOK[(int)i2] = 0;
        	
        	long i3 = i2*i;
        	if(i3>100000){
        		continue;
        	}
        	isOK[(int)i3] = 0;
        }
        
        for(int i=0;i<et.primeNum.size();i++){
        	for(int j=i+1;j<et.primeNum.size();j++){
        		long p1 = et.primeNum.get(i);
        		long p2 = et.primeNum.get(j);
        		long prod = p1*p2;
        		if(prod>100000){
        			break;
        		}
        		isOK[(int)prod] = 0;
        	}
        }
        
        int[] ans = cumulativeSum(isOK);
        
        for(int i=0;i<q;i++){
        	out.println(ans[sc.nextInt()]);
        }
        
        out.flush();
    }
 
	static int[] cumulativeSum(int[] a){
		int[] cs = new int[a.length];
		cs[0] = a[0];
		for(int i=1;i<a.length;i++){
			cs[i] = cs[i-1] + a[i];
		}
		return cs;
	}
    
}

class Eratosthenes {
	boolean[] isPrime; //index+2が素数かどうか(i.e.qが素数か知りたければq-2を見る）
	ArrayList<Integer> primeNum;
	
	//nまでの整数の素数判定テーブルを作成(O(nloglogn))
	public Eratosthenes(int n){
		if(n==0){
			isPrime = new boolean[0];
		}
		else{
			isPrime = new boolean[n-1];
		}
		Arrays.fill(isPrime, true);
		
		//素数定理でnまでの素数の数を見積もってprimeNumの初期サイズを設定
		double pros = (double) n / Math.log(n);
		if(n==1){ pros = 0;}
		primeNum = new ArrayList<Integer>(Math.min((int)pros,Integer.MAX_VALUE)); 
		
		double root = Math.sqrt(n);
		
	    for(int i=2; i<=root; i++) {
	        if (isPrime[i-2]) {
	        	primeNum.add(i);
	            for (int j=i*2; j<=n; j+=i) {
	                isPrime[j-2] = false; 
	            }
	        }
	    }
	    
	    for(int i=(int)root+1;i<=n;i++){
	    	if(isPrime[i-2]){
	    		primeNum.add(i);
	    	}
	    }
	}
	
	//nが素数かどうか
	boolean isPrime(int n){
		return isPrime[n-2];
	}
	
	//n以下の素数の数
	int pi(int n){
		int a = Collections.binarySearch(primeNum,n);
		if(a>=0){
			return a+1;
		}
		else{
			a = -(a+1); //lowerBound
			return a;
		}
	}
	
	//n番目の素数(1スタート）
	int nthPrime(int n){
		return primeNum.get(n-1);
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
	public int[][] nextintMatrix(int h, int w){
		int[][] mat = new int[h][w];
		for(int i=0;i<h;i++){
			for(int j=0;j<w;j++){
				mat[i][j] = nextInt();
			}
		}
		return mat;
	}
	public double nextDouble() {
		return Double.parseDouble(next());
	}
}
