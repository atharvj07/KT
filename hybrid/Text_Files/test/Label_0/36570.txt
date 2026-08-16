import java.util.*;

public class Main {
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int min = 55;
    for(int i=2;i<=N/2;i++){
      int a=i;
      int b=N-i;
      int sum = method(a)+method(b);
      if(sum<min){
        min=sum;
      }
    }
    if(N!=2){
      System.out.println(min);
    }else{
      System.out.println(2);
    }

  }

  static int method(int x){
    return x/100000+(x/10000)%10+(x/1000)%10+(x/100)%10+(x/10)%10+x%10;
  }
}
