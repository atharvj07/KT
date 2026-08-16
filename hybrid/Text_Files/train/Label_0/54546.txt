import java.util.Scanner;

public class Temp1
{
	public static void main(String[] args) 
	{		
		Scanner obj = new Scanner(System.in);
		String s = obj.nextLine();
		int n = s.length();
		
		boolean visited[] = new boolean[n];		
		int counter = 0;
		
		for(int i=0 ; i<n-2 ; i++)
		{
			if(s.charAt(i) == 'Q')
			{
				for(int j = i+1 ; j<n ; j++)
				{
					if(s.charAt(j) == 'A')
					{
						for(int k=j+1 ; k<n ; k++)
						{
							if(s.charAt(k)=='Q')
							{
								counter++;
							}
						}
					}
				}
			}
		}
		
		System.out.println(counter);
	}
}