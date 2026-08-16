import java.util.Scanner;

//Marathon Match
public class Main{

	void run(){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int L = sc.nextInt();
		long[][] comb = new long[51][51];
		comb[0][0] = comb[1][0] = comb[1][1] = 1;
		for(int i=2;i<=50;i++){
			comb[i][0] = comb[i][i] = 1;
			for(int j=1;j<i;j++)comb[i][j] = comb[i-1][j-1]+comb[i-1][j];
		}
		double[] p = new double[n];
		int[] t = new int[n];
		double[] v = new double[n];
		for(int i=0;i<n;i++){
			p[i] = sc.nextDouble()/100.0;
			t[i] = sc.nextInt();
			v[i] = sc.nextDouble();
		}
		double[][] time = new double[n][m+1];
		double[][] pp = new double[n][m+1];
		for(int i=0;i<n;i++){
			double r = L/v[i];
			for(int j=0;j<=m;j++){
				time[i][j] = j*t[i] + r;
				pp[i][j] = comb[m][j]*Math.pow(p[i], j)*Math.pow(1-p[i], m-j);
			}
		}
		for(int i=0;i<n;i++){
			double exp = 0;
			for(int j=0;j<=m;j++){
				double e = pp[i][j];
				for(int k=0;k<n;k++){
					if(i==k)continue;
					double ee = 0;
					for(int l=0;l<=m;l++){
						if(time[i][j]+1e-8<time[k][l])ee += pp[k][l];
					}
					e *= ee;
				}
				exp += e;
			}
			System.out.printf("%.6f\n", exp);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}