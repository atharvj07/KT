import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

//Girls' Party
public class Main{

	int N, res;
	Set<String>[] v;
	
	void dfs(int nb, int ng, int z, String s){
		if(nb<=res)return;
		if(ng==0){
			res = nb; return;
		}
		if(v[z].contains(s))return;
		v[z].add(s);
		int n = s.length(), d = (N-1)%n;
		if(s.charAt(d)=='B'){
			dfs(nb-1, ng, z, s.substring(d+1)+s.substring(0, d));
		}
		else{
			dfs(nb, ng-1, z, s.substring(d+1)+s.substring(0, d));
		}
		if(z==1)return;
		d = N%n;
		if(s.charAt(d)=='B'){
			dfs(nb-1, ng, 1, s.substring(d+1)+s.substring(0, d));
		}
		else{
			dfs(nb, ng-1, 1, s.substring(d+1)+s.substring(0, d));
		}
	}
	
	@SuppressWarnings("unchecked")
	void run(){
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		while(T--!=0){
			N = sc.nextInt();
			String s = sc.next();
			v = new Set[2];
			v[0] = new HashSet<String>(); v[1] = new HashSet<String>();
			res = 0;
			int nb = 0, ng = 0;
			for(char c:s.toCharArray())
				if(c=='B')nb++; 
				else ng++;
			dfs(nb, ng, 0, s);
			System.out.println(res);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}