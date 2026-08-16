import java.util.Scanner;

class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int c = sc.nextInt();
		
		int sum = 0;
		for(int i = 0; i < c; i++) {
			sum += sc.nextInt();
		}
		
		System.out.println((int) Math.ceil((double) sum / (n + 1)));
	}
}
