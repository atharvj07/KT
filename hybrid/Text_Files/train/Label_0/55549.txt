import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sn = new Scanner(System.in);
    int L = sn.nextInt();
    double l = L / (double) 3;
    System.out.println(l * l * l);
  }
}
