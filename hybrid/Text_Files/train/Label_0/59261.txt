import java.util.Scanner;


public class LightOut {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
   
		Scanner in = new Scanner(System.in);
		int[][] arr = new int[5][5];

		for(int i = 1; i <= 3; i++)
		{
			for(int j = 1; j <= 3; j++)
			{
				arr[i][j] = in.nextInt();
				
			}
			
		}

		for(int i = 1; i <= 3; i++)
		{
			for(int j = 1; j <= 3; j++)
			{
				System.out.print(1 - 
						(arr[i][j] +
								arr[i+1][j] + 
								arr[i-1][j] +
								arr[i][j+1]+
								arr[i][j-1])%2);
			}
			System.out.println();
		}
}
}