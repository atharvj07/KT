import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

//Code Art Online
public class Main{

	double EPS = 1e-8;
	double norm(double[] a, double[] b){
		return (a[0]-b[0])*(a[0]-b[0]) + (a[1]-b[1])*(a[1]-b[1]);
	}
	double[] sub(double[] a, double[] b){
		return new double[]{a[0]-b[0], a[1]-b[1]};
	}
	
	double[] smallestCircle(double[][] p){
		int n = p.length;
		double[] pos = new double[2];
		double ratio = 0.5;
		while(ratio > EPS){
			for(int t=0;t<100;t++){
				double max = -1;
				int id = -1;
				for(int i=0;i<n;i++){
					double d = norm(pos, p[i]);
					if(max < d){
						max = d; id = i;
					}
				}
				double[] dt = sub(p[id], pos);
				pos[0]+=dt[0]*ratio;
				pos[1]+=dt[1]*ratio;
			}
			ratio/=2;
		}
		return pos;
	}
	
	class R implements Comparable<R>{
		int id, r;
		public R(int id, int r) {
			this.id = id;
			this.r = r;
		}
		public int compareTo(R o) {
			return r-o.r;
		}
	}
	
	int n, m;
	List<R>[] list;
	boolean[][] e;
	int[] res;
	boolean[] u;
	boolean ok;
	
	void f(int k){
		if(k==m){
			ok = true; return;
		}
		for(int i=0;i<n;i++)if(!u[i] && e[k][i]){
			u[i] = true;
			if(greedy(k+1)){
				res[k] = i;
				f(k+1);
				return;
			}
			u[i] = false;
		}
	}
	
	boolean greedy(int k){
		Set<Integer> use = new HashSet<Integer>();
		boolean res = true;
		for(int i=k;i<m;i++){
			boolean ok = false;
			for(R r:list[i]){
				if(!u[r.id]){
					u[r.id] = true; use.add(r.id); ok = true; break;
				}
			}
			if(!ok){
				res = false; break;
			}
		}
		for(int x:use)u[x] = false;
		return res;
	}
	
	@SuppressWarnings("unchecked")
	void run(){
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt(); m = sc.nextInt();
		int[] r = new int[n];
		for(int i=0;i<n;i++)r[i]=sc.nextInt();
		list = new List[m];
		e = new boolean[m][n];
		for(int i=0;i<m;i++){
			list[i] = new ArrayList<R>();
			int k = sc.nextInt();
			double[][] p = new double[k][2];
			for(int j=0;j<k;j++)for(int f=0;f<2;f++)p[j][f] = sc.nextInt();
			double[] c = smallestCircle(p);
			double R = 0;
			for(int j=0;j<k;j++)R = Math.max(R, norm(c, p[j]));
			R = Math.sqrt(R);
			for(int j=0;j<n;j++)if(R < r[j]+1e-6){
				e[i][j] = true;
				list[i].add(new R(j, r[j]));
			}
			Collections.sort(list[i]);
		}
		res = new int[m];
		u = new boolean[n];
		f(0);
		if(ok)for(int x:res)System.out.println(x+1);
		else System.out.println("NG");
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}