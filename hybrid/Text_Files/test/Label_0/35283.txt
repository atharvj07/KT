import java.util.Scanner;
import static java.lang.Math.log;
public class T4 
{
	public static void main(String[] args) 
	{
		Scanner S1 = new Scanner(System.in);
		int T=0,Num1=0;
		T=S1.nextInt();
		while(T>0)
		{
			Num1=S1.nextInt();
			for(int i=0;i<Num1;i++)
			{
				System.out.print(1+" ");
			}
			System.out.println("");
			T--;
		}
	}
}