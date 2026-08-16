import java.util.Scanner;

//Deadly Dice Game
public class Main{

	void run(){
		Scanner sc = new Scanner(System.in);
		for(;;){
			int n = sc.nextInt(), T = sc.nextInt();
			if((n|T)==0)break;
			char[] a = sc.next().toCharArray();
			double[][] dp = new double[n][2];
			for(int i=0;i<n;i++)dp[i][0]=a[i]=='R'?1:0;
			int x = 1;
			for(int t=1;t<=T;t++,x=1-x)for(int i=0;i<n;i++){
				double p = 0;
				for(int k=1;k<7;k++)p+=dp[(i+k)%n][1-x]/6;
				dp[i][x] = p;
			}
			double res = 0;
			for(int i=0;i<n;i++)res= Math.max(res, dp[i][1-x]);
			System.out.printf("%.9f\n", res);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}