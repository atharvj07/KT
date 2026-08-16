import java.io.*;
import java.util.*;

public class G {
	int oo = (int)1e8;
	
	public static void main(String[] args) {
		new G();
	}

	int SQRT;
	int[] minTandemStart, minTandemEnd, sa, rsa, lcp;
	boolean[] primes;
	RMQ query3RMQ, lcpRMQ;
	int[] trailingZeros, highestOneBit;
	String str;
	
	public G() {
		FastScanner fs = new FastScanner();
		PrintWriter out = new PrintWriter(System.out);
		System.err.println("");

		trailingZeros = new int[200200];
		highestOneBit = new int[200200];
		for(int i = 1; i < 200200; i++) {
			highestOneBit[i] = Integer.highestOneBit(i);
			trailingZeros[i] = Integer.numberOfTrailingZeros(highestOneBit[i]);
		}
		
		doPrimes();
		
		int n = fs.nextInt();
		SQRT = (int)Math.sqrt(n);
		str = fs.next();
		FastSuffixArray fsa = new FastSuffixArray();
		sa = fsa.suffixArray(str.toCharArray());
		rsa = new int[sa.length];
		lcp = fsa.lcp(sa, str.toCharArray());
		lcpRMQ = new RMQ(lcp);
		for(int i = 0; i < sa.length; i++) rsa[sa[i]] = i;
		
		TandemRepeats tr = new TandemRepeats(str);
		minTandemStart = tr.min;
		TandemRepeats tr2 = new TandemRepeats(reverse(str));
		minTandemEnd = reverse(tr2.min);
		
		int[] query3Values = new int[n];
		for(int i = 0; i < n; i++) {
			minTandemStart[i] <<= 1;
			minTandemEnd[i] <<= 1;
		}
		for(int i = 0; i < n; i++) {
			query3Values[i] = i+minTandemStart[i];
		}
		query3RMQ = new RMQ(query3Values);
		
		int[][] pref = new int[26][n];
		for(int i = n-1; i >= 0; i--) {
			for(int j = 0; j < 26 && i+1 < n; j++) pref[j][i] = pref[j][i+1];
			pref[str.charAt(i)-'a'][i]++;
		}
		
		int Q = fs.nextInt();
		for(int qq = 1; qq <= Q; qq++) {
			int L = fs.nextInt()-1, R = fs.nextInt()-1;
			
			//case -1
			boolean good = false;
			for(int i = 0; i < 26; i++) {
				int sum = pref[i][L];
				if(R + 1 < n) sum -= pref[i][R+1];
				if(sum > 1) good = true;
			}
			if(!good) {
				out.println(-1);
				continue;
			}
			
			//case 1:
			boolean ans1 = false;
			int N = R-L+1;
			for(int div = 1; div*div <= N; div++) {
				if(N % div != 0) continue;
				int nd = N/div;
				if(primes[nd] && check(L, R, div)) {
					ans1 = true;
				}
				if(!ans1 && primes[div] && check(L, R, nd)) ans1 = true;
				if(ans1) break;
			}
			if(ans1) {
				out.println(1);
				continue;
			}
			
			//case 2:
			boolean ans2 = false;
			if(minTandemStart[L] < oo && L+minTandemStart[L]-1 <= R) {
				ans2 = true;
			}
			if(minTandemEnd[R] < oo && R-minTandemEnd[R]+1 >= L) {
				ans2 = true;
			}
			if(!ans2 && isBorder(L, R)) {
				ans2 = true;
			}
			if(ans2) {
				out.println(2);
				continue;
			}
			
			//case 3:
			boolean ans3 = false;
			{ //first character
				int idx = str.charAt(L)-'a';
				int sum = pref[idx][L];
				if(R+1 < n) sum -= pref[idx][R+1];
				if(sum > 1) ans3 = true;
			}
			{ //last character
				int idx = str.charAt(R)-'a';
				int sum = pref[idx][L];
				if(R+1 < n) sum -= pref[idx][R+1];
				if(sum > 1) ans3 = true;
			}
			{ //BAAC
				int min = query3RMQ.query(L, R);
				if(min <= R) ans3 = true;
			}
			if(ans3) {
				out.println(3);
				continue;
			}
			
			out.println(4);
		}

		out.close();
	}
	
	boolean check(int L, int R, int div) {
		int minPos = rsa[L], maxPos = rsa[L];
		char beg = str.charAt(L);
		for(int j = L+div; j <= R; j += div) {
			if(str.charAt(j) != beg) return false;
			minPos = min(minPos, rsa[j]);
			maxPos = max(maxPos, rsa[j]);
		}
		int lcp = lcpRMQ.query(minPos, maxPos-1);
		if(lcp >= div) {
			return true;
		}
		return false;
	}
	
	Random rand = new Random();
	boolean isBorder(int L, int R) {
		for(int len = 1; len < SQRT; len++) {
			int ptsTo = R-len+1;
			if(ptsTo <= L+len-1) continue;
			int min = min(rsa[L], rsa[ptsTo]);
			int max = max(rsa[L], rsa[ptsTo]);
			int lcp = lcpRMQ.query(min, max-1);
			if(lcp >= len) {
				return true;
			}
		}
		int st = max(0, rsa[L]-SQRT/2-1);
		int en = min(sa.length-1, rsa[L]+SQRT/2+1);
		int him = rsa[L];
		
		for(int i = him-1; i >= st; i--) {
			int idx = sa[i];
			if(L <= idx && idx <= R) {}
			else continue;
			int min = min(i, him);
			int max = max(i, him);
			int lcp = lcpRMQ.query(min, max-1);
			if(lcp < SQRT) break;
			
			if(idx+lcp-1 < R) continue;
			int size = R-idx+1;
			if(L+size-1 >= idx) continue;
			return true;
		}
		for(int i = him+1; i <= en; i++) {
			int idx = sa[i];
			if(L <= idx && idx <= R) {}
			else continue;
			int min = min(i, him);
			int max = max(i, him);
			int lcp = lcpRMQ.query(min, max-1);
			if(lcp < SQRT) break;
			
			if(idx+lcp-1 < R) continue;
			int size = R-idx+1;
			if(L+size-1 >= idx) continue;
			return true;
		}
		
		return false;
	}
	
	class RMQ {
		int[] vs;
		int[][] lift;

		public RMQ(int[] vs) {
			this.vs = vs;
			int n = vs.length;
			int maxlog = Integer.numberOfTrailingZeros(Integer.highestOneBit(n)) + 1;
			lift = new int[maxlog][n];
			for (int i = 0; i < n; i++)
				lift[0][i] = vs[i];
			int lastRange = 1;
			for (int lg = 1; lg < maxlog; lg++) {
				for (int i = 0; i < n; i++) {
					lift[lg][i] = min(lift[lg - 1][i], lift[lg - 1][min(i + lastRange, n - 1)]);
				}
				lastRange <<= 1;
			}
		}

		public int query(int low, int hi) {
			if(hi < low) return 0;
			int range = hi - low + 1;
			int exp = highestOneBit[range];
			int lg = trailingZeros[exp];
			return min(lift[lg][low], lift[lg][hi - exp + 1]);
		}
	}

	class FastSuffixArray {
		public int[] suffixArray(char[] S) {
			int n = S.length;
			Integer[] order = new Integer[n];
			for (int i = 0; i < n; i++)
				order[i] = n - 1 - i;

			Arrays.sort(order, (a, b) -> Character.compare(S[a], S[b]));

			int[] sa = new int[n];
			int[] classes = new int[n];
			for (int i = 0; i < n; i++) {
				sa[i] = order[i];
				classes[i] = S[i];
			}

			for (int len = 1; len < n; len <<= 1) {
				int[] c = classes.clone();
				for (int i = 0; i < n; i++) {
					classes[sa[i]] = i > 0 && c[sa[i - 1]] == c[sa[i]] && sa[i - 1] + len < n && c[sa[i - 1] + len / 2] == c[sa[i] + len / 2] ? classes[sa[i - 1]] : i;
				}
				int[] cnt = new int[n];
				for (int i = 0; i < n; i++)
					cnt[i] = i;
				int[] s = sa.clone();
				for (int i = 0; i < n; i++) {
					int s1 = s[i] - len;
					if (s1 >= 0)
						sa[cnt[classes[s1]]++] = s1;
				}
			}
			return sa;
		}

		public int[] lcp(int[] sa, char[] s) {
			int n = sa.length;
			int[] rank = new int[n];
			for (int i = 0; i < n; i++)
				rank[sa[i]] = i;
			int[] lcp = new int[n - 1];
			for (int i = 0, h = 0; i < n; i++) {
				if (rank[i] < n - 1) {
					for (int j = sa[rank[i] + 1]; max(i, j) + h < s.length && s[i + h] == s[j + h]; ++h)
						;
					lcp[rank[i]] = h;
					if (h > 0)
						--h;
				}
			}
			return lcp;
		}
	}

	int MAX = 7500000;
	class TandemRepeats {
		Event[] list = new Event[MAX];
		int ptr2 = 0;
		int[] min;
		TandemRepeats(String str) {
			ptr2 = 0;
			findRepetitions(str, 0, str.length()-1);
			Arrays.sort(list, 0, ptr2);
			min = new int[str.length()];
			Arrays.fill(min, oo);

			int n = str.length();
			BIT bit = new BIT(n+1);
			int ptr = 0;
			for(int i = 0; i < str.length(); i++) {
				while(ptr < ptr2) {
					Event now = list[ptr];
					if(now.pos <= i) {
						if(now.type == 0) bit.update(now.val, 1);
						else bit.update(now.val, -1);
						ptr++;
					} else break;
				}
				int pos = bit.getKth(0);
				if(pos <= n) min[i] = min(min[i], pos);
			}
		}

		//Main-Lorentz algorithm
		void findRepetitions(String str, int L, int R) {
			int n = R-L+1;
			if(n < 2 || R < L) return;

			String u = str.substring(0, n/2);
			String v = str.substring(n/2);
			findRepetitions(u, L, L+u.length()-1); findRepetitions(v, L+u.length(), R);

			int[] z1 = zValues(reverse(u));
			int[] z2 = zValues(v + "#" + u);
			int[] z3 = zValues(reverse(u) + "#" + reverse(v));
			int[] z4 = zValues(v);

			int uLen = u.length(), vLen = v.length();
			for(int cntr = 0; cntr < n; cntr++) {
				int totLen, k1, k2;
				if(cntr < uLen) {
					totLen = uLen-cntr;
					k1 = getIdx(z1, uLen-cntr);
					k2 = getIdx(z2, vLen+1+cntr);

					if(k1+k2 >= totLen) {
						int min = findSmall1(k1, k2, totLen);
						int max = findLarge1(k1, k2, totLen);
						if(min < 0 || max < 0 || min > k1 || max > k1) continue;
						int start = max(L, L+cntr-max);
						int end = min(L+cntr-1, L+cntr-min);

						if(start <= end) {
							list[ptr2++] = (new Event(0, start, totLen));
							list[ptr2++] = (new Event(1, end+1, totLen));
						}
					}

				}
				else {
					totLen = cntr-uLen+1;
					k1 = getIdx(z3, uLen + 1 + vLen - 1 - (cntr - uLen));
					k2 = getIdx(z4, (cntr - uLen) + 1);

					if(k1+k2 >= totLen && k1 > 0) {
						int min = findSmall2(k1, k2, totLen);
						int max = findLarge1(k1, k2, totLen);
						if(min < 1 || max < 1 || min > k1 || max > k1) continue;
						int start = max(L, L+n/2-1 - max + 1);
						int end = min(L+n/2-1, L+n/2-1-min+1);

						if(start <= end) {
							list[ptr2++] = (new Event(0, start, totLen));
							list[ptr2++] = (new Event(1, end+1, totLen));
						}
					}
				}
			}

		}
		
		int findSmall1(int k1, int k2, int len) {
			if(k2 >= len) return 0;
			return len-k2;
		}
		int findSmall2(int k1, int k2, int len) {
			if(k2 >= len-1) return 1;
			return min(k1, len - k2);
		}
		int findLarge1(int k1, int k2, int len) {
			if(k1 < len) return k1;
			return len;
		}

		class Event implements Comparable<Event> {
			int type, pos, val;
			Event(int t, int p, int v) {
				type = t; val = v;
				pos = p;
			}
			public int compareTo(Event e) {
				int comp = Integer.compare(pos, e.pos);
				if(comp == 0) comp = Integer.compare(e.type, type);
				return comp;
			}
			public String toString() {
				return String.format("Pos = %d Type = %d V = %d", pos, type, val);
			}
		}

		int getIdx(int[] a, int i) {
			if(i >= 0 && i < a.length) return a[i];
			return 0;
		}

		int[] zValues(String str) {
			int n = str.length();  char[] s = str.toCharArray();
			int[] z = new int[n];  z[0] = n;
			int L = 0, R = 0;
			int[] left = new int[n], right = new int[n];
			for(int i = 1; i < n; ++i) {
				if(i > R) {
					L = R = i;
					while(R < n && s[R-L] == s[R]) R++;
					z[i] = R - L;  R--;
				} else {
					int k = i-L;
					if(z[k] < R-i+1) z[i] = z[k];
					else {
						L = i;
						while(R < n && s[R-L] == s[R]) R++;
						z[i] = R - L;  R--;
					}
				}
				left[i] = L;  right[i] = R;
			}
			return z;
		}


		void add(TreeMap<Integer, Integer> map, int x) {
			map.put(x, map.getOrDefault(x, 0)+1);
		}
		void rem(TreeMap<Integer, Integer> map, int x) {
			int fr = map.get(x)-1;
			if(fr == 0) map.remove(x);
			else map.put(x, fr);
		}
	}
	
	void doPrimes() {
		primes = new boolean[200200];
		Arrays.fill(primes, true);
		primes[0] = primes[1] = false;
		for(int i = 2; i < primes.length; i++) {
			if(!primes[i]) continue;
			for(int j = i+i; j < primes.length; j += i) primes[j] = false;
		}
	}
	
	String reverse(String s) {
		return new StringBuilder(s).reverse().toString();
	}
	int[] reverse(int[] a) {
		int n = a.length;
		int[] res = new int[n];
		for(int i = 0, j = n-1; i < n; i++, j--) {
			res[i] = a[j];
		}
		return res;
	}

	int min(int a, int b) {
		return a < b ? a : b;
	}
	int max(int a, int b) {
		return a > b ? a : b;
	}
	
	class BIT {
		int n, hn;
		int[] tree;
		
		public BIT(int n) {
			this.n = n;
			tree = new int[n + 2];
			hn = Integer.highestOneBit(n);
		}
		
		int read(int i) {
			i++;
			int sum = 0;
			while (i > 0) {
				sum += tree[i];
				i -= i & -i;
			}
			return sum;
		}
		
		void update(int i, int val) {
			i++;
			while (i <= n) {
				tree[i] += val;
				i += i & -i;
			}
		}

		// if the BIT is a freq array, returns the
		// index of the kth item, or n if there are fewer
		// than k items.
		int getKth(int k) {
			int e=hn, o=0;
			for (; e!=0; e>>=1) {
				if (e+o<=n && tree[e+o]<=k) {
					k-=tree[e+o];
					o+=e;
				}
			}
			return o;
		}
		
	}
	
	class FastScanner {
		public int BS = 1<<16;
		public char NC = (char)0;
		byte[] buf = new byte[BS];
		int bId = 0, size = 0;
		char c = NC;
		double num = 1;
		BufferedInputStream in;

		public FastScanner() {
			in = new BufferedInputStream(System.in, BS);
		}

		public FastScanner(String s) {
			try {
				in = new BufferedInputStream(new FileInputStream(new File(s)), BS);
			}
			catch (Exception e) {
				in = new BufferedInputStream(System.in, BS);
			}
		}

		public char nextChar(){
			while(bId==size) {
				try {
					size = in.read(buf);
				}catch(Exception e) {
					return NC;
				}                
				if(size==-1)return NC;
				bId=0;
			}
			return (char)buf[bId++];
		}

		public int nextInt() {
			return (int)nextLong();
		}

		public long nextLong() {
			num=1;
			boolean neg = false;
			if(c==NC)c=nextChar();
			for(;(c<'0' || c>'9'); c = nextChar()) {
				if(c=='-')neg=true;
			}
			long res = 0;
			for(; c>='0' && c <='9'; c=nextChar()) {
				res = (res<<3)+(res<<1)+c-'0';
				num*=10;
			}
			return neg?-res:res;
		}

		public double nextDouble() {
			double cur = nextLong();
			return c!='.' ? cur:cur+nextLong()/num;
		}

		public String next() {
			StringBuilder res = new StringBuilder();
			while(c<=32)c=nextChar();
			while(c>32) {
				res.append(c);
				c=nextChar();
			}
			return res.toString();
		}

		public String nextLine() {
			StringBuilder res = new StringBuilder();
			while(c<=32)c=nextChar();
			while(c!='\n') {
				res.append(c);
				c=nextChar();
			}
			return res.toString();
		}

		public boolean hasNext() {
			if(c>32)return true;
			while(true) {
				c=nextChar();
				if(c==NC)return false;
				else if(c>32)return true;
			}
		}
		
		public int[] nextIntArray(int n) {
			int[] res = new int[n];
			for(int i = 0; i < n; i++) res[i] = nextInt();
			return res;
		}
		
	}

}