import java.io.*;
import java.util.*;
import java.math.*;
import java.math.BigInteger;


public final class A
{    
	static StringBuilder ans=new StringBuilder();
	static FastReader in=new FastReader();
	static ArrayList<ArrayList<Integer>> g,tg;
	static long mod=1000000007;
	static boolean set[]; 
	static int D[],par[],N,M;
	static char G[][];
	static Pair moves[]= {new Pair(-1,0),new Pair(1,0), new Pair(0,-1), new Pair(0,1)};
	public static void main(String args[])throws IOException
	{ 	
		int T=i();
		outer : while(T-->0)
		{
			int N=i();
			long size[]=inputLong(N);
			int A[]=input(N);
			int B[]=input(N);
			long max=0,cycle=0;
			if(A[1]==B[1])
			{
				cycle=size[1]+1;
			}
			else
			{
				cycle=size[1]+Math.abs(A[1]-B[1])+1;
			}		
			max=cycle;
			for(int i=2; i<N; i++)
			{
				int a=A[i],b=B[i];
				if(a==b)
				{
					//System.out.println(size[i]);
					cycle=size[i]+1;
				}
				else
				{
					long cycle2=size[i]+Math.abs(A[i]-B[i])+1;
					long x=(size[i]-size[i-1])+2;
					int temp=Math.min(a, b);
					b=Math.max(a, b);
					a=temp;
					x+=Math.abs(a-1)+Math.abs(size[i-1]-b);
					//System.out.println(x);
					cycle+=x;
					cycle=Math.max(cycle, cycle2);
				}
				max=Math.max(max, cycle);
				//System.out.println(max+" "+cycle);
			}
			System.out.println(max);
		}

	}
	static void bfs(Pair st)
	{
		Queue<Integer> X=new LinkedList<Integer>();		
		Queue<Integer> Y=new LinkedList<Integer>();	
		X.add(st.x);
		Y.add(st.y);
		while(X.size()>0)
		{		
			int x=X.remove(),y=Y.remove();
			G[x][y]='@';
			for(Pair a:moves)
			{
				int x1=a.x+x,y1=a.y+y;
				//System.out.println("FOR--> "+x+" "+y);
				//System.out.println("x1--> "+x1+" y1--> "+y1);
				if(isValid(x1,y1))
				{
					X.add(x1);
					Y.add(y1);
				}
			}			
		}
	}
	static boolean isValid(int x,int y)
	{
		if(x<0 || x>=N || y<0 || y>=M)return false;
		if(G[x][y]=='#' || G[x][y]=='@')return false; 
		for(Pair a:moves)
		{
			int x1=x+a.x,y1=a.y+y;
			if(isValid1(x1,y1))
			{
				return false;
			}
		}
		return true;
	}
	static boolean isValid1(int x,int y)
	{
		if(x<0 || x>=N || y<0 || y>=M)return false;
		if(G[x][y]=='B')return true;
		return false;
	}

	static int find(int a)
	{
		if(par[a]<0)return a;
		return par[a]=find(par[a]);
	}
	static void union(int a,int b)
	{
		a=find(a);
		b=find(b);
		if(a!=b)
		{
			par[a]+=par[b];
			par[b]=a;
		}
	}
	static boolean isSorted(int A[])
	{
		for(int i=1; i<A.length; i++)
		{
			if(A[i]<A[i-1])return false;
		}
		return true;
	}

	static boolean isDivisible(StringBuilder X,int i,long num)
	{
		long r=0;
		for(; i<X.length(); i++)
		{
			r=r*10+(X.charAt(i)-'0');
			r=r%num;
		}
		return r==0;
	}    



	static int lower_Bound(int A[],int low,int high, int x) 
	{ 
		if (low > high) 
			if (x >= A[high]) 
				return A[high]; 

		int mid = (low + high) / 2; 

		if (A[mid] == x) 
			return A[mid]; 

		if (mid > 0 && A[mid - 1] <= x && x < A[mid]) 
			return A[mid - 1]; 

		if (x < A[mid]) 
			return lower_Bound( A, low, mid - 1, x); 

		return lower_Bound(A, mid + 1, high, x); 
	} 

	static String f(String A)
	{
		String X="";
		for(int i=A.length()-1; i>=0; i--)
		{
			int c=A.charAt(i)-'0';
			X+=(c+1)%2;
		}
		return X;
	}

	static void sort(long[] a) //check for long
	{
		ArrayList<Long> l=new ArrayList<>();
		for (long i:a) l.add(i);
		Collections.sort(l);
		for (int i=0; i<a.length; i++) a[i]=l.get(i);
	}

	static String swap(String X,int i,int j)
	{
		char ch[]=X.toCharArray();
		char a=ch[i];
		ch[i]=ch[j];
		ch[j]=a;
		return new String(ch);
	}

	static int sD(long n)  
	{  

		if (n % 2 == 0 )  
			return 2;  

		for (int i = 3; i * i <= n; i += 2) {  
			if (n % i == 0 )  
				return i;  
		}  

		return (int)n;  
	}  

	static void setGraph(int N)
	{
		set=new boolean[N+1];
		D=new int[N+1];
		//st=new Stack<Integer>();
		g=new ArrayList<ArrayList<Integer>>();
		tg=new ArrayList<ArrayList<Integer>>();
		//tg=new ArrayList<ArrayList<Integer>>();
		for(int i=0; i<=N; i++)
		{
			//tg.add(new ArrayList<Integer>());
			//D[i]=Integer.MAX_VALUE;
			g.add(new ArrayList<Integer>());
			tg.add(new ArrayList<Integer>());
		}
	}



	static  long pow(long a,long b)
	{
		long mod=1000000007;
		long pow=1;
		long x=a;
		while(b!=0)
		{
			if((b&1)!=0)pow=(pow*x)%mod;
			x=(x*x)%mod;
			b/=2;
		}
		return pow;
	}

	static long toggleBits(long x)//one's complement || Toggle bits
	{
		int n=(int)(Math.floor(Math.log(x)/Math.log(2)))+1;

		return ((1<<n)-1)^x;
	}

	static int countBits(long a)
	{
		return (int)(Math.log(a)/Math.log(2)+1);
	}

	static long fact(long N)
	{ 
		long n=2; 
		if(N<=1)return 1;
		else
		{
			for(int i=3; i<=N; i++)n=(n*i)%mod;
		}
		return n;
	}

	static int kadane(int A[])
	{
		int lsum=A[0],gsum=A[0];
		for(int i=1; i<A.length; i++)
		{
			lsum=Math.max(lsum+A[i],A[i]);
			gsum=Math.max(gsum,lsum);
		}
		return gsum;
	}

	static void sort(int[] a) {
		ArrayList<Integer> l=new ArrayList<>();
		for (int i:a) l.add(i);
		Collections.sort(l);
		for (int i=0; i<a.length; i++) a[i]=l.get(i);
	}

	static boolean isPrime(long N)
	{
		if (N<=1)  return false; 
		if (N<=3)  return true; 
		if (N%2 == 0 || N%3 == 0) return false; 
		for (int i=5; i*i<=N; i=i+6) 
			if (N%i == 0 || N%(i+2) == 0) 
				return false; 
		return true; 
	}
	static void print(char A[])
	{
		for(char c:A)System.out.print(c+" ");
		System.out.println();
	}
	static void print(boolean A[])
	{
		for(boolean c:A)System.out.print(c+" ");
		System.out.println();
	}
	static void print(int A[])
	{
		for(int a:A)System.out.print(a+" ");
		System.out.println();	
	}
	static void print(long A[])
	{
		for(long i:A)System.out.print(i+ " ");
		System.out.println();

	}
	static void print(ArrayList<Integer> A)
	{
		for(int a:A)System.out.print(a+" ");
		System.out.println();
	}

	static int i()
	{
		return in.nextInt();
	}

	static long l()
	{
		return in.nextLong();
	}

	static int[] input(int N){
		int A[]=new int[N];
		for(int i=0; i<N; i++)
		{
			A[i]=in.nextInt();
		}
		return A;
	}

	static long[] inputLong(int N)     {
		long A[]=new long[N];
		for(int i=0; i<A.length; i++)A[i]=in.nextLong();
		return A;
	}

	static long GCD(long a,long b) 
	{
		if(b==0)
		{
			return a;
		}
		else return GCD(b,a%b );
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

//Code For FastReader
//Code For FastReader
//Code For FastReader
//Code For FastReader
class FastReader
{
	BufferedReader br;
	StringTokenizer st;
	public FastReader()
	{
		br=new BufferedReader(new InputStreamReader(System.in));
	}

	String next()
	{
		while(st==null || !st.hasMoreElements())
		{
			try
			{
				st=new StringTokenizer(br.readLine());
			}
			catch(IOException e)
			{
				e.printStackTrace();
			}
		}
		return st.nextToken();
	}

	int nextInt()
	{
		return Integer.parseInt(next());
	}

	long nextLong()
	{
		return Long.parseLong(next());
	}

	double nextDouble()
	{
		return Double.parseDouble(next());
	}

	String nextLine()
	{
		String str="";
		try
		{
			str=br.readLine();
		}
		catch (IOException e)
		{
			e.printStackTrace();
		}
		return str;
	}

}