import java.io.*;
import java.util.*;

public class Main {

	int slow(char[] s) {
		int n = s.length;
		long initMask = 0;
		int ones = 0;
		for (int i = 0; i < n; i++) {
			if (s[i] == '1') {
				initMask |= 1L << i;
				ones++;
			}
		}
		
		HashSet<Long> vis = new HashSet<>();
		ArrayDeque<Long> q = new ArrayDeque<>();
		vis.add(initMask);
		q.add(initMask);
		
		int ans = 0;
		
		while (!q.isEmpty()) {
			long now = q.poll();
			ans = Math.max(ans, ones - Long.bitCount(now));
			for (int i = 0; i < n - 2; i++) {
				if (((now >> i) & 7) == 5) {
					long newMask = now - (3L << i);
					if (!vis.contains(newMask)) {
						vis.add(newMask);
						q.add(newMask);
					}
				}
			}
		}
		
		return ans;
	}
	
	int solve(char[] s) {
		int ptr = 0;
		int n = s.length;
		int ans = 0;
		ArrayList<Integer> lst = new ArrayList<>();
		while (true) {
			lst.clear();
			while (ptr < n && s[ptr] == '0') {
				ptr++;
			}
			if (ptr == n) {
				return ans;
			}
			int curOnes = 0;
			while (ptr < n) {
				if (s[ptr] == '1') {
					curOnes++;
				} else {
					if (curOnes == 0) {
						break;
					} else {
						lst.add(curOnes);
						curOnes = 0;
					}
				}
				ptr++;
			}
			if (curOnes > 0) {
				lst.add(curOnes);
			}
			ans += go(lst);
		}
	}
	
	int go(ArrayList<Integer> lst) {
		int n = lst.size() - 1;
		if (n == 0) {
			return 0;
		}
		int[][] dp = new int[n + 1][3];
		// skip, takeL, takeR
		for (int i = 0; i < n; i++) {
			int szL = lst.get(i);
			int szR = lst.get(i + 1);
			dp[i + 1][0] = Math.max(Math.max(dp[i][0], dp[i][1]), dp[i][2]);
			dp[i + 1][1] = dp[i][0] + szL;
			if (szL > 1) {
				dp[i + 1][1] = Math.max(dp[i + 1][1], dp[i][1] + szL - 1);
			}
			
			dp[i + 1][2] = dp[i][0] + szR;
			if (szL > 1) {
				dp[i + 1][2] = Math.max(dp[i + 1][2], dp[i][1] + szR);
				dp[i + 1][2] = Math.max(dp[i + 1][2], dp[i][2] + szR - 1);
			}
		}
		
		return Math.max(Math.max(dp[n][0], dp[n][1]), dp[n][2]);
	}
	
	void submit() {
		int n = nextInt();
		char[] s = nextToken().toCharArray();
		out.println(solve(s));
//		out.println(slow(s));
	}

	void preCalc() {
		
	}

	void stress() {
		for (int tst = 0;; tst++) {
			int n = rand(1, 20);
			char[] s = new char[n];
			for (int i = 0; i < n; i++) {
				s[i] = rng.nextBoolean() ? '0' : '1';
			}
			int fast = solve(s);
			int slow = slow(s);
			if (fast != slow) {
				System.err.println(s);
				System.err.println(fast);
				System.err.println(slow);
			}
			System.err.println(tst);
		}
	}

	void test() {

	}

	Main() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		out = new PrintWriter(System.out);
		preCalc();
		submit();
//		stress();
		//test();
		out.close();
	}

	static final Random rng = new Random();

	static int rand(int l, int r) {
		return l + rng.nextInt(r - l + 1);
	}

	public static void main(String[] args) throws IOException {
		new Main();
	}

	BufferedReader br;
	PrintWriter out;
	StringTokenizer st;

	String nextToken() {
		while (st == null || !st.hasMoreTokens()) {
			try {
				st = new StringTokenizer(br.readLine());
			} catch (IOException e) {
				throw new RuntimeException(e);
			}
		}
		return st.nextToken();
	}

	String nextString() {
		try {
			return br.readLine();
		} catch (IOException e) {
			throw new RuntimeException(e);
		}
	}

	int nextInt() {
		return Integer.parseInt(nextToken());
	}

	long nextLong() {
		return Long.parseLong(nextToken());
	}

	double nextDouble() {
		return Double.parseDouble(nextToken());
	}
}
