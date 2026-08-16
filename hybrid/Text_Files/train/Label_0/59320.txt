import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int a = in.nextInt();
		int b = in.nextInt();
		int c = in.nextInt();
		int tar = in.nextInt();
		int cnt = 0;
		for(int i = 0; i <= a; i++) {
			for(int j = 0; j <= b; j++) {
				for(int k = 0; k <= c; k++) {
					int tot = 500 * i + 100 * j + 50 * k;
					if(tot == tar)
						cnt++;
				}
			}
		}
		System.out.println(cnt);
	}

}
