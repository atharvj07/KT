import java.util.Scanner;

public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = 0;
		int a = 0;
		int b = 0;
		n = sc.nextInt();
		sc.nextLine();
		a = sc.nextInt();
		b = sc.nextInt();

		int t = b/n;
		int ans = t*n;

		if(a <= ans && ans <= b){
			System.out.println("OK");
		}else{
			System.out.println("NG");
		}

	}
}