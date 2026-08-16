import java.util.PriorityQueue;
import java.util.Scanner;

//Pump up Batteries
public class Main{

	class E implements Comparable<E>{
		int id, t;
		public E(int id, int t) {
			this.id = id;
			this.t = t;
		}
		public int compareTo(E o) {
			return t==o.t?id-o.id:t-o.t;
		}
	}
	
	void run(){
		Scanner sc = new Scanner(System.in);
		for(;;){
			int n = sc.nextInt();
			int T = sc.nextInt();
			if((n|T)==0)break;
			int[][] com = new int[n][50];
			int[][] ch = new int[n][50];
			int[] k = new int[n];
			for(int i=0;i<n;i++){
				for(;;){
					int x = sc.nextInt();
					if(x==0)break;
					com[i][k[i]] = x;
					ch[i][k[i]] = sc.nextInt();
					k[i]++;
				}
			}
			int res = 0;
			boolean[] wait = new boolean[n];
			int[] val = new int[n];
			for(int i=0;i<n;i++)val[i] = com[i][0];
			int[] p = new int[n];
			PriorityQueue<E> q = new PriorityQueue<E>();
			for(int t=0;t<T;t++){
				for(int i=0;i<n;i++){
					if(wait[i])continue;
					if(val[i]==0){
						wait[i] = true;
						val[i] = ch[i][p[i]];
						q.add(new E(i, t));
					}
					else val[i]--;
				}
				if(q.isEmpty())continue;
				E e = q.peek();
				for(int i=0;i<n;i++){
					if(e.id==i){
						val[i]--;
						if(val[i]==0){
							q.poll();
							p[i] = (p[i]+1)%k[i];
							val[i] = com[i][p[i]];
							wait[i] = false;
						}
					}
					else if(wait[i])res++;
				}
			}
			System.out.println(res);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}