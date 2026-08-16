import java.util.Scanner;

public class Main{
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		while(scan.hasNext()){
			int n = scan.nextInt();
			if(n == 0){
				break;
			}else if(n == 1){
				System.out.println(scan.nextInt() + " " + (scan.nextInt() + scan.nextInt()));
				continue;
			}
			int[][] p = new int[n][2];
			for(int i = 0;i < n;i++){
				p[i][0] = scan.nextInt();
				p[i][1] = scan.nextInt() + scan.nextInt();
			}
			int max = p[0][1];
			int tarI = 0;
			for(int i = 1;i < n;i++){
				if(max < p[i][1]){
					max = p[i][1];
					tarI = i;
				}
			}
			System.out.println(p[tarI][0] + " " + max);
		}
	}
}