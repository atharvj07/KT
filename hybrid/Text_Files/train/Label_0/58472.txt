import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.Set;

//Dice Puzzle
public class Main{

	static class Dice <T>{
		public T[] id;
			enum Face{TOP, BOTTOM, FRONT, BACK, RIGHT, LEFT};
			public T get(Face f){
				return id[f.ordinal()];
			}
			public Dice<T> copy(){
				return new Dice<T>(id[0], id[1], id[2], id[3], id[4], id[5]);
			}
			public Dice() {
				@SuppressWarnings("unchecked")
				T[] tid = (T[])new Object[6];
				id = tid;
			}
			public Dice(T top, T bottom, T front, T back, T right, T left) {
				@SuppressWarnings("unchecked")
				T[] tid = (T[])new Object[6];
				id = tid;
				id[Face.TOP.ordinal()] = top;
				id[Face.BOTTOM.ordinal()]= bottom;
				id[Face.FRONT.ordinal()] = front;
				id[Face.BACK.ordinal()] = back;
				id[Face.RIGHT.ordinal()] = right;
				id[Face.LEFT.ordinal()] = left;
			}
			//true: Xツ篠イツ陛サツ古シツづ可偲ィツ前ツづ可転ツつェツつキ
			//false: Xツ篠イツ陛サツ古シツづ可可慊づ可転ツつェツつキ
			void rollX(boolean isReverse) {
				if(!isReverse) roll(Face.TOP, Face.FRONT, Face.BOTTOM, Face.BACK);
				else roll(Face.TOP, Face.BACK, Face.BOTTOM, Face.FRONT);
			}
			//true: Yツ篠イツ陛サツ古シツづ可債カツづ鳴転ツつェツつキ
			//false: Yツ篠イツ陛サツ古シツづ可右ツづ鳴転ツつェツつキ
			void rollY(boolean isReverse) {
				if(!isReverse) roll(Face.TOP, Face.LEFT, Face.BOTTOM, Face.RIGHT);
				else roll(Face.TOP, Face.RIGHT, Face.BOTTOM, Face.LEFT);
			}
			//true: Zツ篠イツ陛サツ古シツづ可右ツづ鳴嘉アツつキ
			//false: Zツ篠イツ陛サツ古シツづ可債カツづ鳴嘉アツつキ
			void rollZ(boolean isReverse) {
				if(!isReverse) roll(Face.FRONT, Face.LEFT, Face.BACK, Face.RIGHT);
				else roll(Face.FRONT, Face.RIGHT, Face.BACK, Face.LEFT);
			}
			private void roll(Face w, Face x, Face y, Face z) {
				T tmp = id[w.ordinal()];
				id[w.ordinal()] = id[x.ordinal()];
				id[x.ordinal()] = id[y.ordinal()];
				id[y.ordinal()] = id[z.ordinal()];
				id[z.ordinal()] = tmp;
			}
			@Override
			public boolean equals(Object o) {
				if(!(o instanceof Dice<?>))return false;
				@SuppressWarnings("unchecked")
				Dice<T> d = (Dice<T>)o;
				for(Face f : Face.values()){
					if(!id[f.ordinal()].equals(d.id[f.ordinal()])){
						return false;
					}
				}
				return true;
			}
			List<Dice<T>> getAllState(){
				List<Dice<T>> lst = new ArrayList<Dice<T>>();
				for(int i = 0; i < 6; i++){
					for(int j = 0; j < 4; j++){
						lst.add(new Dice<T>(id[Face.TOP.ordinal()], id[Face.BOTTOM.ordinal()], id[Face.FRONT.ordinal()], id[Face.BACK.ordinal()], id[Face.RIGHT.ordinal()], id[Face.LEFT.ordinal()]));
						rollZ(false);
					}
					if(i%2 == 1) rollY(false);
					else rollX(false);
				}
				return lst;
			}
	}
	
	Dice<Integer>[] dice;
	int[][] top, front;
	Dice<Integer>[][][] a;
	Set<Integer> res;
	int[][] move = {
			{-1,0,0},
			{0,-1,0},
			{0,0,-1}
	};
	
	void dfs(int i, int j, int k){
		if(j==3){
			int sum = 0;
			for(int y=0;y<3;y++)for(int z=0;z<3;z++)sum+=a[2][y][z].get(Dice.Face.RIGHT);
			res.add(sum);
			return;
		}
		for(int x=0;x<24;x++){
			Dice<Integer> d = dice[x];
			if(k==0&&top[j][i]!=0&&d.get(Dice.Face.TOP)!=top[j][i])continue;
			if(j==2&&front[k][i]!=0&&d.get(Dice.Face.FRONT)!=front[k][i])continue;
			boolean ok = true;
			for(int m=0;m<3;m++){
				int ni = i+move[m][0], nj = j+move[m][1], nk = k+move[m][2];
				if(0<=ni&&ni<3&&0<=nj&&nj<3&&0<=nk&&nk<3){
					if(m==0){
						if(a[i-1][j][k].get(Dice.Face.RIGHT)+d.get(Dice.Face.LEFT)!=7){
							ok = false; break;
						}
					}
					if(m==1){
						if(a[i][j-1][k].get(Dice.Face.FRONT)+d.get(Dice.Face.BACK)!=7){
							ok = false; break;
						}
					}
					if(m==2){
						if(a[i][j][k-1].get(Dice.Face.BOTTOM)+d.get(Dice.Face.TOP)!=7){
							ok = false; break;
						}
					}
				}
			}
			if(!ok)continue;
			a[i][j][k] = d;
			if(i==2&&k==2){
				dfs(0, j+1, 0);
			}
			else if(i==2){
				dfs(0, j, k+1);
			}
			else dfs(i+1, j, k);
		}
	}
	
	@SuppressWarnings("unchecked")
	void run(){
		Dice<Integer> d = new Dice<Integer>(1, 6, 2, 5, 3, 4);
		dice = new Dice[24];
		int id = 0;
		for(Dice<Integer> x:d.getAllState())dice[id++] = x;
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		while(T--!=0){
			top = new int[3][3]; front = new int[3][3];
			for(int i=0;i<3;i++)for(int j=0;j<3;j++)top[i][j] = sc.nextInt();
			for(int i=0;i<3;i++)for(int j=0;j<3;j++)front[i][j] = sc.nextInt();
			a = new Dice[3][3][3];
			res = new HashSet<Integer>();
			dfs(0, 0, 0);
			if(res.isEmpty())System.out.println(0);
			else{
				PriorityQueue<Integer> q = new PriorityQueue<Integer>();
				for(int x:res)q.add(x);
				System.out.print(q.poll());
				while(!q.isEmpty())System.out.print(" "+q.poll());
				System.out.println();
			}
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}