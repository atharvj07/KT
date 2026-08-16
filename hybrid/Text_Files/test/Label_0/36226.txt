import java.util.Scanner;

//Anipero
public class Main{

	void run(){
		Scanner sc = new Scanner(System.in);
		for(;;){
			int L = sc.nextInt(), n = sc.nextInt(), m = sc.nextInt(), X = sc.nextInt();
			if((L|n|m|X)==0)break;
			int[] e1 = new int[n], s1 = new int[n];
			for(int i=0;i<n;i++){
				sc.next(); e1[i] = sc.nextInt(); s1[i] = sc.nextInt();
			}
			int[] e2 = new int[m], s2 = new int[m];
			for(int i=0;i<m;i++){
				sc.next(); e2[i] = sc.nextInt(); s2[i] = sc.nextInt();
			}
			int[][][] dp1 = new int[n][3][L+1];
			//-1: À»sÂ\Ì}[N
			for(int i=0;i<n;i++)for(int x=1;x<=2;x++)for(int l=0;l<=L;l++)dp1[i][x][l] = -1;
			for(int l=e1[0];l<=L;l++)dp1[0][1][l] = s1[0];
			for(int i=1;i<n;i++)for(int x=1;x<=2;x++)for(int l=0;l<=L;l++){
				int max = -1;
				if(l>0)max = dp1[i][x][l-1];
				if(l-e1[i]<0){
					max = Math.max(max, dp1[i-1][x][l]); 
				}
				else {
					if(dp1[i-1][x][l]>=0)max = Math.max(max, dp1[i-1][x][l]);
					if(dp1[i-1][x-1][l-e1[i]]>=0)max = Math.max(max, dp1[i-1][x-1][l-e1[i]]+s1[i]);
				}
				dp1[i][x][l] = max;
			}
			int[][][] dp2 = new int[m][m+1][L+1];
			for(int i=0;i<m;i++)for(int x=1;x<=m;x++)for(int l=0;l<=L;l++)dp2[i][x][l] = -1;
			for(int l=e2[0];l<=L;l++)dp2[0][1][l] = s2[0];
			for(int i=1;i<m;i++)for(int x=1;x<=m;x++)for(int l=0;l<=L;l++){
				int max = -1;
				if(l>0)max = dp2[i][x][l-1];
				if(l-e2[i]<0){
					max = Math.max(max, dp2[i-1][x][l]); 
				}
				else {
					if(dp2[i-1][x][l]>=0)max = Math.max(max, dp2[i-1][x][l]);
					if(dp2[i-1][x-1][l-e2[i]]>=0)max = Math.max(max, dp2[i-1][x-1][l-e2[i]]+s2[i]);
				}
				dp2[i][x][l] = max;
			}
			int max = 0;
			for(int x=X;x<=m;x++)for(int l=0;l<=L;l++){
				if(dp2[m-1][x][l]==-1)continue;
				if(dp1[n-1][1][L-l]==-1&&dp1[n-1][2][L-l]==-1)continue;
				int v = dp2[m-1][x][l] + Math.max(dp1[n-1][1][L-l], dp1[n-1][2][L-l]);
				max = Math.max(max, v);
			}
			System.out.println(max);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}