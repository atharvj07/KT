import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Queue;
import java.util.Set;
import java.util.Stack;
import java.util.StringTokenizer;
import java.util.TreeMap;
 
public class Solution {

static class Robber{
	int x, y;
	public Robber(int x, int y) {
		this.x = x;
		this.y = y;
	}
}
static class SearchLight{
	int x, y;
	public SearchLight(int x, int y) {
		this.x = x;
		this.y = y;
	}
}

public static void main(String[] args){
 
   new Thread(null, null, "Anshum Gupta", 99999999) {
        public void run() {
            try {
                solve();
            } catch(Exception e) {
                e.printStackTrace();
                System.exit(1);
            }
        }
    }.start();
}
 
static final long mxx = (long)(1e18 + 5);
static final int mxN = (int)(1e6);
static final int mxV = (int)(1e6 + 5), log = 18;
static long mod = (long)(1e9+7);
static final int INF = (int)1e9;
static boolean[]vis;
static ArrayList<ArrayList<Integer>> adj;
static int n, m, k, q, upMoves, rightMoves;
static int[]dp;
static char[]str;

 
public static void solve() throws Exception {
	   // solve the problem here
		s = new MyScanner();
   		out = new PrintWriter(new BufferedOutputStream(System.out), true);
//	   		out = new PrintWriter("output.txt");
        int tc = 1;//s.nextInt();
        for(int i=1; i<=tc; i++) {
//        	out.print("Case #" + i + ": ");
        	testcase();
        }
           
        out.flush();
        out.close();
}


static void testcase() {
	n = s.nextInt();
	m = s.nextInt();
	Robber[] robbers = new Robber[n];
	SearchLight[] searchlLights = new SearchLight[m];
	dp = new int[mxV];
	for(int i=0; i<n; i++) {
		robbers[i] = new Robber(s.nextInt(), s.nextInt());
	}
	for(int i=0; i<m; i++) {
		searchlLights[i] = new SearchLight(s.nextInt(), s.nextInt());
	}
	for(int i=0; i<n; i++) {
		findMinMovesToAvoidSearchLights(searchlLights, robbers[i]);
	}
	int ans = INF;
	for(int i=mxV - 2; i>=0; i--) {
		dp[i] = Math.max(dp[i], dp[i+1]);
		ans = Math.min(ans, Math.max(0, i - 1) + dp[i]);
	}
	out.println(ans);
}




private static void findMinMovesToAvoidSearchLights(SearchLight[] searchlLights, Robber robber) {
	for(int i=0; i<m; i++) {
		int incY = searchlLights[i].y - robber.y + 1;
		if(incY >= 0) {
			dp[incY] = Math.max(dp[incY], searchlLights[i].x - robber.x + 1);
		}
	}
}
public static PrintWriter out;
public static MyScanner s;
static class MyScanner {
 
    BufferedReader br;
    StringTokenizer st;
 
    public MyScanner() {
        br = new BufferedReader(new InputStreamReader(System.in));
    }
    public MyScanner(String fileName) {
    	try {
			br = new BufferedReader(new FileReader(fileName));
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
    }
    String next() {
        while (st == null || !st.hasMoreElements()) {
            try {
                st = new StringTokenizer(br.readLine());
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return st.nextToken();
    }
 
    int nextInt() { return Integer.parseInt(next()); }
    long nextLong() { return Long.parseLong(next()); }
    double nextDouble() { return Double.parseDouble(next()); }
    int[] nextIntArray(int n){
    	int[]a = new int[n];
    	for(int i=0; i<n; i++) {
    		a[i] = this.nextInt();
    	}
    	return a;
    }
    long[] nextlongArray(int n) {
    	long[]a = new long[n];
    	for(int i=0; i<n; i++) {
    		a[i] = this.nextLong();
    	}
    	return a;
    }
    Integer[] nextIntegerArray(int n){
    	Integer[]a = new Integer[n];
    	for(int i=0; i<n; i++) {
    		a[i] = this.nextInt();
    	}
    	return a;
    }
    Long[] nextLongArray(int n) {
    	Long[]a = new Long[n];
    	for(int i=0; i<n; i++) {
    		a[i] = this.nextLong();
    	}
    	return a;
    }
    char[][] next2DCharArray(int n, int m){
    	char[][]arr = new char[n][m];
    	for(int i=0; i<n; i++) {
    		arr[i] = this.next().toCharArray();
    	}
    	return arr;
    }
    ArrayList<ArrayList<Integer>> readUndirectedUnweightedGraph(int n, int m) {
    	ArrayList<ArrayList<Integer>>adj = new ArrayList<ArrayList<Integer>>();
    	for(int i=0; i<=n; i++)adj.add(new ArrayList<Integer>());
    	for(int i=0; i<m; i++) {
    		int u = s.nextInt();
    		int v = s.nextInt();
    		adj.get(u).add(v);
    		adj.get(v).add(u);
    	}
    	return adj;
    }
    ArrayList<ArrayList<Integer>> readDirectedUnweightedGraph(int n, int m) {
    	ArrayList<ArrayList<Integer>>adj = new ArrayList<ArrayList<Integer>>();
    	for(int i=0; i<=n; i++)adj.add(new ArrayList<Integer>());
    	for(int i=0; i<m; i++) {
    		int u = s.nextInt();
    		int v = s.nextInt();
    		adj.get(u).add(v);
    	}
    	return adj;
    }
    String nextLine(){
        String str = "";
        try {
            str = br.readLine();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return str;
    }
}
 
 
}