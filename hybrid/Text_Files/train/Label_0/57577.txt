import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

//Space-Time Sugoroku Road
public class Main{

	void run(){
		int LOOP = 1<<29;
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] p = new int[n], nx = new int[n];
		Arrays.fill(nx, -1);
		for(int i=0;i<n;i++)p[i]=sc.nextInt();
		for(int i=0;i<n;i++){
			if(nx[i]!=-1)continue;
			if(p[i]==0){
				nx[i] = i; continue;
			}
			Set<Integer> s = new HashSet<Integer>();
			s.add(i);
			int v = i+p[i], r = 0;
			for(;;){
				if(nx[v]!=-1){
					r = nx[v]; break;
				}
				if(p[v]==0){
					r = v; s.add(v); break;
				}
				if(s.contains(v)){
					r = LOOP; s.add(v); break;
				}
				s.add(v);
				v+=p[v];
			}
			for(int x:s)nx[x] = r;
		}
		boolean[] u = new boolean[n];
		u[0] = true;
		List<Integer> l = new ArrayList<Integer>();
		l.add(0);
		int step = 0;
		while(!l.isEmpty()){
			List<Integer> next = new ArrayList<Integer>();
			for(int v:l){
				if(v==n-1){
					System.out.println(step); next.clear(); break;
				}
				for(int k=1;k<=6;k++){
					if(n<=v+k)break;
					int t = nx[v+k];
					if(t==LOOP||u[t])continue;
					u[t] = true; next.add(t);
				}
			}
			l = next;
			step++;
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}