import java.util.*;
import static java.lang.Math.*;
public class Main {
	final Scanner sc = new Scanner(System.in);
	public static void main(String[] args) {
		new Main().init();
	}
	void init(){
		new AOJ2005();
	}
	class AOJ2005{
		AOJ2005(){
			while(sc.hasNext()){
				int n=sc.nextInt(),m=sc.nextInt(),s=sc.nextInt(),g1=sc.nextInt(),g2=sc.nextInt();
				if(n==0)	break;
				--s; --g1; --g2;
				solve(n,m,s,g1,g2);
			}
		}
		final int INF=Integer.MAX_VALUE/4;
		void solve(int n,int m,int s,int g1,int g2){
			int[][] g=new int[n][n];
			for(int i=0; i<n; ++i)for(int j=0; j<n; ++j)	g[i][j]=(i==j?0 :INF);
			for(int i=0; i<m; ++i){
				int a=sc.nextInt(),b=sc.nextInt(),c=sc.nextInt();
				--a; --b;
				g[a][b]=c;
			}
			
			for(int j=0; j<n; ++j)for(int i=0; i<n; ++i)for(int k=0; k<n; ++k)g[i][k]=min(g[i][k], g[i][j]+g[j][k]);
			
			int ans=INF;
			for(int i=0; i<n; ++i)	ans=min(ans, g[s][i]+g[i][g1]+g[i][g2]);
			System.out.println(ans);
		}
	}
}