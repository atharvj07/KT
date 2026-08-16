import java.util.*;
public class Main 
{
	public static void main(String[] args) 
	{
		Scanner stdIn = new Scanner(System.in);
		while(stdIn.hasNext())
		{
			int n = stdIn.nextInt();
			if(n == 0)
			{
				break;
			}
			for(int i = 0; i < n; ++i)
			{
				int x1 = stdIn.nextInt();
				int y1 = stdIn.nextInt();
				int z1 = stdIn.nextInt();
				int w1 = stdIn.nextInt();
				int x2 = stdIn.nextInt();
				int y2 = stdIn.nextInt();
				int z2 = stdIn.nextInt();
				int w2 = stdIn.nextInt();
				System.out.println((x1 * x2 - y1 * y2 - z1 * z2 - w1 * w2) + " " + (x1 * y2 + y1 * x2 + z1 * w2 - w1 * z2) + " " + (x1 * z2 + z1 * x2 - y1 * w2 + w1 * y2) + " " + (x1 * w2 + w1 * x2 + y1 * z2 - z1 * y2));
			}
		}
	}
}