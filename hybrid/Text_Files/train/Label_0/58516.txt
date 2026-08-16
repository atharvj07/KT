

import java.util.Scanner;

public class Main
{
	static Scanner scan = new Scanner(System.in);

	public static void main(String[] args) 
	{
		int shortest;
		int blocks;
		
		while(true)
		{
			shortest = scan.nextInt();
			blocks = scan.nextInt();
			
			if(shortest == 0 && blocks == 0)
			{
				return;
			}
			else
			{
				new DataSet(shortest, blocks);
			}
		}
	}
	
	static class DataSet
	{
		boolean[] yearMark = new boolean[8000000];
		int year = 0;
		
		public DataSet(int s, int b)
		{
			int gap = s;
			
			year = s;
			for(int tree = 0; tree < b; tree++)
			{
				for(int jumper = year; jumper < 8000000; jumper+= gap)
				{
					yearMark[jumper] = true;
				}
				
				//find false
				while(yearMark[year] == true)
				{
					year += 1;

				}
				//year is now first false, ready to plant next tree
				gap = year;
			}
			
			System.out.println(year);
		}
	}
}

