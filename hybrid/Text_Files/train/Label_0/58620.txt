import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		
		int num = 0;
		int max = 0;
		
		for(int i = 1; i <= N; i++) {
			int count = 0;
			int x = i;
			while(x % 2 == 0) {
				count++;
				x /= 2;
			}
			if(num <= count) {
				max = i;
				num = count;
			}
		}
		System.out.println(max);
	}
}
