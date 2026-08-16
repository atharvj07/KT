import java.util.*;
import java.io.*;
import java.math.BigInteger;

public class Solution {

	BufferedReader in;
	PrintWriter out;
	StringTokenizer st;
	
	String nextToken() throws Exception {
		while (st == null || !st.hasMoreTokens()) st = new StringTokenizer(in.readLine());
		return st.nextToken();
	}
	
	int nextInt() throws Exception {
		return Integer.parseInt(nextToken());
	}
	
	long nextLong() throws Exception {
		return Long.parseLong(nextToken());
	}
	
	int[] gl = {0, 4, 16, 82, 6724, 50626};
	int[] gr = {0, 1, 2, 0, 3, 1};
	
	void solve() throws Exception {
		int n = nextInt();
		int ans = 0;
		for (int i = 0; i < n; i++) {
			long a = nextLong();
			if (a == 1) continue;
			long b = Math.max(0, Math.round(Math.pow(a, 1 / 4)) - 5);
			while (b * b * b * b < a) b++;
			long e = Math.max(0, Math.round(Math.sqrt(a)) - 5);
			while (e * e <= a) e++;
			e--;
			if (e < b) continue;
			int bb = 0;
			while (bb < 5 && gl[bb + 1] <= b) bb++;
			int ee = 0;
			while (ee < 5 && gl[ee + 1] <= e) ee++;
			boolean[] q = new boolean[10];
			for (int qq = bb; qq <= ee; qq++) q[gr[qq]] = true;
			int tm = 0;
			while (q[tm]) tm++;
			ans ^= tm;
		}
		if (ans == 0) out.println("Rublo"); else out.println("Furlo");
	}
	
	void run() {
		try {
			Locale.setDefault(Locale.US);
//			in = new BufferedReader(new FileReader("input.txt"));
//			out = new PrintWriter("output.txt");
			in = new BufferedReader(new InputStreamReader(System.in));
			out = new PrintWriter(System.out);
			solve();
		} catch (Exception e) {
			e.printStackTrace();
			System.exit(1);
		} finally {
			out.close();
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Solution().run();
	}

}
