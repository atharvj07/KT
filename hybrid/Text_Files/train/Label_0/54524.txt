import java.util.*;

public class Main {
	public static void main(String[] args) {
	
		Scanner s = new Scanner(System.in);
		int n = s.nextInt();

		int[] a = new int[n];
		for(int i = 0; i < n; i++)
			a[i] = s.nextInt();

		Arrays.sort(a);

		int i = 0, j = 0;

		while(j < n) {
			if(a[j] > a[i])
				i++;
			j++;
		}

		System.out.println(i);
	}
}