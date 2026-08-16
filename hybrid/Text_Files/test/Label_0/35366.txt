/* 
 * UMANG PANCHAL
 * DAIICT
 */

import java.util.*;
import java.io.*;
import java.math.*;
import java.util.Comparator;
public class Main
{
 
	private static final Comparator<? super Integer> Comparator = null;
	static LinkedList<Integer> adj[];
	static ArrayList<Integer> adj1[];
	static int[] color,visited1;
	static boolean b[],visited[],possible;
	static int level[];
	static Map<Integer,HashSet<Integer>> s;
	static int totalnodes,colored;
	static int count[];
	static long sum[];
	static int nodes;
	static long ans=0;
	static long[] as=new long[10001];
	static long c1=0,c2=0;
	static int[] a,d,k;
	static int max=100000000;
	static long MOD = 1000000007,sm=0,m=Long.MIN_VALUE;
	static boolean[] prime=new boolean[1000005];
	static int[] levl;
    static int[] eat;
    static int price[];
    static int res[],par[],co[];
    static int result=0;
    static int[] root,size,du,dv;
    static long p=Long.MAX_VALUE;
    static int start,end,r=0;
    static boolean[] vis1,vis2;
    static long n;
  
	// --------------------My Code Starts Here----------------------
	
	public static void main(String[] args) throws IOException
	{
		in=new InputReader(System.in);
	    w=new PrintWriter(System.out);

	       int n=ni(),k=ni();
	       long d=nl();
	       long[] a=new long[n];
	       for(int i=0;i<n;i++)
	    	   a[i]=nl();
	       shuffle(a,n);
	       Arrays.sort(a);
	       int[] dp=new int[n];
	       int pos=-1;
	       for(int i=k-1;i<n;i++)
	       {
	    	   if(i!=k-1 && dp[i-k]==1)
	    		   pos=i-k;
	    	   if(a[i]-a[pos+1]<=d)
	    		   dp[i]=1;
	       }
	    if(dp[n-1]==1)
	    	w.print("YES");
	    else
	    	w.print("NO");
	  
   w.close();
   }
	

	// --------------------My Code Ends Here------------------------
     
	
	/*
	 *  PriorityQueue<Integer> pq = new PriorityQueue<Integer>(new Comparator<Integer>()
  			{
  				public int compare(Integer o1, Integer o2)
  				{
  					return Intege
  					r.compare(o2,o1);
  				}
  			});
	 * 
	 * 
	 */
	public static void shuffle(long[] a,int n)
	{
		Random r=new Random();
		for(int i=n-1;i>0;i--)
		{
			int j=r.nextInt(i);
			long t=a[j];
			a[j]=a[i];
			a[i]=t;
		}
	}
	public static void bfs1(int u)
	{
	    Queue<Integer> q=new LinkedList();
	    q.add(u);
	    visited[u]=true;
	    while(!q.isEmpty())
	    {
	    	//w.print(1);
	    	int p=q.poll();
	      for(int i=0;i<adj[p].size();i++)
	     { 
	    	  if(!visited[adj[p].get(i)])
	    	  {
	    	q.add(adj[p].get(i));
	    	visited[adj[p].get(i)]=true;
	    	  }
	    	  levl[adj[p].get(i)]=levl[p]+1;
	    	  }
	    }
	    
	}
	public static void bfs2(int u)
	{
	    Queue<Integer> q=new LinkedList();
	    q.add(u);
	    vis2[u]=true;
	    while(!q.isEmpty())
	    {
	    	int p=q.poll();
	      for(int i=0;i<adj[p].size();i++)
	     { 
	    	  if(!vis2[adj[p].get(i)])
	    	  {
	    	dv[adj[p].get(i)]=dv[p]+1;
	    	q.add(adj[p].get(i));
	    	  
	    	vis2[adj[p].get(i)]=true;
	    	  }
	    	  }
	    }
	    
	}
	 public static void buildgraph(int n)
	 {
         adj=new LinkedList[n+1];
         visited=new boolean[n];
         level=new int[n];
         par=new int[n];
         for(int i=0;i<=n;i++)
         	{
        	 adj[i]=new LinkedList<Integer>();
         	
         	}
      
	 }
	
	/*public static long kruskal(Pair[] p)
	{
		long ans=0;
		int w=0,x=0,y=0;
		for(int i=0;i<p.length;i++)
		{
			w=p[i].w;
			x=p[i].x;
			y=p[i].y;
			if(root(x)!=root(y))
			{
				ans+=w;
				union(x,y);
			}
		}
		return ans;
	}*/
	
	 static class Pair implements Comparable<Pair>
	 {
		 Long x,w;
		 Integer ind;
	        Pair(long x,long w,int ind)
	        {
	            this.x=x;
	            this.w=w;
	            this.ind=ind;
	        }
	        public int compareTo(Pair p)
	        {
	            return Long.compare(this.w,p.w);
	        }
		
	}
	 static  class npair implements Comparable<npair>
	 {
	     int a,b;
	     
	
		npair(int a,int b)
		{
			this.a=a;
			this.b=b;
			//this.index=index;
		}


		public int compareTo(npair o) {
			// TODO Auto-generated method stub
			return Integer.compare(this.a,o.a);
		}


	
		
	}
	public static int root(int i)
	{
		while(root[i]!=i)
		{
			root[i]=root[root[i]];
			i=root[i];
		}
		return i;
	}
	
	public static void init(int n)
	{
		root=new int[n+1];
		for(int i=1;i<=n;i++)
			root[i]=i;
	}
	public static void union(int a,int b)
	{
	    int root_a=root(a);	
	    int root_b=root(b);
	    root[root_a]=root_b;
	   // size[root_b]+=size[root_a];
	}


	
	public static boolean isPrime(long n)
	{
	    // Corner cases
	    if (n <= 1)  return false;
	    if (n <= 3)  return true;
	 
	    // This is checked so that we can skip 
	    // middle five numbers in below loop
	    if (n%2 == 0 || n%3 == 0)
	    	return false;
	 
	    for (long i=5; i*i<=n; i=i+6)
	        if (n%i == 0 || n%(i+2) == 0)
	           return false;
	 
	    return true;
	}
	

	
	public static String ns()
	{
		return in.nextLine();
	}
	public static int ni()
	{
		return in.nextInt();
	}
	public static long nl()
	{
		return in.nextLong();
	}
	public static int[] na(int n)
	{
		int[] a=new int[n];
		for(int i=0;i<n;i++)
		a[i]=ni();
		return a;
	}
	public static long[] nla(int n)
	{
		long[] a=new long[n];
		for(int i=0;i<n;i++)
		a[i]=nl();
		return a;
	}
	public static void sieve()
	    {
	       int n=prime.length;
	        for(int i=0;i<n;i++)
	            prime[i] = true;
	         
	        for(int p = 2; p*p <=n; p++)
	        {
	            if(prime[p] == true)
	            {
	                for(int i = p*2; i <n; i += p)
	                    prime[i] = false;
	            }
	        }
	    }

  public static String rev(String s)
	{
		StringBuilder sb=new StringBuilder(s);
		sb.reverse();
		return sb.toString();
	}
	static long lcm(long a, long b)
	{
	    return a * (b / gcd(a, b));
	}
	static long gcd(long a, long b)
	{
	    while (b > 0)
	    {
	        long temp = b;
	        b = a % b; // % is remainder
	        a = temp;
	    }
	    return a;
	}
	static InputReader in;
	static PrintWriter w;
static class InputReader 
{
 
private final InputStream stream;
private final byte[] buf = new byte[8192];
private int curChar, snumChars;
private SpaceCharFilter filter;
 
public InputReader(InputStream stream)
{
  this.stream = stream;
}
 
public int snext()
{
  if (snumChars == -1)
    throw new InputMismatchException();
  if (curChar >= snumChars)
  {
    curChar = 0;
    try 
    {
      snumChars = stream.read(buf);
    }
    catch (IOException e)
    {
      throw new InputMismatchException();
    }
    if (snumChars <= 0)
      return -1;
  }
  return buf[curChar++];
}
 
public int nextInt() 
{
  int c = snext();
  while (isSpaceChar(c)) 
  {
    c = snext();
  }
  int sgn = 1;
  if (c == '-')
  {
    sgn = -1;
    c = snext();
  }
  int res = 0;
  do
  {
    if (c < '0' || c > '9')
      throw new InputMismatchException();
    res *= 10;
    res += c - '0';
    c = snext();
  }
  while (!isSpaceChar(c));
  return res * sgn;
}
 
public long nextLong() 
{
  int c = snext();
  while (isSpaceChar(c)) 
  {
    c = snext();
  }
  int sgn = 1;
  if (c == '-')
  {
    sgn = -1;
    c = snext();
  }
  long res = 0;
  do
  {
    if (c < '0' || c > '9')
      throw new InputMismatchException();
    res *= 10;
    res += c - '0';
    c = snext();
  }
  while (!isSpaceChar(c));
  return res * sgn;
}	    
public String readString() 
{
  int c = snext();
  while (isSpaceChar(c)) 
  {
    c = snext();
  }
  StringBuilder res = new StringBuilder();
  do
  {
    res.appendCodePoint(c);
    c = snext();
  }
  while (!isSpaceChar(c));
  return res.toString();
}
 
public String nextLine() 
{
  int c = snext();
  while (isSpaceChar(c))
    c = snext();
  StringBuilder res = new StringBuilder();
  do
  {
    res.appendCodePoint(c);
    c = snext();
  }
  while (!isEndOfLine(c));
  return res.toString();
}
 
public boolean isSpaceChar(int c)
{
  if (filter != null)
    return filter.isSpaceChar(c);
  return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
}
 
private boolean isEndOfLine(int c) 
{
  return c == '\n' || c == '\r' || c == -1;
}
 
public interface SpaceCharFilter
{
  public boolean isSpaceChar(int ch);
}
}
	
}