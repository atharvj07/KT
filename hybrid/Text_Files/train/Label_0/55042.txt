import java.util.Scanner;

class Main{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int a=sc.nextInt();
		int a_noriho=sc.nextInt();
		int b=sc.nextInt();
		int b_noriho=sc.nextInt();

		int kei=Math.min(a,a_noriho)+Math.min(b,b_noriho);
		System.out.println(kei);
	}
}