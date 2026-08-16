import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.io.BufferedWriter;
import java.util.InputMismatchException;
import java.util.HashMap;
import java.util.Set;
import java.io.BufferedReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.io.Writer;
import java.util.StringTokenizer;
import java.util.HashSet;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 * @author Andrey Rechitsky (arechitsky@gmail.com)
 */
public class Main {
	public static void main(String[] args) {
		InputStream inputStream = System.in;
		OutputStream outputStream = System.out;
		FastScanner in = new FastScanner(inputStream);
		FastPrinter out = new FastPrinter(outputStream);
		TaskC solver = new TaskC();
		solver.solve(1, in, out);
		out.close();
	}
}

class TaskC {
    public void solve(int testNumber, FastScanner in, FastPrinter out) {
        int n = in.nextInt();
        HashMap<Integer, Integer>[] adj = new HashMap[n];
        HashSet<Integer>[] steps = new HashSet[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new HashMap<Integer, Integer>();
            steps[i] = new HashSet<Integer>();
        }
        for (int i = 0; i < n - 1; i++) {
            int u = in.nextInt()-1;
            int v = in.nextInt()-1;
            adj[u].put(v,i);
            adj[v].put(u,i);
        }
        int []step = new int[n];
        Arrays.fill(step, -2);
        step[0] = -1;
        dfs(0,adj, steps, step);
        int k = 0;
        for (int i = 0; i < n; i++) {
            if (!steps[i].isEmpty()) k++;
        }
        out.printLine(k);
        for (int i = 0; i < k; i++) {
            out.print(steps[i].size());
            out.print(' ');
            for (int j:steps[i]){
                out.print(j+1);
                out.print(' ');
            }
            out.printLine();
        }
    }

    void dfs(int from, HashMap<Integer, Integer>[] adj, HashSet<Integer>[] steps, int []step){
        int c = 0;
        for (int to: adj[from].keySet()){
            if (step[to]!=-2) continue;
            if (c==step[from]) c++;
            step[to] = c;
            steps[c].add(adj[from].get(to));
            dfs(to, adj, steps, step);
            c++;
        }
    }
}

class FastScanner {

    private BufferedReader reader;
    private StringTokenizer st;

    public FastScanner(InputStream stream) {
        this.reader = new BufferedReader(new InputStreamReader(stream));
        this.st = new StringTokenizer("");
    }

    public int nextInt() {
        return Integer.parseInt(next());
    }

    public String next() {
        while (!st.hasMoreTokens()) {
            st = new StringTokenizer(readLine());
        }
        return st.nextToken();
    }

    private String readLine() {
        String line = tryReadLine();
        if (line == null) throw new InputMismatchException();
        return line;
    }

    private String tryReadLine() {
        try {
            return reader.readLine();
        } catch (IOException e) {
            throw new InputMismatchException();
        }
    }

}

class FastPrinter {
    private final PrintWriter writer;

    public FastPrinter(OutputStream outputStream) {
        writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(outputStream)));
    }

    public void close() {
        writer.close();
    }

    public void printLine(long i) {
        writer.println(i);
    }

    public void printLine() {
        writer.println();
    }

    public void print(long i) {
        writer.print(i);
    }

    public void print(char c) {
        writer.print(c);
    }

}
