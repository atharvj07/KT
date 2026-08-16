import java.util.*;
import static java.lang.Math.*;

public class Main {
	final Scanner sc=new Scanner(System.in);
	public static void main(String[] args) {
		new Main().init();
	}
	void init(){
		new AOJ1262();
	}
	
	class AOJ1262{
		final double INF=Double.MAX_VALUE/4.0;
		AOJ1262(){
			while(true){
				int N=sc.nextInt();
				if(N==0)	break;
				System.out.printf("%.4f\n",solve(N));
			}
		}
		double solve(int N){
			int[] a=new int[N+1];
			for(int i=1; i<=N; i++)	a[i]=sc.nextInt();
			double b=sc.nextDouble();
			int r=sc.nextInt();
			double v=sc.nextDouble(),e=sc.nextDouble(),f=sc.nextDouble();
			double[][] dp=new double[N+1][N+1];
			for(int i=1; i<=N; i++)for(int j=0; j<=N; j++)dp[i][j]=INF;
			//flash(dp,N);
			double tmp=0.0;
			for(int i=0; i<a[1]; i++)	tmp+=exp(i,r,v,e,f);
			dp[1][0]=tmp;
			for(int w=1; w<N; w++){
				for(int h=0; h<w; h++){
					int d=a[w+1]-a[w],x=a[w]-a[h];
					double exp=0.0;
					for(int i=0; i<d; i++)	exp+=exp(x++,r,v,e,f);
					//TODO debug
					//System.out.println(exp);
					dp[w+1][h]=dp[w][h]+exp;
					double exp2=0.0;
					for(int i=0; i<d; i++)	exp2+=exp(i,r,v,e,f);
					dp[w+1][w]=min(dp[w+1][w], dp[w][h]+exp2+b);
				}
				//TODO debug
				//System.out.println("new "+dp[w+1][w]);
			}
			//flash(dp,N);
			double ans=INF;
			for(int i=0; i<=N; i++)	ans=min(ans,dp[N][i]);
			return ans;
		}
		double exp(int x,double r,double v,double e,double f){
			return x>=r?(1/(v-e*(x-r))):(1/(v-f*(r-x)));
		}
		void flash(double[][] dp,int N){
			for(int y=0; y<=N; y++){
				for(int x=0; x<=N; x++)	System.out.printf("%3.3f ",dp[x][y]>=INF?-1:dp[x][y]);
				System.out.println();
			}
		}
	}
}