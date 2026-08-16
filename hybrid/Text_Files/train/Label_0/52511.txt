import static java.lang.Math.*;
import static java.lang.System.currentTimeMillis;
import static java.lang.System.exit;
import static java.lang.System.arraycopy;
import static java.util.Arrays.sort;
import static java.util.Arrays.binarySearch;
import static java.util.Arrays.fill;
import java.util.*;
import java.io.*;
import java.math.BigInteger;

public class Main {

	public static void main(String[] args) throws IOException {
		try {
			if (new File("input.txt").exists())
				System.setIn(new FileInputStream("input.txt"));
		} catch (SecurityException e) {
		}
		new Thread(null, new Runnable() {
			public void run() {
				try {
					new Main().run();
				} catch (Throwable e) {
					e.printStackTrace();
					exit(999);
				}
			}
		}, "1", 1 << 23).start();
	}

	BufferedReader in;
	PrintWriter out;
	StringTokenizer st = new StringTokenizer("");

	
	int n;
	
	
	int bound = 1048574;
	int mp = 0;
	long m[] = new long[bound];
	
	BigInteger up[] = new BigInteger[bound];
	BigInteger down[] = new BigInteger[bound];
	
	boolean fup = true;
	Item it[];
	
	BigInteger lim;
	Long maxL = Long.MAX_VALUE;
	
	private void run() throws IOException {
		in = new BufferedReader(new InputStreamReader(System.in));
		out = new PrintWriter(System.out);

		long t = currentTimeMillis();
		
		n = nextInt();
		it = new Item[n];
		lim = BigInteger.valueOf(nextLong());
		for(int len = 1; len <= 19; len++)
			for(long mask = 0; mask < (1L << len); mask++){
				long cur = 0L;
				for(int i = 0; i < len; i++){
					cur *= 10;
					if((mask & (1L << i)) == 0L)
						cur += 4;
					else
						cur += 7;
				}
				m[mp++] = cur;
//				if(len == 19 && mask == (1<<len) - 1)
//					System.err.println(cur);
			}
		sort(m, 0, mp);
		for(int i = 0; i < n; i++){
			it[i] = new Item(nextLong(), nextLong());
			maxL = min(maxL, it[i].up - it[i].down + 1);
		}
		{
			fup = true;
			sort(it);
			int cur = 0;
			BigInteger sum = BigInteger.ZERO;
			for(int id = 0; id < mp; id++){
				if(id != 0)
					sum = sum.add(BigInteger.valueOf(cur).multiply(BigInteger.valueOf(m[id] - m[id - 1])));
				while(cur < n && it[cur].up <= m[id]){
					sum = sum.add(BigInteger.valueOf(m[id] - it[cur].up));
					cur++;
				}
				up[id] = sum;
			}
		}
		
		{
			fup = false;
			sort(it);
			int cur = 0;
			BigInteger sum = BigInteger.ZERO;
			for(int id = mp - 1; id >= 0; id--){
				if(id != mp - 1)
					sum = sum.add(BigInteger.valueOf(cur).multiply(BigInteger.valueOf(m[id + 1] - m[id])));
				while(cur < n && it[cur].down >= m[id]){
					sum = sum.add(BigInteger.valueOf(it[cur].down - m[id]));
					cur++;
				}
				down[id] = sum;
			}
		}

		

		int le = 1;
		int ri = mp;
		int ans = 0;
		while(le <= ri){
			int mid = (le + ri) >> 1;
			if(bin_solve(mid)){
				ans = max(ans, mid);
				le = mid + 1;
			}
			else
				ri = mid - 1;
		}
		out.println(ans);
		in.close();
		out.close();
	}
	
	boolean bin_solve(int dist){
		for(int i = 0; i < mp - dist + 5; i++){
			int j = i + dist - 1;
			if(j >= mp) return false;
			if(m[j] - m[i] + 1 <= maxL && up[j].add(down[i]).compareTo(lim) <= 0){
				return true;
			}
		}
		return false;
	}
	
	class Item implements Comparable<Item>{
		long up, down;
		Item(long a, long b){
			down = a;
			up = b;
		}
		public int compareTo(Item e){
			if(fup)
				return up > e.up ? 1 : -1;
			else
				return e.down > down ? 1 : -1;
		}
	}
	String nextToken() throws IOException {
		while (!st.hasMoreTokens())
			st = new StringTokenizer(in.readLine());
		return st.nextToken();
	}
	int nextInt() throws IOException {
		return Integer.parseInt(nextToken());
	}
	long nextLong() throws IOException {
		return Long.parseLong(nextToken());
	}
	double nextDouble() throws IOException {
		return Double.parseDouble(nextToken());
	}
	String nextLine() throws IOException {
		st = new StringTokenizer("");
		return in.readLine();
	}
	boolean EOF() throws IOException {
		while (!st.hasMoreTokens()) {
			String s = in.readLine();
			if (s == null)
				return true;
			st = new StringTokenizer(s);
		}
		return false;
	}
}
