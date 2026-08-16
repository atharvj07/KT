import java.io.*;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;
import java.util.function.Supplier;
import java.util.Queue;
import java.util.Collection;
import java.util.function.IntFunction;
import java.util.StringTokenizer;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
	public static void main(String[] args) {
		InputStream inputStream = System.in;
		OutputStream outputStream = System.out;
		InputReader in = new InputReader(inputStream);
		OutputWriter out = new OutputWriter(outputStream);
		TaskG solver = new TaskG();
		solver.solve(1, in, out);
		out.close();
	}
}

class TaskG {
	private List<Integer>[] g;
	private boolean[] used;
	private int[] min;

	class VertVal {
	    int v, val;

        public VertVal(int v, int val) {
            this.v = v;
            this.val = val;
        }
    }

	private void bfs(int first){
        Queue<VertVal> q = new LinkedList<>();
        q.add(new VertVal(first, first));
        while (!q.isEmpty()){
            int v = q.peek().v;
            int val = q.peek().val;
            q.poll();
            if (used[v]){
                continue;
            }
            used[v] = true;
            int newVal = Math.min(val, v);
            min[v] = newVal;
            List<Integer> next = g[v];
            for (Integer to: next){
                q.add(new VertVal(to, newVal));
            }
        }
	}

	public void solve(int testNumber, InputReader in, OutputWriter out) {
		int n = in.nextInt(), q = in.nextInt();
		g = GraphUtils.getEmptyGraph(n + 1);
		used = new boolean[n + 1];
		min = new int[n + 1];
		for (int i = 0; i < n - 1; ++i){
			int u = in.nextInt(), v = in.nextInt();
			g[u].add(v);
			g[v].add(u);
		}
		in.nextInt();
		int last = 0;
		int x = (in.nextInt() + last) % n + 1;
		bfs(x);
		q--;
		int curMin = Integer.MAX_VALUE;
		while (q-- > 0){
			int qType = in.nextInt();
			x = (in.nextInt() + last) % n + 1;
			if (qType == 1){
				curMin = Math.min(curMin, min[x]);
			} else {
				last = Math.min(curMin, min[x]);
				out.println(last);
			}
		}
	}
}

class InputReader {
    BufferedReader br;
    StringTokenizer st;

    public InputReader(InputStream in)
    {
        br = new BufferedReader(new
                InputStreamReader(in));
    }

    public InputReader(String filename) throws IOException{
        br = new BufferedReader(new FileReader(filename));
    }

    public String next()
    {
        while (st == null || !st.hasMoreElements())
        {
            try
            {
                st = new StringTokenizer(br.readLine());
            }
            catch (IOException  e)
            {
                e.printStackTrace();
            }
        }
        return st.nextToken();
    }

    public int nextInt()
    {
        return Integer.parseInt(next());
    }

    public long nextLong()
    {
        return Long.parseLong(next());
    }

    public double nextDouble()
    {
        return Double.parseDouble(next());
    }

    public String nextLine()
    {
        String str = "";
        try
        {
            str = br.readLine();
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
        return str;
    }
}

class OutputWriter extends PrintWriter{
    public OutputWriter(Writer out) {
        super(out);
    }

    public OutputWriter(Writer out, boolean autoFlush) {
        super(out, autoFlush);
    }

    public OutputWriter(OutputStream out) {
        super(out);
    }

    public OutputWriter(OutputStream out, boolean autoFlush) {
        super(out, autoFlush);
    }

    public OutputWriter(String fileName) throws FileNotFoundException {
        super(fileName);
    }

    public OutputWriter(String fileName, String csn) throws FileNotFoundException, UnsupportedEncodingException {
        super(fileName, csn);
    }

    public OutputWriter(File file) throws FileNotFoundException {
        super(file);
    }

    public OutputWriter(File file, String csn) throws FileNotFoundException, UnsupportedEncodingException {
        super(file, csn);
    }
}

class GraphUtils {
    public static <T> List<T>[] getEmptyGraph(int n) {
        return Stream.generate(ArrayList::new).limit(n).toArray(List[]::new);
    }

}

