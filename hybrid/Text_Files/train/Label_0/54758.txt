import java.util.Map.Entry;
import java.io.*;
import java.util.*;

public class Main {
	
	static int[][] dp;
	static int N;
	static int[][] graph;
	static int INF = 16000;
	
	public static void main(String[] args) throws IOException {
		FastScanner sc = new FastScanner(System.in);
		
		N = sc.nextInt();
		int M = sc.nextInt();
		graph = new int[N][N];
		for(int i = 0; i < N; i++) Arrays.fill(graph[i], INF);
		for(int i = 0; i < M; i++){
			int s = sc.nextInt();
			int t = sc.nextInt();
			int d = sc.nextInt();
			graph[s][t] = d;
		}
		
		dp = new int[1 << N][N];
		for(int i = 0; i < 1 << N; i++) Arrays.fill(dp[i], -1);
		//どこからスタートしても1周分のコストは変わらない
		dp[(1 << N) - 1][0] = 0;
		
		int ans = solve(0, 0);
		if(ans == INF)
			System.out.println(-1);
		else
			System.out.println(ans);
	}
	
	public static int solve(int S, int v){
		if(dp[S][v] != -1) return dp[S][v];
		
		int d = INF;
		for(int i = 0; i < N; i++){
			if(((S >> i) & 1) == 0 && graph[v][i] != INF){
				d = Math.min(d, solve((S | 1 << i), i) + graph[v][i]);
			}
		}
		
		dp[S][v] = d;
		
		return dp[S][v];
	}
}

class Pair{
	int to;
	int dist;
	public Pair(int t, int d){
		to = t;
		dist = d;
	}
}

class FastScanner {
    private InputStream in;
    private final byte[] buffer = new byte[1024];
    private int ptr = 0;
    private int buflen = 0;
    public FastScanner(InputStream in) {
		this.in = in;
	}
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
    private int readByte() {
    	if (hasNextByte()) return buffer[ptr++];
    	else return -1;
    }
    private static boolean isPrintableChar(int c){
    	return 33 <= c && c <= 126;
    }
    public boolean hasNext() {
    	while(hasNextByte() && !isPrintableChar(buffer[ptr]))
    		ptr++; return hasNextByte();
    }
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
    public double nextDouble() {
    	return Double.parseDouble(next());
    }
}

