import java.io.*;
import java.util.*;
public class Main{

	static class InputReader
	{
		public BufferedReader reader;
		public StringTokenizer tok;
		
		public InputReader(InputStream inputStream)
		{
			reader=new BufferedReader(new InputStreamReader(inputStream));
		    tok = null;
		}
		
		public InputReader(String inputFile) throws FileNotFoundException
		{
			reader = new BufferedReader(new FileReader(inputFile));
            tok=null;		
		}
		
		public String nextLine()
		{
			String c="";
			try
			{
				c=reader.readLine();
			}
			catch (IOException e){
				throw new RuntimeException(e);
			}
			
			return c;
		}
		
		public String next()
		{
			while(tok ==null || !tok.hasMoreTokens())
			{
				try
				{
					tok=new StringTokenizer(nextLine());
				}
				catch(Exception e)
				{
					throw new RuntimeException(e);
				}
			}
			
			return tok.nextToken();
		}
		
		public int nextInt()
		{
			return Integer.parseInt(next());
		}
		
		public long nextLong()
		{
			return Long.parseLong(next());
		}
	}
	
	public static void main(String args[])
	{
		InputStream inputstream=System.in;
		OutputStream outputstream=System.out;
		InputReader in=new InputReader(inputstream);
		PrintWriter out=new PrintWriter (outputstream);
		Task solver=new Task();
		solver.solve(in,out);
		out.flush();
	}
	
	static class Task
	{
		static class Node{
			int val;
			long l,r;
			boolean visited;
			List<Node> neighbours;
			Node(int val){
				this.val = val;
				this.visited = false;
				neighbours = new ArrayList<Node>();
			}
			public void SetRanges(long l,long r) {
				this.l = l;
				this.r = r;
			}
			public void AddNeighbour(Node n) {
				this.neighbours.add(n);
			}
			public List<Node> getNeighbours() {
				return this.neighbours;
			}
			
		}
		public static void dfs(Node v,long[][] dp) {
			v.visited = true;
			List<Node> adj = v.getNeighbours();
			int x = v.val;
			for(Node u : adj) {
				if(u.visited == false) {
					dfs(u,dp);
					int y = u.val;
					dp[x][0]+=Math.max(dp[y][0]+Math.abs(v.l - u.l),dp[y][1]+Math.abs(v.l-u.r));
					dp[x][1]+=Math.max(dp[y][0]+Math.abs(v.r - u.l),dp[y][1]+Math.abs(v.r-u.r));
				}
			}
		}
	    public void solve(InputReader cin,PrintWriter out)
		{
	    	int tc = cin.nextInt();
	    	
	    	for(int t =0 ;t < tc;t++) {
	    		int n = cin.nextInt();
	    		Node nodes[] = new Node[n];
	    		for(int i =0 ;i < n ;i++) {
	    			nodes[i] = new Node(i);
	    		}
	    		for(int i=0;i<n;i++) {
	    			long l = cin.nextLong();
	    			long r = cin.nextLong();
	    			nodes[i].SetRanges(l,r);
	    		}
	    		long dp[][] = new long[n][2];
	    		for(int i =0 ;i<n;i++)for(int j=0;j<2;j++)dp[i][j]=0;
	    		for(int i=0 ; i<n-1;i++) {
	    			int x = cin.nextInt();
	    			int y = cin.nextInt();
	    			--x;
	    			--y;
	    			nodes[x].AddNeighbour(nodes[y]);
	    			nodes[y].AddNeighbour(nodes[x]);
	    		}
	    		dfs(nodes[0],dp);
	    		out.println(Math.max(dp[0][0],dp[0][1]));
	    		
	    	}
		}
		
	}
}