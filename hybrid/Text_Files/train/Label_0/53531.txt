
import java.util.*;
import java.io.*;
import java.lang.*;



public class Main {
    static class Reader 
{ 
    final private int BUFFER_SIZE = 1 << 16; 
    private DataInputStream din; 
    private byte[] buffer; 
    private int bufferPointer, bytesRead; 

    public Reader() 
    { 
        din = new DataInputStream(System.in); 
        buffer = new byte[BUFFER_SIZE]; 
        bufferPointer = bytesRead = 0; 
    } 

    public Reader(String file_name) throws IOException 
    { 
        din = new DataInputStream(new FileInputStream(file_name)); 
        buffer = new byte[BUFFER_SIZE]; 
        bufferPointer = bytesRead = 0; 
    } 

    public String readLine() throws IOException 
    { 
        byte[] buf = new byte[64]; // line length 
        int cnt = 0, c; 
        while ((c = read()) != -1) 
        { 
            if (c == '\n') 
                break; 
            buf[cnt++] = (byte) c; 
        } 
        return new String(buf, 0, cnt); 
    } 

    public int nextInt() throws IOException 
    { 
        int ret = 0; 
        byte c = read(); 
        while (c <= ' ') 
            c = read(); 
        boolean neg = (c == '-'); 
        if (neg) 
            c = read(); 
        do
        { 
            ret = ret * 10 + c - '0'; 
        }  while ((c = read()) >= '0' && c <= '9'); 

        if (neg) 
            return -ret; 
        return ret; 
    } 

    public long nextLong() throws IOException 
    { 
        long ret = 0; 
        byte c = read(); 
        while (c <= ' ') 
            c = read(); 
        boolean neg = (c == '-'); 
        if (neg) 
            c = read(); 
        do { 
            ret = ret * 10 + c - '0'; 
        } 
        while ((c = read()) >= '0' && c <= '9'); 
        if (neg) 
            return -ret; 
        return ret; 
    } 

    public double nextDouble() throws IOException 
    { 
        double ret = 0, div = 1; 
        byte c = read(); 
        while (c <= ' ') 
            c = read(); 
        boolean neg = (c == '-'); 
        if (neg) 
            c = read(); 

        do { 
            ret = ret * 10 + c - '0'; 
        } 
        while ((c = read()) >= '0' && c <= '9'); 

        if (c == '.') 
        { 
            while ((c = read()) >= '0' && c <= '9') 
            { 
                ret += (c - '0') / (div *= 10); 
            } 
        } 

        if (neg) 
            return -ret; 
        return ret; 
    } 

    private void fillBuffer() throws IOException 
    { 
        bytesRead = din.read(buffer, bufferPointer = 0, BUFFER_SIZE); 
        if (bytesRead == -1) 
            buffer[0] = -1; 
    } 

    private byte read() throws IOException 
    { 
        if (bufferPointer == bytesRead) 
            fillBuffer(); 
        return buffer[bufferPointer++]; 
    } 

    public void close() throws IOException 
    { 
        if (din == null) 
            return; 
        din.close(); 
    } 
} 
    
    public static void main(String[] args) throws java.lang.Exception, IOException {
	 Reader sc = new Reader() ;
	 int n = sc.nextInt() ;
	 int m = sc.nextInt() ;
	 ArrayList<Integer> g[] = new ArrayList[n] ;
	 for(int i = 0 ; i < n ; i++) {
		 g[i] = new ArrayList<Integer>() ;
	 }
	 int ind[] = new int[n] ;
	 while(m-->0) {
	  int u = sc.nextInt() - 1 ;
	  int v = sc.nextInt() - 1 ;
	  g[v].add(u) ;
	  ind[u]++ ;
	 }
	 int s = sc.nextInt() - 1 ;
	 int t = sc.nextInt() - 1 ;
	 System.out.println(robotControl(s, t, ind, g, n)) ;
	}
	
	public static long robotControl(int s, int t, int ind[], ArrayList<Integer> g[], int n) {
		long dp[] = new long[n] ;
		Arrays.fill(dp, Integer.MAX_VALUE);
		boolean vis[] = new boolean[n] ;
	    ArrayDeque<Integer> q = new ArrayDeque<>(); 
		q.addLast(t) ; 
		dp[t] = 0 ;
		int u ;
		while(!q.isEmpty()) {
		 u = q.poll() ;
		 if(!vis[u]) {
		 vis[u] = true ;
		 for(int v : g[u]) {
			ind[v]-- ;
			if(ind[v] == 0) {
			 if(dp[v] > dp[u]) {
				dp[v] = dp[u] ;
				q.addFirst(v);
			 }
			} else if(dp[v] > dp[u] + 1) {
				dp[v] = dp[u] + 1 ;
				q.addLast(v) ;
			}
		  }
		 }
		}
		return (dp[s] == Integer.MAX_VALUE) ? -1 : dp[s] ;
	}
}
