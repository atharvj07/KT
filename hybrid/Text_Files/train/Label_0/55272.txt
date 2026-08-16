import java.util.Arrays;
import java.util.Scanner;

//Convenient Location
public class Main{

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while(true){
			int n = sc.nextInt();
			if(n==0)break;
			int[][] c = new int[10][10];
			for(int[]a:c)Arrays.fill(a, 1<<25);
			for(int i=0;i<10;i++)c[i][i]=0;
			int max = 0;
			while(n--!=0){
				int s = sc.nextInt();
				int t = sc.nextInt();
				int d = sc.nextInt();
				c[s][t]=c[t][s]=Math.min(c[s][t], d);
				max = Math.max(max, Math.max(s, t));
			}
			for(int k=0;k<10;k++)for(int i=0;i<10;i++)for(int j=0;j<10;j++)c[i][j]=Math.min(c[i][j], c[i][k]+c[k][j]);
			int k = 0;
			int w = 1<<25;
			for(int i=0;i<10;i++){
				int s = 0;
				for(int j=0;j<=max;j++)s+=c[i][j];
				if(s<w){
					k = i;
					w = s;
				}
			}
			System.out.println(k+" "+w);
		}
	}
}