import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Palisection {

	static int mod = 51123987;
	public static void main(String[] args) {
		FS in = new FS();
		int N = in.nextInt();
		char c[] = in.next().toCharArray();
		Eertree et = new Eertree(N);
		int end[] = new int[N];
		for(int i = 0; i < N; i++) {
			et.addLetter(c[i]);
			end[i] = et.numLinks[et.last];
		}
		
		et.clear();
		int res = 0, starts = 0;
		for(int i = N-1; i >= 0; i--) {
			res = (int) ((res + end[i] * (long)starts)%mod);
			et.addLetter(c[i]);
			starts = (starts + et.numLinks[et.last])%mod;
		}
		long total = 0;
		if(et.pCnt %2 == 0) total = ((et.pCnt/2)%mod)*((et.pCnt-1)%mod);
		else total = (et.pCnt%mod) * (((et.pCnt-1)/2)%mod);
		total %= mod;
		long answer = total-res;
		if(answer < 0) answer += mod;
		System.out.println(answer);
	}
	
	//Nodes 0 and 1 are dummy nodes. Not actual palindromes in the string
	//len[i] is the length of the palindrom at node i
	//numAppearences[i] is the amount of times palindrome I appears (Call topsort first!)
	//pCnt is number of non-unique palin. sz-2 is number of unique
	static class Eertree {
		static final int nonHashed = 10;
		int[] len, link, numLinks;
		byte[] s;
		short[][] toShort;
		byte[][] toByte;
		HashMap<Integer, Integer> to[];
		int sz, last, n;
		long pCnt;
		public Eertree(int nn) {
			s = new byte[nn+2];
			len = new int[nn+2];
			link = new int[nn+2];
			toShort = new short[nonHashed][nn+2];
			toByte = new byte[nonHashed][nn+2];
			to = new HashMap[26-nonHashed];
			for(int i = 0; i < to.length; i++) to[i] = new HashMap<>();
			numLinks = new int[nn+2];
			s[n++] = -1;
			link[0] = 1;
			len[1] = -1;
			sz = 2;
		}
		void clear() {
			Arrays.fill(s, (byte)0);
			Arrays.fill(len, 0);
			Arrays.fill(link, 0);
			for(int i = 0; i < nonHashed; i++) {
				Arrays.fill(toShort[i],(short) 0);
				Arrays.fill(toByte[i], (byte) 0);
			}
			for(int i = 0; i < to.length; i++) to[i].clear();
			Arrays.fill(numLinks, 0);
			n=0; pCnt = 0; last = 0;
			s[n++] = -1;
			link[0] = 1;
			len[1] = -1;
			sz = 2;
		}
		int getLink(int v) {
			while(s[n-len[v]-2] != s[n-1]) v = link[v];
			return v;
		}
		void addLetter(char ch) {
			int c = ch-'a';
			s[n++] = (byte) c;
			last = getLink(last);
			if(get(c, last) == 0) {
				len[sz] = len[last]+2;
				link[sz] = get(c, getLink(link[last]));
				numLinks[sz] = numLinks[link[sz]]+1;
				if(c < nonHashed) {
					short ss = (short)(sz&((1<<15)-1));
					byte bb = (byte) ((sz>>15)&((1<<15)-1));
					toShort[c][last] = ss;
					toByte[c][last] = bb;
				}
				else {
					to[c-nonHashed].put(last, sz);
				}
				sz++;
			}
			if(c < nonHashed)
				last = val(toShort[c][last], toByte[c][last]);
			else 
				last = to[c-nonHashed].get(last);
			pCnt += numLinks[last];
		}
		
		int get(int c, int node) {
			if(c >= nonHashed) return to[c-nonHashed].getOrDefault(node, 0);
			return val(toShort[c][node], toByte[c][node]);
		}
		
		int val(short s, byte b) {
			int x = 0;
			x |= s;
			x |= (((int)b)<<15);
			return x;
		}
	}

	static class FS{
		BufferedReader br;
		StringTokenizer st;
		public FS() { br = new BufferedReader(new InputStreamReader(System.in));}
		String next() {
			while(st == null || !st.hasMoreElements()) {
				try {st = new StringTokenizer(br.readLine());}
				catch(Exception e) { throw null;}//yeet
			}
			return st.nextToken();
		}
		int nextInt() { return Integer.parseInt(next()); }
	}
}
