
import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Main{
	
	String INPUT = "./data/judge/201709/A2164.txt";
	
	public static void main(String[] args) throws IOException {
		new Main().run();
	}
	
	static final int MOD = 1000003;
	static final int MAX_N = 1000 + 16;
	
	
	long[] inv = new long[MAX_N];
	int[][] dp_a = new int[MAX_N][MAX_N];
	int[][] dp_b = new int[MAX_N][MAX_N];
	int[] dp = new int[MAX_N];
	
	void init_inverse(){
		inv[1] = 1;
		for (int i = 2; i < MAX_N; ++i){
			inv[i] = (MOD - (MOD / i) * inv[MOD % i] % MOD) % MOD; 
		}
	}
	
	class GCD{
		int d;
		int x;
		int y;
		public GCD(int d, int x, int y){
			this.d = d;
			this.x = x;
			this.y = y;
		}
	}
	
	GCD extgcd(int a, int b){
		if (b == 0){
			return new GCD(a, 1, 0);
		}
		else{
			GCD p   = extgcd(b, a % b);
			GCD ans = new GCD(0, 0, 0);
			ans.d = p.d;
			ans.x = p.y;
			ans.y = p.x - (a / b) * p.y;
			return ans;
		}
	}
	
	long mod_inverse(int a, int m){
		GCD p = extgcd(a, m);
		if (p.d != 1) return -1;
		return (p.x % m + m) % m;
	}
	
	void DP()
	{
		dp_a = new int[MAX_N][MAX_N];
		dp_b = new int[MAX_N][MAX_N];
		dp   = new int[MAX_N];
		
		int a_sum = 1;
		int b_sum = 0;
		if (K >= N)
	    {
	        K = N - 1;
	        all = 2;
	    }
		
	    dp_a[1][1] = 1;
	    dp_b[1][1] = 0;
	 
	    for (int i = 2; i <= N; i++)
	    {
	        dp_a[i][1] = b_sum; // ??\B?????´??\A????°????????????´?????????A
	        dp_b[i][1] = a_sum; // ??\A?????´??\A????°????????????´?????????B
	        
	        int sum = a_sum + b_sum;
	        a_sum = sum - a_sum;
	        b_sum = sum - a_sum;
	        for (int j = 2; j <= K; j++)
	        {
	            dp_a[i][j] = dp_a[i - 1][j - 1];        // ??¨????°???????A
	            a_sum = (a_sum + dp_a[i][j]) % MOD;
	            dp_b[i][j] = dp_b[i - 1][j - 1];        // ??¨????°???????B
	            b_sum = (b_sum + dp_b[i][j]) % MOD;
	        }
	    }
	 
	    // ???????????????dp_b[i][1~k]??????????¶?dp[i]?????????????°???????????°????????????????????????????????¶????k
	    for (int i = 1; i <= N; i++)
	    {
	        for (int j = 1; j <= K; j++)
	        {
	            dp[i] += dp_b[i][j];
	            dp[i] %= MOD;
	        }
	    }
	 
	    // ????????\A?????´?????????????°?dp_b??????????±??????\
	    for (int i = 1; i <= N; i++)
	    {
	        for (int j = 1; j < K; j++)
	        {
	            dp_b[i][j + 1] += dp_b[i][j];
	            dp_b[i][j + 1] %= MOD;
	        }
	    }
	 
	    // ???????????¢???p???A?????£???????°????A???????¶????k-p?????????dp_b[i-p][0~k-p]???????????????
	    for (int i = 1; i <= N; i++)
	    {
	        for (int p = 1; p <= Math.min(i, K); p++)
	        {
	            dp[i] += dp_b[i - p][K - p];
	            dp[i] %= MOD;
	        }
	    }
	}
	
	int gcd(int a, int b){
		if (b == 0) return a;
		else return gcd(b, a % b);
	}
	
	int N;
	int K;
	
	long ans;
	long all;
	void solve() {
		
		init_inverse();
		
		while (true){
			N = ni();
			K = ni();
			
			if (N + K == 0) break;
			
			ans = 0;
			all = 0;
			
			DP();
			
			for (int i = 0; i < N; ++i){
				ans += 2 * dp[gcd(i, N)];
				ans %= MOD;
			}
			ans = (ans * inv[N]) % MOD;
			out.println(ans + all);
		}
	}

	FastScanner in;
	PrintWriter out;
	
	void run() throws IOException {
		boolean oj;
		try {
			oj = ! System.getProperty("user.dir").equals("F:\\java_workspace\\leetcode");
		} catch (Exception e) {
			oj = System.getProperty("ONLINE_JUDGE") != null;
		}
		
		InputStream is = oj ? System.in : new FileInputStream(new File(INPUT));
		in = new FastScanner(is);
		out = new PrintWriter(System.out);
		long s = System.currentTimeMillis();
		solve();
		out.flush();
		if (!oj){
			System.out.println("[" + (System.currentTimeMillis() - s) + "ms]");
		}
	}
	
	public boolean more(){
		return in.hasNext();
	}
	
	public int ni(){
		return in.nextInt();
	}
	
	public long nl(){
		return in.nextLong();
	}
	
	public double nd(){
		return in.nextDouble();
	}
	
	public String ns(){
		return in.nextString();
	}
	
	public char nc(){
		return in.nextChar();
	}
	
	class FastScanner {
		BufferedReader br;
		StringTokenizer st;
		boolean hasNext;

		public FastScanner(InputStream is) throws IOException {
			br = new BufferedReader(new InputStreamReader(is));
			hasNext = true;
		}

		public String nextToken() {
			while (st == null || !st.hasMoreTokens()) {
				try {
					st = new StringTokenizer(br.readLine());
				} catch (Exception e) {
					hasNext = false;
					return "##";
				}
			}
			return st.nextToken();
		}
		
		String next = null;
		public boolean hasNext(){
			next = nextToken();
			return hasNext;
		}

		public int nextInt() {
			if (next == null){
				hasNext();
			}
			String more = next;
			next = null;
			return Integer.parseInt(more);
		}

		public long nextLong() {
			if (next == null){
				hasNext();
			}
			String more = next;
			next = null;
			return Long.parseLong(more);
		}

		public double nextDouble() {
			if (next == null){
				hasNext();
			}
			String more = next;
			next = null;
			return Double.parseDouble(more);
		}
		
		public String nextString(){
			if (next == null){
				hasNext();
			}
			String more = next;
			next = null;
			return more;
		}
		
		public char nextChar(){
			if (next == null){
				hasNext();
			}
			String more = next;
			next = null;
			return more.charAt(0);
		}
	}
}