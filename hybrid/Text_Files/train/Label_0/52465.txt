
import java.util.*;

public class Main {
	
	static int check(int a, int b, int c)
	{
		if (b-a==4&&c-b==3)
			return 1;
		if (b-a==3&&c-b==4)
			return 2;
		return 0;
		
	}
	
	public static void main(String[] args)
	{
		String[] notes={"C", "C#", "D", "D#", "E", "F", "F#",
				"G", "G#", "A", "B", "H"};
		Scanner cin = new Scanner(System.in);
		int[] given=new int[5];
		for (int i=1; i<=3; i++)
		{
			String temp=cin.next();
			for (int j=0; j<12; j++)
				if (temp.compareTo(notes[j])==0)
				{
					given[i]=j;
					break;
				}
		}
		Arrays.sort(given, 1, 4);
	//	for (int i=1; i<=3; i++)
	//		System.out.println(given[i]);
		int flag=0;
		int temp;
		if ((temp=check(given[1], given[2], given[3]))>0)
			flag=temp;
		if ((temp=check(given[2], given[3], given[1]+12))>0)
			flag=temp;
		if ((temp=check(given[3], given[1]+12, given[2]+12))>0)
			flag=temp;
		
		if (flag==1)
			System.out.println("major");
		else if (flag==2)
			System.out.println("minor");
		else
			System.out.println("strange");
	}
}
