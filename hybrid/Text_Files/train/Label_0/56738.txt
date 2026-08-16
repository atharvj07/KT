import java.util.Scanner;

public class Main
{
	public static void main(String[] args)
	{
		Scanner scanner = new Scanner(System.in);
		int num;
		while((num = scanner.nextInt()) != 0)
		{
			String r = "";
			String s = String.format("%o", num);
			for(int i = 0; i < s.length(); i++)
			{
				char c = s.charAt(i);
				if(c > '4')
					r += (c-'0')+2;
				else if(c > '3')
					r += (c-'0')+1;
				else
					r += c;
			}
			System.out.println(r);
		}
	}
}