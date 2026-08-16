import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

//Digits on the Floor
public class Main{

	class UnionFind {
		final int[] tree;
		int num;
		public UnionFind(int n) {
			this.tree = new int[n];
			Arrays.fill(tree, -1);
			num=n;
		}
		void union(int x, int y) {
			x = root(x);
			y = root(y);
			if(x != y) {
				if(tree[x] < tree[y]) {
					x ^= y; y ^= x; x^= y;
				}
				tree[x] += tree[y];
				tree[y] = x;
				num--;
			}
		}
		boolean find(int x, int y) {
			return root(x) == root(y);
		}
		int root(int x) {
			return tree[x] < 0 ? x : (tree[x] = root(tree[x]));
		}
		int size(int x) {
			return -tree[root(x)];
		}
		int getNum() {
			return num;
		}
	}
	
	@SuppressWarnings("unchecked")
	void run(){
		Scanner sc = new Scanner(System.in);
		int[][] check = {{0,0,4,0,0,0},
				{1,0,0,0,0,0},
				{0,2,3,0,0,0},
				{0,2,1,0,0,1},
				{1,1,0,1,0,0},
				{0,2,3,0,0,0},
				{0,1,3,1,0,0},
				{0,2,1,0,0,0},
				{0,0,4,0,1,0},
				{0,1,2,1,0,0}};
		for(;;){
			int n = sc.nextInt();
			if(n==0)break;
			int[][] x = new int[n][2], y = new int[n][2];
			for(int i=0;i<n;i++)for(int j=0;j<2;j++){
				x[i][j] = sc.nextInt(); y[i][j] = sc.nextInt();
			}
			UnionFind uf = new UnionFind(n);
			int[] info = new int[n];
			for(int i=0;i<n;i++){
				int c = 0, m = 0;
				int x1 = x[i][0], y1 = y[i][0], x2 = x[i][1], y2 = y[i][1];
				for(int j=0;j<n;j++){
					if(i==j)continue;
					int x3 = x[j][0], y3 = y[j][0], x4 = x[j][1], y4 = y[j][1];
					if(x1==x3&&y1==y3 || x1==x4&&y1==y4 || x2==x3&&y2==y3 || x2==x4&&y2==y4){
						if(!uf.find(i, j))uf.union(i, j);
						c++;
					}
					else if((y1-y3)*(x4-x3)==(y4-y3)*(x1-x3)&&Math.min(x3, x4)<=x1&&x1<=Math.max(x3, x4)&&Math.min(y3, y4)<=y1&&y1<=Math.max(y3, y4) ||
						(y2-y3)*(x4-x3)==(y4-y3)*(x2-x3)&&Math.min(x3, x4)<=x2&&x2<=Math.max(x3, x4)&&Math.min(y3, y4)<=y2&&y2<=Math.max(y3, y4)){
						if(!uf.find(i, j))uf.union(i, j);
						m++;
					}
				}
				if(c==2)info[i]=2;
				else if(m==2)info[i]=4;
				else if(c==1&&m==1)info[i]=3;
				else if(c==1)info[i]=1;
				else if(m==1)info[i]=5;
				else info[i]=0;
			}
			Set<Integer>[] set = new Set[n];
			for(int i=0;i<n;i++)set[i]=new HashSet<Integer>();
			int[][] at = new int[n][6];
			for(int i=0;i<n;i++){
				set[uf.root(i)].add(i);
				at[uf.root(i)][info[i]]++;
			}
			int[] res = new int[10];
			for(int i=0;i<n;i++){
				for(int j=0;j<10;j++){
					boolean ok = true;
					for(int k=0;k<6;k++)if(at[i][k]!=check[j][k])ok=false;
					if(ok){
						if(j!=2)res[j]++;
						else{
							int e = -1, px = -1, py = -1, qx = -1, qy = -1;
							for(int v:set[i])if(info[v]==1)e = v;
							for(int v:set[i])if(v!=e){
								if(x[e][0]==x[v][0]&&y[e][0]==y[v][0]){
									px = x[e][0]-x[e][1]; py = y[e][0]-y[e][1]; qx = x[v][1]-x[e][1]; qy = y[v][1]-y[e][1];
								}
								else if(x[e][0]==x[v][1]&&y[e][0]==y[v][1]){
									px = x[e][0]-x[e][1]; py = y[e][0]-y[e][1]; qx = x[v][0]-x[e][1]; qy = y[v][0]-y[e][1];
								}
								else if(x[e][1]==x[v][0]&&y[e][1]==y[v][0]){
									px = x[e][1]-x[e][0]; py = y[e][1]-y[e][0]; qx = x[v][1]-x[e][0]; qy = y[v][1]-y[e][0];
								}
								else if(x[e][1]==x[v][1]&&y[e][1]==y[v][1]){
									px = x[e][1]-x[e][0]; py = y[e][1]-y[e][0]; qx = x[v][0]-x[e][0]; qy = y[v][0]-y[e][0];
								}
							}
							if(px*qy-qx*py<0)res[2]++;
							else res[5]++;
						}
						break;
					}
				}
			}
			for(int i=0;i<10;i++)System.out.print(res[i]+(i==9?"\n":" "));
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}