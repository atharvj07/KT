import java.util.*;

class Main {
	static final int MOD = 1_000_000_007;
	Scanner sc;
	int N;
	List<Edge>[] edges;
	int[] pow2;
	long pow2Ninv;
	
	static class Edge {
		int from, to, c;
		Edge rev;
		Edge(int from) { this.from = from; }
	}
	
	@SuppressWarnings("unchecked")
	private void calc() {
		sc = new Scanner(System.in);
		N = sc.nextInt();
		edges = new List[N];
		for (int i = 0; i < N; i++) edges[i] = new ArrayList<Edge>();
		Edge f = null;
		Edge b = null;
		for (int i = 0; i < N-1; i++) {
			f = new Edge(sc.nextInt() - 1);
			b = new Edge(sc.nextInt() - 1);
			f.to = b.from; b.to = f.from;
			f.rev = b; b.rev = f;
			edges[b.to].add(f);
			edges[f.to].add(b);
		}
		pow2 = new int[N+1];
		pow2[0] = 1;
		for (int i = 1; i < N+1; i++) pow2[i] = (pow2[i-1] << 1)%MOD;
		pow2Ninv = extgcd(pow2[N], MOD)[1];
		
		countByDFS(f);
		countByDFS(b);
		
		long sum = 0;
		for (int v = 0; v < N; v++) {
			if (edges[v].size() == 1) continue;
			int s = 0;
			for (Edge e : edges[v]) s = (s -1 + pow2[e.c]) % MOD;
			sum = (sum + pow2[N-1] - s - 1 + MOD) % MOD;
		}
		System.out.println(sum*pow2Ninv%MOD);
	}
	
	private void countByDFS(Edge target) {
		int c = 0;
		int from = target.from;
		for (Edge e : edges[target.to]) {
			if (e.to == from) continue;
			countByDFS(e);
			c += e.c;
		}
		target.c = c + 1;
		target.rev.c = N - target.c;
	}
	
	static final long[] extgcd(long a, long b) {
		long aa = a, bb = b;
		long x0 = 1, x1 = 0;
		long y0 = 0, y1 = 1;
	
		while (b != 0) {
			long q = a / b;
			long r = a % b;
			long x2 = x0 - q * x1;
			long y2 = y0 - q * y1;
	
			a = b; b = r;
			x0 = x1; x1 = x2;
			y0 = y1; y1 = y2;
		}
		if (bb > 0 && x0 < 0) {
			long n = -x0/bb;
			if (-x0%bb != 0) n++;
			x0 += n*bb; y0 -= n*aa;
		}
	    return new long[]{a, x0, y0};
	}
	
	public static void main(String[] args) {
		new Main().calc();
	}
}