import java.util.*;

class Main {
	public class T{
		int a,b,c;
		T(int a,int b,int c){
			this.a = a;
			this.b = b;
			this.c = c;
		}
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int M = sc.nextInt();
		int s = sc.nextInt()-1;
		int t = sc.nextInt()-1;
		ArrayList<ArrayList<Integer>> g = new ArrayList<ArrayList<Integer>>();
		for(int i = 0 ; i < N ; i++)
			g.add(new ArrayList<Integer>());
		for(int i = 0 ; i < M ; i++){
			int a = sc.nextInt()-1;
			int b = sc.nextInt()-1;
			g.get(a).add(b);
			g.get(b).add(a);
		}
		ArrayDeque<Integer> Q = new ArrayDeque<Integer>();
		int[] shortest1 = new int[N+1];
		int[] shortest2 = new int[N+1];
		
		int[] counter1 = new int[N+1];
		int[] counter2 = new int[N+1];
		
		Arrays.fill(shortest1,N);
		Arrays.fill(shortest2,N);
		Q.offer(s);
		shortest1[s] = 0;
		while( Q.size() > 0 ){
			int q = Q.poll();
			counter1[shortest1[q]]++;
			//System.out.println(q+1+" "+shortest1[q]);
			for( int to : g.get(q) ){
				if( shortest1[to] == N ){
					shortest1[to] = shortest1[q] + 1;
					Q.offer(to);
				}
			}
		}
		Q.offer(t);
		shortest2[t] = 0;
		while( Q.size() > 0 ){
			int q = Q.poll();
			counter2[shortest2[q]]++;
			//System.out.println(q+1+" "+shortest2[q]);
			for( int to : g.get(q) ){
				if( shortest2[to] == N ){
					shortest2[to] = shortest2[q] + 1;
					Q.offer(to);
				}
			}
		}
		//System.out.println("");

		int maximum = shortest1[t];
		long ans = 0;
		//for(int i = 0 ; i <= maximum ; i++){
		//	System.out.println(i+" "+counter[i]);
		//}
		for(int i = 0 ; i+2 <= maximum ; i++){

			ans += (long) counter1[i] * counter2[maximum-(i+2)];
		}
		System.out.println(ans);
		return;
	}
}