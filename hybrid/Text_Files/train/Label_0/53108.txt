
import java.util.Scanner;
import java.util.ArrayList;

public class Main
{

	public static void main(String[] args)
	{
		Scanner sc = new Scanner(System.in);
		int numCards = sc.nextInt();
		
		ArrayList<String> cards = new ArrayList<String>();
		for(int i = 0; i < numCards; i++)
		{
			String nextCard = sc.next().trim();
			cards.add(nextCard);
		}
		sc.close();
		
		String hints = "12345BYWGR";

		int minHints = 11;
		int numHintSets = (int)Math.pow(2, 10);
		for(int i = 0; i < numHintSets; i++)
		{
			ArrayList<Character> currHints = new ArrayList<Character>();
			for(int j = 0; j < hints.length(); j++)
			{
				if((i & (1 << j)) > 0)
				{
					currHints.add(hints.charAt(j));
				}
			}
			
			boolean validHints = true;
			for(int j = 1; j < numCards; j++)
			{
				for(int k = 0; k < j; k++)
				{
					char num1 = cards.get(j).charAt(0);
					char color1 = cards.get(j).charAt(1);
					char num2 = cards.get(k).charAt(0);
					char color2 = cards.get(k).charAt(1);
					
					if(num1 == num2 && color1 == color2)
					{
						continue;
					}
					else if(num1 == num2 && color1 != color2)
					{
						validHints &= (currHints.contains(color1) || currHints.contains(color2));
					}
					else if(num1 != num2 && color1 == color2)
					{
						validHints &= (currHints.contains(num1) || currHints.contains(num2));
					}
					else if(num1 != num2 && color1 != color2)
					{
						validHints &= (currHints.contains(num1) || currHints.contains(num2)
								|| currHints.contains(color1) || currHints.contains(color2));
					}
				}
			}
			
			if(validHints)
			{
				if(currHints.size() < minHints)
					minHints = currHints.size();
			}
		}
		
		System.out.println(minHints);
	}

}
