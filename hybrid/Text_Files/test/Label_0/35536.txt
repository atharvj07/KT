import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.Closeable;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;

public class Main {
	static ContestScanner in;
	static Writer out;
	public static void main(String[] args) {
		Main main = new Main();
		try {
			in = new ContestScanner();
			out = new Writer();
			main.solve();
			out.close();
			in.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	void solve() throws IOException {
		while(true) {
			int n = in.nextInt();
			int m = in.nextInt();
			if(n == 0) break;
			int hlim = in.nextInt();
			int rn = in.nextInt();
			@SuppressWarnings("unchecked")
			List<Edge>[] node = new List[n];
			for(int i = 0; i < n; i++) node[i] = new ArrayList<>();
			for(int i = 0; i < m; i++) {
				int a = in.nextInt() - 1;
				int b = in.nextInt() - 1;
				int c = in.nextInt();
				int h = in.nextInt();
				int r = in.nextInt() - 1;
				node[a].add(new Edge(b, c, h, r));
				node[b].add(new Edge(a, c, h, r));
			}
			int s = in.nextInt() - 1;
			int t = in.nextInt() - 1;
			int pn = in.nextInt();
			boolean[] k = new boolean[rn];
			int min = getMin(node, hlim, s, t, k);
			int[] d = new int[pn];
			int[] ks = new int[pn];
			for(int i = 0; i < pn; i++) {
				int l = in.nextInt();
				d[i] = in.nextInt();
				for(int j = 0; j < l; j++) {
					ks[i] |= 1 << in.nextInt() - 1;
				}
			}
			int[] da = new int[1 << rn];
			ticketList(d, ks, da);
			for(int i = 0; i < da.length; i++) {
				if(da[i] == inf) continue;
				Arrays.fill(k, false);
				for(int j = 0; j < rn; j++) {
					if((i & 1 << j) > 0) k[j] = true;
				}
				min = Math.min(min, da[i] + getMin(node, hlim, s, t, k));
			}
			if(min == inf) min = -1;
			out.println(min);
		}
	}
	
	void ticketList(int[] d, int[] ks, int[] da) {
		Arrays.fill(da, inf);
		for(int i = 0; i < ks.length; i++) {
			da[ks[i]] = d[i];
		}
		for(int i = 0; i < da.length; i++) {
			for(int j = i + 1; j < da.length; j++) {
				da[i | j] = Math.min(da[i | j], da[i] + da[j]);
			}
		}
	}
	
	final int inf = Integer.MAX_VALUE / 2;
	int getMin(List<Edge>[] node, int hlim, int s, int t, boolean[] k) {
		final int n = node.length;
		int[][] cost = new int[n][hlim + 1];
		for(int i = 0; i < n; i++) {
			Arrays.fill(cost[i], inf);
		}
		Queue<Pos> qu = new PriorityQueue<>();
		qu.add(new Pos(s, 0, 0));
		while(!qu.isEmpty()) {
			Pos p = qu.poll();
			if(cost[p.id][p.time] < inf) continue;
			cost[p.id][p.time] = p.cost;
			if(p.id == t) return p.cost;
			for(Edge e: node[p.id]) {
				final int ntime = p.time + e.hour;
				final int ncost = p.cost + (k[e.ret] ? 0 : e.cost);
				if(ntime > hlim || cost[e.to][ntime] <= ncost)
					continue;
//				out.printf("%d -> %d (time: %d -> %d, cost: %d -> %d)\n",
//						p.id, e.to, p.time, ntime, p.cost, ncost);
				qu.add(new Pos(e.to, ntime, ncost));
			}
		}
		return inf;
	}
}

class Pos implements Comparable<Pos> {
	int id, time, cost;
	public Pos(int id, int t, int c) {
		this.id = id;
		time = t;
		cost = c;
	}
	@Override
	public int compareTo(Pos o) {
		return cost - o.cost;
	}
}

class Edge {
	int to, cost, hour, ret;
	public Edge(int t, int c, int h, int r) {
		to = t;
		cost = c;
		hour = h;
		ret = r;
	}
}

@SuppressWarnings("serial")
class MultiSet<T> extends HashMap<T, Integer>{
	@Override public Integer get(Object key){return containsKey(key)?super.get(key):0;}
	public void add(T key,int v){put(key,get(key)+v);}
	public void add(T key){put(key,get(key)+1);}
	public void sub(T key){final int v=get(key);if(v==1)remove(key);else put(key,v-1);}
	public MultiSet<T> merge(MultiSet<T> set)
	{MultiSet<T>s,l;if(this.size()<set.size()){s=this;l=set;}else{s=set;l=this;}
	for(Entry<T,Integer>e:s.entrySet())l.add(e.getKey(),e.getValue());return l;}
}

class Writer extends PrintWriter{
	public Writer(String filename)throws IOException
	{super(new BufferedWriter(new FileWriter(filename)));}
	public Writer()throws IOException{super(System.out);}
}
class ContestScanner implements Closeable{
	private BufferedReader in;private int c=-2;
	public ContestScanner()throws IOException 
	{in=new BufferedReader(new InputStreamReader(System.in));}
	public ContestScanner(String filename)throws IOException
	{in=new BufferedReader(new InputStreamReader(new FileInputStream(filename)));}
	public String nextToken()throws IOException {
		StringBuilder sb=new StringBuilder();
		while((c=in.read())!=-1&&Character.isWhitespace(c));
		while(c!=-1&&!Character.isWhitespace(c)){sb.append((char)c);c=in.read();}
		return sb.toString();
	}
	public String readLine()throws IOException{
		StringBuilder sb=new StringBuilder();if(c==-2)c=in.read();
		while(c!=-1&&c!='\n'&&c!='\r'){sb.append((char)c);c=in.read();}
		return sb.toString();
	}
	public long nextLong()throws IOException,NumberFormatException
	{return Long.parseLong(nextToken());}
	public int nextInt()throws NumberFormatException,IOException
	{return(int)nextLong();}
	public double nextDouble()throws NumberFormatException,IOException 
	{return Double.parseDouble(nextToken());}
	public void close() throws IOException {in.close();}
}