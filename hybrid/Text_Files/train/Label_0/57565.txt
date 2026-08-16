import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;
import static java.lang.Math.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;

public class Main{
	Scanner sc=new Scanner(System.in);

	int INF=1<<28;
	double EPS=1e-12;

	int w, h;
	int s;
	char[][] map;
	char[][][] maps;

	void run(){
		w=sc.nextInt();
		h=sc.nextInt();
		map=new char[h][];
		for(int i=0; i<h; i++){
			map[i]=sc.next().toCharArray();
		}
		s=sc.nextInt();
		maps=new char[s][h][];
		for(int j=0; j<s; j++){
			for(int i=0; i<h; i++){
				maps[j][i]=sc.next().toCharArray();
			}
		}
		solve();
	}

	char WALL='#', STAIRS='|', FIRST='_', SECOND='^', START='%', GOAL='&';

	void solve(){
		int[][][][] d=new int[h][w][2][1<<s];
		for(int j=0; j<h; j++){
			for(int i=0; i<w; i++){
				fill(d[j][i][0], INF);
				fill(d[j][i][1], INF);
			}
		}

		int xs=-1, ys=-1;
		int xg=-1, yg=-1;
		for(int j=0; j<h; j++){
			for(int i=0; i<w; i++){
				if(map[j][i]==START){
					xs=i;
					ys=j;
				}else if(map[j][i]==GOAL){
					xg=i;
					yg=j;
				}
			}
		}

		int[] dx={0, 0, -1, 1};
		int[] dy={-1, 1, 0, 0};

		boolean[][][] ok=new boolean[2][h][w];
		for(int j=0; j<h; j++){
			for(int i=0; i<w; i++){
				char c=map[j][i];
				ok[0][j][i]=c==STAIRS||c==FIRST||Character.isLowerCase(c)
						||c==START||c==GOAL;
				ok[1][j][i]=c==STAIRS||c==SECOND||Character.isUpperCase(c);
			}
		}

		LinkedList<P> que=new LinkedList<P>();
		que.offer(new P(xs, ys, 0, 0));
		d[ys][xs][0][0]=0;

		for(; !que.isEmpty();){
			P p=que.poll();
//			debug(p.x, p.y, p.floor, p.sw, d[p.y][p.x][p.floor][p.sw]);
			int virtualFloor=p.floor;
			for(int i=0; i<s; i++){
				if((p.sw>>i&1)==1&&maps[i][p.y][p.x]=='*'){
					virtualFloor=1-virtualFloor;
				}
			}
			LinkedList<P> next=new LinkedList<P>();
			if(map[p.y][p.x]==STAIRS){
				next.add(new P(p.x, p.y, 1-p.floor, p.sw));
			}
			// スイッチ
			if(Character.isLetter(map[p.y][p.x])){
				int sw=Character.toLowerCase(map[p.y][p.x])-'a';
				if(maps[sw][p.y][p.x]=='*'){
					next.add(new P(p.x, p.y, 1-p.floor, p.sw^(1<<sw)));
				}else{
					next.add(new P(p.x, p.y, p.floor, p.sw^(1<<sw)));
				}
			}
			for(int k=0; k<4; k++){
				P q=new P(p.x+dx[k], p.y+dy[k], p.floor, p.sw);
				int virtualFloor2=q.floor;
				for(int i=0; i<s; i++){
					if((q.sw>>i&1)==1&&maps[i][q.y][q.x]=='*'){
						virtualFloor2=1-virtualFloor2;
					}
				}
				if(ok[virtualFloor2][q.y][q.x]){
					next.add(q);
				}
			}
			for(P q : next){
				if(d[p.y][p.x][p.floor][p.sw]+1<d[q.y][q.x][q.floor][q.sw]){
					d[q.y][q.x][q.floor][q.sw]=d[p.y][p.x][p.floor][p.sw]+1;
					que.offer(q);
				}
			}
		}
		int min=INF;
		for(int sw=0; sw<1<<s; sw++){
			int virtualFloor=0;
			for(int i=0; i<s; i++){
				if((sw>>i&1)==1&&maps[i][yg][xg]=='*'){
					virtualFloor=1-virtualFloor;
				}
			}
			// min=min(min, d[yg][xg][0][sw]);
			if(virtualFloor==0){
				min=min(min, d[yg][xg][0][sw]);
			}else{
				min=min(min, d[yg][xg][1][sw]);
			}
		}
		println((min<INF?min:-1)+"");
	}

	class P{
		int x, y, floor, sw;

		P(int x, int y, int floor, int sw){
			this.x=x;
			this.y=y;
			this.floor=floor;
			this.sw=sw;
		}
	}

	void debug(Object... os){
		System.err.println(Arrays.deepToString(os));
	}

	void print(String s){
		System.out.print(s);
	}

	void println(String s){
		System.out.println(s);
	}

	public static void main(String[] args){
		new Main().run();
	}
}