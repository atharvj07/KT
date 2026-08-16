import java.util.*;
import java.lang.*;
import java.io.*;
import java.math.*;

public class bmail{
	
	static void path(Stack<Integer> s)
	{
		while(!s.isEmpty())
		{
			System.out.print(s.pop() + " ");
		}
	}

	
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		int n= sc.nextInt();
		int arr[]=new int[n+1];
		Stack<Integer> stack=new Stack<Integer>();
		for(int i=1; i<n; i++)
		{	
			arr[i]= sc.nextInt();
		}
		int j=n;
		while(j>1)
		{
			stack.add(j);
			j=arr[j-1];
		}
		stack.add(1);
		path(stack);
	}
}