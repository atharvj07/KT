import java.util.Scanner;
public class fibbing {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long A = sc.nextLong();
		long B = sc.nextLong();
		int place = sc.nextInt();
		long[] array = new long[place+1];
		array[0]=A;
		array[1]=B;
		for(int a=2;a<=place;a++){
			array[a]=array[a-1]+array[a-2];
		}
		System.out.println(array[place]);

	}

}
