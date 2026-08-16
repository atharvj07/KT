import java.io.*;
import java.util.*;
public class E{
	long[][][]cached;
	int[][][]by;
	int[][]g;
	long[]cost;
	int K;
	long inf=Integer.MAX_VALUE;
	int n;
	ArrayList<Integer>centers;
	void solve()throws Exception
    {		
		centers=new ArrayList<Integer>();
		n=nextInt();
		K=nextInt();
		cost=new long[n+1];
		cost[n]=inf;
		for(int i=1;i<=n-1;i++)
			cost[i]=nextInt();
		int[]x=new int[n-1];
		int[]y=new int[n-1];
		int[]deg=new int[n];
		for(int i=0;i<n-1;i++)
		{
			x[i]=nextInt()-1;
			y[i]=nextInt()-1;
			deg[x[i]]++;
			deg[y[i]]++;
		}
		g=new int[n][];
		for(int i=0;i<n;i++)
			g[i]=new int[deg[i]];
		int[]ind=new int[n];
		for(int i=0;i<n-1;i++)
		{
			g[x[i]][ind[x[i]]++]=y[i];
			g[y[i]][ind[y[i]]++]=x[i];			
		}
		cached=new long[n][n+1][n+1];
		for(int i=0;i<n;i++)
			for(int j=0;j<=n;j++)
				Arrays.fill(cached[i][j], -1);
		long res=go(0, -1, n, n);
		search(0, -1, n, n);
		System.out.println(res);
		int[]ans=new int[n];
		for(int i=0;i<n;i++)
			ans[i]=-1;
		int[]d=new int[n];
		for(int z: centers)
			ans[z]=z;
		Queue<Integer>q=new LinkedList<Integer>();
		for(int z: centers)
			q.add(z);
		long c=centers.size()*K;
		while(q.size()>0)
		{
			Queue<Integer>nq=new LinkedList<Integer>();
			for(int z: q)
				for(int t: g[z])
					if(ans[t]==-1)
					{
						nq.add(t);
						d[t]=d[z]+1;
						c+=cost[d[t]];
						ans[t]=ans[z];
					}
			q=nq;					
		}
		if(c!=res)
			throw new RuntimeException();
		for(int i=0;i<n;i++)
			System.out.println(ans[i]+1);
	}
	void search(int at,int par,int dist,int should)
	{
		long res=go(at, par, dist, should);
		if(should==n)
		{
			long sum=cost[dist];
			for(int x: g[at])
				if(x!=par)
				{
					sum+=go(x,at,Math.min(dist+1, n),n);
				}
			if(sum==res)
			{
				for(int x: g[at])
					if(x!=par)
					{
						search(x,at,Math.min(dist+1, n),n);
					}
				return ;
			}
			for(int s=0;s<n;s++)
			{
				long cur=go(at,par,dist,s);
				if(cur==res)
				{
					search(at, par, dist, s);
					return ;
				}
			}
		}
		else if(should==0)
		{
			centers.add(at);
			for(int x: g[at])
				if(x!=par)
				{
					search(x,at,1,n);
				}
		}
		else
		{
			long sum=0;
			for(int x: g[at])
				if(x!=par)
				{
					sum+=go(x, at, Math.min(dist+1, should+1),n);
				}
			int what=-1;
			for(int x: g[at])
				if(x!=par)
				{
					long cur=sum;
					cur-=go(x, at, Math.min(dist+1, should+1),n);
					cur+=go(x, at, Math.min(dist+1,n),should-1);
					cur+=cost[Math.min(dist,should)];
					if(cur==res)
					{
						what=x;
					}
				}
			for(int x: g[at])
				if(x!=par)
				{
					if(x==what)
					{
						search(x, at, Math.min(dist+1,n),should-1);
					}
					else
					{
						search(x, at, Math.min(dist+1, should+1),n);
					}
				}			
		}
	}
	long go(int at,int par,int dist,int should)
	{
		if(cached[at][dist][should]!=-1)
			return cached[at][dist][should];
		long res=inf;
		if(should==n)
		{
			long sum=cost[dist];
			for(int s=0;s<n;s++)
			{
				long cur=go(at,par,dist,s);				
				res=Math.min(res, cur);
			}
			for(int x: g[at])
				if(x!=par)
				{
					sum+=go(x,at,Math.min(dist+1, n),n);
				}
			res=Math.min(res, sum);
						
		}
		else if(should==0)
		{
			long cur=K;
			for(int x: g[at])
				if(x!=par)
				{
					cur+=go(x,at,1,n);
				}
			res=Math.min(res, cur);			
		}
		else
		{
			long sum=0;
			for(int x: g[at])
				if(x!=par)
				{
					sum+=go(x, at, Math.min(dist+1, should+1),n);
				}
			for(int x: g[at])
				if(x!=par)
				{
					long cur=sum;
					cur-=go(x, at, Math.min(dist+1, should+1),n);
					cur+=go(x, at, Math.min(dist+1,n),should-1);
					cur+=cost[Math.min(dist,should)];
					res=Math.min(res, cur);
				}
					
		}
		return cached[at][dist][should]=res;			
	}



	BufferedReader reader;
	PrintWriter writer;
	StringTokenizer stk;
	void run()throws Exception
	{
		reader=new BufferedReader(new InputStreamReader(System.in));
		stk=null;
		writer=new PrintWriter(System.out);
		solve();
		reader.close();
		writer.close();
	}
	int nextInt()throws Exception
	{
		return Integer.parseInt(nextToken());
	}
	long nextLong()throws Exception
	{	
		return Long.parseLong(nextToken());
	}
	double nextDouble()throws Exception
	{		
		return Double.parseDouble(nextToken());
	}
	String nextString()throws Exception
	{
		return nextToken();
	}
	String nextLine()throws Exception
	{
		return reader.readLine();
	}
	String nextToken()throws Exception
	{
		if(stk==null || !stk.hasMoreTokens())
		{
			stk=new StringTokenizer(nextLine());
			return nextToken();
		}
		return stk.nextToken();
	}
	
	public static void main(String[]a) throws Exception
	{	
		new E().run();

	}
	
}