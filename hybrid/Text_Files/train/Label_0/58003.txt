 
import java.util.Scanner;
public class FloorNumber {

	public static void main(String[] args) {
		
		Scanner scn = new Scanner(System.in);
		int t = scn.nextInt(); 
		int n,x;
		for(int j = 1; j <= t; j++)
		{
			n = scn.nextInt(); 
			x = scn.nextInt(); 
			int appartment_no = 2, i = 0, floor = 2;  
			if(n == 1 || n == 2)
			{
				System.out.println(1);
			}
			else
			{
				while(true)
				{
					++i;
					++appartment_no;
					 
					if(n == appartment_no)
					{
						System.out.println(floor);
						break;
					}
					
					if(i == x)
					{
						floor++;
						i = 0;
					}
				}
			} 
		}
	} 
}
