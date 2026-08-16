import java.util.Scanner;
import java.util.Arrays;
class Main {
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    int n;

    while (true){
      n = input.nextInt();
      if (n == 0) break;
      if (n % 1111 == 0){
        System.out.println("NA");
        continue;
      }
      int ct = 0;
      while (n != 6174){
        int l, s;
        int[] num = new int[4];
        for (int i = 0; i < 4; i++){
          num[i] = n % 10;
          n /= 10;
        }
        Arrays.sort(num);
        l = s = 0;
        for(int i = 0; i < 4; i++){
          s = s * 10 + num[i];
          l = l * 10 + num[3 - i];
        }
        n = l - s;
        ct++;
      }
      System.out.println(ct);
    }
  }
}