import java.util.Scanner;

public class Main {

	static int a,b,c,N;
	public static void main(String[] args) {
		Scanner cin = new Scanner(System.in);
		while(true){
			a=cin.nextInt();
			b=cin.nextInt();
			c=cin.nextInt();
			if(a+b+c==0){
				break;
			}
			N=cin.nextInt();
			int[] normal=new int[a+b+c+1];
			int[] ans=new int[a+b+c+1];
			int[][] d = new int[N][4];
			for(int i = 0;i<N;i++){
				for(int j = 0;j<4;j++){
					d[i][j]=cin.nextInt();
				}
				if(d[i][3]==1){
					normal[d[i][0]]=ans[d[i][0]]=1;
					normal[d[i][1]]=ans[d[i][1]]=1;
					normal[d[i][2]]=ans[d[i][2]]=1;
				}
			}
			for(int i =0;i<N;i++){
				if(normal[d[i][0]]+normal[d[i][1]]+normal[d[i][2]]==2){
					for(int j = 0;j<3;j++){
						if(normal[d[i][j]]==0){
							ans[d[i][j]]=2;
						}
					}
				}
			}
			for(int i = 1;i<normal.length;i++){
				if(ans[i]==0){
					System.out.println(2);
				}
				else if(ans[i]==2){
					System.out.println(0);
				}
				else{
					System.out.println(1);
				}
			}
		}
	}
}