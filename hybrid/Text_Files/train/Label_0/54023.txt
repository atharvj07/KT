

import java.util.ArrayList;
import java.util.Scanner;
import java.util.Stack;

public class ggg {

	public static void main(String args[])
	{
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		String eg=scan.next();
		int cost=0;
		String ans="";
		Stack<Character> stk=new Stack<Character>();
		ArrayList<Character> anss=new ArrayList<Character>();
		for(int i=0;i<n;i++)
		{
//			System.out.println(eg.charAt(i));
			int j=i+1;
			int x=0;
			while(j<n &&eg.charAt(i)==eg.charAt(j))
			{
				j++;
				x++;
				cost++;
			}
			if(j>=n)
			{
				cost++;
				break;
			}
//			System.out.print(eg.charAt(i));
//			System.out.print(eg.charAt(j));
			anss.add(eg.charAt(i));
			anss.add(eg.charAt(j));
			i+=x+1;
		}
		System.out.println(cost);
//		System.out.println(ans);
		for(char x:anss)
		{
			System.out.print(x);;
		}
	}
}
