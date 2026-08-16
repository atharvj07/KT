import java.util.Scanner;

public class Main {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner cin = new Scanner(System.in);
		while(true){
			int n = cin.nextInt();
			int q = cin.nextInt();
			if(n+q==0){
				break;
			}
			int[][] date = new int[n][101];
			for(int i = 0;i<n;i++){
				int m = cin.nextInt();
				for(int j = 0;j<m;j++){
					int a = cin.nextInt();
					date[i][a]=1;
				}
			}
			boolean f = true;
			int max=0,day=0;
			for(int j = 1;j<101;j++){
				int sum=0;
				for(int i = 0;i<n;i++){
					sum+=date[i][j];
				}
				if(sum>max){
					max=sum;
					day=j;
				}
			}
			if(max>=q){
				System.out.println(day);
			}
			else{
				System.out.println(0);
			}
		}

	}

}