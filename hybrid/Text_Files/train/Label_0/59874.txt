import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashSet;
import java.util.List;
import java.util.Locale;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		new Thread(null, new Runnable() {
			public void run() {
				try {
					long prevTime = System.currentTimeMillis();
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

	void run() throws IOException {
		in = new BufferedReader(new InputStreamReader(System.in));
		out = new PrintWriter(System.out);
		Object o = solve();
		if (o != null)
			out.println(o);
		out.close();
		in.close();
	}

	private Object solve() throws IOException {
		int n = ni();
		int[] arr = nia(n);
		for(int i =0;i<n;i++)
			arr[i]--;
		
		int least =0;
		long cycle = 1;
		for(int i =0;i<n;i++){
			int[] pair = go(arr, i);
			least = Math.max(least, pair[0]);
			cycle = mcm(cycle, pair[1]);
		}
		
		long coef =1;
		while(coef * cycle < least)
			coef++;
		return coef * cycle;
	}
	
	private long mcm(long a, long b) {
		return (a*b) / gcd(Math.min(a, b), Math.max(a, b));
	}

	private long gcd(long min, long max) {
		if(min==0)
			return max;
		return gcd(max%min, min);
	}

	private int[] go(int[] arr, int u) {
		List<Integer> list = new ArrayList<Integer>();
		list.add(u);
		
		Set<Integer> set = new HashSet<Integer>();
		set.add(u);
		
		while(!set.contains(arr[u])){
			u = arr[u];
			set.add(u);
			list.add(u);
		}
		int index = list.indexOf(arr[u]);
		int len = list.size() - index;
		return new int[]{index, len};
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