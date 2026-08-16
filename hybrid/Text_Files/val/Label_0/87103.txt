import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

//Name the Crossing
public class Main{

	class R{
		int id, col;
		Set<Integer> adj, eq;
		boolean visit;
		public R(int id) {
			this.id = id;
			col = -1;
			eq = new HashSet<Integer>();
			adj = new HashSet<Integer>();
		}
		void color(int c){
			if(visit)return;
			col = c;
			visit = true;
			for(int v:adj)rs[v].color(c%2==0?(c+1):(c-1));
		}
		boolean reach(int g){
			if(id==g)return true;
			if(visit)return false;
			visit = true;
			for(int v:eq)if(rs[v].reach(g))return true;
			return false;
		}
	}
	
	int ID;
	Map<String, R> ref;
	Set<String> streets;
	String[] names;
	R get(String s){
		if(ref.containsKey(s))return ref.get(s);
		R res = new R(ID);
		names[ID] = s;
		rs[ID++] = res;
		ref.put(s, res);
		return res;
	}
	R[] rs;
	
	void reset(){
		for(int i=0;i<ID;i++)rs[i].visit = false;
	}
	
	void run(){
		Scanner sc = new Scanner(System.in);
		for(;;){
			int n = sc.nextInt();
			if(n==0)break;
			ID = 0;
			ref = new HashMap<String, R>();
			rs = new R[200];
			names = new String[200];
			streets = new HashSet<String>();
			while(n--!=0){
				String t = sc.next();
				streets.add(t);
				String s[] = t.split("-");
				R a = get(s[0]), b = get(s[1]);
				a.adj.add(b.id); b.adj.add(a.id);
				b.eq.add(a.id);
			}
			int col = 0;
			for(int i=0;i<ID;i++){
				if(rs[i].visit)continue;
				rs[i].color(col);
				col+=2;
			}
			int N =	ID;
			for(int i=0;i<N;i++)for(int j=i+1;j<N;j++){
				boolean C, D, E;
				C = false;
				D = E = true;
				for(int k=0;k<N;k++){
					if(k==i||k==j)continue;
					if(rs[i].adj.contains(k)&&rs[j].adj.contains(k))C = true;
					if(streets.contains(names[k]+"-"+names[i])&&streets.contains(names[j]+"-"+names[k]))D = false;
					if(streets.contains(names[i]+"-"+names[k])&&streets.contains(names[k]+"-"+names[j]))E = false;
				}
				if(C&&D&&E){
					R a = get(names[i]), b = get(names[j]);
					a.eq.add(b.id); b.eq.add(a.id);
				}
			}
			System.out.println(N);
			int m = sc.nextInt();
			while(m--!=0){
				String[] t = sc.next().split("-");
				R a = get(t[0]), b = get(t[1]);
				if(a.col==b.col||Math.abs(a.col-b.col)>=2||a.col==-1||b.col==-1){
					System.out.println("NO"); continue;
				}
				reset();
				System.out.println(b.reach(a.id)?"YES":"NO");
			}
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}