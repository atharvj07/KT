import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;
import static java.util.Collections.*;
import static java.util.Arrays.*;
import static java.lang.Math.*;

// Trading Ship
// 2012/12/15
public class Main{
	Scanner sc=new Scanner(System.in);

	double w, h;
	int n;
	double[] xs, ys;

	void run(){
		w=sc.nextInt();
		h=sc.nextInt();
		n=sc.nextInt();
		xs=new double[n];
		ys=new double[n];
		for(int i=0; i<n; i++){
			xs[i]=sc.nextInt();
			ys[i]=sc.nextInt();
		}
		solve();
	}

	void solve(){
		double left=0, right=1e9;
		for(int t=0; t<100; t++){
			double mid=(left+right)/2;
			if(check(mid)){
				left=mid;
			}else{
				right=mid;
			}
		}
		double ans=(left+right)/2;
		println(String.format("%.3f", ans));
	}

	boolean check(double r){
		LinkedList<Integer> que=new LinkedList<Integer>();
		boolean[] visited=new boolean[n];
		for(int i=0; i<n; i++){
			if(abs(xs[i])<r){
				que.offer(i);
				visited[i]=true;
			}
		}
		for(; !que.isEmpty();){
			int v=que.poll();
			for(int u=0; u<n; u++){
				if(!visited[u]){
					double dx=xs[u]-xs[v], dy=ys[u]-ys[v];
					if(dx*dx+dy*dy<4*r*r){
						que.offer(u);
						visited[u]=true;
					}
				}
			}
		}
		for(int i=0; i<n; i++){
			if(visited[i]&&abs(w-xs[i])<r){
				return false;
			}
		}
		return true;
	}

	void println(String s){
		System.out.println(s);
	}

	public static void main(String[] args){
		new Main().run();
	}
}