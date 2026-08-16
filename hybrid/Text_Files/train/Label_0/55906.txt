import java.util.Scanner;

//KULASIS
public class Main{

	int[] f(int x){
		int[] r = new int[4];
		int k = 0;
		while(x>0){
			r[k++] = x%4;
			x/=4;
		}
		return r;
	}

	void run(){
		Scanner sc = new Scanner(System.in);
		int[] p = {0, 60, 70, 80};
		int[][] k = new int[256][];
		for(int i=0;i<256;i++)k[i]=f(i);
		int T = sc.nextInt();
		while(T--!=0){
			int[][] a = new int[5][5];
			for(int i=0;i<5;i++)for(int j=0;j<5;j++)a[i][j]=sc.nextInt()-1;
			int[] dp = new int[256];
			for(int i=0;i<256;i++){
				for(int j=0;j<5;j++){
					int s = a[0][j];
					if(s==-1)continue;
					if(j<4)s+=k[i][j];
					if(j>0)s+=k[i][j-1];
					dp[i] += p[s%4];
				}
			}
			for(int n=1;n<4;n++){
				int[] next = new int[256];
				//niÚÌóÔ
				for(int i=0;i<256;i++){
					int max = 0;
					//n-1iÚÌóÔ
					for(int j=0;j<256;j++){
						int sum = 0;
						for(int v=0;v<5;v++){
							if(a[n][v]==-1)continue;
							int s = a[n][v];
							if(v<4)s+=k[i][v]+k[j][v];
							if(v>0)s+=k[i][v-1]+k[j][v-1];
							sum += p[s%4];
						}
						max = Math.max(max, dp[j]+sum);
					}
					next[i] = max;
				}
				dp = next;
			}
			int res = 0;
			for(int i=0;i<256;i++){
				int sum = 0;
				for(int j=0;j<5;j++){
					if(a[4][j]==-1)continue;
					int s = a[4][j];
					if(j<4)s+=k[i][j];
					if(j>0)s+=k[i][j-1];
					sum += p[s%4];
				}
				res = Math.max(res, dp[i]+sum);
			}
			System.out.println(res);
		}
	}

	public static void main(String[] args) {
		new Main().run();
	}
}