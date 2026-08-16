import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.NoSuchElementException;

public class Main{
	static final int INF = (int)1e9 + 7;
	int N,u,v;
	ArrayList<Integer>[] G;
	int[] prev1,prev2;

	public void dijkstra(int s,int[] dis,int[] prev){
		Arrays.fill(prev, -1);
		Arrays.fill(dis, INF);
		dis[s] = 1;

		ArrayDeque<int[]> q = new ArrayDeque<int[]>();
		q.add(new int[]{s,1});

		while(q.size() > 0){
			int[] p = q.poll();
			if(dis[p[0]] < p[1])continue;
			for(int n : G[p[0]]){
				if(dis[p[0]]+1 <= N/2 && dis[n] > dis[p[0]]+1){
					dis[n] = dis[p[0]]+1;
					q.add(new int[]{n,p[1]+1});
					prev[n] = p[0];
				}
			}
		}
	}

	public ArrayList<Integer> getPath(int t,int[] prev){
		ArrayList<Integer> path = new ArrayList<Integer>();
		for(;t != -1;t = prev[t])path.add(t);
		Collections.reverse(path);
		return path;
	}

	@SuppressWarnings("unchecked")
	public void solve() {
		N = nextInt();
		u = nextInt()-1;
		v = nextInt()-1;

		G = new ArrayList[N];
		for(int i = 0;i < N;i++)G[i] = new ArrayList<Integer>();
		for(int i = 0;i < N-1;i++){
			int a = nextInt()-1;
			int b = nextInt()-1;
			G[a].add(b);
			G[b].add(a);
		}

		if(N % 2 == 1){
			out.println("No");
			return;
		}
		int[] dis1 = new int[N],dis2 = new int[N];
		prev1 = new int[N];
		prev2 = new int[N];
		dijkstra(u,dis1,prev1);
		dijkstra(v,dis2,prev2);

		ArrayList<Integer> du = new ArrayList<Integer>(),dv = new ArrayList<Integer>();
		for(int i = 0;i < N;i++){
			if(dis1[i] == N/2)du.add(i);
			if(dis2[i] == N/2)dv.add(i);
		}

		if(du.size() == 0 || dv.size() == 0){
			out.println("No");
			return;
		}
		boolean[] used = new boolean[N];
		for(int i = 0;i < du.size();i++){
			for(int j = 0;j < dv.size();j++){
				Arrays.fill(used, false);

				for(int n : getPath(du.get(i),prev1)){
					used[n] = true;
				}
				boolean flag = true;
				for(int n : getPath(dv.get(j),prev2)){
					if(used[n]){
						flag = false;
						break;
					}
				}

				if(flag){
					out.println("Yes");
					return;
				}
			}
		}
		out.println("No");

	}

	public static void main(String[] args) {
		out.flush();
		new Main().solve();
		out.close();
	}

	/* Input */
	private static final InputStream in = System.in;
	private static final PrintWriter out = new PrintWriter(System.out);
	private final byte[] buffer = new byte[2048];
	private int p = 0;
	private int buflen = 0;

	private boolean hasNextByte() {
		if (p < buflen)
			return true;
		p = 0;
		try {
			buflen = in.read(buffer);
		} catch (IOException e) {
			e.printStackTrace();
		}
		if (buflen <= 0)
			return false;
		return true;
	}

	public boolean hasNext() {
		while (hasNextByte() && !isPrint(buffer[p])) {
			p++;
		}
		return hasNextByte();
	}

	private boolean isPrint(int ch) {
		if (ch >= '!' && ch <= '~')
			return true;
		return false;
	}

	private int nextByte() {
		if (!hasNextByte())
			return -1;
		return buffer[p++];
	}

	public String next() {
		if (!hasNext())
			throw new NoSuchElementException();
		StringBuilder sb = new StringBuilder();
		int b = -1;
		while (isPrint((b = nextByte()))) {
			sb.appendCodePoint(b);
		}
		return sb.toString();
	}

	public int nextInt() {
		return Integer.parseInt(next());
	}

	public long nextLong() {
		return Long.parseLong(next());
	}

	public double nextDouble() {
		return Double.parseDouble(next());
	}
}