import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

import static java.lang.Integer.parseInt;

/**
 * Zombie Island
 * JOI 15th, Pre 5
 */
public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line;
		String[] words;

		Main main = new Main();

		//
		words = br.readLine().split(" ");
		int N, M, K, S, sta, end;
		N = parseInt(words[0]); //????????°
		M = parseInt(words[1]); //????????¬??°
		K = parseInt(words[2]); //??????????????????????????????
		S = parseInt(words[3]); //????????¬??° <= S ? ??±?????????
		sta = 1;
		end = N;

		words = br.readLine().split(" ");
		int P, Q;
		P = parseInt(words[0]);
		Q = parseInt(words[1]);

		//
		Vertex[] towns = new Vertex[N + 1];
		Graph graph = main.new Graph();

		for (int i = 1; i <= N; i++) {
			towns[i] = main.new Vertex(i);
			graph.addVertex(towns[i]);
		}

		for (int i = 0; i < K; i++) {
			towns[parseInt(br.readLine())].isZombied = true;
		}

		for (int i = 0; i < M; i++) {
			words = br.readLine().split(" ");
			int a = parseInt(words[0]);
			int b = parseInt(words[1]);
			if (b == sta || b == end) {
				graph.addEdge(main.new Edge(towns[a], towns[b], 0));
			} else {
				graph.addEdge(main.new Edge(towns[a], towns[b], P));
			}
			if (a == sta || a == end) {
				graph.addEdge(main.new Edge(towns[b], towns[a], 0));
			} else {
				graph.addEdge(main.new Edge(towns[b], towns[a], P));
			}
		}

		//
		Deque<Vertex> q = new ArrayDeque<>();

		for (int i = 1; i <= N; i++) {
			if (towns[i].isZombied) q.add(towns[i]);
		}
		while (!q.isEmpty()) {
			Vertex v = q.poll();
			for (Edge e : graph.getEdgesTo(v)) {
				e.weight = Q;
				if (!e.from.isZombied
						&& !e.from.isDanger
						&& e.from.id != sta
						&& e.from.id != end) {
					if (v.distance + 1 <= S) {
						e.from.distance = v.distance + 1;
						e.from.isDanger = true;
						q.offer(e.from);
					}
				}
			}
		}

		//Dijkstra
		Map<Vertex, Long> visited = new HashMap<>();
		Queue<Edge> pq = new PriorityQueue<>();

		pq.add(main.new Edge(towns[sta], towns[sta], 0));
		while (!pq.isEmpty()) {

			Edge e = pq.poll();

			if (visited.containsKey(e.to)) continue;
			if (e.to.isZombied) continue;
			visited.put(e.to, e.weight);

			for (Edge _e : graph.getEdgesFrom(e.to)) {
				if (visited.containsKey(_e.to)) continue;
				if (_e.to.isZombied) continue;
				_e.weight += e.weight;
				pq.offer(_e);
			}
		}
		System.out.println(visited.get(towns[end]));
	}

	/**
	 * Helpers
	 */
	class Graph {
		Set<Vertex> vs;
		Map<Vertex, List<Edge>> esf;
		Map<Vertex, List<Edge>> est;

		Graph() {
			this.vs = new HashSet<>();
			this.esf = new HashMap<>();
			this.est = new HashMap<>();
		}

		void addVertex(Vertex v) {
			if (!vs.contains(v)) vs.add(v);
			if (!esf.containsKey(v)) esf.put(v, new ArrayList<>());
			if (!est.containsKey(v)) est.put(v, new ArrayList<>());
		}

		void addEdge(Edge e) {
			addVertex(e.from);
			addVertex(e.to);
			esf.get(e.from).add(e);
			est.get(e.to).add(e);
		}

		List<Edge> getEdgesFrom(Vertex v) {
			return esf.get(v);
		}

		List<Edge> getEdgesTo(Vertex v) {
			return est.get(v);
		}
	}

	class Vertex {
		int id;
		//properties
		boolean isZombied;
		boolean isDanger;
		int distance;

		Vertex(int id) {
			this.id = id;
		}
	}

	class Edge implements Comparable<Edge> {
		Vertex from, to;
		//properties
		long weight;

		Edge(Vertex from, Vertex to) {
			this(from, to, 0);
		}

		Edge(Vertex from, Vertex to, long weight) {
			this.from = from;
			this.to = to;
			this.weight = weight;
		}

		@Override
		public int compareTo(Edge o) {
			return Long.compare(this.weight, o.weight);
		}
	}
}