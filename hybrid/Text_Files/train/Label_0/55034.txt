import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;
import static java.lang.Math.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;

public class Main{
	Scanner sc=new Scanner(System.in);

	int INF=1<<28;
	double EPS=1e-12;

	int a, b;
	V[] vs;

	void run(){
		a=sc.nextInt();
		b=sc.nextInt();
		vs=new V[a+b];
		for(int i=0; i<a+b; i++){
			vs[i]=new V();
		}
		for(int i=0; i<a; i++){
			for(int n=sc.nextInt(); n>0; n--){
				int j=sc.nextInt()-1;
				vs[i].add(vs[a+j]);
			}
		}
		solve();
	}

	void solve(){
		println(bipartiteMathing(vs)==b?"Bob":"Alice");
	}

	int bipartiteMathing(V[] vs){
		int match=0;
		for(V v : vs){
			if(v.match==null){
				for(V u : vs)
					u.used=false;
				if(dfs(v))
					match++;
			}
		}
		return match;
	}

	boolean dfs(V v){
		v.used=true;
		for(V u : v){
			if(u.match==null||!u.match.used&&dfs(u.match)){
				v.match=u;
				u.match=v;
				return true;
			}
		}
		return false;
	}

	class V extends ArrayList<V>{
		V match;
		boolean used;

		void connect(V v){
			add(v);
			v.add(this);
		}
	}

	void debug(Object... os){
		System.err.println(Arrays.deepToString(os));
	}

	void print(String s){
		System.out.print(s);
	}

	void println(String s){
		System.out.println(s);
	}

	public static void main(String[] args){
		new Main().run();
	}
}