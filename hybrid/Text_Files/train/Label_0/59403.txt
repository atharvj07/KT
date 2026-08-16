
import java.util.Scanner;

public class Main {

	public static void main(String[] args){
		// TODO 自動生成されたメソッド・スタブ
		Scanner in = new Scanner(System.in);
		int a = in.nextInt()
				,b = in.nextInt()
				,c = in.nextInt();
		int x;
		x = a>=b ? a : b;
		x = x < c ? c : x;
		System.out.println(a+b+c-x);
	}

}
