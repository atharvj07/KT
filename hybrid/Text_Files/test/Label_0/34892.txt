import java.util.Scanner;

public class Main {

	static Scanner sc = new java.util.Scanner(System.in);

	public static void main(String[] args) {

		while (true){

		double x =sc.nextInt();
		double h = sc.nextInt();

		if(x==0 && h==0){
			break;
		}

		double s4 = x*x;
		double s3  = Math.sqrt(h*h+x*x/4)*2*x;

		System.out.println(s4+s3);
		}
	}

}