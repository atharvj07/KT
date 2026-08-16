import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;
class Main{


	static final int MOD = 1000000007;


	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);			//文字の入力
		int n = sc.nextInt();
		int m = sc.nextInt();

		Edge[] edge = new Edge[n];
		for(int i = 0;i < n;i++){				//頂点の作成と、一個前に戻る辺の作成
			edge[i] = new Edge();
			if(i != 0){
				edge[i].add(new P(i-1, 0));
			}
		}

		for(int i = 0;i < m;i++){
			int l = sc.nextInt()-1, r = sc.nextInt()-1,c = sc.nextInt();
			edge[l].add(new P(r, c));
		}
		System.out.println(dijkstra(edge,n));

	}


	static long dijkstra(Edge[] edge,int n){

		long[] d = new long[n];		//始点からの最短距離
		Arrays.fill(d, 1l << 60);
		d[0] = 0;
		PriorityQueue<P> q = new PriorityQueue<>(Comparator.comparingLong(p-> p.cost));			//costをソート
		q.add(new P(0,0));

		while(!q.isEmpty()){
			P current = q.remove();
			if(current.to == n-1){
				return current.cost;
			}
			if(current.cost != d[current.to]){
				continue;
			}
			for(P next: edge[current.to]){
				if(d[next.to] > current.cost + next.cost){
					d[next.to] = current.cost + next.cost;
					q.add(new P(next.to, current.cost+next.cost));
				}
			}


		}
		return -1;



	}



	static int upperbond(int k,int currentindex, ArrayList<Pair> a,ArrayList<Pair> b,int[] aa,int[] bb){		//kより小さい最大の値をdataの中から探し、返す二分探索
		int min = -1;
		int max = a.size();

		while(max-min > 1){
			int mid = (max+min)/2;
			if(a.get(mid).from > k){
				max = mid;
			}else{
				min = mid;
			}
		}

		if(max == a.size()){
			max--;
		}
		for(int i = max; i>=0;i--){
			if(a.get(i).from <= bb[currentindex] && aa[currentindex] <= bb[a.get(i).end]){
				int tmp = a.get(i).end;
				a.get(i).end = a.get(currentindex).end;
				a.get(currentindex).end = tmp;

				return tmp;
			}
		}

		return -1;
	}

	static int lowerbond(int k, ArrayList<Integer> data){		//kより小さい最小の値をdataの中から探し、返す二分探索
		int min = -1;
		int max = data.size();

		while(max-min > 1){
			int mid = (max+min)/2;
			if(data.get(mid) >= k){
				max = mid;
			}else{
				min = mid;
			}
		}
		return data.get(min);
	}



	static int gcd(int a,int b){				//最大公約数を返す
		if(b == 0){
			return a;
		}else{
			return gcd(b, a%b);
		}
	}
	static long gcd(long a,long b){
		if(b == 0){
			return a;
		}else{
			return gcd(b, a%b);
		}
	}



	static long lcm (long a, long b) {
		long g = gcd(a,b);
		return a/g*b;
	}




}


class Edge extends ArrayList<P>{

}

class P{
	int to;
	long cost;
	P(int to,long cost){
		this.to = to;
		this.cost = cost;
	}
}


class Pair implements Comparable{
	int from;
	int end;
	@Override
	public int compareTo(Object other) {
		Pair otherpair = (Pair)other;

		return   from- otherpair.from;
	}








}




