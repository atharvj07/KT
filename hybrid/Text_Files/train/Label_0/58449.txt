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
        int k = sc.nextInt();
        long L = sc.nextLong();
        long R = sc.nextLong();
        long[] a = sc.nextlongArray(n);

        System.out.println(coinCombination(a,k,L,R));
    }
    
	//L円以上R円以下になる丁度k枚のコインの選び方の個数
	static long coinCombination(long[] a, int k, long L, long R){
        int N = a.length;
        class SumList extends ArrayList<Long>{
			private static final long serialVersionUID = 1L;
        }
        
        //半分全列挙
        //S:0 - (N/2)-1
        //T:N/2 - N-1
        int Tnum = N-(N/2);
        SumList[] TL = new SumList[Math.min(Tnum,k)+1];
        for(int i=0;i<TL.length;i++){
        	TL[i] = new SumList();
        }
        int Tstt = N/2;
        for(int S = (1<<Tnum) -1;S>=0;S--){
            long sum = 0;
            int num = 0;
            for(int i=0;i<Tnum;i++){
                if(((S>>i)&1) == 1){
                    sum += a[Tstt+i];
                    num++;
                }
            }
            if(sum<=R && num <= k){
                TL[num].add(sum);
            }
        }

        for(SumList l:TL){
        	Collections.sort(l);
        }
        
        long ans = 0;
        for(int S = (1<<(N/2)) -1;S>=0;S--){
            long sum = 0;
            int num = 0;
            for(int i=0;i<N/2;i++){
                if(((S>>i)&1) == 1){
                    sum += a[i];
                    num++;
                }
            }

            if(sum<=R && 0 <= k-num && k-num < TL.length && !TL[k-num].isEmpty()){	//[k-num]に入るべき要素が全て>Rで空のことがある
            	int min = lowerBound(TL[k-num],L-sum);
            	int max = upperBound(TL[k-num],R-sum);
            	ans += max - min;
            }
        }
        
        return ans;
	}
	
	static int upperBound(ArrayList<Long> a, long key){
		int idx = Collections.binarySearch(a, key, (x,y)->x.compareTo(y)>0?1:-1);
		
		if(idx<0){
			idx = ~idx;
		}
		
		return idx;
	}
	static int lowerBound(ArrayList<Long> a, long key){
		int idx = Collections.binarySearch(a, key, (x,y)->x.compareTo(y)>=0?1:-1);
		
		if(idx<0){
			idx = ~idx;
		}
		
		return idx;
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
