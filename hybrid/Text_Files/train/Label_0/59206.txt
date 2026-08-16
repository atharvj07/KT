import java.util.Scanner;

//Card Game
public class Main{

	int[] a, b;
	boolean[] u;
	int res;
	
	void dfs(int k, int pa, int pb){
		if(k==9){
			res+=pb<pa?1:0;
			return;
		}
		for(int i=0;i<9;i++){
			if(u[i])continue;
			u[i] = true;
			dfs(k+1, pa+(b[k]<a[i]?a[i]+b[k]:0), pb+(b[k]<a[i]?0:a[i]+b[k]));
			u[i] = false;
		}
	}
	
	void run(){
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		while(T--!=0){
			a = new int[9]; b = new int[9]; u = new boolean[9];
			for(int i=0;i<9;i++)a[i]=sc.nextInt();
			for(int i=0;i<9;i++)b[i]=sc.nextInt();
			res = 0;
			dfs(0, 0, 0);
			double x = res*1.0/362880;
			System.out.printf("%.5f %.5f\n", x, 1-x);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}