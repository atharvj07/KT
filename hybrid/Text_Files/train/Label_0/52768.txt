import java.util.Arrays;
import java.util.Scanner;

//Finding the Top RPS Player
public class Main{

	void run(){
		Scanner sc = new Scanner(System.in);
		for(int T=1;;T++){
			int N = sc.nextInt(), M = sc.nextInt();
			if((N|M)==0)break;
			int[][] c = new int[2][M+1];
			c[0][0] = N;
			for(int x=1,t=1;;t++,x=1-x){
				Arrays.fill(c[x], 0);
				for(int i=0;i<M;i++){
					c[x][i+1]+=c[1-x][i]/2;
					c[x][0]+=c[1-x][i]/2;
					if(c[1-x][i]%2!=0)c[x][i]++;
				}
				if(c[x][M]!=0){
					System.out.println("Case "+T+": "+t); break;
				}
			}
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}