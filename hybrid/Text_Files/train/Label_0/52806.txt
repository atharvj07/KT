import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;
import static java.lang.Math.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;

// Approximate Circle
public class Main{
	Scanner sc=new Scanner(System.in);

	int INF=1<<28;
	double EPS=1e-12;

	int n;
	double[] xs, ys;

	void run(){
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
		double[][] A=new double[3][3];
		double[] b=new double[3];
		for(int i=0; i<n; i++){
			A[0][0]+=sq(xs[i]);
			A[0][1]+=xs[i]*ys[i];
			A[0][2]+=xs[i];
			A[1][0]+=xs[i]*ys[i];
			A[1][1]+=sq(ys[i]);
			A[1][2]+=ys[i];
			A[2][0]+=xs[i];
			A[2][1]+=ys[i];
			A[2][2]+=1;
			b[0]-=xs[i]*(sq(xs[i])+sq(ys[i]));
			b[1]-=ys[i]*(sq(xs[i])+sq(ys[i]));
			b[2]-=sq(xs[i])+sq(ys[i]);
		}
		double[] x=gaussianElimination(A, b);
		println(String.format("%.9f %.9f %.9f", x[0], x[1], x[2]));
	}

	double[] gaussianElimination(double[][] A_, double[] b){
		int n=A_.length;
		double[][] A=new double[n][n+1];
		for(int i=0; i<n; i++){
			System.arraycopy(A_[i], 0, A[i], 0, n);
			A[i][n]=b[i];
		}
		for(int j=0; j<n; j++){
			int pivot=j;
			for(int i=j+1; i<n; i++)
				if(abs(A[i][j])>abs(A[pivot][j]))
					pivot=i;
			double[] t=A[j];
			A[j]=A[pivot];
			A[pivot]=t;
			if(abs(A[j][j])<EPS)
				return null;
			for(int k=j+1; k<n; k++){
				double r=A[k][j]/A[j][j];
				for(int i=j; i<=n; i++)
					A[k][i]-=A[j][i]*r;
			}
		}
		double[] x=new double[n];
		for(int j=n-1; j>=0; j--){
			x[j]=A[j][n];
			for(int i=j+1; i<n; i++)
				x[j]-=x[i]*A[j][i];
			x[j]/=A[j][j];
		}
		return x;
	}

	double sq(double x){
		return x*x;
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