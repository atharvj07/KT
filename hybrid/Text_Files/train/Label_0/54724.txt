import java.awt.Point;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class C {
	static final int MAX = (int)5e5+10;
	static int mod = (int)1e9+7;
	static long [] fac, facInv;
	public static void main(String[] args) throws NumberFormatException, IOException {
		Scanner sc = new Scanner(System.in);
		PrintWriter out = new PrintWriter(System.out);
		fac = new long[MAX];
		facInv = new long[MAX];
		fac[0] = 1;
		facInv[0] = 1;
		for (int i = 1; i < facInv.length; ++i) {
			fac[i] = fac[i-1]*i;
			fac[i] %= mod;
			facInv[i] = modPow(fac[i], mod-2, mod);
		}
		int h = sc.nextInt(), w = sc.nextInt(), n = sc.nextInt();
		Point [] obs = new Point[n];
		for (int i = 0; i < obs.length; ++i) {
			obs[i] = new Point(sc.nextInt(), sc.nextInt());
		}
		Arrays.sort(obs, new Comparator<Point>() {

			@Override
			public int compare(Point o1, Point o2) {
				// TODO Auto-generated method stub
				return o1.x == o2.x?o1.y - o2.y:o1.x - o2.x;
			}
		});
		long [] ways = new long[n];
		for (int i = 0; i < n; ++i) {
			ways[i] = ncr(obs[i].x + obs[i].y - 2, obs[i].x-1);
			for (int j = 0; j < i; ++j) {
				int dx = obs[i].x - obs[j].x;
				int dy = obs[i].y - obs[j].y;
				if(dx < 0 || dy < 0) continue;
				ways[i] = (ways[i] - ways[j] * ncr(dx+dy, dx) % mod + mod) % mod;
			}
		}
		long ans = ncr(h+w-2, h-1);
		for (int i = 0; i < n; ++i) {
			int dx = h - obs[i].x;
			int dy = w - obs[i].y;
			ans = (ans - ways[i] * ncr(dx+dy, dx) % mod + mod) % mod;
		}
		out.println(ans);
		out.flush();
		out.close();
	}
	static long ncr(int n, int k){
		return fac[n] * facInv[k] % mod * facInv[n-k] % mod;
	}
	static long modPow(long a, int e, int mod)	// O(log e)
	{
		a %= mod;
		long res = 1;
		while(e > 0)
		{
			if((e & 1) == 1)
				res = (res * a) % mod;
			a = (a * a) % mod;
			e >>= 1;
		}
		return res;
	}
	static class Scanner {
		BufferedReader br;
		StringTokenizer st;

		public Scanner(InputStream is) {
			br = new BufferedReader(new InputStreamReader(is));

		}

		public String next() throws IOException {
			while (st == null || !st.hasMoreTokens()) {
				st = new StringTokenizer(br.readLine());
			}
			return st.nextToken();
		}

		public int nextInt() throws NumberFormatException, IOException {
			return Integer.parseInt(next());
		}
		public long nextLong() throws NumberFormatException, IOException {
			return Long.parseLong(next());
		}
	}
}
