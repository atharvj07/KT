import java.util.*;
import java.awt.Point;

public class Main{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		while(true){
			int w = sc.nextInt(), h = sc.nextInt();
			if(w==0 && h==0) break;
			char[][] map = new char[h][w];

			for(int i=0;i<h;i++){
				String s = "";
				for(int j=0;j<w;j++) s += sc.next();
				map[i] = s.toCharArray();
			}

			State st = null;
			Queue<State> open = new PriorityQueue<State>();
			Map<State, State> closed = new HashMap<State, State>();

			for(int x=0;x<w;x++){
				if(map[h-1][x] == 'S'){
					open.add(new State(0, new Foot(x, h-1, true)));
					open.add(new State(0, new Foot(x, h-1, false)));
				}
			}

			int ans = Integer.MAX_VALUE;
			while(!open.isEmpty()){
				st = open.poll();
				if(closed.get(st) != null) continue;
				closed.put(st,st);
				if(st.ans(map)){
					ans = st.cost;
					break;
				}
				open.addAll(st.nexts(map));
			}
			if(ans == Integer.MAX_VALUE) System.out.println("-1");
			else System.out.println(ans);
		}
	}
}

class State implements Comparable<State>{
	int cost;
	Foot foot;

	public State(int cost, Foot foot){
		this.cost = cost;
		this.foot = foot;
	}

	public ArrayList<State> nexts(char[][] map){
		ArrayList<State> al = new ArrayList<State>();

		for(int i=0;i<9;i++){
			Foot f = foot.copy();
			int rst = f.move(i,map);

			if(rst != -1){
				int c = cost;
				c += rst;
				al.add(new State(c,f));
			}
		}
		return al;
	}

	public boolean ans(char[][] map){
		return map[foot.p.y][foot.p.x]=='T';
	}

	public int compareTo(State st){
		return this.cost - st.cost;
	}

	public boolean equals(Object o){
		State st = (State)o;
		return this.foot.p.equals(st.foot.p) &&
			this.foot.nextFlg==st.foot.nextFlg;
	}

	public int hashCode(){
		return foot.p.x + foot.p.y;
	}
}

class Foot{
	Point p;
	boolean nextFlg;

	final int[][] dr = new int[][]{{1,-2}, {1,-1}, {1,0}, {1,1}, {1,2},
																 {2,-1}, {2,0}, {2,1},
																 {3,0}};
	final int[][] dl = new int[][]{{-1,-2}, {-1,-1}, {-1,0}, {-1,1}, {-1,2},
																 {-2,-1}, {-2,0}, {-2,1},
																 {-3,0}};

	public Foot(int x, int y, boolean nextFlg){
		this.p = new Point(x,y);
		this.nextFlg = nextFlg;
	}

	public int move(int to, char[][] map){
		int h = map.length;
		int w = map[0].length;

		if(nextFlg){
			nextFlg = !nextFlg;
			this.p.translate(dl[to][0], dl[to][1]);
		}
		else{
			nextFlg = !nextFlg;
			this.p.translate(dr[to][0], dr[to][1]);
		}

		if(p.x<0 || p.x>=w || p.y<0 || p.y>=h || map[p.y][p.x]=='X')
			return -1;
		else if(map[p.y][p.x] == 'S' || map[p.y][p.x] == 'T')
			return 0;
		else
			return map[p.y][p.x] - '0';
	}

	public Foot copy(){
		Foot cp = new Foot(p.x, p.y, nextFlg);
		return cp;
	}
}