import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;


public class Main {
    static int [][][] memo;
    static char [] s;
    static int solve(int idx, int cur, int mx, int k, int n)
	{
		if(idx == n)
			return mx == k? 1 : 0;
		if(memo[idx][cur][mx] != -1)
			return memo[idx][cur][mx];
		int ret = 0;
		if(s[idx] != 'Y')
		    ret |= solve(idx + 1, cur + 1, Math.max(mx, cur + 1), k, n);
		 if(s[idx] != 'N')
		    ret |= solve(idx + 1, 0, mx, k, n);
		return memo[idx][cur][mx] = ret;
	}
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		PrintWriter out = new PrintWriter(System.out);
        
		memo = new int[105][105][105];
		for(int i = 0; i < 105; i++)
		    for(int j = 0; j < 105; j++)
		        for(int k = 0; k < 105; k++)
		            memo[i][j][k] = -1;
		int a = sc.nextInt(), b = sc.nextInt();
		s = sc.next().toCharArray();
		int yes = 0;
		int cur = 0, mx = 0;
		
		yes |= solve(0 , 0,  0, b, a);
		out.println(yes == 1 ? "YES" : "NO");
		out.flush();
		out.close();
	}

	static boolean check(int a, int b, int tx, int ty, int px, int py)
	{
		int lx = check(a - px, tx), ly = check(b - py, ty);
		if(lx == -2 || ly == -2)
			return false;
		return  lx == -1 || ly == -1 || lx == ly;
	}

	static int check(int c, int t)
	{
		if(t == 0)
			return c == 0 ? -1 : -2;
		return 1l * c * t >= 0 && c % t == 0 ? c / t : -2;
	}

	static class Scanner
	{
		StringTokenizer st;
		BufferedReader br;

		public Scanner(InputStream s){	br = new BufferedReader(new InputStreamReader(s));}

		public String next() throws IOException
		{
			while (st == null || !st.hasMoreTokens())
				st = new StringTokenizer(br.readLine());
			return st.nextToken();
		}

		public int nextInt() throws IOException {return Integer.parseInt(next());}

		public long nextLong() throws IOException {return Long.parseLong(next());}

		public String nextLine() throws IOException {return br.readLine();}

		public double nextDouble() throws IOException { return Double.parseDouble(next()); }

		public boolean ready() throws IOException {return br.ready();}
	}
}
