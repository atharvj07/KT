import java.util.Scanner;
public class Main{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int a = sc.nextInt();
    int b = sc.nextInt();
    int[] c = new int[a];
    int d = 0;
    int counter = 1;
    for(int i = 0;i < c.length;i++){
      c[i] = sc.nextInt();
    }
    for(int j = 0;j < c.length;j++){
      d += c[j];
      if(b >= d){
        counter++;
      }
    }
    System.out.println(counter);
  }
}