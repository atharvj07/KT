import java.util.*;
import java.io.*;

public class Main {
	public static void main(String args[]) {new Main().run();}

	FastReader in = new FastReader();
	PrintWriter out = new PrintWriter(System.out);
	void run(){
		work();
		out.flush();
	}
	long mod=1000000007;
	long gcd(long a,long b) {
		return a==0?b:b>=a?gcd(b%a,a):gcd(b,a);
	}
	void work() {
		long n=nl(),H=nl();
		long v=(1+H)*H/2;
		if(v*2<0||(long)Math.sqrt(2*v)!=H||v>=n) {
			long l=1,r=H;
			while(l<r) {
				long m=(l+r)/2;
				long v2=(1+m)*m/2;
				if(v2*2<0||(long)Math.sqrt(2*v2)!=m||v2>=n) {
					r=m;
				}else {
					l=m+1;
				}
			}
			out.println(l);
		}else {
			long l=H,r=99999999999L;//最大峰值
			while(l<r) {
				long m=(l+r)/2;
				long v1=(H+m)*(m-H+1)/2;
				long v2=(m)*(m-1)/2;
				long v3=v1+v2;
				if(v1*2/(H+m)!=(m-H+1)||v2*2<0||(long)Math.sqrt(v2*2)!=m-1||v3-v2!=v1||v3>=n) {
					r=m;
				}else {
					l=m+1;
				}
			}
			long ret=l-H+1+l-1;
			if((H+l-1)*(l-H)/2+(1+l-1)*(l-1)/2>=n)ret--;//最大峰值去掉
			out.println(ret);
		}
	}
	
	
	
	
	//input
	private ArrayList<Integer>[] ng(int n, int m) {
		ArrayList<Integer>[] graph=(ArrayList<Integer>[])new ArrayList[n];
		for(int i=0;i<n;i++) {
			graph[i]=new ArrayList<>();
		}
		for(int i=1;i<=m;i++) {
			int s=in.nextInt()-1,e=in.nextInt()-1;
			graph[s].add(e);
			graph[e].add(s);
		}
		return graph;
	}

	private int ni() {
		return in.nextInt();
	}
	
	private long nl() {
		return in.nextLong();
	}
	
	private long[] na(int n) {
		long[] A=new long[n];
		for(int i=0;i<n;i++) {
			A[i]=in.nextLong();
		}
		return A;
	}
}	

class FastReader
{
	BufferedReader br;
	StringTokenizer st;

	public FastReader()
	{
		br=new BufferedReader(new InputStreamReader(System.in));
	}


	public String next() 
	{
		while(st==null || !st.hasMoreElements())//回车，空行情况
		{
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
		return Long.parseLong(next());
	}
}