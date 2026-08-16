import java.io.*;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 * Created by IntelliJ IDEA.
 * User: piyushd
 * Date: Dec 9, 2010
 * Time: 1:33:22 AM
 * To change this template use File | Settings | File Templates.
 */
public class School {
    private BufferedReader in;
    private PrintWriter out;
    private StringTokenizer st;

	int[] g, b, v, seq;
	boolean[] vis;

    void solve() throws IOException {
		int n = nextInt(), m = nextInt();
		g = new int[n];
		seq = new int[n];
		b = new int[m];
		v = new int[m];
		vis = new boolean[n];
		for(int i = 0; i < n; i++) g[i] = nextInt() - 1;
		for(int i = 0; i < m; i++) v[i] = nextInt();
		for(int i = 0; i < m; i++) b[i] = nextInt();

		int res = 0, a = 0;
		for(int i = 0; i < m; i++){
			a = (v[i] + res - 1) % n;
			res = 0;
			for(int j = a; seq[j] < b[i] && b[i] > 0; j = g[j], b[i]--){
				if(!vis[j]){
					vis[j] = true;
					res++;
				}
				seq[j] = b[i];
			}
			out.println(res);
		}
    }

    School() throws IOException {
        in = new BufferedReader(new InputStreamReader(System.in));
        //in  = new BufferedReader(new InputStreamReader(new FileInputStream(new File("C://Users/piyushd/Desktop/codeforces/sample.txt"))));
        out = new PrintWriter(System.out);

        eat("");

        solve();

        in.close();
        out.close();
    }

    private void eat(String str) {
        st = new StringTokenizer(str);
    }

    String next() throws IOException {
        while (!st.hasMoreTokens()) {
            String line = in.readLine();
            if (line == null) {
                return null;
            }
            eat(line);
        }
        return st.nextToken();
    }

    int nextInt() throws IOException {
        return Integer.parseInt(next());
    }

    long nextLong() throws IOException {
        return Long.parseLong(next());
    }

    double nextDouble() throws IOException {
        return Double.parseDouble(next());
    }

    public static void main(String[] args) throws IOException {
        new School();
    }
}
