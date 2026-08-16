import  java.util.Scanner;

public class Main{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    while(true){
      int n = Integer.parseInt(sc.next());
      if(n == 0) break;
      int a[] = new int[n];
      double sum = 0;
      double sum2 = 0;
      for(int i = 0; i < n; i++){
        a[i] = Integer.parseInt(sc.next());
        sum += a[i];
        sum2 += a[i] * a[i];
      }
      double a1 = sum2 / n;
      double a2 = (sum / n) * (sum / n);
      System.out.printf("%f\n", Math.sqrt(a1 - a2));
    }
  }
}
