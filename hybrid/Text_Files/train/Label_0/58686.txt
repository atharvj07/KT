import java.io.*;
import java.util.*;

public class E984{
	
	int[] from;
	int[] to;
	
	int n;
	
	private void solve() throws Exception {
		n = nextInt();
		from = new int[n];
		to = new int[n];
		for(int i = 0; i < n; i++) {
			from[i] = nextInt();
			to[i] = nextInt();
		}
		memo = new HashMap<State, Integer>();
		out.println(doit(new State(0, 1, 0)));
	}
	
	HashMap<State, Integer> memo;
	
	int doit(State state) {
		if(state.passenger == n && state.floors == 0) return 0;
		else if(!memo.containsKey(state)) {
			int best = 1<<30;
			int[] floors = intToArray(state.floors);
			int i = 0;
			while(i < 4 && floors[i] == 0) i++;
			int empty = i;
			while(i < 4 && floors[i] <= state.cur) i++;			
			int down = (1<=i&&i<5)?floors[i-1]:0;
			int up = (0<=i&&i<4)?floors[i]:10;
			if(state.passenger < n && empty > 0 ) {
				if(from[state.passenger] <= state.cur) down = Math.max(from[state.passenger], down);
				else up = Math.min(from[state.passenger], up);
			}					
			if(down > 0) best = Math.min(best, prepare(floors, state.cur, down, state.passenger));
			if(up < 10) best = Math.min(best, prepare(floors, state.cur, up, state.passenger));
			
			memo.put(state, best);
		}		
		return memo.get(state);
	}
	
	int prepare(int[] floors, int cur, int next, int passenger) {
		int cost1 = Math.abs(cur-next);
		
		int[] temp = new int[4];
		int idx = 0;
		int cost2 = 0;
		int free = 0;
		for(int t = 0; t < 4; t++) {
			if(floors[t] == 0) free++;
			else if(floors[t] == next) {
				temp[t] = 0;
				cost2++;
				free++;
			} else temp[idx++] = floors[t];
		}
		
		int cost3 = 0;
		while(cost3 < free && passenger < n && from[passenger] == next) temp[idx+cost3++] = to[passenger++];
		Arrays.sort(temp);
		return cost1+cost2+cost3+doit(new State(arrayToInt(temp), next, passenger));
	}
	
	int[] intToArray(int floors){
		int[] f = new int[4];
		for(int i = 0; i < 4; i++) {
			f[3-i] = floors%10;
			floors/=10;
		}
		return f;
	}
	
	int arrayToInt(int[] floors) {
		int f = 0;
		for(int i = 0; i < 4; i++) {
			f*=10;
			f = f+floors[i];
		}
		return f;
	}
	
	class State{
		int floors;
		int cur;
		int passenger;
		
		public State(int floors, int cur, int next) {
			this.floors = floors;
			this.cur = cur;
			this.passenger = next;
		}

		@Override
		public int hashCode() {
			final int prime = 31;
			int result = 1;
			result = prime * result + getOuterType().hashCode();
			result = prime * result + cur;
			result = prime * result + floors;
			result = prime * result + passenger;
			return result;
		}

		@Override
		public boolean equals(Object obj) {
			if (this == obj)
				return true;
			if (obj == null)
				return false;
			if (getClass() != obj.getClass())
				return false;
			State other = (State) obj;
			if (!getOuterType().equals(other.getOuterType()))
				return false;
			if (cur != other.cur)
				return false;
			if (floors != other.floors)
				return false;
			if (passenger != other.passenger)
				return false;
			return true;
		}

		private E984 getOuterType() {
			return E984.this;
		}
		
		
		
		
	}
	
	public static void main(String[] args) {
		(new E984()).run();
	} 
	
	private BufferedReader in;
	private PrintWriter out;
	private StringTokenizer tokenizer;

	public void run() {
		try {
			in = new BufferedReader(new InputStreamReader(System.in));
			tokenizer = null;
			out = new PrintWriter(System.out);
			solve();
			in.close();
			out.close();
		} catch (Exception e) {
			e.printStackTrace();
			System.exit(1);
		}
	}

	private int nextInt() throws IOException {
		return Integer.parseInt(nextToken());
	}

	private long nextLong() throws IOException {
		return Long.parseLong(nextToken());
	}

	private float nextFloat() throws IOException {
		return Float.parseFloat(nextToken());
	}

	private String nextLine() throws IOException {
		return new String(in.readLine());
	}

	private String nextToken() throws IOException {
		while (tokenizer == null || !tokenizer.hasMoreTokens()) {
			tokenizer = new StringTokenizer(in.readLine());
		}
		return tokenizer.nextToken();
	}
	
	class Edge{
		int v;
		long w;
		
		public Edge(int v, long w){
			this.v = v;
			this.w = w;
		}
	}


}
