import java.util.*;

public class Main682C{
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt()+1;
		Node[] v = new Node[n];
		//int[][] d = new int[n][n];
		boolean[] visited = new boolean[n];
		for(int i=1; i<n; i++){
			v[i] = new Node(in.nextInt());
		}
		for(int i=1; i<n-1; i++){
			int des = in.nextInt();
			int dis = in.nextInt();

			v[i+1].children.put(des,dis);
			v[des].children.put(i+1,dis);

		}

		dfs(v,1,0,visited);

		// for(int i=1; i<n; i++){
		// 	if(v[i] != null){
		// 		System.out.println(i+" --> "+v[i].val);
		// 	for(int j : v[i].children){
		// 		System.out.print(j+" ");
		// 	}
		// 	System.out.println();
		// 	}
		// }
		int count =0;
		for(int i=1; i<n; i++){
			if(v[i] == null){
				count++;
			}
		}
		System.out.println(count);
	}

	static void dfs(Node[] v,int root, int max, boolean[] visited){
		//System.out.println(root+" "+max );
		visited[root] = true;
		if(max>v[root].val){
			pruneDfs(v,root,visited);
			return;
		}
		for(int child : v[root].children.keySet()){
			int distance = Math.max(v[root].children.get(child), 
							max + v[root].children.get(child));

			if(!visited[child]){
				dfs(v,child,distance,visited);
			}
		}
		return;
	}

	static void pruneDfs(Node[] v,int root,boolean[] visited){
		visited[root] = true;
		for(int child : v[root].children.keySet()){
			if(!visited[child]){
				pruneDfs(v,child,visited);

			}
		}
		v[root] = null;
	}

	static class Node{
		int val;
		Map<Integer,Integer> children;
		Node(int val){
			this.val = val;
			children = new HashMap<>();
		}
	}
}