import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;
import static java.lang.Math.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;

// Reverse Game
public class Main{
	Scanner sc=new Scanner(System.in);

	int m, n;
	int[][] a;

	void run(){
		n=sc.nextInt();
		m=sc.nextInt();
		a=new int[n][m];
		for(int j=0; j<n; j++){
			for(int i=0; i<m; i++){
				a[j][i]=sc.nextInt();
			}
		}
		solve();
	}

	void solve(){
		int N=n*m, M=N/64+1;
		long[][] A=new long[N][M];
		for(int y=0; y<n; y++){
			for(int x=0; x<m; x++){
				int q=y*m+x;
				for(int j=0; j<n; j++){
					for(int i=0; i<m; i++){
						if(i==x||j==y||abs(x-i)==abs(y-j)){
							int p=j*m+i;
							A[q][p>>>6]|=1L<<(p&63);
						}
					}
				}
				if(a[y][x]==1){
					int p=m*n;
					A[q][p>>>6]|=1L<<(p&63);
				}
			}
		}
		int rank=0;
		boolean NG=false;
		for(int j=0; j<N; j++){
			int at=-1;
			for(int i=j; i<N; i++){
				if((A[i][j>>>6]>>>(j&63)&1)==1){
					at=i;
					break;
				}
			}
			if(at==-1){
				continue;
			}
			long[] t=A[j];
			A[j]=A[at];
			A[at]=t;
			for(int k=j+1; k<N; k++){
				if((A[k][j>>>6]>>>(j&63)&1)==1){
					for(int i=0; i<M; i++){
						A[k][i]^=A[j][i];
					}
				}
			}
			rank++;
		}
		for(int j=N-1; j>=0; j--){
			int at=-1;
			for(int i=N-1; i>=0; i--){
				if((A[j][i>>>6]>>>(i&63)&1)==1){
					at=i;
					break;
				}
			}
			if(at==-1){
				NG|=(A[j][m*n/64]>>>(m*n%64)&1)==1;
				continue;
			}
			for(int k=j-1; k>=0; k--){
				if((A[k][at>>>6]>>>(at&63)&1)==1){
					for(int i=0; i<M; i++){
						A[k][i]^=A[j][i];
					}
				}
			}
		}
		println(NG?"0":powMod(2, N-rank, (long)1e9+9)+"");
	}

	long powMod(long x, long k, long mod){
		if(k==0){
			return 1%mod;
		}else if(k%2==0){
			return powMod(x*x%mod, k/2, mod);
		}else{
			return x*powMod(x, k-1, mod)%mod;
		}
	}

	void println(String s){
		System.out.println(s);
	}

	public static void main(String[] args){
		new Main().run();
	}
}