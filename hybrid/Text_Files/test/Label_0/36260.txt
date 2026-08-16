import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;



public class Main{
	Scanner sc;
	int INF = 1<<27;
	
	int[][] map;
	int X, Y;
	int N;
	int[] start;
	int[] d_list;
	int[] s_list;
	int[] e_list;
	
	int[][] ofs = { {0, 1}, {0, -1}, {1, 0}, {-1, 0} };
	
	int[][][] dp;
	int[] ans;
	
	void solve(){
		dp = new int[X][Y][1<<N];
		ans = new int[1<<N];
		
		for(int x=0; x<X; ++x)for(int y=0; y<Y; ++y)for(int n=0; n<1<<N; ++n){
			dp[x][y][n] = INF;
		}
		Arrays.fill(ans, -1);
		
		dp[start[0]][start[1]][0] = 0;
		ans[0] = 0;
		bfs(0, start[0], start[1], 0);
		
		for( int from = 0; from < 1<<N; ++from ){
			for( int to = 0; to < N; ++to ){
				if( ((from>>to)&0x01) == 0x00 ){
					LinkedList<ArrayList<Integer>> req = get_req( to );
					Iterator<ArrayList<Integer>> ite = req.iterator();
					
					while(ite.hasNext()){
						ArrayList<Integer> e = ite.next();
						int x = e.get(0);
						int y = e.get(1);
						
						if( dp[x][y][from] < e_list[to] ){
							if( s_list[to] <= dp[x][y][from] ){
								dp[x][y][from | (1<<to)] = Math.min(dp[x][y][from | (1<<to)], dp[x][y][from]);
								bfs(from | (1<<to), x, y, dp[x][y][from | (1<<to)]);
								ans[from | (1<<to)] = ans[from] + d_list[to];
							}else{
								assert( dp[x][y][from] < s_list[to] );
								int d = s_list[to] - dp[x][y][from];
								if( d%2==1 ) ++d;
								assert( s_list[to] <= dp[x][y][from] + d );
								if( dp[x][y][from] + d < e_list[to] ){
									dp[x][y][from | (1<<to)] = Math.min(dp[x][y][from | (1<<to)], dp[x][y][from] + d);
									bfs(from | (1<<to), x, y, dp[x][y][from | (1<<to)]);
									ans[from | (1<<to)] = ans[from] + d_list[to];
								}
							}
						}
					}
				}
			}
		}
		
		int max = -1;
		for(int i=0; i<1<<N; ++i){
			max = Math.max(max, ans[i]);
		}
		assert(max>=0);
		
		System.out.println(max);
	}
	
	void bfs(int n, int sx, int sy, int scost){
		Queue<Integer> qx = new LinkedList<Integer>();
		Queue<Integer> qy = new LinkedList<Integer>();
		
		qx.add(sx);
		qy.add(sy);
		boolean[][] done = new boolean[Y][X];
		done[sy][sx] = true;
		
		while(qx.size()>0){
			int[] p = new int[]{qx.poll(), qy.poll()};
			assert(qx.size() == qx.size());
			
			for( int[] ope : ofs ){
				int[] e = new int[]{p[0], p[1]};
				e[0] += ope[0];
				e[1] += ope[1];
				if( isSafe(e[0], e[1]) ){
					if( !done[e[1]][e[0]] && map[e[1]][e[0]] == -1 ){
						done[e[1]][e[0]] = true;
						dp[e[0]][e[1]][n] = Math.min(dp[e[0]][e[1]][n], dp[p[0]][p[1]][n] + 1);
						qx.add(e[0]);
						qy.add(e[1]);
					}
				}
			}
		}
	}
	
	void run(){
		sc = new Scanner(System.in);
		while(true){
			X = ni();
			Y = ni();
			if((X|Y)==0) break;
			map = new int[Y][X];
			
			start = new int[2];
			for(int y=0; y<Y; ++y)for(int x=0; x<X; ++x){
				char c = sc.next().charAt(0);
				if(c=='.'){
					map[y][x] = -1;
				}else if(c=='P'){
					map[y][x] = -1;
					start[0] = x;
					start[1] = y;
				}else{
					map[y][x] = c - '0';
				}
			}
			
			N = ni();
			d_list = new int[N];
			s_list = new int[N];
			e_list = new int[N];
			for(int i=0; i<N; ++i){
				int g = ni();
				int d = ni();
				int s = ni();
				int e = ni();
				assert(g==i);
				
				d_list[i] = d;
				s_list[i] = s;
				e_list[i] = e;
			}
			
			solve();
		}
		sc.close();
	}
	
	LinkedList<ArrayList<Integer>> get_req(int trg){
		HashSet<ArrayList<Integer>> set = new HashSet<ArrayList<Integer>>();
		for(int y=0; y<Y; ++y)for(int x=0; x<X; ++x){
			int[] e = new int[]{x, y};
			if(map[e[1]][e[0]] == -1){
				for(int[] ope : ofs){
					int[] buf = new int[]{e[0], e[1]};
					buf[0] += ope[0];
					buf[1] += ope[1];
					
					if(isSafe(buf[0], buf[1])){
						if( map[buf[1]][buf[0]] == trg ){
							ArrayList<Integer> p = new ArrayList<Integer>();
							p.add(e[0]);
							p.add(e[1]);
							
							set.add(p);
						}
					}
				}
			}
		}
		
		LinkedList<ArrayList<Integer>> list = new LinkedList<ArrayList<Integer>>();
		Iterator<ArrayList<Integer>> ite = set.iterator();
		while(ite.hasNext()){
			list.add(ite.next());
		}
		
		return list;
	}
	
	int ni(){
		return sc.nextInt();
	}
	
	boolean isSafe(int x, int y){
		return (0<=x && x<X) && (0<=y && y<Y);
	}
	
	public static void main(String[] args){
		new Main().run();
	}
}