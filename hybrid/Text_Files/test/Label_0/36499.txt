import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.InputMismatchException;
import java.util.PriorityQueue;

public class CompleteTheGraph {
	private static final long MAX = 1000000000000L;
	
    public static void main(String[] args) {
        FasterScanner sc = new FasterScanner();
        
        int N = sc.nextInt();
        int M = sc.nextInt();
        long L = sc.nextLong();
        int S = sc.nextInt();
        int T = sc.nextInt();
        
        Node[] nodes = new Node[N];
        Edge[] edges = new Edge[M];
        
        for (int i = 0; i < N; i++) {
        	nodes[i] = new Node(i);
        }
        
        for (int i = 0; i < M; i++) {
        	int U = sc.nextInt();
        	int V = sc.nextInt();
        	long W = sc.nextLong();
        	edges[i] = new Edge(U, V, W);
        	nodes[U].next.put(nodes[V], edges[i]);
        	nodes[V].next.put(nodes[U], edges[i]);
        }

        Node[] prev = new Node[N];
        long[] dist = new long[N];
        
        setBlanks(edges, 1);
        
        calcDist(nodes[S], nodes[T], N, dist, prev);
        
        if (dist[T] > L) {
        	System.out.println("NO");
        	return;
        }
        
        Edge[] path = getBlanksOnPath(nodes[T], prev, nodes);
        int P = path.length;
        
        setBlanks(edges, MAX);
        
        long lo = 0;
        long hi = P * (MAX - 1);
        long good = -1;
        while (lo <= hi) {
        	long mid = (lo + hi) / 2;
        	
        	setBlanks(path, 1);
        	
        	long rem = mid;
        	for (int i = 0; i < P && rem > 0; i++) {
        		long add = Math.min(rem, MAX - 1);
        		path[i].weight += add;
        		rem -= add;
        	}
        	
        	calcDist(nodes[S], nodes[T], N, dist, prev);
        	
        	if (dist[T] < L) {
        		lo = mid + 1;
        	} else if (dist[T] > L) {
        		hi = mid - 1;
        	} else {
        		good = mid;
        		break;
        	}
        }
        
        if (good < 0) {
        	System.out.println("NO");
        	return;
        }

        StringBuilder sb = new StringBuilder();
        for (Edge e : edges) {
        	sb.append(String.format("%d %d %d\n", e.U, e.V, e.weight));
        }
        System.out.println("YES");
        System.out.print(sb.toString());
    }
    
    public static void setBlanks(Edge[] edges, long w) {
    	for (Edge e : edges) {
    		if (e.blank) {
    			e.weight = w;
    		}
    	}
    }
    
    public static Edge[] getBlanksOnPath(Node start, Node[] prev, Node[] nodes) {
        ArrayList<Edge> lst = new ArrayList<Edge>();
        Node curr = start;
        while (true) {
        	Node pred = prev[curr.index];
        	Edge e = curr.next.get(pred);
        	if (e == null) {
        		break;
        	}
        	if (e.blank) {
        		lst.add(e);
        	}
        	curr = pred;
        }
        return lst.toArray(new Edge[0]);
    }
    
    public static void calcDist(Node start, Node end, int N, long[] dists, Node[] prev) {
    	Arrays.fill(dists, MAX);
    	PriorityQueue<PQElt> pq = new PriorityQueue<PQElt>();
    	PQElt init = new PQElt(0, null, start);
    	pq.offer(init);
    	while (!pq.isEmpty()) {
    		PQElt pqe = pq.poll();
    		long d = pqe.dist;
    		Node p = pqe.pred;
    		Node u = pqe.trgt;
    		if (d < dists[u.index]) {
    			dists[u.index] = d;
    			prev[u.index] = p;
    			if (u == end) {
    				break;
    			}
    			for (Node v : u.next.keySet()) {
    				Edge e = u.next.get(v);
    				long w = e.weight;
    				if (d + w < dists[v.index]) {
    					PQElt next = new PQElt(d + w, u, v);
    					pq.offer(next);
    				}
    			}
    		}
    	}
    }
    
    public static class PQElt implements Comparable<PQElt> {
    	public long dist;
    	public Node pred;
    	public Node trgt;
    	
    	public PQElt(long d, Node p, Node t) {
    		this.dist = d;
    		this.pred = p;
    		this.trgt = t;
    	}
    	
    	public int compareTo(PQElt pqe) {
    		return Long.compare(this.dist, pqe.dist);
    	}
    }
    
    public static class Edge {
    	public int U, V;
    	public long weight;
    	
    	public boolean blank;
    	
    	public Edge(int u, int v, long w) {
    		this.U = u;
    		this.V = v;
    		this.weight = w;
    		this.blank = (w == 0);
    	}
    }
    
    public static class Node {
    	public int index;
    	public HashMap<Node, Edge> next = new HashMap<Node, Edge>();
    	
    	public Node(int idx) {
    		this.index = idx;
    	}
    }
    
	public static class FasterScanner {
		private byte[] buf = new byte[1024];
		private int curChar;
		private int numChars;

		public int read() {
			if (numChars == -1)
				throw new InputMismatchException();
			if (curChar >= numChars) {
				curChar = 0;
				try {
					numChars = System.in.read(buf);
				} catch (IOException e) {
					throw new InputMismatchException();
				}
				if (numChars <= 0)
					return -1;
			}
			return buf[curChar++];
		}

		public String nextLine() {
			int c = read();
			while (isSpaceChar(c))
				c = read();
			StringBuilder res = new StringBuilder();
			do {
				res.appendCodePoint(c);
				c = read();
			} while (!isEndOfLine(c));
			return res.toString();
		}

		public String nextString() {
			int c = read();
			while (isSpaceChar(c))
				c = read();
			StringBuilder res = new StringBuilder();
			do {
				res.appendCodePoint(c);
				c = read();
			} while (!isSpaceChar(c));
			return res.toString();
		}

		public long nextLong() {
			int c = read();
			while (isSpaceChar(c))
				c = read();
			int sgn = 1;
			if (c == '-') {
				sgn = -1;
				c = read();
			}
			long res = 0;
			do {
				if (c < '0' || c > '9')
					throw new InputMismatchException();
				res *= 10;
				res += c - '0';
				c = read();
			} while (!isSpaceChar(c));
			return res * sgn;
		}

		public int nextInt() {
			int c = read();
			while (isSpaceChar(c))
				c = read();
			int sgn = 1;
			if (c == '-') {
				sgn = -1;
				c = read();
			}
			int res = 0;
			do {
				if (c < '0' || c > '9')
					throw new InputMismatchException();
				res *= 10;
				res += c - '0';
				c = read();
			} while (!isSpaceChar(c));
			return res * sgn;
		}
	        
	    public int[] nextIntArray(int n) {
	        int[] arr = new int[n];
	        for (int i = 0; i < n; i++) {
	            arr[i] = nextInt();
	        }
	        return arr;
	    }
        
		public long[] nextLongArray(int n) {
		    long[] arr = new long[n];
		    for (int i = 0; i < n; i++) {
		        arr[i] = nextLong();
		    }
		    return arr;
		}

	    private boolean isSpaceChar(int c) {
			return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
		}

		private boolean isEndOfLine(int c) {
			return c == '\n' || c == '\r' || c == -1;
		}
	}
}