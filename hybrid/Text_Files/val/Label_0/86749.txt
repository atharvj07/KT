import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		double s = Math.sqrt(n);
		int m = (int)s;
		System.out.println(m*m);
	}
}
