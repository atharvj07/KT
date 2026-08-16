import java.util.Arrays;
import java.util.Scanner;

//Selecting Teams Advanced to Regional
public class Main{

	class R implements Comparable<R>{
		int i,u,a,p;
		public R(int i, int u, int a, int p) {
			this.i = i;
			this.u = u;
			this.a = a;
			this.p = p;
		}
		public int compareTo(R o) {
			return a!=o.a?o.a-a:p!=o.p?p-o.p:i-o.i;
		}
	}

	void run(){
		Scanner sc = new Scanner(System.in);
		while(true){
			int n = sc.nextInt();
			if(n==0)break;
			R[] r = new R[n];
			for(int i=0;i<n;i++)r[i]=new R(sc.nextInt(), sc.nextInt(), sc.nextInt(), sc.nextInt());
			int[] u = new int[1001];
			Arrays.sort(r);
			int s = 0;
			for(R t:r){
				if(s<10&&u[t.u]<3 || s<20&&u[t.u]<2 || s<26&&u[t.u]==0){
					u[t.u]++;
					System.out.println(t.i);
					s++;
				}
			}
		}
	}

	public static void main(String[] args) {
		new Main().run();
	}
}