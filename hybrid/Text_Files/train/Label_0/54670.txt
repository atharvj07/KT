
import java.util.Scanner;



public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while(sc.hasNext()) {
			int n = sc.nextInt();
			int m = sc.nextInt();
			int p = sc.nextInt();
			if(n+m+p==0) break;
			
			int sum = 0;
			int win = 0;
			boolean winer = true;
			for(int i=1;i<=n;i++) {
				int bet = sc.nextInt();
				if(i==m) {
					if(bet==0) {
						winer = false;
					}
					else
						win = bet;
				}
				sum += bet*100;
			}
			if(!winer)
				System.out.println(0);
			else {
				sum = sum*(100-p)/100;
				System.out.println(sum/win);
			}
		}
	}
}
