import java.util.Scanner;

public class P456ALaptops {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		long laptopLength = s.nextLong();
		int index = 0;
		long[] priceList = new long[(int)laptopLength];
		long[] qualityList = new long[(int)laptopLength];
		boolean flag = false;
		String message = "Poor Alex";
		
		for(index=0; index<laptopLength; index++)	{
			priceList[index] = s.nextLong();
			qualityList[index] = s.nextLong();
			
			if(priceList[index] < qualityList[index])	{
				message = "Happy Alex";
			}
		}
		
		System.out.println(message);
	}
}
