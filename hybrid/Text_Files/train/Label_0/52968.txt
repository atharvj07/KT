import java.util.*;
public class Main{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int A = sc.nextInt();
    int B = sc.nextInt();
    int tmp =1;
    int answer = 0;
    while(tmp<B){
      tmp=tmp+A-1;
      answer=answer+1;
    }
    System.out.print(answer);
  }
}