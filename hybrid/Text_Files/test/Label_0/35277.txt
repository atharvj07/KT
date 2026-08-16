import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

//Watchin' TVA
public class Main{

	class R implements Comparable<R>{
		String name;
		int s, t;
		boolean u;
		public R(String n, int s, int t) {
			this.s = s;
			this.t = t;
			name = n;
		}
		boolean lap(R r){
			return s<=r.s&&r.s<s+30 || r.s<=s&&s<r.s+30;
		}
		public int compareTo(R o) {
			return t-o.t;
		}
	}
	
	void run(){
		Scanner sc = new Scanner(System.in);
		while(true){
			int n = sc.nextInt();
			if(n==0)break;
			R[] r = new R[n];
			Map<String, Integer> ref = new TreeMap<String, Integer>();
			for(int i=0;i<n;i++){
				String name = sc.next();
				ref.put(name, i);
				int k = sc.nextInt();
				int t = sc.nextInt();
				int s = k*2400 + t/100*60 + t%100;
				r[i] = new R(name, s, s+30);
			}
			int p = sc.nextInt();
			List<R> l = new ArrayList<R>();
			boolean f = true;
			while(p--!=0){
				R fav = r[ref.get(sc.next())];
				boolean ok = true;
				for(R v:l){
					if(v.lap(fav)){
						ok = false;
						break;
					}
				}
				if(ok){
					fav.u = true;
					l.add(fav);
				}
				else{
					f = false;
				}
			}
			if(!f){
				System.out.println(-1);continue;
			}
			Arrays.sort(r);
			for(R v:r){
				if(v.u)continue;
				boolean ok = true;
				for(R z:l){
					if(z.lap(v)){
						ok = false;break;
					}
				}
				if(ok){
					l.add(v);
				}
			}
			System.out.println(l.size());
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}