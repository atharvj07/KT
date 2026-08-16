import java.math.BigInteger;
import java.util.Scanner;

public class Main {

	public static void main(String args[]){

		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();

		BigInteger big_num = BigInteger.valueOf(1);

		for(int i = 2; i <= num+1; i++){
			big_num = big_num.multiply(BigInteger.valueOf(i));
		}

		System.out.println(big_num.add(BigInteger.valueOf(2)));

		for(int i = 2; i <= num+1; i++){
			System.out.println(i);
		}

	}
}