
import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int m = sc.nextInt();
		
		DisjointSet dj = new DisjointSet(n);
		
		int a[] = new int[m];
		int b[] = new int[m];
		for(int i = 0; i < m; i++) {
			int tmpA = sc.nextInt();
			int tmpB = sc.nextInt();
			
			a[m - i - 1] = tmpA;
			b[m - i - 1] = tmpB;
		}
		//橋を0本から1本ずつ足していくという考え方で解く
		//最初の不便度はMAX
		long pattern = (long)n*(n - 1)/2;
		long result[] = new long[m + 1];
		result[m] = pattern;
		//aとbを繋いだ場合
		//(1)aとbが同じグループなら不便度変化無し
		//(2)異なるグループならAのグループの要素数とBのグループの要素数の積だけ不便度が減る
		for(int i = 0; i < m; i++) {
			if(!dj.isSameSet(a[i], b[i])) {
				pattern -= (long)dj.amountOfOwnGroup(a[i])*dj.amountOfOwnGroup(b[i]);
				dj.union(a[i], b[i]);
			}
			result[m - i - 1] = pattern;
		}
		
		for(int i = 1; i < m + 1; i++) {
			System.out.println(result[i]);
		}
	}

}
//各グループの要素数をまあまあ高速で取得できるよう改造
class DisjointSet {
	private int n;
	private int[] p;
	private int[] rank;
	//各グループの要素数を管理する
	private int[] num;

	public DisjointSet(int n){
		this.n = n;

		p = new int[n + 1];
		rank = new int[n + 1];

		num = new int[n + 1];
		
		Arrays.fill(num, 1);
		
		for(int i = 1; i <= n; i++){
			makeSet(i);
		}
	}

	private void makeSet(int x){
		p[x] = x;
		rank[x] = 0;
	}

	public void union(int x, int y){
		int p1 = findSet(x), p2 = findSet(y);
		int num1 = num[p1];
		int num2 = num[p2];
		link (findSet(x), findSet(y));
		
		if(p1 != p2) {
			num[p1] = num[p2] = num1 + num2;
		}
		
	}
	
	public int amountOfOwnGroup(int x) {
		return num[findSet(x)];
	}

	private int findSet(int x){
		if(x != p[x]){
			p[x] = findSet( p[x]);
		}
		return p[x];
	}

	public boolean isSameSet(int x, int y){
		return findSet(x) == findSet(y);
	}

	private void link(int x, int y){
		if(rank[x] > rank[y]){
			p[y] = x;
		}
		else {
			p[x] = y;
			if(rank[x] == rank[y]){
				rank[y]++;
			}
		}
	}
}
