import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int m = in.nextInt();
		Map<Integer,List<Integer>> map = new HashMap<>();
		for(int i=0;i<m;i++) {
			int u = in.nextInt();
			int v = in.nextInt();
			if(map.containsKey(u)) map.get(u).add(v);
			else {
				List<Integer> list = new ArrayList<>();
				list.add(v);
				map.put(u, list);
			}
		}
		int s = in.nextInt();
		int t = in.nextInt();
		int[][] dist = new int[n+1][3];
		for(int i=0;i<n+1;i++) {
			for(int j=0;j<3;j++) {
				dist[i][j] = 100000000;
			}
		}
		dist[s][0] = 0;
		boolean[][] used = new boolean[n+1][3];
		used[s][0] = true;
		Queue<int[]> deq = new ArrayDeque<>();
		int[] start = {s,0};
		deq.add(start);
		while(!deq.isEmpty()) {
			int[] tmp = deq.poll();
			if(!map.containsKey(tmp[0])) continue;
			for(int next : map.get(tmp[0])) {
				dist[next][(tmp[1]+1)%3] = Math.min(dist[tmp[0]][tmp[1]]+1, dist[next][(tmp[1]+1)%3]);
				if(!used[next][(tmp[1]+1)%3]) {
					int[] tmp2 = {next,(tmp[1]+1)%3};
					deq.add(tmp2);
					used[next][(tmp[1]+1)%3] = true;
				}
			}
		}
		if(dist[t][0]==100000000) System.out.println(-1);
		else System.out.println(dist[t][0]/3);
		
		in.close();

	}

}
