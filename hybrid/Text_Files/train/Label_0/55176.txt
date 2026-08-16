import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;

//Rolling Dice
public class Main{

	static class Dice <T>{
		public T[] id;
		enum Face{TOP, BOTTOM, FRONT, BACK, RIGHT, LEFT};

		public T get(Face f){
			return id[f.ordinal()];
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
		void rollX(boolean isReverse) {
			if(!isReverse) roll(Face.TOP, Face.FRONT, Face.BOTTOM, Face.BACK);
			else roll(Face.TOP, Face.BACK, Face.BOTTOM, Face.FRONT);
		}
		void rollY(boolean isReverse) {
			if(!isReverse) roll(Face.TOP, Face.LEFT, Face.BOTTOM, Face.RIGHT);
			else roll(Face.TOP, Face.RIGHT, Face.BOTTOM, Face.LEFT);
		}
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
		boolean isEquivalent(Dice<T> d) {
			for(int i=0; i<6; i++) {
				for(int j=0; j<4; j++) {
					if(this.equals(d)) return true;
					rollZ(false);
				}
				if(i%2==1) rollY(false);
				else rollX(false);
			}
			return false;
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

		@Override
		public String toString() {
			String str = "";
			for(Face f : Face.values()){
				str += id[f.ordinal()] + " ";
			}
			return str;
		}

		@Override
		public int hashCode() {
			int hash = 31;
			for(Face f : Face.values()){
				hash += hash*17+id[f.ordinal()].hashCode();
			}
			return hash;
		}
	}

	static int[][][] dist;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while(true){
			int h = sc.nextInt();
			int w = sc.nextInt();
			if(h==0&&w==0)break;
			int[][] m = new int[h][w];
			for(int i=0;i<h;i++)for(int j=0;j<w;j++)m[i][j]=sc.nextInt();
			int si = sc.nextInt();
			int sj = sc.nextInt();
			int gi = sc.nextInt();
			int gj = sc.nextInt();
			Dice<Integer> dd = new Dice<Integer>(1, 6, 2, 5, 3, 4);
			List<Dice<Integer>> d = dd.getAllState();
			dist = new int[h][w][24];
			for(int[][] a:dist)for(int[] b:a)Arrays.fill(b, Integer.MAX_VALUE);
			PriorityQueue<int[]> q = new PriorityQueue<int[]>(h*w, new Comparator<int[]>() {
				public int compare(int[] o1, int[] o2) {
					return dist[o1[0]][o1[1]][o1[2]]-dist[o2[0]][o2[1]][o2[2]];
				}
			});
			dist[si][sj][0]=0;
			q.add(new int[]{si, sj, 0});
			int min = Integer.MAX_VALUE;
			while(!q.isEmpty()){
				int[] a = q.poll();
				if(a[0]==gi&&a[1]==gj){
					min = Math.min(min, dist[a[0]][a[1]][a[2]]);
				}
				Dice<Integer> tt = d.get(a[2]);
				Dice<Integer> t = new Dice<Integer>(tt.get(Dice.Face.TOP), 
						tt.get(Dice.Face.BOTTOM),
						tt.get(Dice.Face.FRONT), 
						tt.get(Dice.Face.BACK), 
						tt.get(Dice.Face.RIGHT), 
						tt.get(Dice.Face.LEFT));
				for(int k=0;k<4;k++){
					int ni = a[0] + move[k][0];
					int nj = a[1] + move[k][1];
					if(0<=ni&&ni<h&&0<=nj&&nj<w){
						switch(k){
						case 0: t.rollX(true);break;
						case 1: t.rollX(false);break;
						case 2: t.rollY(false);break;
						case 3: t.rollY(true);break;
						}
						int index = -1;
						for(int i=0;i<24;i++)if(t.equals(d.get(i))){index=i;break;}
						int v = dist[a[0]][a[1]][a[2]] + m[ni][nj]*t.get(Dice.Face.BOTTOM);
						switch(k){
						case 0: t.rollX(false);break;
						case 1: t.rollX(true);break;
						case 2: t.rollY(true);break;
						case 3: t.rollY(false);break;
						}
						if(v < dist[ni][nj][index]){
							dist[ni][nj][index] = v;
							q.add(new int[]{ni,nj,index});
						}
					}
				}
			}
			System.out.println(min);
		}
	}
	static int[][] move = {{1, 0},{-1,0},{0,1},{0,-1}};
}