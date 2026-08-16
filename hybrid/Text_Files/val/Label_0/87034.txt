//package CF;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class A {

	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		PrintWriter out = new PrintWriter(System.out);
		int n = sc.nextInt();
		a = new int[n];
		for (int i = 0; i < a.length; i++) {
			a[i] = sc.nextInt();
		}
		boolean[] prime = new boolean[1000];
		Arrays.fill(prime, true);
		prime[0] = prime[1] = false;
		prm = new ArrayList<>();
		for (int i = 2; i < prime.length; i++) {
			if (prime[i]) {
				prm.add(i);
				for (int j = i * i; j < prime.length; j += i) {
					prime[j] = false;
				}
			}
		}
		idx = new int[100001]; // idx[i] = the index of the greatest value in []
								// dp of any multiple of i
		dp = new int[n];
		Arrays.fill(idx, -1);
		Arrays.fill(dp, 1);
		id(0, true);
		for (int i = 1; i < dp.length; i++) {
			int id = id(i, false);
			if (id > -1)
				dp[i] = dp[id] + 1;
			id(i, true);
			// System.out.println(Arrays.toString(dp));
//			System.out.println(Arrays.toString(Arrays.copyOf(idx, 10)));
		}
		int ans = 0;
		for (int i = 0; i < dp.length; i++) {
			ans = Math.max(ans, dp[i]);
		}
		out.println(ans);
		out.flush();
		out.close();
	}

	static ArrayList<Integer> prm;
	static int[] dp, idx, a;

	static int id(int i, boolean update) {
		int p = 0, prim = 0, tmp = a[i];
		int id = update ? i : -1;
		while (p < prm.size()) {
			prim = prm.get(p++);
			if (tmp % prim == 0) {
				if (update) {
					if (idx[prim] == -1 || dp[id] >= dp[idx[prim]])
						idx[prim] = id;
				} else {
					if (id == -1 || idx[prim] != -1 && dp[idx[prim]] >= dp[id])
						id = idx[prim];
				}
			}
			while (tmp % prim == 0) {
				tmp /= prim;
			}
		}
		if (tmp > 1) {
			if (!update && (id == -1 || idx[tmp] != -1 && dp[idx[tmp]] >= dp[id])) {
				id = idx[tmp];
			} else if (update && (idx[tmp] == -1 || dp[id] >= dp[idx[tmp]]))
				idx[tmp] = id;
		}
		// System.out.println(id);
		return id;
	}

	static class Scanner {
		BufferedReader bf;
		StringTokenizer st;

		public Scanner(InputStream i) {
			bf = new BufferedReader(new InputStreamReader(i));

		}

		public String next() throws IOException {
			while (st == null || !st.hasMoreTokens())
				st = new StringTokenizer(bf.readLine());
			return st.nextToken();
		}

		public int nextInt() throws NumberFormatException, IOException {
			return Integer.parseInt(next());
		}
	}
}