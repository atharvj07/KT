import java.util.*;

public class Main{
	
	class C implements Comparable<C>{
		int d,p;

		public C(int d, int p) {
			this.d = d;
			this.p = p;
		}

		@Override
		public int compareTo(C o) {
			if(this.p < o.p) return 1;
			if(this.p > o.p) return -1;
			return 0;
		}
	}
	
	private void doit(){
		Scanner sc = new Scanner(System.in);
		while(true){
			int n = sc.nextInt();
			int m = sc.nextInt();
			if((n|m) == 0) break;
			C [] data = new C[n];
			for(int i = 0; i < n; i++){
				int d = sc.nextInt();
				int p = sc.nextInt();
				data[i] = new C(d, p);
			}
			Arrays.sort(data);
			int ind = 0;
			while(true){
				int res = m - data[ind].d;
				if(res >= 0){
					m = res;
					data[ind].d = 0;
					ind++;
					if(ind == n) break;
				}
				else {
					data[ind].d = data[ind].d - m;
					break;
				}
			}
			int sum = 0;
			for(int i = 0; i < n; i++){
				sum += data[i].d * data[i].p;
			}
			System.out.println(sum);
		}
	}

	public static void main(String[] args) {
		new Main().doit();
	}
}