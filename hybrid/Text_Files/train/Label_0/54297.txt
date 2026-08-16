
import java.io.*;
import java.util.*;
import static java.lang.Math.*;

public class BetaRound64_B implements Runnable {

	final boolean ONLINE_JUDGE = System.getProperty("ONLINE_JUDGE") != null;
	BufferedReader in;
	PrintWriter out;
	StringTokenizer tok = new StringTokenizer("");

	void init() throws IOException {
		if (ONLINE_JUDGE) {
			in = new BufferedReader(new InputStreamReader(System.in));
			out = new PrintWriter(System.out);
		} else {
			in = new BufferedReader(new FileReader("input.txt"));
			out = new PrintWriter("output.txt");
		}
	}

	String readString() throws IOException {
		while (!tok.hasMoreTokens()) {
			tok = new StringTokenizer(in.readLine());
		}
		return tok.nextToken();
	}

	int readInt() throws IOException {
		return Integer.parseInt(readString());
	}

	@Override
	public void run() {
		try {
			long t1 = System.currentTimeMillis();
			init();
			solve();
			out.close();
			long t2 = System.currentTimeMillis();
			System.err.println("Time = " + (t2 - t1));
		} catch (Exception e) {
			e.printStackTrace(System.err);
			System.exit(-1);
		}
	}

	public static void main(String[] args) {
		new Thread(new BetaRound64_B()).start();
	}
	
	void solve() throws IOException {
		int m = readInt();
		ArrayList<StringBuilder> a = new ArrayList<StringBuilder>();
		int n = 0;
		for (int k = 0; k < 10000; k++) {
			a.add(new StringBuilder());
		}
		try {
			while (true) {
				String s = readString();
				if (s.endsWith(".") || s.endsWith("!") || s.endsWith("?")) {
					a.get(n++).append(s);
				} else {
					a.get(n).append(s).append(" ");
				}
			}
		} catch (Exception e) {
		}
		int ans = 1;
		int cur = 0;
		for (int i = 0; i < n; i++) {
			int len = a.get(i).length();
			if (cur + (cur==0 ? 0 : 1) + len <= m) {
				cur += (cur==0 ? 0 : 1) + len;
				continue;
			}
			if (len <= m) {
				cur = len;
				ans++;
				continue;
			}
			out.print("Impossible");
			return;
		}
		out.print(ans);
	}
	
}
