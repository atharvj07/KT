import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;
import static java.lang.Math.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;

// Audition
// 2012/09/19
public class Main{
	Scanner sc=new Scanner(System.in);

	int n, m;
	int[] vi, da, vo;

	double[][] comb, combSum;

	void run(){
		n=sc.nextInt();
		m=sc.nextInt();
		vi=new int[n];
		da=new int[n];
		vo=new int[n];
		for(int i=0; i<n; i++){
			vi[i]=sc.nextInt();
			da[i]=sc.nextInt();
			vo[i]=sc.nextInt();
		}
		solve();
	}

	void solve(){
		int M=2010;
		comb=new double[M][M];
		combSum=new double[M][M];
		// comb[n][k] = C(n,k)(1/3)^k(2/3)^{n-k}
		// combSum[n][k] = comb[n][k]+...+comb[n][n]

		comb[0][0]=1;
		for(int j=1; j<M; j++){
			comb[j][0]=comb[j-1][0]*(2/3.0);
			for(int i=1; i<M; i++){
				comb[j][i]=comb[j-1][i]*(2/3.0)+comb[j-1][i-1]*(2/3.0)*(1/2.0);
			}
		}
		for(int j=0; j<M; j++){
			combSum[j][M-1]=comb[j][M-1];
			for(int i=M-2; i>=0; i--){
				combSum[j][i]=combSum[j][i+1]+comb[j][i];
			}
		}

		double[] viE=calcE(vi, 5);
		double[] daE=calcE(da, 3);
		double[] voE=calcE(vo, 2);

		double max=-Double.MAX_VALUE;
		for(int i=0; i<=m; i++){
			for(int j=0; i+j<=m; j++){
				int k=m-(i+j);
				max=max(max, viE[i]+daE[j]+voE[k]);
			}
		}
		println(String.format("%.12f", max));
	}

	double[] calcE(int[] value, int point){
		double[] E=new double[m+1];
		for(int i=0; i<=m; i++){
			int myValue=value[0]*i;
			double[][] top3=new double[n][3];
			top3[0][0]=1;
			double worst=1;
			for(int j=1; j<n; j++){
				int a=(myValue+value[j]-1)/value[j];
				double p=a<=m?combSum[m][a]:0;
				top3[j][0]=top3[j-1][0]*(1-p);
				top3[j][1]=top3[j-1][1]*(1-p)+top3[j-1][0]*p;
				top3[j][2]=top3[j-1][2]*(1-p)+top3[j-1][1]*p;
				worst*=p;
			}
			E[i]=point*(top3[n-1][0]+top3[n-1][1]+top3[n-1][2])-1*worst;
		}
		return E;
	}

	void println(String s){
		System.out.println(s);
	}

	public static void main(String[] args){
		new Main().run();
	}
}