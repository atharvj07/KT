import java.util.Scanner;

public class Main
{
	public static void main(String arg[])
	{
		Scanner sc = new Scanner(System.in);

		char ch[][] = new char[8][8];
		char tmp[][] = new char[8][8];
		for(int i=0; i<8; i++)
			ch[i]=sc.next().toCharArray();

		System.out.println(90);
		for(int i=7; i>=0; i--)
			for(int j=0; j<8; j++)
				tmp[j][i]=ch[7-i][j];
		ch=tmp;
		for(int i=0; i<8; i++)
		{
			for(int j=0; j<8; j++)
				System.out.print(ch[i][j]);
			System.out.println();
		}
		
		System.out.println(180);
		char tmp2[][] = new char[8][8];
		for(int i=7; i>=0; i--)
			for(int j=0; j<8; j++)
				tmp2[j][i]=ch[7-i][j];
		ch=tmp2;
		for(int i=0; i<8; i++)
		{
			for(int j=0; j<8; j++)
				System.out.print(ch[i][j]);
			System.out.println();
		}
		System.out.println(270);
		char tmp3[][] = new char[8][8];
		for(int i=7; i>=0; i--)
			for(int j=0; j<8; j++)
				tmp3[j][i]=ch[7-i][j];
		ch=tmp3;
		for(int i=0; i<8; i++)
		{
			for(int j=0; j<8; j++)
				System.out.print(ch[i][j]);
			System.out.println();
		}
		
	}
}