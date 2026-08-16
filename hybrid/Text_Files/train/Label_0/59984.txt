import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = Integer.parseInt(sc.next());
		int k = Integer.parseInt(sc.next());

		int[] array = new int[n];
		for (int i = 0; i < n; i++)
			array[i] = Integer.parseInt(sc.next());
		Arrays.sort(array);
		
		int sum = 0;
		for(int i = 0; i < k; i++)
			sum += array[i];
		
		System.out.println(sum);
	}

}
