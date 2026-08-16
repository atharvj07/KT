import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.util.*;

// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail


public class Ideone {
	final static class Edge{
		int v;
		int w;
		public Edge(int v, int w) {
			this.v = v;
			this.w = w;
		}
	}
	static class Cell{
		
		long d;
		int s;
		int u;
		public Cell(long d, int s, int u) {
			this.d = d;
			this.s = s;
			this.u = u;
		}
	}
	public static void main(String args[]) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int [] ta = nia(br);
		int n = ta[0];
		int m = ta[1];
		int ec = 0;
		int i, j;
		List<Edge>[]g = new ArrayList[n+1];
		while(m-- > 0) {
			ta = nia(br);
			if(g[ta[0]] == null)
				g[ta[0]] = new ArrayList<Edge>();
			if(g[ta[1]] == null)
				g[ta[1]] = new ArrayList<Edge>(); 
			
			g[ta[0]].add(new Edge(ta[1], ta[2]));
			g[ta[1]].add(new Edge(ta[0], ta[2]));
				
		}
		long da[][] = new long[n+1][4];
		long visited[][] = new long[n+1][4];

		Cell lta;
		for(i =0; i < n+1; i++)
			Arrays.fill(da[i],  Long.MAX_VALUE);
		//Arrays.fill(d[1],  0);
		Queue<Cell> pq = new PriorityQueue<>(100000, (a,b) -> a.d >= b.d? 1 : -1 );
		pq.offer(new Cell(0, 0, 1));
		while(!pq.isEmpty()) {
			lta = pq.poll();
			int state = lta.s;
			int u = lta.u;
			long d = da[lta.u][lta.s];
			if(visited[u][state] == 1)
				continue;
			visited[u][state] = 1;
			da[u][state] = d= lta.d;
			ec++;
			if(ec > 4 * n + 2)
				break;
			
			if(lta.s == 0) {
				for(Edge e: g[u]) {
					if(da[e.v][0] > d+ e.w) {
						 da[e.v][0] =  d+ e.w;
						 pq.offer(new Cell(d+ e.w,     0, e.v));
					}
					
					if(da[e.v][1] > d) {
						 da[e.v][1] =  d;
						 pq.offer(new Cell(d,          1, e.v));
					}
					
					if(da[e.v][2] > d+ 2 * e.w) {
						 da[e.v][2] =  d+ 2 * e.w;
	 					 pq.offer(new Cell(d+ 2 * e.w, 2, e.v));
					}
					
					if(da[e.v][3] > d+ e.w) {
						 da[e.v][3] =  d+ e.w;
						 pq.offer(new Cell(d + e.w,          3, e.v));
					}
				}
				
			}
			else if(lta.s == 1) {//max
				for(Edge e: g[u]) {
					if(da[e.v][1] > d+ e.w) {
						 da[e.v][1] =  d+ e.w;
						 pq.offer(new Cell(d+ e.w,     1, e.v));

					}
					
					if(da[e.v][3] > d+ 2 * e.w) {
						 da[e.v][3] =  d + 2 * e.w;
						 pq.offer(new Cell(d+ 2 * e.w, 3, e.v));

					}
				}
				
			}
			else if(lta.s == 2) {//min
				for(Edge e: g[u]) {
					if(da[e.v][2] > d+ e.w) {
						 da[e.v][2] =  d+ e.w;
						  pq.offer(new Cell(d+ e.w,     2, e.v));

					}
					if(da[e.v][3] > d) {
						 da[e.v][3] =  d;
						 pq.offer(new Cell(d , 3, e.v));

					}
				}
				
			}
			else {
				for(Edge e: g[u]) 
					if(da[e.v][3] > d+ e.w) {
						  da[e.v][3] =  d + e.w;
	 				      pq.offer(new Cell(d+ e.w, 3, e.v));
					}
				
			}
		}
		for( i = 2; i <=n; i++) {
			System.out.print(da[i][3] + " ");
		}
		
//		int t = ni(br.readLine());
//		
// 		while(t-- > 0) {
// 			
// 		}
		
	}
	
	
//////////////////////////////////////////////////////////////////////////////////////////////////////
	static Integer[] nIa(BufferedReader br) throws Exception {
		String sa[] = br.readLine().split(" ");
		Integer[] a = new Integer[sa.length];
		for (int i = 0; i < sa.length; i++) {
			a[i] = ni(sa[i]);
		}
		return a;
	}

	static int[] nia(BufferedReader br) throws Exception {
		String sa[] = br.readLine().split(" ");
		int[] a = new int[sa.length];
		for (int i = 0; i < sa.length; i++) {
			a[i] = ni(sa[i]);
		}
		return a;
	}

	static long[] nla(BufferedReader br) throws Exception {
		String sa[] = br.readLine().split(" ");
		long[] a = new long[sa.length];
		for (int i = 0; i < sa.length; i++) {
			a[i] = nl(sa[i]);
		}
		return a;
	}

	static int ni(String s) {
		return Integer.parseInt(s);
	}

	static long nl(String s) {
		return Long.parseLong(s);
	}

	static float nf(String s) {
		return Float.parseFloat(s);
	}

	static double nd(String s) {
		return Double.parseDouble(s);
	}

	////// specific to problem

	static int[][] nia(BufferedReader br, int a[][]) throws Exception {
		for (int i = 0; i < a.length; i++) {
			String sa[] = br.readLine().split(" ");
			a[i][0] = ni(sa[0]);
			a[i][1] = ni(sa[1]);
		}
		return a;
	}

}
