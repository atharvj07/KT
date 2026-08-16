import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

//Dice Puzzle
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
	
	static Dice<Character> d[];
	static List<Dice<Character>> dice[];
	static Dice<Character>[][][] a;
	static boolean[] u;
	
	static boolean dfs(int i, int j, int k){
		for(int m=1;m<8;m++){
			if(!u[m]){
				u[m] = true;
				for(int f=0;f<24;f++){
					a[i][j][k] = dice[m].get(f);
					if(k==0){
						if(i==0){
							if(j==1){
								if(match(a[0][0][0].get(Dice.Face.RIGHT), a[i][j][k].get(Dice.Face.LEFT))){
									if(dfs(1,0,0))return true;
								}
							}
						}
						else {
							if(j==0){
								if(match(a[0][0][0].get(Dice.Face.FRONT), a[i][j][k].get(Dice.Face.BACK))){
									if(dfs(1,1,0))return true;
								}
							}
							else{
								if(match(a[0][1][0].get(Dice.Face.FRONT), a[i][j][k].get(Dice.Face.BACK)) &&
										match(a[1][0][0].get(Dice.Face.RIGHT), a[i][j][k].get(Dice.Face.LEFT))){
									if(dfs(0,0,1))return true;
								}
							}
						}
					}
					else{
						if(i==0){
							if(j==0){
								if(match(a[0][0][0].get(Dice.Face.BOTTOM), a[i][j][k].get(Dice.Face.TOP))){
									if(dfs(0,1,1))return true;
								}
							}
							else{
								if(match(a[0][1][0].get(Dice.Face.BOTTOM), a[i][j][k].get(Dice.Face.TOP)) &&
										match(a[0][0][1].get(Dice.Face.RIGHT), a[i][j][k].get(Dice.Face.LEFT))){
									if(dfs(1,0,1))return true;
								}
							}
						}
						else{
							if(j==0){
								if(match(a[1][0][0].get(Dice.Face.BOTTOM), a[i][j][k].get(Dice.Face.TOP)) &&
										match(a[0][0][1].get(Dice.Face.FRONT), a[i][j][k].get(Dice.Face.BACK))){
									if(dfs(1,1,1))return true;
								}
							}
							else{
								if(match(a[1][1][0].get(Dice.Face.BOTTOM), a[i][j][k].get(Dice.Face.TOP)) &&
										match(a[0][1][1].get(Dice.Face.FRONT), a[i][j][k].get(Dice.Face.BACK)) &&
										match(a[1][0][1].get(Dice.Face.RIGHT), a[i][j][k].get(Dice.Face.LEFT)))return true;
							}
						}
					}
				}
				u[m] = false;
			}
		}
		return false;
	}
	
	static boolean match(char a, char b){
		return Character.toUpperCase(a)==Character.toUpperCase(b)&&a!=b;
	}
	
	@SuppressWarnings("unchecked")
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while(true){
			char[] s = sc.next().toCharArray();
			if(s[0]=='0')break;
			d = new Dice[8];
			dice = new ArrayList[8];
			d[0] = new Dice<Character>(s[0],s[5],s[1],s[4],s[2],s[3]);
			dice[0] = d[0].getAllState();
			for(int i=1;i<8;i++){
				s = sc.next().toCharArray();
				d[i] = new Dice<Character>(s[0],s[5],s[1],s[4],s[2],s[3]);
				dice[i] = d[i].getAllState();
			}
			u = new boolean[8];
			u[0] = true;
			a = new Dice[2][2][2];
			boolean f = false;
			for(int i=0;i<24;i++){
				a[0][0][0] = dice[0].get(i);
				if(dfs(0,1,0)){f = true;break;}
			}
			System.out.println(f?"YES":"NO");
		}
	}
}