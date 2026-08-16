import java.util.Scanner;

public class Main
{
	public static void main(String arg[])
	{
		Scanner sc = new Scanner(System.in);
		while(sc.hasNext())
		{
			String str1 = sc.next();
			String str2 = sc.next();
			int hi=0;
			int bl=0;
			if(str1.equals("0")&&str2.equals("0"))
				return;
			for(int i=0; i<4; i++){
				if(str1.charAt(i)==str2.charAt(i))	
					hi++;
			}
			for(int i=0; i<4; i++)
				for(int j=0; j<4;j++)
					if(i==j)
						continue;
					else
						if(str1.charAt(i)==str2.charAt(j))
							bl++;

			System.out.println(hi+" "+bl);
		}
	}

}