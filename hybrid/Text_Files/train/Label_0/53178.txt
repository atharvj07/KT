import java.io.*;
import java.util.*;
import java.math.*;
import java.util.concurrent.*;

class Main
{
    static BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
	static FastScanner sc=new FastScanner(br);
    static PrintWriter out=new PrintWriter(System.out);
	static Random rnd=new Random();
	static int[] parent,size;
	
	static int find(int u)
	{
		if(parent[u]==u)
		{
			return u;
		}
		
		else
		{
			parent[u]=find(parent[u]);
			
			return parent[u];
		}
	}
	
	static void merge(int u,int v)
	{
		int x=find(u),y=find(v);
		
		if(x!=y)
		{
			parent[y]=x;
			
			size[x]=size[x]+size[y];
			
			size[y]=0;
		}
	}
	
    public static void main(String args[]) throws Exception
    {
		int n=sc.nextInt(),m=sc.nextInt();char[][] a=new char[n][];
		
		int[] cnt=new int[26];
		
		for(int i=0;i<n;i++)
		{
			a[i]=sc.next().toCharArray();
			
			for(int j=0;j<m;j++)
			{
				cnt[a[i][j]-'a']++;
			}
		}
		
		List<Integer> list=new ArrayList<>();
		
		parent=new int[n*m];size=new int[n*m];
		
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				parent[i*m+j]=(i*m)+j;
				
				size[i*m+j]=1;
			}
		}
		
		for(int i=0;i<n;i++)
		{
			for(int j=0,k=m-1;j<k;j++,k--)
			{
				merge(i*m+j,i*m+k);
			}
		}
		
		for(int j=0;j<m;j++)
		{
			for(int i=0,k=n-1;i<k;i++,k--)
			{
				merge(i*m+j,k*m+j);
			}
		}
		
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				if(find(i*m+j)==i*m+j)
				{
					list.add(size[i*m+j]);
				}
			}
		}
		
		Collections.sort(list);boolean ans=true;
		
	//	out.println(list);
		
		for(int i=list.size()-1;i>=0;i--)
		{
			int max=-1,ch=-1;
			
			for(int j=0;j<26;j++)
			{
				if(cnt[j]>max)
				{
					max=cnt[j];ch=j;
				}
			}
			
			if(max>=list.get(i))
			{
				cnt[ch]-=list.get(i);
			}
			else
			{
				ans=false;break;
			}
		}
		
		out.println(ans?"Yes":"No");out.close();
    }
}
class FastScanner
{
    BufferedReader in;
    StringTokenizer st;

    public FastScanner(BufferedReader in) {
        this.in = in;
    }
	
    public String nextToken() throws Exception {
        while (st == null || !st.hasMoreTokens()) {
            st = new StringTokenizer(in.readLine());
        }
        return st.nextToken();
    }
	
	public String next() throws Exception {
		return nextToken().toString();
	}
	
    public int nextInt() throws Exception {
        return Integer.parseInt(nextToken());
    }

    public long nextLong() throws Exception {
        return Long.parseLong(nextToken());
    }

    public double nextDouble() throws Exception {
        return Double.parseDouble(nextToken());
    }
}