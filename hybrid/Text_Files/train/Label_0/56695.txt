import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int a=scan.nextInt(),b=scan.nextInt(),c=scan.nextInt();
		if(a==c) {
			System.out.println(b);
		}
		else if(a==b) {
			System.out.println(c);
		}
		else if(b==c) {
			System.out.println(a);
		}

	}

}