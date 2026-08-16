import java.util.HashSet;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

//Cubic Eight-Puzzle
public class Main{

	int[] top = {0, 0, 1, 1, 2, 2, 3};
	int[][] d = {{-1,0},{0,1},{1,0},{0,-1}};
	int[][] adj = {
			{2, 5, 2, 5},
			{4, 3, 4, 3},
			{0, 4, 0, 4},
			{5, 1, 5, 1},
			{1, 2, 1, 2},
			{3, 0, 3, 0}
	};

	int[][] goal, state;
	Map<String, Integer>[][] ref;
	//
	//	void bfs(int si, int sj){
	//		int[][] init = new int[3][3];
	//		init[si][sj] = 6;
	//		ref[si][sj] = new HashMap<String, Integer>();
	//		ref[si][sj].put(get(init), 0);
	//		int step = 1;
	//		Set<String> u = new HashSet<String>();
	//		u.add(trans(init));
	//		List<String> l = new ArrayList<String>();
	//		l.add(trans(init));
	//		int[][] tmp = new int[3][3];
	//		while(!l.isEmpty()&&step<=10){
	//			System.out.println(step+" "+u.size());
	//			List<String> next = new ArrayList<String>();
	//			for(String r:l){
	////				System.out.println("step:"+step+" R:"+r);
	//				int ei = -1, ej = -1;
	//				for(int i=0;i<3;i++)for(int j=0;j<3;j++){
	//					tmp[i][j] = r.charAt(i*3+j)-'0';
	//					if(tmp[i][j]==6){
	//						ei = i; ej = j;
	//					}
	//				}
	////				System.out.println(ei+","+ej);
	//				for(int k=0;k<4;k++){
	//					int ni = ei+d[k][0], nj = ej+d[k][1];
	//					if(0<=ni&&ni<3&&0<=nj&&nj<3){
	//						tmp[ei][ej] = adj[tmp[ni][nj]][k]; tmp[ni][nj] = 6;
	//						String tops = get(tmp), nr = trans(tmp);
	//						if(!ref[si][sj].containsKey(tops))ref[si][sj].put(tops, step);
	//						if(!u.contains(nr)){
	//							u.add(nr); next.add(nr);
	//						}
	//						tmp[ni][nj] = adj[tmp[ei][ej]][k]; tmp[ei][ej] = 6;
	//					}
	//				}
	//			}
	//
	//			l = next;
	//			step++;
	//		}
	//	}

	String get(int[][] s){
		StringBuilder sb = new StringBuilder();
		for(int i=0;i<3;i++)for(int j=0;j<3;j++)sb.append(top[s[i][j]]);
		return sb.toString();
	}
	String trans(int[][] s){
		StringBuilder sb = new StringBuilder();
		for(int i=0;i<3;i++)for(int j=0;j<3;j++)sb.append(s[i][j]);
		return sb.toString();
	}

	Set<String> u;
	boolean dfs(int ei, int ej, int depth, int limit, int pre){
		//		System.out.println("Depth:"+depth+" Limit:"+limit);
		int dif = 0;
		for(int i=0;i<3;i++)for(int j=0;j<3;j++)dif+=top[state[i][j]]!=goal[i][j]?1:0;
		if(dif==0)return true;
		if(limit<depth)return false;
		if(limit<depth+dif-1)return false;
//		String s = trans(state);
//		if(u.contains(s))return false;
//		u.add(s);
		for(int k=0;k<4;k++){
			if(pre==(k+2)%4)continue;
			int ni = ei+d[k][0], nj = ej+d[k][1];
			if(0<=ni&&ni<3&&0<=nj&&nj<3){
				state[ei][ej] = adj[state[ni][nj]][k]; state[ni][nj] = 6;
				if(dfs(ni, nj, depth+1, limit, k))return true;
				state[ni][nj] = adj[state[ei][ej]][k]; state[ei][ej] = 6;
			}
		}
		return false;
	}

	void run(){
		//		ref = new Map[3][3];
		//		for(int i=0;i<3;i++)for(int j=0;j<3;j++)bfs(i, j);
		//		System.out.println("OK");
		Scanner sc = new Scanner(System.in);
		for(;;){
			int x = sc.nextInt(), y = sc.nextInt();
			if((x|y)==0)break;
			goal = new int[3][3];
			for(int i=0;i<3;i++)for(int j=0;j<3;j++){
				char c = sc.next().charAt(0);
				goal[i][j] = c=='W'?0:c=='R'?1:c=='B'?2:3;
			}
			state = new int[3][3];
			for(int i=0;i<3;i++)for(int j=0;j<3;j++){
				state[i][j] = i+1==y&&j+1==x?6:0;
			}
			int res = -1;
			for(int L=0;L<=30;L++){
				u = new HashSet<String>();
				if(dfs(y-1, x-1, 0, L, -1)){
					res = L; break;
				}
				//				System.out.println("Limit:"+L+" visit state:"+u.size());
			}
			System.out.println(res);
		}
	}

	public static void main(String[] args) {
		new Main().run();
	}
}