import java.util.Arrays;
import java.util.Scanner;

public class P911C
{
	public static void main(String[] args)
	{
		Scanner scan = new Scanner(System.in);
		int[] arr = {scan.nextInt(), scan.nextInt(), scan.nextInt()};
		Arrays.sort(arr);
		if (arr[0] == 1)
			System.out.println("YES");
		else if (arr[0] == 2)
		{
			if (arr[1] == 2 || arr[1] == 4 && arr[2] == 4)
				System.out.println("YES");
			else
				System.out.println("NO");
		}
		else if (arr[0] == 3)
		{
			if (arr[1] == 3 && arr[2] == 3)
				System.out.println("YES");
			else
				System.out.println("NO");
		}
		else
			System.out.println("NO");
	}
}
