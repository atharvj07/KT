import java.util.*;
import java.lang.*;
import java.io.*;
import java.math.*;
//BigInteger A;
//A= BigInteger.valueOf(54);
//ArrayList<Integer> a=new ArrayList<>();
//TreeSet<Integer> ts=new TreeSet<>();
//HashMap<Integer,Integer> hm=new HashMap<>();
//PriorityQueue<Integer> pq=new PriorityQueue<>();
public final class CF
{
    static boolean vis[];
    public static void dfs(ArrayList<ArrayList<Integer>> adj,int s)
    {
        vis[s]=true;
        for (int i = 0; i < adj.get(s).size(); i++) {
            if(!vis[adj.get(s).get(i)])
            dfs(adj,adj.get(s).get(i));
        }
    }
   public static void main(String[]args)throws IOException
	{
		//int K=(int)Math.pow(10,9)+7;
          FastReader ob=new FastReader();
          StringBuffer sb=new StringBuffer();
          //int t=ob.nextInt();
          //while(t-->0)
          {
            int n=ob.nextInt();
            int m=ob.nextInt();
            ArrayList<ArrayList<Integer>> adj=new ArrayList<>(n);
            for (int i=0;i<n;i++) {
                adj.add(new ArrayList<>());
            }
            for (int i = 0; i < m; i++) {
                int u=ob.nextInt();
                int v=ob.nextInt();
                --u;--v;
                adj.get(u).add(v);
                adj.get(v).add(u);
            }
            int d[]=new int[n];
            for (int i = 0; i < d.length; i++) {
                for(int j=0;j<adj.get(i).size();j++)
                    ++d[adj.get(i).get(j)];
            }
            int min=Integer.MAX_VALUE,minvertex=-1;
            for (int i = 0; i < d.length; i++) {
                if(min>d[i])
                {
                    min=d[i];
                    minvertex=i;
                }
            }
            ArrayList<Integer> y=adj.get(minvertex);//1 weight edges
            ArrayList<Integer> x=new ArrayList<>();//0 weight edges
            Collections.sort(y);
            boolean vis1[]=new boolean[n];
            for(int i=0;i<y.size();i++)
            vis1[y.get(i)]=true;
            vis1[minvertex]=true;
            for (int i = 0; i < n; i++) {
                if(!vis1[i])
                x.add(i);
            }
            //System.out.println(x);
            ArrayList<ArrayList<Integer>> adj1=new ArrayList<>();
            for (int i=0;i<n;i++) {
                adj1.add(new ArrayList<>());
            }
            for (int i = 0; i < x.size(); i++) {
                adj1.get(minvertex).add(x.get(i));
                adj1.get(x.get(i)).add(minvertex);
            }
            //System.out.println(adj1);
            for (int i = 0; i < y.size(); i++) {
                int u=y.get(i);
                boolean vis[]=new boolean[n];
                for(int j=0;j<adj.get(u).size();j++)
                vis[adj.get(u).get(j)]=true;
                for (int j = 0; j < vis.length; j++) {
                    if(!vis[j])
                    {
                        adj1.get(u).add(j);
                        adj1.get(j).add(u);
                    }
                }
            }
            //System.out.println(adj1);
            vis=new boolean[n];
            int c=0;
            for(int i=0;i<n;i++)
            {
                if(!vis[i])
                {
                    ++c;
                    dfs(adj1,i);
                }
            }
            sb.append((c-1));
          }
          System.out.println(sb);
	}
}
class Pair
{
	int x,y;
	Pair(int x,int y)
	{
		this.x=x;
		this.y=y;
	}
}
class PairComparator implements Comparator<Pair>
{
	public int compare(Pair a,Pair b)
	{
        return a.y-b.y;
	}
}
class FastReader {
    BufferedReader br;
    StringTokenizer st;
    public FastReader() {
        br = new BufferedReader(new InputStreamReader(System.in));
    }

    public String next() {
        while (st == null || !st.hasMoreElements()) {
            try {
                st = new StringTokenizer(br.readLine());
            } catch (IOException e)  {
                e.printStackTrace();
            }
        }
        return st.nextToken();
    }
    public String nextLine()
    {
        String s="";
        try {
        s=br.readLine();
        } catch (IOException e)  {
                e.printStackTrace();
            }
        return s;
    }
    public int nextInt() {
        return Integer.parseInt(next());
    }
    public long nextLong() {
        return Long.parseLong(next());
    }
    public double nextDouble() {
        return Double.parseDouble(next());
    }
}