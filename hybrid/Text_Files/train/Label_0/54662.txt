
import java.util.Scanner;

public class Spinner {
	private static Scanner in = new Scanner(System.in);
	public static void main(String[] args) {
		Spinner s = new Spinner();
		String answer = new String();
		SpinPosition initialPosition = s.new SpinPosition(in.next().charAt(0));
		SpinPosition finalPosition = s.new SpinPosition(in.next().charAt(0));
		long time = in.nextLong();
		time %= 4;
		int clockWise = (finalPosition.positionOrder > initialPosition.positionOrder) ? finalPosition.positionOrder - initialPosition.positionOrder
																					  :  4 - Math.abs(finalPosition.positionOrder - initialPosition.positionOrder);
		int counterCW = (finalPosition.positionOrder > initialPosition.positionOrder) ?  4 - Math.abs(finalPosition.positionOrder - initialPosition.positionOrder)
				  : Math.abs(finalPosition.positionOrder - initialPosition.positionOrder);
		if(time == 0 || clockWise == counterCW)
		{
			answer = "undefined";
		}
		else 
		{
			if(time - clockWise == 0)
			{
				answer = "cw";
			}
			else if(time - counterCW == 0)
			{
				answer = "ccw";
			}
			else
			{
				answer = "undefined";
			}
		}
		System.out.println(answer);
	}
	
	public class SpinPosition
	{
		int positionOrder;
		char position;
		public SpinPosition(char x)
		{
			position = x;
			if(position == 'v')
			{
				positionOrder = 1;
			}else if(position == '<') {
				positionOrder = 2;
			}else if (position == '^') {
				positionOrder = 3;
			}else {
				positionOrder = 4;
			}
		}
	}

}
