import java.util.Scanner;
public class teh {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int a = in.nextInt();
		while(a!=0){
			a--;
			int n = in.nextInt();
			if(n == 2)
				System.out.println("2");
			else if(n%2==0)
				System.out.println("0");
			else
				System.out.println("1");
		}

	}

}
