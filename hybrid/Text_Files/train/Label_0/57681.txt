import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main
{
  public static void main(String[] args) throws NumberFormatException, IOException
  {
    BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    ArrayList<Integer[]> inputList = new ArrayList<>(100);

    while (input.ready())
    {
      final String[] inputStrArray = input.readLine().split(",");
      final Integer[] inputIntArray =
      { Integer.parseInt(inputStrArray[0]), Integer.parseInt(inputStrArray[1]) };

      inputList.add(inputIntArray);
    }
    final int[] ans = solver(inputList);
    System.out.println(ans[0]);
    System.out.println(ans[1]);

  }

  private static int[] solver(ArrayList<Integer[]> list)
  {
    int prodSum = 0;
    double sum = 0;
    for (Integer[] each : list)
    {
      prodSum += each[0] * each[1];
      sum += each[1];
    }
    final int[] ret =
    { prodSum, (int) Math.round(sum / list.size()) };
    return ret;
  }

}