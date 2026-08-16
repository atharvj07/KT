import java.io.PrintStream;
import java.util.Arrays;
import java.util.Scanner;

public class Chores {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    PrintStream out = new PrintStream(System.out);

    String inputs[] = in.nextLine().split(" ");
    int total = Integer.parseInt(inputs[0]);
    int petsyaChoresNumber = Integer.parseInt(inputs[1]);
    int vasyaChoresNumber = Integer.parseInt(inputs[2]);
    int[] complexities = Arrays.stream(in.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
    Arrays.sort(complexities);

    out.print(complexities[vasyaChoresNumber] - complexities[vasyaChoresNumber - 1]);
  }
}