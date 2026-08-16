import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		for (int i = 0; i < N; i++) {
			int n = scanner.nextInt();
			int sum = 0;
			for(int j = 0; j < n;j++) {
				int c = scanner.nextInt();
				if(c == 1) {
					sum++;
				}else if(c == 3) {
					sum++;
				}
			}
			System.out.println(sum);
		}
		scanner.close();
	}
}
	 	   	   	 	   		  	 	 		 	 	