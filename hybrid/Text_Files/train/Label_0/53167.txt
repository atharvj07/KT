import java.util.Scanner;

public class Main{
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		int x = scan.nextInt();
		int y = scan.nextInt();

		while(x != 0 || y != 0){
			if(x > y){
				System.out.println(y + " " + x);
			}else{
				System.out.println(x + " " + y);
			}
			x = scan.nextInt();
			y = scan.nextInt();
		}
	}
}