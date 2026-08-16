import java.util.Scanner;

//Bitwise Kingdom
public class Main{

	int n;
	long M;
	char[] r;
	long[][] comb;

	boolean dfs(int k, long L, long R, int c){
		if(!(L<=M&&M<=R))return false;
		if(k==n){
			return c==0;
		}
		if(n-k-1>=c){
			r[k] = '0';
			if(dfs(k+1, L, L+comb[n-k-1][c]-1, c))return true;
		}
		if(c==0)return false;
		r[k] = '1';
		long up = 0;
		if(n-k-1>=c)up += comb[n-k-1][c];
		return dfs(k+1, L+up, R, c-1);
	}

	long[][] comb(int N){
		long[][] r = new long[N+1][N+1];
		r[0][0]=1;
		for(int i=1;i<=N;i++){
			r[i][0]=r[i][i]=1;
			for(int j=1;j<i;j++){
				r[i][j] = r[i-1][j-1]+r[i-1][j];
			}
		}
		return r;
	}

	void run(){
		Scanner sc = new Scanner(System.in);
		comb = comb(60);
		for(;;){
			n = sc.nextInt(); M = sc.nextLong();
			if((n|M)==0)break;
			long s = 0;
			int c = 0;
			for(;c<=n;c++){
				s += comb[n][c];
				if(M<=s)break;
			}
			s -= comb[n][c];
			M -= s;
			r = new char[n];
			dfs(0, 1, comb[n][c], c);
			System.out.println(new String(r));
		}
	}

	public static void main(String[] args) {
		new Main().run();
	}
}