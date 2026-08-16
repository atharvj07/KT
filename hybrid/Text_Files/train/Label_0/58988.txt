import java.io.*;
import java.util.*;

public class C {

	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner();
		PrintWriter out = new PrintWriter(System.out);
		int n = sc.nextInt(), S = sc.nextInt(), q = sc.nextInt();
		BitSet[] switches = new BitSet[S];
		for (int i = 0; i < S; i++) {
			switches[i] = new BitSet(n);
			int sz = sc.nextInt();
			while (sz-- > 0)
				switches[i].set(sc.nextInt() - 1);

		}
		HashMap<Long, Integer> map = new HashMap();
		int set_half = Math.min(20, S);
		int loop_half = S - set_half;
		BitSet[] loop_map = new BitSet[1 << loop_half];

		for (int msk = 0; msk < 1 << loop_half; msk++) {
			BitSet curr = new BitSet(n);
			for (int i = 0; i < loop_half; i++)
				if ((msk & 1 << i) > 0)
					curr.xor(switches[i]);
			loop_map[msk] = curr;

		}
		for (int msk = 0; msk < 1 << set_half; msk++) {
			BitSet curr = new BitSet(n);
			for (int i = 0; i < set_half; i++)
				if ((msk & 1 << i) > 0)
					curr.xor(switches[i + loop_half]);
			long h = curr.hash();
			Integer val = map.get(h);
			if (val == null || val > Integer.bitCount(msk))
				map.put(h, Integer.bitCount(msk));

		}
		while (q-- > 0) {
			BitSet query = new BitSet(n);
			int sz = sc.nextInt();
			while (sz-- > 0)
				query.set(sc.nextInt() - 1);
			int ans = 100;
			for (int msk = 0; msk < 1 << loop_half; msk++) {
				BitSet needed = BitSet.xor(query, loop_map[msk], n);
				long needed_hash = needed.hash();
				ans = Math.min(ans, Integer.bitCount(msk) + map.getOrDefault(needed_hash, 100));
			}
			out.println(ans == 100 ? -1 : ans);

		}
		out.close();

	}

	static class BitSet implements Comparable<BitSet> {
		long[] msks;

		BitSet(int n) {
			msks = new long[(n + 63 - 1) / 63];
		}

		long hash() {
			long h = 0;
			for (long x : msks)
				h = h * 239017239 + x;
			return h;
		}

		void set(int idx) {
			int bit = idx % 63;
			msks[idx / 63] |= 1L << bit;
		}

		void or(BitSet other) {
			for (int i = 0; i < msks.length; i++)
				msks[i] |= other.msks[i];
		}

		void xor(BitSet other) {
			for (int i = 0; i < msks.length; i++)
				msks[i] ^= other.msks[i];
		}

		static BitSet xor(BitSet a, BitSet b, int n) {
			BitSet ans = new BitSet(n);
			for (int i = 0; i < a.msks.length; i++)
				ans.msks[i] = a.msks[i] ^ b.msks[i];
			return ans;
		}

		@Override
		public int compareTo(BitSet o) {
			for (int i = 0; i < msks.length; i++)
				if (msks[i] != o.msks[i])
					return Long.compare(msks[i], o.msks[i]);
			return 0;
		}
	}

	static class Scanner {
		BufferedReader br;
		StringTokenizer st;

		Scanner() {
			br = new BufferedReader(new InputStreamReader(System.in));
		}

		Scanner(String fileName) throws FileNotFoundException {
			br = new BufferedReader(new FileReader(fileName));
		}

		String next() throws IOException {
			while (st == null || !st.hasMoreTokens())
				st = new StringTokenizer(br.readLine());
			return st.nextToken();
		}

		String nextLine() throws IOException {
			return br.readLine();
		}

		int nextInt() throws IOException {
			return Integer.parseInt(next());
		}

		long nextLong() throws NumberFormatException, IOException {
			return Long.parseLong(next());
		}

		double nextDouble() throws NumberFormatException, IOException {
			return Double.parseDouble(next());
		}

		boolean ready() throws IOException {
			return br.ready() || st.hasMoreTokens();
		}

		int[] nxtArr(int n) throws IOException {
			int[] ans = new int[n];
			for (int i = 0; i < n; i++)
				ans[i] = nextInt();
			return ans;
		}

	}

	static void sort(int[] a) {
		shuffle(a);
		Arrays.sort(a);
	}

	static void shuffle(int[] a) {
		int n = a.length;
		Random rand = new Random();
		for (int i = 0; i < n; i++) {
			int tmpIdx = rand.nextInt(n);
			int tmp = a[i];
			a[i] = a[tmpIdx];
			a[tmpIdx] = tmp;
		}
	}

}