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

        int n = sc.nextInt();
        Imos im = new Imos(1000,1000);
        
        for(int i=0;i<n;i++){
        	im.addSquare(sc.nextInt(), sc.nextInt(), sc.nextInt()-1, sc.nextInt()-1, 1);
        }

        out.println(im.max());
        
        out.flush();
    }

    
}

class Imos {
	int[][] mat;
	int h;
	int w;
	
	//0<=x<=h, 0<=y<=w
	public Imos(int h, int w){
		mat = new int[h+1][w+1];
		this.h = h+1;
		this.w = w+1;
	}
	
	//左下のマスが(x1,y1)、右下のマスが(x2,y2)の正方形領域に重みwを追加
	void addSquare(int x1, int y1, int x2, int y2, int weight){
		mat[x1][y1] += weight;
		if(y2+1<w){
			mat[x1][y2+1] -= weight;
		}
		if(x2+1<h){
			mat[x2+1][y1] -= weight;
			if(y2+1<w){
				mat[x2+1][y2+1] += weight;
			}
		}
	}
	
	//最も重みの大きいマスの重み
	int max(){
		int[][] cm = copy(mat);
		cumulativeSum(cm);
		return max(cm);
	}
	
	//行列のディープコピー
	static int[][] copy(int[][] x){
		int[][] y = new int[x.length][x[0].length];
		for(int i=0;i<x.length;i++){
			y[i] = x[i].clone();
		}
		return y;
	}
	
	//左上からの累積和にする
	static void cumulativeSum(int[][] x){
		for(int i=0;i<x.length;i++){
			for(int j=1;j<x[0].length;j++){
				x[i][j] += x[i][j-1];
			}
		}
		
		for(int j=0;j<x[0].length;j++){
			for(int i=1;i<x.length;i++){
				x[i][j] += x[i-1][j];
			}
		}
	}

	//最大値
	static int max(int[][] x){
		int max = Integer.MIN_VALUE;
		for(int i=0;i<x.length;i++){
			for(int j=0;j<x[0].length;j++){
				if(x[i][j] > max){
					max = x[i][j];
				}
			}
		}
		return max;
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
