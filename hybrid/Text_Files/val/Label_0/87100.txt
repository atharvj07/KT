import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	static class Vertex{
		List<Integer> adj;
		public Vertex() {
			adj = new ArrayList<Integer>();
		}
	}
	static List<Integer> findCircuit(Vertex vs[] , int startPoint){
		Vertex v = vs[startPoint];
		if(v.adj.isEmpty()){
			return null;
		}
		Queue<Integer> q = new LinkedList<Integer>();
		q.add(startPoint);
		int N = vs.length;
		int prev[] = new int[N];
		Arrays.fill(prev, -1);
		while(!q.isEmpty()){
			int cur = q.poll();
			Vertex vcur = vs[cur];
			for(int n : vcur.adj){
				if(n == startPoint){ // find circuit
					List<Integer> ret = new ArrayList<Integer>();
					while(prev[cur] != startPoint){
						ret.add(cur);
						cur = prev[cur];
					}
					ret.add(cur);
					ret.add(startPoint);					
					return ret;
				}
				if(prev[n] == -1){
					prev[n] = cur;
					q.add(n);
				}
			}
		}
		return null;
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		Vertex vs[] = new Vertex[N];
		for(int i = 0 ; i < vs.length ; ++i){
			vs[i] = new Vertex();
		}
		for(int i = 0 ; i < M ; ++i){
			int a = sc.nextInt() - 1;
			int b = sc.nextInt() - 1;
			vs[a].adj.add(b);
		}
		List<Integer> minCircuit = null;
		for(int i = 0 ; i < N ; ++i){
			List<Integer> circuit = findCircuit(vs, i);
			if(circuit != null){
				if(minCircuit == null){
					minCircuit = circuit;
				}else if(circuit.size() < minCircuit.size()){
					minCircuit = circuit;
				}
			}
		}
		if(minCircuit == null){
			System.out.println(-1);			
		}else{
			System.out.println(minCircuit.size());
			for(int v : minCircuit){
				System.out.println(v + 1);
			}
		}
	}
}
