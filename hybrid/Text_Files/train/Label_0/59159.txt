import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.Set;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class Main {
	static long prevTime;
	public static void main(String[] args) throws IOException {
		new Thread(null, new Runnable() {
			public void run() {
				try {
					prevTime = System.currentTimeMillis();
					new Main().run();
					System.err.println("Total time: "
							+ (System.currentTimeMillis() - prevTime) + " ms");
					System.err.println("Memory status: " + memoryStatus());
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}, "1", 1L << 24).start();
	}
// 1000000 1 1

	void run() throws IOException {
		in = new BufferedReader(new InputStreamReader(System.in));
		out = new PrintWriter(System.out);
		Object o = solve();
		if (o != null)
			out.println(o);
		out.close();
		in.close();
	}
	
	static int MOD = 1000000007;

	private Object solve() throws IOException {
		int n = ni();
		long L = nl();
		int k = ni();
		
		long[] arr = nla(n);
//		System.out.println(System.currentTimeMillis() - prevTime);
		int M = compress(arr);
//		System.out.println(System.currentTimeMillis() - prevTime);
		long[] count = new long[M];
		for(long a : arr)
			count[(int)a]++;
		
		long sure = (((L / ((long) n))));
		long rem = (int) (L % ((long)n));
		
		long[][] dp = new long[k+1][M]; // usando i bloques de n, hasta el j-esimo mas grande cuantos terminan en a lo sumo i -esimo
		dp[0] = new long[M];
		Arrays.fill(dp[0], 1);
		for(int blo = 1; blo <dp.length;blo++){
			for(int j =0;j<M;j++)
				dp[blo][j] =  ((count[j] * dp[blo-1][j]) % MOD);
			for(int j =1;j<dp[blo].length;j++)
				dp[blo][j] =  ((dp[blo][j] + dp[blo][j-1]) % MOD);
		}	
//		System.out.println(System.currentTimeMillis() - prevTime);
		long ret =0;
		for(int i =1;i<= k;i++){
			long aux = (dp[i][M-1] * (Math.max(0, (sure - i + 1 )%MOD)))%MOD;
			ret = (ret + aux)%MOD;
		}
		Arrays.fill(count, 0);
		for(int i =0 ;i<rem;i++){
			count[(int)arr[i]]++;
		}
		for(int i =0;i < k && i <= sure; i++){
			for(int j=0;j<M;j++)
				ret = ( ((dp[i][j] * count[j]) % MOD) + ret ) %MOD;
			
		}
		return ret;
		
	}
	
	private int compress(long[] arr) {
		long[] aux = arr.clone();
		for(int i =1;i<arr.length;i++){
			int index = (int) (Math.random() * (i+1));
			long tmp = aux[index];
			aux[index]= aux[i];
			aux[i] = tmp;
		}
		Arrays.sort(aux);
		Map<Long,Long> map = new HashMap<Long,Long>();

		int lo =0; 
		int index =0;
		while(lo < arr.length){
			int hi= lo+1;
			while(hi < aux.length && aux[hi] == aux[lo])
				hi++;
			map.put(aux[lo], (long) index);
			index++;
			lo = hi;
		}
		for(int i =0;i<arr.length;i++){
			arr[i] = map.get(arr[i]);
		}
		return map.size();
	}

	BufferedReader in;
	PrintWriter out;
	StringTokenizer strTok = new StringTokenizer("");

	String nextToken() throws IOException {
		while (!strTok.hasMoreTokens())
			strTok = new StringTokenizer(in.readLine());
		return strTok.nextToken();
	}

	int ni() throws IOException {
		return Integer.parseInt(nextToken());
	}

	long nl() throws IOException {
		return Long.parseLong(nextToken());
	}

	double nd() throws IOException {
		return Double.parseDouble(nextToken());
	}

	int[] nia(int size) throws IOException {
		int[] ret = new int[size];
		for (int i = 0; i < size; i++)
			ret[i] = ni();
		return ret;
	}

	long[] nla(int size) throws IOException {
		long[] ret = new long[size];
		for (int i = 0; i < size; i++)
			ret[i] = nl();
		return ret;
	}

	double[] nda(int size) throws IOException {
		double[] ret = new double[size];
		for (int i = 0; i < size; i++)
			ret[i] = nd();
		return ret;
	}

	String nextLine() throws IOException {
		strTok = new StringTokenizer("");
		return in.readLine();
	}

	boolean EOF() throws IOException {
		while (!strTok.hasMoreTokens()) {
			String s = in.readLine();
			if (s == null)
				return true;
			strTok = new StringTokenizer(s);
		}
		return false;
	}

	void printRepeat(String s, int count) {
		for (int i = 0; i < count; i++)
			out.print(s);
	}

	void printArray(int[] array) {
		for (int i = 0; i < array.length; i++) {
			if (i > 0)
				out.print(' ');
			out.print(array[i]);
		}
		out.println();
	}

	void printArray(long[] array) {
		for (int i = 0; i < array.length; i++) {
			if (i > 0)
				out.print(' ');
			out.print(array[i]);
		}
		out.println();
	}

	void printArray(double[] array) {
		for (int i = 0; i < array.length; i++) {
			if (i > 0)
				out.print(' ');
			out.print(array[i]);
		}
		out.println();
	}

	void printArray(double[] array, String spec) {
		for (int i = 0; i < array.length; i++) {
			if (i > 0)
				out.print(' ');
			out.printf(Locale.US, spec, array[i]);
		}
		out.println();
	}

	void printArray(Object[] array) {
		boolean blank = false;
		for (Object x : array) {
			if (blank)
				out.print(' ');
			else
				blank = true;
			out.print(x);
		}
		out.println();
	}

	@SuppressWarnings("rawtypes")
	void printCollection(Collection collection) {
		boolean blank = false;
		for (Object x : collection) {
			if (blank)
				out.print(' ');
			else
				blank = true;
			out.print(x);
		}
		out.println();
	}

	static String memoryStatus() {
		return (Runtime.getRuntime().totalMemory()
				- Runtime.getRuntime().freeMemory() >> 20)
				+ "/" + (Runtime.getRuntime().totalMemory() >> 20) + " MB";
	}

	public void pln() {
		out.println();
	}

	public void pln(int arg) {
		out.println(arg);
	}

	public void pln(long arg) {
		out.println(arg);
	}

	public void pln(double arg) {
		out.println(arg);
	}

	public void pln(String arg) {
		out.println(arg);
	}

	public void pln(boolean arg) {
		out.println(arg);
	}

	public void pln(char arg) {
		out.println(arg);
	}

	public void pln(float arg) {
		out.println(arg);
	}

	public void pln(Object arg) {
		out.println(arg);
	}

	public void p(int arg) {
		out.print(arg);
	}

	public void p(long arg) {
		out.print(arg);
	}

	public void p(double arg) {
		out.print(arg);
	}

	public void p(String arg) {
		out.print(arg);
	}

	public void p(boolean arg) {
		out.print(arg);
	}

	public void p(char arg) {
		out.print(arg);
	}

	public void p(float arg) {
		out.print(arg);
	}

	public void p(Object arg) {
		out.print(arg);
	}

}