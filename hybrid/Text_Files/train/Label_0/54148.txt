import java.util.Scanner;

public class Driver
{
    public static int[][] ranges;

    public static void main(String args[])
    {
        try
        {
            Scanner scanner = new Scanner(System.in);
            int count = scanner.nextInt();
            int[] bars = new int[count];

            for(int i = 0; i < count; i++){
                bars[i] = scanner.nextInt();
            }

            int aliceIndex = 0;
            int bobIndex = count - 1;

            int aliceCount = 0;
            int bobCount = 0;

            if(aliceIndex == bobIndex){
                aliceCount++;
            } else {
                long aliceTotal = bars[aliceIndex];
                long bobTotal = bars[bobIndex];

                while(aliceIndex <= bobIndex){
                    if(aliceTotal < bobTotal){
                        aliceIndex++;
                        aliceCount++;
                        aliceTotal += bars[aliceIndex];
                    } else if(bobTotal < aliceTotal){
                        bobIndex--;
                        bobCount++;
                        bobTotal += bars[bobIndex];
                    } else {
                        aliceIndex++;
                        aliceCount++;
                        aliceTotal += bars[aliceIndex];
                    }
                }
            }

            System.out.println("" + aliceCount + " " + bobCount);
        }
        catch(Exception ex)
        {
            System.out.println("ERROR");
        }
    }
}