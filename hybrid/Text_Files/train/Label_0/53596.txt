import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

//Restaurant
public class Main{

	class R implements Comparable<R>{
		int oid, id;
		public R(int oid, int id) {
			this.oid = oid;
			this.id = id;
		}
		public int compareTo(R o) {
			return oid!=o.oid?oid-o.oid:p[id]!=p[o.id]?p[o.id]-p[id]:id-o.id;
		}
		@Override
		public String toString() {
			return oid+","+id;
		}
	}

	int n, m;
	int[] p, limit, T, K, res;
	Map<String, Integer> ref;
	
	@SuppressWarnings("unchecked")
	void run(){
		Scanner sc = new Scanner(System.in);
		for(boolean head = true;;head = false){
			n = sc.nextInt(); m = sc.nextInt();
			if((n|m)==0)break;
			if(!head)System.out.println();
			ref = new HashMap<String, Integer>();
			limit = new int[n];
			p = new int[n];
			T = new int[m];
			K = new int[m];
			for(int i=0;i<n;i++){
				ref.put(sc.next(), i);
				limit[i] = sc.nextInt();
				p[i] = sc.nextInt();
			}
			List<R>[] l = new List[m];
			for(int i=0;i<m;i++){
				l[i] = new ArrayList<R>();
				T[i] = sc.nextInt();
				K[i] = sc.nextInt();
				for(int j=0;j<K[i];j++)l[i].add(new R(i, ref.get(sc.next())));
			}
			res = new int[m];
			int f = 0, t = 0;
			LinkedList<R> list = new LinkedList<R>();
			while(f<m||!list.isEmpty()){
				while(f<m&&T[f]<=t){
					list.addAll(l[f++]);
				}
				if(list.isEmpty()&&f<m){
					t = T[f]; list.addAll(l[f++]);
				}
				Collections.sort(list);
				R r = list.get(0);
				t += p[r.id];
				int L = limit[r.id];
				for(int i=0;i<list.size()&&0<L;i++){
					R d = list.get(i);
					if(d.id!=r.id)continue;
					--L;
					if(--K[d.oid]==0)res[d.oid] = t;
					list.remove(i--);
				}
			}
			for(int r:res)System.out.println(r);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}