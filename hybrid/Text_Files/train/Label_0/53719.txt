/**
 * @author prakhar28
 *
 */
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Main{
	
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
            byte[] buf = new byte[200005]; // line length+1
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
	
	static class FastScanner {

	    private final BufferedReader bufferedReader;
	    private StringTokenizer stringTokenizer;

	    public FastScanner() {
	        bufferedReader = new BufferedReader(new InputStreamReader(System.in));
	    }

	    public String next() {
	        while (stringTokenizer == null || !stringTokenizer.hasMoreElements()) {
	            try {
	                stringTokenizer = new StringTokenizer(bufferedReader.readLine());
	            } catch (IOException e) {
	                throw new RuntimeException("Can't read next value", e);
	            }
	        }
	        return stringTokenizer.nextToken();
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

	    public String nextLine(){
	        String str = "";
	        try {
	            str = bufferedReader.readLine();
	        } catch (IOException e) {
	            e.printStackTrace();
	        }
	        return str;
	    }
	}
	
	static void closeall() throws IOException{
		printWriter.close();
		sc.close();
		in.close();
	}
	static Scanner sc = new Scanner(System.in);
	static Reader in = new Reader();
	static FastScanner fastScanner = new FastScanner();
	static PrintWriter printWriter = new PrintWriter(new BufferedOutputStream(System.out));
	static BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
	static long INF = (long)(1e18);

	
	int V,E;
	ArrayList<Integer> adj[];
	ArrayList<Integer> path;
	Main(){
	}
	Main(int v,int e){
		V=v;
		E=e;
		adj=new ArrayList[v];
		path = new ArrayList<>();
		for(int i=0;i<v;i++)
			adj[i] = new ArrayList<>();
	}
	void addEdge(int u,int v){
		adj[u].add(v);
		adj[v].add(u);
	}
	
	
	static long power(long a,long k)
	{
		long m = 1000000007;
	    long ans=1;
	    long tmp=a%m;
	    while(k>0)
	    {
	        if(k%2==1)
	        	ans=ans*tmp%m;
	        tmp=tmp*tmp%m;
	        k>>=1;
	    }
	    return ans;
	}
	
	static class Pair /*implements Comparable<Pair>*/{
		long F,S;
		Pair(long x,long y){
			F = x;
			S = y;
		}
		/*public int compareTo(Pair ob){
			return this.num-ob.num;
		}*/
		
	}
	static long gcd(long a,long b) {
		if(a<b) {
			long t = a;
			a = b;
			b = t;
		}
		long r = a%b;
		if(r==0)
			return b;
		return gcd(b,r);
	}
	
	static int lower_bound(int[] a,int low,int high,int val) {
		while(low!=high) {
			int mid = (low+high)/2;
			if(a[mid]<val)
				low=mid+1;
			else
				high=mid;
		}
		return low;
	}
	
	static int max(int a,int b) {
		return (int)Math.max(a, b);
	}
	static long max(long a,long b) {
		return (long)Math.max(a, b);
	}
	static long min(long a,long b) {
		if(a<b)
			return a;
		return b;
	}
	static long mod = 1000000007;
	
	public static void main(String args[])throws IOException{
		Reader in = new Reader();
		int n = in.nextInt();
		int k = in.nextInt();
		String s = in.readLine();
		s = in.readLine();
		//printWriter.println(s);
		int[][] dp = new int[n][2*k+1];
		char c[] = s.toCharArray();
		if(c[0]=='L')
			dp[0][k-1]=1;
		else if(c[0]=='W')
			dp[0][k+1]=1;
		else if(c[0]=='D')
			dp[0][k]=1;
		else {
			dp[0][k-1]=1;
			dp[0][k]=1;
			dp[0][k+1]=1;
		}
		for(int i=1;i<n;i++) {
			for(int j=0;j<=2*k;j++) {
				if(dp[i-1][j]<=0)
					continue;
				if(c[i]=='D')
					dp[i][j]=1;
				else if(c[i]=='L') {
					if(j-1>=0)
						dp[i][j-1]=1;
				}
				else if(c[i]=='W') {
					if(j+1<=2*k)
						dp[i][j+1]=1;
				}
				else {
					if(j-1>=0)
						dp[i][j-1]=1;
					if(j+1<=2*k)
						dp[i][j+1]=1;
					dp[i][j]=1;
				}
			}
			if(i<n-1) {
			if(dp[i][2*k]==1)
				dp[i][2*k]=-1;
			if(dp[i][0]==1)
				dp[i][0]=-1;}
		}
		if(dp[n-1][2*k]!=1 && dp[n-1][0]!=1)
			printWriter.println("NO");
		else if(dp[n-1][2*k]==1){
			Stack<Character> stack = new Stack<>();
			int p = 2*k;
			for(int i=n-1;i>=0;i--) {
				if(c[i]=='D') 
					stack.push(c[i]);
				else if(c[i]=='W') {
					stack.push(c[i]);
					p--;
				}
				else if(c[i]=='L') {
					stack.push(c[i]);
					p++;
				}
				else if(c[i]=='?' && i>0) {
					if(dp[i-1][p]==1) 
						stack.push('D');
					else if(p-1>=0 && dp[i-1][p-1]==1) {
						stack.push('W');
						p--;
					}
					else {
						stack.push('L');
						p++;
					}
				}
				else{
					if(p==k-1)
						stack.push('L');
					if(p==k)
						stack.push('D');
					if(p==k+1)
						stack.push('W');
				}
			}
			Stack<Character> b = (Stack<Character>) stack.clone();
			int cnt = 0;
			while(!b.isEmpty()) {
				char a = b.pop();
				if(a=='L')
					cnt--;
				if(a=='W')
					cnt++;
				if((cnt==-k || cnt==k) && !b.isEmpty()) {
					cnt=-12345;
					break;
				}
			}
			if(cnt==-12345)
				printWriter.println("NO");
			else {

				while(!stack.isEmpty())
					printWriter.print(stack.pop());
			}
			
		}
		else if(dp[n-1][0]==1){
			Stack<Character> stack = new Stack<>();
			int p = 0;
			for(int i=n-1;i>=0;i--) {
				if(c[i]=='D') 
					stack.push(c[i]);
				else if(c[i]=='W') {
					stack.push(c[i]);
					p--;
				}
				else if(c[i]=='L') {
					stack.push(c[i]);
					p++;
				}
				else if(c[i]=='?' && i>0) {
					if(dp[i-1][p]==1) 
						stack.push('D');
					else if(p-1>=0 && dp[i-1][p-1]==1) {
						stack.push('W');
						p--;
					}
					else {
						stack.push('L');
						p++;
					}
				}
				else{
					if(p==k-1)
						stack.push('L');
					if(p==k)
						stack.push('D');
					if(p==k+1)
						stack.push('W');
				}
			}
			Stack<Character> b = (Stack<Character>) stack.clone();
			int cnt = 0;
			while(!b.isEmpty()) {
				char a = b.pop();
				if(a=='L')
					cnt--;
				if(a=='W')
					cnt++;
				if((cnt==-k || cnt==k) && !b.isEmpty()) {
					cnt=-12345;
					break;
				}
			}
			if(cnt==-12345)
				printWriter.println("NO");
			else {

				while(!stack.isEmpty())
					printWriter.print(stack.pop());
			}
			
		}
		closeall();
	}
} 