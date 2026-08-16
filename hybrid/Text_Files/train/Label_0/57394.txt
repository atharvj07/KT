import java.util.*;
import java.io.*;
import java.math.*;

public class c {


    public static void main(String[] args) throws IOException {
        FastScanner in = new FastScanner(System.in);
        PrintWriter out = new PrintWriter(System.out);
        
        int n = in.nextInt();
        int m = in.nextInt();
        int[] lens = new int[n];
        int[][] strs = new int[n][];
        for (int i = 0; i < n; i++) {
        	lens[i] = in.nextInt();
        	strs[i] = in.nextOffsetIntArray(lens[i]);
        }
        
        TwoSat sat = new TwoSat(m);
        boolean good = true;
        for (int i = 0; i < n - 1; i++) {
        	int[] a = strs[i];
        	int[] b = strs[i + 1];
        	int lenA = lens[i];
        	int lenB = lens[i + 1];
        	int max = Math.max(lenA, lenB);
        	for (int j = 0; j < max; j++) {
        		int ca = j < lenA ? a[j] : -1;
        		int cb = j < lenB ? b[j] : -1;
        		if (ca == -1) {
        			break;
        		}
        		if (cb == -1) {
        			good = false;
        			break;
        		}
        		if (ca == cb) continue;
        		if (ca < cb) {
        			sat.addImpl(cb, true, ca, true);
        			break;
        		} else {
        			sat.addForce(ca, true);
        			sat.addForce(cb, false);
        			break;
        		}
        	}
        }
        //System.out.println(good);
        if (!good || !sat.solve()) {
        	out.println("No");
        } else {
        	out.println("Yes");
        	IntList arr = new IntList();
        	for (int i = 0; i < m; i++) {
        		if (sat.vals[i*2] == 1)
        			arr.add(i + 1);
        	}
        	out.println(arr.size());
        	for (int i = 0; i < arr.size(); i++)
        		out.print(arr.get(i) + " ");
        	out.println();
        }
        
        out.close();
    }
    
    static class TwoSat {
    	int n, n2;  int[] vals, cvals;  SCC scc;

    	public TwoSat(int nn) {  n2 = 2 * (n = nn);  scc = new SCC(n2);  vals = new int[n2];  }

    	void addImpl(int a, boolean va, int b, boolean vb) {
    		a *= 2; b *= 2;  if (!va) a++;  if (!vb) b++;
    		scc.add(a, b);  scc.add(b ^ 1, a ^ 1);
    	}

    	//# Add (a NAND b)
    	void addNand(int a, boolean va, int b, boolean vb) {
    		addImpl(a, va, b, !vb);
    	}//$

    	//# Add (a OR b) where va and vb represent whether a and b are inverted
    	public void addOr(int a, boolean va, int b, boolean vb) {
    		addImpl(a, !va, b, vb); // ~a -> b
    	}//$

    	//# Add (a XOR b) where va and vb represent whether a and b are inverted
    	public void addXor(int a, boolean va, int b, boolean vb) {
    		addImpl(a, !va, b, vb); // ~a -> b
    		addImpl(a, va, b, !vb); // a -> ~b
    	}//$

    	//# Forces a to have whatever value va is
    	public void addForce(int a, boolean va) {
    		addOr(a, va, a, va);
    	}//$

    	boolean solve() {
    		ArrayList<ArrayList<Integer>> comps = scc.go();
    		int[] id2c = new int[scc.n];  SCC graph = scc.compressSCC(id2c);
    		cvals = new int[graph.adj.length];  Arrays.fill(cvals, -1);
    		for(int i = 0; i < n; i++)  if(id2c[2*i] == id2c[2*i+1]) return false;

    		int[] deg = new int[graph.adj.length];
    		for(int u = 0; u < graph.adj.length; u++) for(int v : graph.adj[u]) deg[v]++;

    		ArrayDeque<Integer> q = new ArrayDeque<Integer>();
    		for(int i = 0; i < graph.adj.length; i++) if(deg[i] == 0) q.offer(i);

    		while (!q.isEmpty()) {
    			int u = q.poll();  ArrayList<Integer> comp = comps.get(u);
    			if (cvals[u] == -1) {
    				cvals[u] = 0;
    				for(int i = 0; i < comp.size(); i++)
    					cvals[id2c[comp.get(i) ^ 1]] = 1;
    			}
    			for(int v : graph.adj[u]) if((--deg[v]) == 0) q.offer(v);
    		}
    		for(int i = 0; i < comps.size(); i++) for(int v : comps.get(i)) vals[v] = cvals[i];

    		return true;
    	}
    }
    
  //Tarjan Strongly Connected Components O(V + E)
    static class SCC {
      ArrayList<Integer>[] adj;
      int n;
      @SuppressWarnings("unchecked")
      SCC(int n) {
        this.n = n;
        adj = new ArrayList[n];
        for (int curr = 0; curr < n; ++curr)
          adj[curr] = new ArrayList<Integer>();
      }

      void add(int v1, int v2) {
        adj[v1].add(v2);
      }

      int index;
      boolean[] visited;
      int[] indices;
      int[] lowlink;
      ArrayDeque<Integer> stack;
      ArrayList<ArrayList<Integer>> components;
      ArrayList<ArrayList<Integer>> go() {
        index = 1;
        indices = new int[n];
        lowlink = new int[n];
        visited = new boolean[n];
        components = new ArrayList<ArrayList<Integer>>();
        stack = new ArrayDeque<Integer>();

        for (int curr = 0; curr < n; ++curr)
          if (indices[curr] == 0)
            dfs(curr);

        return components;
      }

      void dfs(int node) {
        indices[node] = lowlink[node] = index++;
        stack.push(node);
        visited[node] = true;

        for (int next : adj[node]) {
          if (indices[next] == 0) {
            dfs(next);
            lowlink[node] = Math.min(lowlink[node], lowlink[next]);
          } else if (visited[next]) {
            lowlink[node] = Math.min(lowlink[node], indices[next]);
          }
        }

        if (lowlink[node] == indices[node]) {
          ArrayList<Integer> component = new ArrayList<Integer>();
          int next;
          do {
            next = stack.pop();
            visited[next] = false;
            component.add(next);
          } while (next != node);
          components.add(component);
        }
      }

      //#
      public class StackState {
        int node, child;
        boolean beforeDFS;
        StackState(int n) {
          node = n;
          child = 0;
          beforeDFS = true;
        }
        void setChild(int c) {
          child = c;
          beforeDFS = true;
        }
      }

      void dfsItr(int start) {
        ArrayDeque<StackState> s = new ArrayDeque<StackState>();
        s.push(new StackState(start));

        while (!s.isEmpty()) {
          StackState st = s.pop();
          if (indices[st.node] == 0) {
            indices[st.node] = lowlink[st.node] = index++;
            stack.push(st.node);
            visited[st.node] = true;
          }
          if (st.child == adj[st.node].size()) {
            if (lowlink[st.node] == indices[st.node]) {
              ArrayList<Integer> component = new ArrayList<Integer>();
              int next;
              do {
                next = stack.pop();
                visited[next] = false;
                component.add(next);
              } while (next != st.node);
              components.add(component);
            }
          } else {
            int next = adj[st.node].get(st.child);
            if (st.beforeDFS) {
              if (indices[next] == 0) {
                st.beforeDFS = false;
                s.push(st);
                s.push(new StackState(next));
              } else if (visited[next]) {
                lowlink[st.node] = Math.min(lowlink[st.node], indices[next]);
                st.setChild(st.child + 1);
                s.push(st);
              } else {
                st.setChild(st.child + 1);
                s.push(st);
              }
            } else {
              lowlink[st.node] = Math.min(lowlink[st.node], lowlink[next]);
              st.setChild(st.child + 1);
              s.push(st);
            }
          }
        }
      }
      //$

      //# Make sure to call go() before calling this function.
      // Function returns a new graph such that all SCCs are
      // compressed into one node and only the edges connecting
      // two components are in the new graph.
      // nodeMapping is an integer array that will store the mapping
      // for each node in the old graph into the new graph.//$
      SCC compressSCC(int[] nodeMapping) {
        for (int i = 0; i < components.size(); ++i) {
          ArrayList<Integer> component = components.get(i);
          for (int node : component)
            nodeMapping[node] = i;
        }
        SCC g = new SCC(components.size());
        int[] added = new int[components.size()];
        Arrays.fill(added, -1);
        for (int i = 0; i < components.size(); ++i) {
          ArrayList<Integer> component = components.get(i);
          for (int node : component) {
            for (int next : adj[node]) {
              int comp = nodeMapping[next];
              if (comp != i && added[comp] != i) {
                g.add(i, comp);
                added[comp] = i;
              }
            }
          }
        }
        return g;
      }
    }


    static Random rand = new Random();
    static void sort(int[] a) {
        lsbRadixSort(a, true);
    }
    static void sort(long[] a) {
        int n = a.length;
        for (int i = a.length - 1; i > 0; i--) {
            int j = rand.nextInt(i + 1);
            long tmp = a[i];
            a[i] = a[j];
            a[j] = tmp;
        }
        Arrays.sort(a);
    }
    static void sort(double[] a) {
        int n = a.length;
        for (int i = a.length - 1; i > 0; i--) {
            int j = rand.nextInt(i + 1);
            double tmp = a[i];
            a[i] = a[j];
            a[j] = tmp;
        }
        Arrays.sort(a);
    }
    static void lsbRadixSort(int[] a, boolean signed) {
        int s = 0, n = a.length;
        int[] p = new int[257], b = new int[n];
        int sb = 1 << 31;
        if(signed) for(int i=0;i<n;i++)  a[i] ^= sb;
        while (s < 32) {
            Arrays.fill(p, 0);
            for (int i = 0; i < n; i++)
                p[((a[i] >>> s) & 255)+1]++;
            for(int i=2;i<256;i++)
                p[i] += p[i-1];
            for (int i = 0; i < n; i++)
                b[p[(a[i] >>> s) & 255]++] = a[i];
            int[] tmp = b;  b = a;  a = tmp;
            s += 8;
        }
        if(signed) for(int i=0;i<n;i++)  a[i] ^= sb;
    }
    static long gcd(long a, long b) { return b == 0 ? a : gcd(b, a % b); }
    static long lcm(long a, long b) { return a / gcd(a, b) * b; }
    static long[] eEuclid(long a, long b) {
        if (b == 0) return new long[] { a, 1, 0 };
        long[] ans = eEuclid(b, a % b);
        long temp = ans[1] - ans[2] * (a / b);
        ans[1] = ans[2];  ans[2] = temp;
        return ans;
    }
    static long modInverse(long a, long m) {
        return ((eEuclid(a, m)[1] % m) + m) % m;
    }
    static class IntList {
        static int[] EMPTY = {};
        int[] a = EMPTY;
        int n = 0;
        void add(int v) {
            if (n >= a.length)
                a = Arrays.copyOf(a, (n << 2) + 8);
            a[n++] = v;
        }
        int get(int idx) {
            return a[idx];
        }
        int size() {
            return n;
        }
    }
    static class DisjointSet {
        int[] s;
	
        public DisjointSet(int n) {
            Arrays.fill(s = new int[n], -1);
        }	
        public int find(int i) {
            return s[i] < 0 ? i : (s[i] = find(s[i]));
        }	
        public boolean union(int a, int b) {
            if ((a = find(a)) == (b = find(b))) return false;
            if(s[a] == s[b]) s[a]--;
            if(s[a] <= s[b]) s[b] = a; else s[a] = b;
            return true;
        }
    }
    static class FastScanner {
        BufferedReader br;
        StringTokenizer st;
        public FastScanner(InputStream i) {
            br = new BufferedReader(new InputStreamReader(i));
            st = new StringTokenizer("");
        }
        public String next() throws IOException {
            if(st.hasMoreTokens())
                return st.nextToken();
            else
                st = new StringTokenizer(br.readLine());
            return next();
        }
        public int nextInt() throws IOException {
            return Integer.parseInt(next());
        }
        public long nextLong() throws IOException {
            return Long.parseLong(next());
        }
        public double nextDouble() throws IOException {
            return Double.parseDouble(next());
        }
        public int[] nextOffsetIntArray(int n) throws IOException {
            int[] arr = new int[n];
            for (int i = 0; i < n; i++)
                arr[i] = nextInt() - 1;
            return arr;
        }
        public int[] nextIntArray(int n) throws IOException {
            int[] arr = new int[n];
            for (int i = 0; i < n; i++)
                arr[i] = nextInt();
            return arr;
        }
        public int[][] nextIntArray(int n, int m) throws IOException {
            int[][] arr = new int[n][m];
            for (int i = 0; i < n; i++)
                for (int j = 0; j < m; j++)
                    arr[i][j] = nextInt();
            return arr;
        }
        public long[] nextLongArray(int n) throws IOException {
            long[] arr = new long[n];
            for (int i = 0; i < n; i++)
                arr[i] = nextLong();
            return arr;
        }
        public long[][] nextLongArray(int n, int m) throws IOException {
            long[][] arr = new long[n][m];
            for (int i = 0; i < n; i++)
                for (int j = 0; j < m; j++)
                    arr[i][j] = nextLong();
            return arr;
        }
        public double[] nextDoubleArray(int n) throws IOException {
            double[] arr = new double[n];
            for (int i = 0; i < n; i++)
                arr[i] = nextDouble();
            return arr;
        }
        public double[][] nextDoubleArray(int n, int m) throws IOException {
            double[][] arr = new double[n][m];
            for (int i = 0; i < n; i++)
                for (int j = 0; j < m; j++)
                    arr[i][j] = nextDouble();
            return arr;
        }
        public char[][] nextCharArray(int n, int m) throws IOException {
            char[][] arr = new char[n][];
            for (int i = 0; i < n; i++)
                arr[i] = next().toCharArray();
            return arr;
        }
    }
}