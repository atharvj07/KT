import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int d = sc.nextInt();
		int[] p = new int[n];
		for(int i=0;i<n;i++) {
			p[i] = sc.nextInt();
		}
		int score = 0;
		for(int i=0;i<n;i++) {
			int s = p[i] - d;
			if (s > 0) {
				score+=s;
			}
		}
		if (score <= 0) {
			System.out.println("kusoge");
		}else{
			System.out.println(score);
		}
	}

}