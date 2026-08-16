import java.util.*;

public class Main {
	Scanner sc = new Scanner(System.in);
	int [][] data;
	int h,w;
	int [] vx = {0,1,0,-1};
	int [] vy = {1,0,-1,0};
	boolean [][] used;
	class C{
		int step;
		String state;
		public C(int step, String state) {
			this.step = step;
			this.state = state;
		}
	}

	private void doit(){
		while(sc.hasNext()){
			w = sc.nextInt();
			h = sc.nextInt();
			if((w|h) == 0) break;
			data = new int[h][w];
			for(int i = 0; i < h; i++){
				for(int j = 0; j < w; j++){
					char c = sc.next().charAt(0);
					if(c == 'R'){
						data[i][j] = 0;
					}
					else if(c == 'G'){
						data[i][j] = 1;
					}
					else{
						data[i][j] = 2;
					}
				}
			}
			int res = solve();
			System.out.println(res);
		}
	}

	private int solve() {
		LinkedList<C> open = new LinkedList<Main.C>();
		StringBuilder sb = new StringBuilder();
		for(int i = 0; i < h; i++){
			for(int j = 0; j < w; j++){
				sb.append(data[i][j]);
			}
		}
		open.add(new C(0, sb.toString()));
		HashSet<String> close = new HashSet<String>();
		close.add(sb.toString());
		int ans = -1;
		while(! open.isEmpty()){
			C now = open.poll();
			if(isGoal(now.state)){
				ans = now.step;
				break;
			}
			used = new boolean[h][w];
			count(now.state,now.state.charAt(0), 0, 0);
			for(int i = 0; i < 3; i++){
				String nextstate = paint(i, now.state);
				if(! close.contains(nextstate)){
					open.add(new C(now.step + 1, nextstate));
					close.add(nextstate);
				}
			}
		}
		return ans;
	}

	private String paint(int color, String state) {
		StringBuilder sb = new StringBuilder(state);
		for(int i = 0; i < h; i++){
			for(int j = 0; j < w; j++){
				if(used[i][j]){
					int pos = i * w + j;
					sb.setCharAt(pos, (char)(color + '0'));
				}
			}
		}
		return sb.toString();
	}

	private void count(String state, char color, int x, int y) {
		used[y][x] = true;
		for(int i = 0; i < 4; i++){
			int xx = x + vx[i];
			int yy = y + vy[i];
			if(!isOK(xx, yy)) continue;
			if(used[yy][xx]) continue;
			int pos = yy * w + xx;
			if(state.charAt(pos) == color){
				count(state, color, xx, yy);
			}
		}
	}

	private boolean isGoal(String state) {
		char c = state.charAt(0);
		for(int i = 1; i < state.length(); i++){
			if(state.charAt(i) != c){
				return false;
			}
		}
		return true;
	}

	private boolean isOK(int xx, int yy) {
		if(0<= xx && xx < w && 0<= yy && yy < h) return true;
		return false;
	}

	private void debug(Object... o) {
		System.out.println("debug = " + Arrays.deepToString(o));
	}

	public static void main(String[] args) {
		new Main().doit();
	}
}