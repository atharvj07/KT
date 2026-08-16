
import java.util.Scanner;

public class AniaAndMinimizing {
	public static void main(String arg[])
	{
		Scanner scr = new Scanner(System.in);
		
		int s = scr.nextInt();
		int k = scr.nextInt();
		String str = scr.next();
		char n[] = str.toCharArray();
		
		for(int i=0;i<s && k>0;i++)
		{
			if(i==0)
			{
				if(s==1)
				{
					n[0]='0';
					k--;
				}else
				if(n[0]!='1')
				{
					n[0]='1';
					k--;
				}
			}
			else
			if(n[i]!='0')
			{
				n[i]='0';
				k--;
			}
		}
		
		for(int i=0;i<s;i++)
			System.out.print(n[i]);
	}
}