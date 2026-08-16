import java.util.Scanner;

public class Main {
	int n,m;
	double table[][];
	double memo[][];
	public static void main(String[] args) {
		new Main().run();
	}
	void run(){
		Scanner sc=new Scanner(System.in);

		while(true){
			n=sc.nextInt();
			m=sc.nextInt();
			if(n+m==0) break;
			table=new double[n][n];
			memo=new double[n][m];

			for(int i=0;i<n;i++){
				for(int j=0;j<n;j++){
					table[i][j]=sc.nextDouble();
				}
			}
			for(int i=0;i<n;i++){
				for(int j=0;j<m;j++){
					memo[i][j]=-1;
				}
			}
			for(int i=0;i<n;i++){
				memo[i][m-1]=1;
			}
			for(int i=0;i<n;i++){
				bt(i,0);
//				for(int j=0;j<n;j++){
//					for(int k=0;k<m;k++){
//						System.out.print(" "+j+","+k+" "+memo[j][k]);
//					}
//					System.out.println();
//				}
//				System.out.println();
			}
			
			double max=0;
			for(int i=0;i<n;i++){
				max=Math.max(max, memo[i][0]);
			}
			System.out.printf("%.2f\n",max);
		}
	}

	double bt(int x,int d){
		if(m<=d) return 1;

		if(memo[x][d]!=-1) return memo[x][d];

		double max=0;
		for(int i=0;i<n;i++){
			//System.out.println("x="+x+" d="+d+" i="+i+" x="+x);
			max=Math.max(max,bt(i,d+1)*table[i][x]);
		}

		return memo[x][d]=max;
	}

}