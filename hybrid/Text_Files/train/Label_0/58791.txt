import java.io.BufferedReader;
import java.util.ArrayList;
import java.util.Stack;
import java.util.StringTokenizer;
import java.io.InputStreamReader;
import java.io.IOException;
 
public class codeforces {
    static node[] g ;
    static node[] G;
    static Stack<Integer> stack = new Stack<>();
    static int min ;
    static ArrayList<Integer> y;
    static long ways = 1;
    static long cost= 0;
    static long no = 1000000007;
	public static void main(String[] args) {	
     scanner in  = new scanner();
     int n = in.nextInt();
     g = new node[n+1];
     G = new node[n+1];
     for(int i = 1;i<=n;i++)
     {
    	g[i] = new node();
    	g[i].cost = in.nextInt();
    	g[i].v = i;
     }
     int m = in.nextInt();
     for(int i = 0;i<m;i++)
     {
    	 int src = in.nextInt();
    	 int to = in.nextInt();
    	 g[src].t.add(to);
     }
     for(int i = 1;i<=n;i++)
    	 if(!g[i].vis)
              dfs(g[i].v);
     for(int i = 1;i<=n;i++)
     {
    	 G[i] = new node();
    	 G[i].v = i;
    	 G[i].cost = g[i].cost;
     }
     for(int i = 1;i<=n;i++)
     {
    	 for(int j : g[i].t)
    		 G[j].t.add(i);
     }
     while(!stack.isEmpty())
     {
    	 int pop = stack.pop();
    	   if(!G[pop].vis)
    	   {
    		   min = Integer.MAX_VALUE;
    		   y = new ArrayList<>();
              rdfs(pop);
              int count = 0;
              for(int j : y)
            	  if(G[j].cost == min)
            		  count++;
              ways = ((ways%no)*(count%no))%no;
              cost+=min;
    	   }
     }
     System.out.println(cost+" "+ways);
   }
	public static void dfs(int n)
	{
		g[n].vis = true;
		for(int i : g[n].t)
		{
			if(!g[i].vis)
				dfs(g[i].v);
		}
		stack.add(n);
	}
	public static void rdfs(int n)
	{
		G[n].vis = true;
		for(int i : G[n].t)
		{
			if(!G[i].vis)
				rdfs(G[i].v);
		}
		y.add(n);
      if(G[n].cost<min)
    	  min = G[n].cost;
	}
}
class node
{
	int v;
	boolean vis = false;
	int cost;
	ArrayList<Integer> t = new ArrayList<>();
}
class scanner
{
	BufferedReader br ;
	StringTokenizer st;
	
	public scanner()
	{
		br = new BufferedReader(new InputStreamReader(System.in));
		st = null;
	}
	 public String next() {
	        while (st == null || !st.hasMoreElements()) {
	            try {
	                st = new StringTokenizer(br.readLine());
	            } catch (IOException e) {
	                e.printStackTrace();
	            }
	        }
	        return st.nextToken();
	    }
	public int nextInt()
	{
		return Integer.parseInt(next());
	}
	public long nextLong()
	{
	  return	Long.parseLong(next());
	}
}