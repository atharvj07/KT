import java.io.*;
import java.util.*;

public class B{

	static int N=(int)1e6+10;
	static ArrayList<Integer> primes;
	static void sieve() {
		boolean []isPrime=new boolean[N];
		primes=new ArrayList();
		Arrays.fill(isPrime, true);
		for(int i=2;i<N;i++)
			if(isPrime[i]) {
				primes.add(i);
				for(int j=i+i;j<N;j+=i)
					isPrime[j]=false;
			}
	}
	public static void main(String[] args) throws IOException {
		Scanner sc=new Scanner();
		PrintWriter out=new PrintWriter(System.out);
		long n=sc.nextLong(),b=sc.nextLong();
		long ans=(long)1e18;;
		sieve();
		
		for(int p:primes) {
			if(b%p!=0)
				continue;
			
			int cnt=0;
			while(b%p==0) {
				b/=p;
				cnt++;
			}
			long curr=0;
			for(long d=p;d<=n;) {
				curr+=n/d;
				if(d>n/p)
					break;
				else
					d*=p;
				
				
			}
			
			ans=Math.min(ans, curr/cnt);
		}
		if(b!=1) {
			int cnt=0;
			long p=b;
			while(b%p==0) {
				b/=p;
				cnt++;
			}
			long curr=0;
			for(long d=p;d<=n;) {
				curr+=n/d;
				if(d>n/p)
					break;
				else
					d*=p;
				
				
			}
			ans=Math.min(ans, curr/cnt);
		}
		out.println(ans);
		
		
		out.close();

	}
	static class Scanner
	{
		BufferedReader br;
		StringTokenizer st;
		Scanner(){
			br=new BufferedReader(new InputStreamReader(System.in));
		}
		Scanner(String fileName) throws FileNotFoundException{
			br=new BufferedReader(new FileReader(fileName));
		}
		String next() throws IOException {
			while(st==null || !st.hasMoreTokens())
				st=new StringTokenizer(br.readLine());
			return st.nextToken();
		}
		String nextLine() throws IOException {
			return br.readLine();
		}
		int nextInt() throws IOException{
			return Integer.parseInt(next());
		}
		long nextLong()  throws NumberFormatException, IOException {
			return Long.parseLong(next());
		}
		double nextDouble() throws NumberFormatException, IOException {
			return Double.parseDouble(next());
		}
	}
}