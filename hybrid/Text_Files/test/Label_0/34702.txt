import java.io.*;
import java.util.*;
import java.util.concurrent.TimeUnit;

public class technoD implements Runnable{
	
    public static void main(String[] args) {
    	try{
            new Thread(null, new technoD(), "process", 1<<26).start();
        }
        catch(Exception e){
            System.out.println(e);
        }
    }
	public void run() {
		FastReader scan = new FastReader();
        PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
		//PrintWriter out = new PrintWriter("file.out");
		Task solver = new Task();
		int t = scan.nextInt();
		//int t = 1;
		for(int i = 1; i <= t; i++) solver.solve(i, scan, out);
		out.close();
	}

	static class Task {
		static int N;
		static int[] arr;
		static boolean[] visited;
		
		static TreeMap<Integer, tup> map = new TreeMap<>();
		
		public void solve(int testNumber, FastReader sc, PrintWriter out) {
			N = sc.nextInt();
			map = new TreeMap<>();
			arr = new int[N];
			visited = new boolean[N];
			for(int i = 0; i < N; i++) {
				arr[i] = sc.nextInt();
				if(map.containsKey(arr[i])) {
					map.get(arr[i]).b = i;
				} else {
					map.put(arr[i], new tup(i, i));
				}
			}
			//System.out.println(map);
			
			Iterator<Integer> it = map.keySet().iterator();
			int max = 0;
			while(it.hasNext()) {
				tup t = map.get(it.next());
				if(!visited[t.a]) {
					max = Math.max(max, recurse(t.a) + 1);
				}
			}
			
			out.println(map.size() - max);
		}
		
		public static int recurse(int loc) {
			visited[loc] = true;
			if(map.higherKey(arr[loc]) == null || map.higherEntry(arr[loc]).getValue().a < map.get(arr[loc]).b) {
				return 0;
			}
			return 1 + recurse(map.get(map.higherKey(arr[loc])).a);
		}
	}
	static class tup implements Comparable<tup>, Comparator<tup>{
		int a, b;
		tup(int a,int b){
			this.a=a;
			this.b=b;
		}
		public tup() {
		}
		@Override
		public int compareTo(tup o){
			return b == o.b ? Integer.compare(a, o.a) : Integer.compare(b, o.b);
		}
		@Override
		public int compare(tup o1, tup o2) {
			return o1.b == o2.b ? Integer.compare(o1.a, o2.a) : Integer.compare(o1.b,  o2.b);
		}
		
		@Override
	    public int hashCode() {
			return Objects.hash(a, b);
	    }
 
	    @Override
	    public boolean equals(Object obj) {
	    	if (this == obj)
                return true;
	    	if (obj == null)
                return false;
	    	if (getClass() != obj.getClass())
                return false;
	    	tup other = (tup) obj;
	    	return a==other.a && b==other.b;
	    }
	    
	    @Override
	    public String toString() {
	    	return a + " " + b;
	    }
	}

	static class FastReader {
		BufferedReader br;
		StringTokenizer st;

		public FastReader() {
			br = new BufferedReader(new InputStreamReader(System.in));
		}

		public FastReader(String s) throws FileNotFoundException {
			br = new BufferedReader(new FileReader(new File(s)));
		}

		String next() {
			while (st == null || !st.hasMoreElements()) {
				try {
					st = new StringTokenizer(br.readLine());
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
			return st.nextToken();
		}

		int nextInt() {
			return Integer.parseInt(next());
		}

		long nextLong() {
			return Long.parseLong(next());
		}

		double nextDouble() {
			return Double.parseDouble(next());
		}

		String nextLine() {
			String str = "";
			try {
				str = br.readLine();
			} catch (IOException e) {
				e.printStackTrace();
			}
			return str;
		}
	}

}