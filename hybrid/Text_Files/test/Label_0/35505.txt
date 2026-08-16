import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Lexicography {
	public static void main(String[] args)
	{
		Scanner scan = new Scanner(System.in);
		String[] nlk = scan.nextLine().split(" ");
		int n = Integer.parseInt(nlk[0]); //number of words
		int l = Integer.parseInt(nlk[1]); //length of each word
		int k = Integer.parseInt(nlk[2]) - 1; //index of smallest word
		PriorityQueue<Character> data = new PriorityQueue<Character>();
		for (char c : scan.nextLine().toCharArray())
			data.add(c);
		String[] output = new String[n];
		Arrays.fill(output, "");
		boolean diff = false;
		char in;
		char prev = '-';
		int same = 0;
		int x = 0;
		while (diff == false && !data.isEmpty())
		{
			for(int i = x; i <= k; i++)
			{
				if (output[i].length() >= l)
				{
					same = 0;
					break;
				}
				in = data.poll();
				if (prev == in)
					same++;
				else
					same = 0;
				output[i] = output[i] + in;
				prev = in;
			}
			if (same > 0)
			{
				x = k-same;
				same = 0;
				prev = '-';
			}
			else
				diff = true;
		}
		while (output[k].length() < l)
		{
			output[k] = output[k] + data.poll();
		}
		int point = k + 1;
		while (!data.isEmpty())
		{
			point%=output.length;
			if (output[point].length() < l)
			{
				output[point] = output[point] + data.poll();
			}
			point++;
		}
		for (String s: output)
			System.out.println(s);
		scan.close();
	}
}
