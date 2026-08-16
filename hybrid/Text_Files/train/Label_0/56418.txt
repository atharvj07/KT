import java.util.Scanner;


public class Main {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		int n = input.nextInt();
		int[] a = new int[100];
		
		for (int i=0;i<n;i++)
		{
			a[i] = input.nextInt();
		}
		
		int sum = 0;
		for (int i=1;i<n;i++)
		{
			if (a[i]==a[i-1])
			{
				sum++;
				a[i] = 100+sum;
				
			}
		}
		
		System.out.println(sum);

	}

}
