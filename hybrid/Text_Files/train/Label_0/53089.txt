
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;
public class Main {
	static PrintWriter out = new PrintWriter(System.out);
	static Scanner sc = new Scanner(System.in);
	static int INF = 2 << 20;
	static Node[] node;
	public static void main(String[] args) {
		while(true) {
			int n = sc.nextInt();
			if(n == 0)break;
			node = new Node[101];
			for(int i = 0; i < 101; i++) {
				node[i] = new Node(i);
			}
			for(int i = 0; i < n; i++) {
				int a = sc.nextInt();
				int b = sc.nextInt();
				node[a].to.add(node[b]);
				node[b].to.add(node[a]);
			}
			int ans = 0;
			boolean[] tmp = new boolean[101];
			for(int i = 1; i < 101; i++) {
				if(node[i].to.size() == 0) continue;
				tmp[i] = true;
				ans = Math.max(ans,dfs(i,tmp,1));
				tmp[i] = false;
			}
			System.out.println(ans);
		}
	}
	static int dfs(int now, boolean[] use, int count) {
		int ret = count;
		for(int i = 0; i < node[now].to.size(); i++) {
			int tmp = node[now].to.get(i).id;
			if(use[tmp]) continue;
			use[tmp] = true;
			ret = Math.max(ret, dfs(tmp,use,count+1));
			use[tmp] = false;
		}
		return ret;
	}
	static class Node {
			int id;
			ArrayList<Node> to = new ArrayList<Node>();
			Node(int a) {
				id = a;
			}
	}

}