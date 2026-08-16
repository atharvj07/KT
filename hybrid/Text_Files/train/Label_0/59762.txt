import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int d = Integer.parseInt(sc.next());
		if (d == 22){
			System.out.println("Christmas Eve Eve Eve");
		}else if(d == 23){
			System.out.println("Christmas Eve Eve");
		}else if(d == 24){
			System.out.println("Christmas Eve");
		}else {
			System.out.println("Christmas");
		}
	}
}
