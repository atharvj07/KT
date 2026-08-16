import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.Iterator;
import java.util.Stack;

public class Main {
	public static void main(String[] args) {
		Graph g = new Graph();
		g.load_from_edgelist();
		g.helper();
		while(!g.get_order().isEmpty()) {
			System.out.println(g.get_order().pop());
		}
	}
}

class Graph {
	
	private int totalVertex;
	private LinkedList<LinkedList<Integer>> adjList;
	private boolean[] if_visited;
	private int[] discover_time;
	private int[] complete_time;
	private int[] id;
	private static int timestamp = 1;
	private int[] dist;
	private Stack<Integer> order = new Stack<>();
	
	public Stack<Integer> get_order(){
		return order;
	}
	
	public boolean[] getVisited() {
		return if_visited;
	}
	
	public int[] getDistance() {
		return dist;
	}
	
	//adjacency list of edges
	public Graph() { totalVertex = 0; }
	public void loadAdjList() {
		Scanner in = new Scanner(System.in);
		
		totalVertex = in.nextInt();
		adjList = new LinkedList<LinkedList<Integer>>();
		if_visited = new boolean[totalVertex];
		discover_time = new int[totalVertex];
		complete_time = new int[totalVertex];
		id = new int[totalVertex];
		dist = new int[totalVertex];
		
		for(int i = 0; i < totalVertex; i ++) {
			LinkedList<Integer> tmp = new LinkedList<Integer>();
			int idx1 = in.nextInt() - 1;
			if_visited[idx1] = false;
			id[idx1] = i;
			dist[idx1] = 0;
			int degree = in.nextInt();
			//System.out.println("mark idx1 = " + idx1 + " degree = " + degree);
			for(int j = 0; j < degree; j ++) {
				int idx2 = in.nextInt() - 1;
				tmp.add(idx2);
			}	
			adjList.add(tmp);
		}
		in.close();
	}
	
	public void load_from_edgelist() {
		Scanner in = new Scanner(System.in);
		totalVertex = in.nextInt();
		int totalEdges = in.nextInt();
		adjList = new LinkedList<LinkedList<Integer>>();
		if_visited = new boolean[totalVertex];
		//discover_time = new int[totalVertex];
		//complete_time = new int[totalVertex];
		id = new int[totalVertex];
		
		for (int i = 0; i < totalVertex; i++) {
			if_visited[i] = false;
			id[i] = i;
			LinkedList<Integer> tmp = new LinkedList<Integer>();
			adjList.add(tmp);
		}
		
		for (int i = 0; i < totalEdges; i++) {
			int idx1 = in.nextInt();
			int v = in.nextInt();
			adjList.get(idx1).add(v);
		}
		
		in.close();
	}
	
	public void printAdjMatrix() {
		Integer[][] adjMatrix = new Integer[totalVertex][totalVertex];
		//complete the following
		for (int i = 0; i < totalVertex; i++) {
			for (int j = 0; j< totalVertex; j++) {
				if (adjList.get(i).contains(j)) {
					adjMatrix[i][j] = 1;
				}else {
					adjMatrix[i][j] = 0;				
				}
				if (j == totalVertex - 1) {
					System.out.println(adjMatrix[i][j]);
					
				}else {
					System.out.print(adjMatrix[i][j] + " ");
				}
			}
		}
	}
	
	public void DFS(int id) {
			if_visited[id] = true;
			//discover_time[id] = timestamp;
			//timestamp += 1;
			Iterator<Integer> i = adjList.get(id).listIterator();
			while(i.hasNext()) {
				int n = i.next();
				if ( !if_visited[n]) {
					DFS(n);
				}
			}
			order.add(id);
			//complete_time[id] = timestamp++;

		
	}
	
	public void helper() {
		for(int i = 0; i < totalVertex; i++) {
			if(!if_visited[i]) {
				DFS(i);
			}
		}
	}
	
	
	public void show_result() {
		for (int i = 0; i < totalVertex; i++) {
			System.out.print(id[i] + 1 + " ");
			System.out.print(discover_time[id[i]] + " ");
			System.out.print(complete_time[id[i]] + " ");
			System.out.println();
		}
	}
	
	public void BFS(int src) {
		if_visited[src] = true;
		Queue<Integer> q = new LinkedList<>();
		q.add(src);
		while(!q.isEmpty()) {
			int u = q.remove();
			//if_visited[u] = true;
			LinkedList<Integer> tmp = adjList.get(u);
			for(int i = 0; i < tmp.size(); i++) {
				if(!if_visited[tmp.get(i)]) {
					if_visited[tmp.get(i)] = true;
					//if(!q.contains(tmp.get(i))){
					q.add(tmp.get(i));
					dist[tmp.get(i)] = dist[u] + 1;
					//}
				}
			}
		}
	}
	
}


