import java.util.Scanner;
public class Main {
	public static void main(String[] args) throws java.io.IOException {
		Scanner scan = new Scanner(System.in);
		int a[] = new int[7];
		int b[] = new int[7];
		for(int i = 0; i<7 ; i++){
			a[i] = scan.nextInt();
			b[i] = scan.nextInt();
		}
		for(int i = 0; i<7 ; i++){
			System.out.println(a[i]-b[i]);
		}
	}
}